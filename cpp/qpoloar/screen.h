#ifndef SCREEN_H
#define SCREEN_H

#include <SDL2/SDL.h>
#include <vector>
#include <cstring>

using std::vector;


struct Screen
{
    Screen();
    bool init();
    void background(Uint8, Uint8, Uint8);
    void clear();
    void update();
    bool process_events();
    void close();

    SDL_Window* window;
    SDL_Renderer* renderer;
};

#endif
