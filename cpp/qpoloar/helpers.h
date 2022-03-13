#pragma once
#include "global.h"

#include <SDL2/SDL.h>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <tuple>

//#include <cmath>
//#include <complex>
#include <random> 
//#include <chrono>
//#include <thread>
//#include <memory>
//#include <utility>
//using std::this_thread::sleep_for;
//using std::chrono::milliseconds;

using std::cout; using std::setw; using std::ostream; using std::hex;
using std::sin; using std::abs;
using std::sqrt; using std::pow;
using std::tuple; using std::make_tuple;


constexpr Uint32 black = 0x000000ff;
constexpr Uint32 white = 0xffffffff;


int random_int(int lo, int hi);
SDL_Color to_sdl_color(Uint8, Uint8, Uint8, Uint8=0xff);
tuple<uint8_t, uint8_t, uint8_t> get_rgb(SDL_Color);
void draw_point(SDL_Renderer *renderer, int x, int y, int radius, Uint8 r, Uint8 g, Uint8 b);
void draw_line(SDL_Renderer* renderer, int x1, int y1, int x2, int y2,
               Uint8 r, Uint8 g, Uint8 b);

/*
vector<double> linspace(double start, double stop, size_t N);
double distance(int x1, int y1, int x2, int y2);
double square(double n);
double cube(double n);
double cube_root(double n);
void sleep(int n);
bool toggle_10();
SDL_Color random_color();
*/
