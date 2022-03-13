#include "helpers.h"


int random_int(int lo, int hi)
{
    std::random_device rd;
    std::mt19937 mt(rd());
    std::uniform_int_distribution<int> dist(lo, hi);
    return dist(mt);
}


void draw_point(SDL_Renderer* renderer, int x, int y, int radius, Uint8 r, Uint8 g, Uint8 b)
{
    if (x < radius || x >= WIDTH - radius || y < radius || y >= HEIGHT - radius)
        return;

    SDL_SetRenderDrawColor(renderer, r, g, b, 255);
    for (int w = 0; w < radius * 2; w++)
    {
        for (int h = 0; h < radius * 2; h++)
        {
            int dx = radius - w;
            int dy = radius - h;
            if ((dx * dx + dy * dy) <= (radius * radius))
                SDL_RenderDrawPoint(renderer, x + dx, y + dy);
        }
    }
}


void draw_line(SDL_Renderer* renderer, int x1, int y1, int x2, int y2,
               Uint8 r, Uint8 g, Uint8 b)
{
    SDL_SetRenderDrawColor(renderer, r, g, b, 255);
    SDL_RenderDrawLine(renderer, x1, y1, x2, y2);
}


SDL_Color to_sdl_color(Uint8 r, Uint8 g, Uint8 b, Uint8 a)
{
    SDL_Color color;
    color.r = r;
    color.g = g;
    color.b = b;
    color.a = a;
    return color;
}

tuple<uint8_t, uint8_t, uint8_t> get_rgb(SDL_Color c)
{
    return make_tuple(c.r, c.g, c.b);
}

/*
vector<double> linspace(double start, double stop, size_t N)
{
    vector<double> v;
    double step = (stop - start) / (N - 1);
    double d { start };
    for (size_t i{ 0 }; i < N; ++i) {
        v.push_back(d);
        d += step;
    }
    return v;
}

double distance(int x1, int y1, int x2, int y2)
{
    return sqrt(square(x2 - x1) + square(y2 - y1));
}

double square(double n)
{
    return n * n;
}

double cube(double n)
{
    return n * n * n;
}

double cube_root(double n)
{
    return pow(n, 1.0 / 3.0);
}

void sleep(int n) 
{
    sleep_for(milliseconds(n));
}
 */


//SDL_Color random_color()
//{
//    SDL_Color color;
//    color.r = (unsigned char) random_int(210, 250);
//    color.g = (unsigned char) random_int(70, 120);
//    color.b = (unsigned char) random_int(0, 100);
//    color.a = 255;
//    return color;
//}

//bool toggle_10()
//{
//    static bool b = false;
//    return b = !b;
//}

