#include"MyDirectX.h"
LPDIRECT3D9 d3d = NULL;
LPDIRECT3DDEVICE9 d3ddev = NULL;
LPDIRECT3DSURFACE9 surface = NULL;
LPDIRECT3DSURFACE9 backbuffer = NULL;
LPDIRECTINPUT8 dinput = NULL;
LPDIRECTINPUTDEVICE8 dimouse = NULL;
LPDIRECTINPUTDEVICE8 dikeyboard = NULL;
DIMOUSESTATE mouse_state;
char keys[256];


void Game_Music(char *name)
{
	TCHAR shortName[50 * 8] = { 0 };
	GetShortPathName(name, shortName, sizeof(shortName) / sizeof(TCHAR));
	TCHAR cmd[MAX_PATH + 10];
	wsprintf(cmd, "play %s", name);

	mciSendString(cmd, NULL, 0, NULL);
}
bool Direct3D_Init(HWND hwnd, int width, int height, bool fullscreen)
{
	//初始化 Direct3D
	d3d = Direct3DCreate9(D3D_SDK_VERSION);
	if (d3d == NULL)
	{
		MessageBox(hwnd, "Error initializing Direct3D", "Error", MB_OK);
		return false;
	}
	//设置 Direct3D 显示参数
	D3DPRESENT_PARAMETERS d3dpp;
	ZeroMemory(&d3dpp, sizeof(d3dpp));
	d3dpp.Windowed = (!fullscreen);
	d3dpp.SwapEffect = D3DSWAPEFFECT_DISCARD;
	d3dpp.BackBufferFormat = D3DFMT_X8R8G8B8;
	d3dpp.BackBufferCount = 1;
	d3dpp.BackBufferWidth = width;
	d3dpp.BackBufferHeight = height;
	d3dpp.hDeviceWindow = hwnd;
	
	//创建 Direct3D 设备
	d3d->CreateDevice(D3DADAPTER_DEFAULT, D3DDEVTYPE_HAL, hwnd, D3DCREATE_SOFTWARE_VERTEXPROCESSING, &d3dpp, &d3ddev);
	if (!d3ddev)
	{
		MessageBox(hwnd, "Error creating Direct3D device", "Error", MB_OK);
		return false;
	}
	d3ddev->Clear(0, NULL, D3DCLEAR_TARGET, D3DCOLOR_XRGB(0, 0, 0), 1.0f, 0);
	d3ddev->GetBackBuffer(0, 0, D3DBACKBUFFER_TYPE_MONO, &backbuffer);
	//创建精灵对象
	D3DXCreateSprite(d3ddev, &sprite);
	return true;
}	
void Direct3D_End()
{
	if (d3ddev)	d3ddev->Release();
	if (d3d)	d3d->Release();
	if (sprite)	sprite->Release();
}

//渲染表面到屏幕上
void DrawSurface(LPDIRECT3DSURFACE9 dest, float x, float y, LPDIRECT3DSURFACE9 source)
{
	D3DSURFACE_DESC desc;
	source->GetDesc(&desc);

	RECT source_rect = { 0,0,desc.Width,desc.Height };
	RECT dest_rect = { x,y,x + desc.Width,y + desc.Height };
	d3ddev->StretchRect(source, &source_rect, dest, &dest_rect, D3DTEXF_NONE);	
}
//加载位图到表面
LPDIRECT3DSURFACE9 LoadSurface(string filename)
{
	LPDIRECT3DSURFACE9 image = NULL;
	D3DXIMAGE_INFO info;
	HRESULT result = D3DXGetImageInfoFromFile(filename.c_str(), &info);
	if (result != D3D_OK)
		return NULL;
	result = d3ddev->CreateOffscreenPlainSurface(info.Width, info.Height, D3DFMT_X8R8G8B8, D3DPOOL_DEFAULT, &image, NULL);
	if (result != D3D_OK)
		return NULL;
	result = D3DXLoadSurfaceFromFile(
		image,
		NULL,		//调色板
		NULL,
		filename.c_str(),
		NULL,
		D3DX_DEFAULT,		//过滤方式
		D3DCOLOR_XRGB(0, 0, 0),		//透明度
		NULL);
	if (result != D3D_OK)
		return NULL;
	return image;
	}
//加载精灵图像
LPDIRECT3DTEXTURE9 LoadTexture(string filename, D3DCOLOR transcolor)
{
	LPDIRECT3DTEXTURE9 texture = NULL;
	D3DXIMAGE_INFO info;
	HRESULT result = D3DXGetImageInfoFromFile(filename.c_str(), &info);
	if (result != D3D_OK)	return NULL;
	
	D3DXCreateTextureFromFileEx(
		d3ddev, 
		filename.c_str(), 
		info.Width, 
		info.Height, 
		1, 
		D3DPOOL_DEFAULT, 
		D3DFMT_UNKNOWN, 
		D3DPOOL_DEFAULT, 

		D3DX_DEFAULT, 
		D3DX_DEFAULT, 
		transcolor, 
		&info, 
		NULL, 
		&texture);
	if (result != D3D_OK)	return NULL;
	return texture;
}
//获取位图尺寸
D3DXVECTOR2 GetBitmapSize(string filename)
{
	D3DXIMAGE_INFO info;
	D3DXVECTOR2 size = D3DXVECTOR2(0.0f, 0.0f);
	HRESULT result = D3DXGetImageInfoFromFile(filename.c_str(), &info);
	if (result == D3D_OK)
		size = D3DXVECTOR2((float)info.Width, (float)info.Height);
	else
		size = D3DXVECTOR2((float)info.Width, (float)info.Height);
	return size;
}

	//加载图片并渲染到屏幕
//void LoadSurfaceToScreen(string filename, LPDIRECT3DSURFACE9 dest, float x, float y)
//{
//	D3DSURFACE_DESC desc;
//	LPDIRECT3DSURFACE9 source=NULL;
//	D3DXIMAGE_INFO info;
//	HRESULT result = D3DXGetImageInfoFromFile(filename.c_str(), &info);
//	if (result != D3D_OK)
//		MessageBox(NULL, "渲染出错", "ERROR", 0);
//	result = d3ddev->CreateOffscreenPlainSurface(info.Width, info.Height, D3DFMT_X8R8G8B8, D3DPOOL_DEFAULT, &source, NULL);
//	if (result != D3D_OK)
//		MessageBox(NULL, "渲染出错", "ERROR", 0);
//	result = D3DXLoadSurfaceFromFile(
//		source,
//		NULL,		//调色板
//		NULL,
//		filename.c_str(),
//		NULL,
//		D3DX_DEFAULT,		//过滤方式
//		D3DCOLOR_XRGB(255, 255, 255),		//透明度
//		NULL);
//	if (result != D3D_OK)
//		MessageBox(NULL, "渲染出错", "ERROR", 0);
//	source->GetDesc(&desc);
//	RECT source_rect = { 0,0,desc.Width,desc.Height };
//	RECT dest_rect = { x,y,x + desc.Width,y + desc.Height };
//	d3ddev->StretchRect(source, &source_rect, dest, &dest_rect, D3DTEXF_NONE);
//}

//DirectInput 初始化
bool DirectInput_Init(HWND hwnd)
{
	HRESULT result = DirectInput8Create(
		GetModuleHandle(NULL),
		DIRECTINPUT_VERSION,
		IID_IDirectInput8,
		(void**)&dinput,
		NULL);
	//初始化键盘
	dinput->CreateDevice(GUID_SysKeyboard, &dikeyboard, NULL);
	dikeyboard->SetDataFormat(&c_dfDIKeyboard);
	dikeyboard->SetCooperativeLevel(hwnd, DISCL_NONEXCLUSIVE | DISCL_FOREGROUND);
	dikeyboard->Acquire();
	//初始化鼠标
	dinput->CreateDevice(GUID_SysMouse, &dimouse, NULL);
	dimouse->SetDataFormat(&c_dfDIMouse);
	dimouse->SetCooperativeLevel(hwnd, DISCL_NONEXCLUSIVE | DISCL_FOREGROUND);
	dimouse->Acquire();
	d3ddev->ShowCursor(false);
	return true;
}

//DirectInput 更新
void DirectInput_Update()
{
	dimouse->GetDeviceState(sizeof(mouse_state), (LPVOID)&mouse_state);
	dikeyboard->GetDeviceState(sizeof(keys), (LPVOID)&keys);
}
//返回鼠标的运动
int Mouse_X()
{
	return mouse_state.lX;
}
int Mouse_Y()
{
	return mouse_state.lY;
}
int Mouse_Button(int button)
{
	return mouse_state.rgbButtons[button] & 0x80;
}
int Key_Down(int key)
{
	return(keys[key] & 0x80);
}


//DirectInput 结束
void DirectInput_End()
{
	if (dikeyboard)
	{
		dikeyboard->Unacquire();
		dikeyboard->Release();
		dikeyboard = NULL;
	}
	if (dimouse)
	{
		dimouse->Unacquire();
		dimouse->Release();
		dimouse = NULL;
	}
}









