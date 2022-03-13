#include "global.h"
#include "polar.h"
#include "screen.h"
#include "helpers.h"

#include <SDL2/SDL.h>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <queue>

using std::queue;

constexpr int N{ 200 };  // nr of points
Uint8 red1 = 250;
Uint8 green1 = 250;
Uint8 blue1 = 20;

Point next_point(int tick);
tuple<Uint8, Uint8, Uint8> next_color(int tick);


int main(int argc, char* args[])
{
    Screen screen;
    if (!screen.init())
    {
        cout << "error initializing SDL\n";
        return 1;
    }

    queue<Point> q;
    Point p, p2;

    while (true) 
    {
        int tick = SDL_GetTicks();
        q.push(next_point(tick));

        auto [red, green, blue] = next_color(tick);

        screen.clear();

        for (int i{ 0 }; i < q.size(); ++i)
        {
            p = q.front();
            p2 = q.back();
            draw_point(screen.renderer, p.x, p.y, 5, red, green, blue);
            draw_line(screen.renderer, p.x, p.y, p2.x, p2.y, red1, green1, blue1);
            draw_line(screen.renderer, p.x + 1, p.y + 1, p2.x + 1, p2.y + 1, red1, green1, blue1);
            draw_line(screen.renderer, p.x + 2, p.y + 2, p2.x + 2, p2.y + 2, red1, green1, blue1);
            draw_line(screen.renderer, p.x - 2, p.y - 2, p2.x - 2, p2.y - 2, 0, green1, blue1);
            draw_line(screen.renderer, p.x - 1, p.y - 1, p2.x - 1, p2.y - 1, red1, green1, blue1);
            q.pop();
            q.push(p);
        }

        p = q.back();
        draw_point(screen.renderer, p.x, p.y, 9, blue, green, red);

        if (q.size() < N)
            q.push(next_point(SDL_GetTicks()));
        while (q.size() > N)
            q.pop();

        screen.update();

        if (!screen.process_events())
            break;
    }
    screen.close();

    return 0;
}


Point next_point(int tick)
{
    double theta1 = (1.0 + sin(tick * 0.0017)) * PI;     // [0, 2π]
    double theta2 = (1.0 + sin(tick * 0.0013)) * PI;     // [0, 2π]
    double theta3 = (1.0 + sin(tick * 0.0011)) * PI;     // [0, 2π]
    auto z = create_z(theta1, theta2, theta3);           // min, max: -1.75, 1.75
    return Point(z.real(), z.imag());
}


tuple<Uint8, Uint8, Uint8> next_color(int tick)
{
    Uint8 red =  127 * (1 + 0.5 * (1 + sin(tick * 0.0011))); // [127, 254]
    Uint8 green = 127 * (1 + 0.5 * (1 + sin(tick * 0.0007)));
    Uint8 blue = 127 * (1 + 0.5 * (1 + sin(tick * 0.0013)));
    return make_tuple(red, green, blue);
}
