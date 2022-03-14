#include <cstdio>
#include "global.h"
#include "screen.h"

using std::printf;

int WIDTH; int HEIGHT;


Screen::Screen() : 
    window(NULL), renderer(NULL) {}


bool Screen::init()
{
    if (SDL_Init(SDL_INIT_VIDEO) != 0)
        return false;

    window = SDL_CreateWindow(
        "Points", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED,
        0, 0, SDL_WINDOW_FULLSCREEN_DESKTOP);

    if (window == NULL)
    {
        printf("Could not create window: %s\n", SDL_GetError());
        SDL_Quit();
        return false;
    }

    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_PRESENTVSYNC);

    if (renderer == NULL)
    {
        printf("Could not create renderer: %s\n", SDL_GetError());
        SDL_DestroyWindow(window);
        SDL_Quit();
        return false;
    }

    SDL_GetWindowSize(this->window, &WIDTH, &HEIGHT);
    SDL_RenderClear(renderer);
    SDL_RenderPresent(renderer);

    return true;
}

void Screen::clear()
{
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, SDL_ALPHA_OPAQUE);
    SDL_RenderClear(renderer);
}

void Screen::update()
{
    SDL_RenderPresent(renderer);
}

void Screen::background(Uint8 r, Uint8 g, Uint8 b)
{
    SDL_SetRenderDrawColor(renderer, r, g, b, SDL_ALPHA_OPAQUE);
    update();
}


bool Screen::process_events()
{
    SDL_Event event;
    while (SDL_PollEvent(&event))
        if (event.type == SDL_QUIT)
            return false;
    return true;
}


void Screen::close()
{
    if (renderer) SDL_DestroyRenderer(renderer);
    if (window)   SDL_DestroyWindow(window);
    SDL_Quit();
}
