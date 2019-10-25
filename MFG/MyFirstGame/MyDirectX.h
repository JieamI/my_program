#pragma once
#define WIN32_EXTRA_LEAN
#define DIRECTINPUT_VERSION 0x800

//链接库
#pragma comment(lib,"winmm.lib")
#pragma comment(lib,"user32.lib")
#pragma comment(lib,"gdi32.lib")
#pragma comment(lib,"dxguid.lib")
#pragma comment(lib,"d3d9.lib")
#pragma comment(lib,"d3dx9.lib")
#pragma comment(lib,"dinput8.lib")
#pragma comment(lib,"xinput.lib")

//头文件
#include<Windows.h>
#include<d3d9.h>
#include<d3dx9.h>
#include<dinput.h>
#include<xinput.h>
#include<ctime>
#include<iostream>
#include<iomanip>
#include<sstream>
#include<math.h>
using namespace std;

//程序相关值
extern const string APPTITLE;
extern const int SCREENW;
extern const int SCREENH;
extern bool gameover;

//DirectX3D 对象
extern LPDIRECT3D9 d3d;
extern LPDIRECT3DDEVICE9 d3ddev;
extern LPDIRECT3DSURFACE9 backbuffer;
extern LPD3DXSPRITE sprite;

//DirectX3D 函数
bool Direct3D_Init(HWND Hwnd, int width, int height, bool fullscreen);
void Direct3D_End();
void DrawSurface(LPDIRECT3DSURFACE9 dest, float x, float y, LPDIRECT3DSURFACE9 source);
LPDIRECT3DSURFACE9 LoadSurface(string filename);
D3DXVECTOR2 GetBitmapSize(string filename);
LPDIRECT3DTEXTURE9 LoadTexture(string filename, D3DCOLOR transcolor = D3DCOLOR_XRGB(255, 0, 0));
//void LoadSurfaceToScreen(string filename, LPDIRECT3DSURFACE9 dest, float x, float y);

//Direct输入对象，设备和状态
extern LPDIRECTINPUT8 dinput;
extern LPDIRECTINPUTDEVICE8 dimouse;
extern LPDIRECTINPUTDEVICE8 dikeyboard;
extern DIMOUSESTATE mouse_state;


//Direct输入函数
bool DirectInput_Init(HWND);
void DirectInput_Update();
void DirectInput_End();
int Key_Down(int);
int Mouse_Button(int);		
int Mouse_X();
int Mouse_Y();



//游戏实现方法
void Game_Music(char*name);
bool Game_Init(HWND window);
void Game_Run(HWND window);
void Game_End();
