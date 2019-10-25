#include"MyDirectX.h"

bool gameover = false;

LRESULT WINAPI WinProc(HWND hwnd, UINT msg, WPARAM wparam, LPARAM lparam)
{
	switch (msg)
	{
	case WM_DESTROY:
		gameover = true;
		PostQuitMessage(0);
		return 0;
	}
	return DefWindowProc(hwnd, msg, wparam, lparam);
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
	WNDCLASSEX wc;
	wc.cbSize = sizeof(WNDCLASSEX);
	wc.style = CS_HREDRAW | CS_VREDRAW;
	wc.lpfnWndProc = (WNDPROC)WinProc;
	wc.cbClsExtra = 0;
	wc.cbWndExtra = 0;
	wc.hInstance = hInstance;
	wc.hIcon = NULL;
	wc.hCursor = LoadCursor(NULL, IDC_ARROW);
	wc.hbrBackground = (HBRUSH)GetStockObject(WHITE_BRUSH);
	wc.lpszMenuName = NULL;
	wc.lpszClassName = "MyWindowClass";
	wc.hIconSm = NULL;
	RegisterClassEx(&wc);


	HWND Wnd = CreateWindow("MyWindowClass", APPTITLE.c_str(), WS_OVERLAPPEDWINDOW, CW_USEDEFAULT, CW_USEDEFAULT, SCREENW, SCREENH, NULL, NULL, hInstance, NULL);
	/*试试全屏？*/
	//HWND Wnd = CreateWindow("MyWindowClass", APPTITLE.c_str(), WS_EX_TOPMOST | WS_POPUP, 0, 0, 640, 480, (HWND)NULL, (HMENU)NULL, hInstance, (LPVOID)NULL);
	if (Wnd == 0) MessageBox(Wnd, "Error creating Window", "Error", MB_OK);
	ShowWindow(Wnd, nCmdShow);
	UpdateWindow(Wnd);

	if (!Game_Init(Wnd))	return 0;

	//消息循环
	MSG msg;
	while (!gameover)
	{
		if (PeekMessage(&msg, NULL, 0, 0, PM_REMOVE))
		{
			TranslateMessage(&msg);
			DispatchMessage(&msg);
		}
		Game_Run(Wnd);
	}
	Game_End();
	return msg.wParam;

}

