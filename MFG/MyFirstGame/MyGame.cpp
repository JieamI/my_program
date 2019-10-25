#include"MyDirectX.h"
#define Image1Wid 50
#define Image1Hei 50
#define Image2Wid 150
#define Image2Hei 150
float a = 1.0, b = 0.5;
const string APPTITLE = "KUNKUN CATCHER";
const int SCREENW = 1024;
const int SCREENH = 768;
char Music_Path[] = "JNTM.mp3";
//LPDIRECT3DSURFACE9 ball_surf = NULL;
//LPDIRECT3DSURFACE9 kun_surf = NULL;
//LPDIRECT3DSURFACE9 bucket_surf = NULL;
LPDIRECT3DSURFACE9 BackGround = NULL;
LPDIRECT3DTEXTURE9 image_ball = NULL;
LPDIRECT3DTEXTURE9 image_bucket = NULL;
LPDIRECT3DTEXTURE9 image_kun = NULL;
LPD3DXSPRITE sprite = NULL;

struct  Ball
{
	float x, y;
	void reset()
	{
		x = (float)(rand() % (SCREENW-Image1Wid));
		y = 0;
	}
};
Ball ball,kun;
struct BUCKET
{
	float x, y;
}bucket;
int score = 0;
bool Game_Init(HWND window)
{
	Game_Music(Music_Path);
	Direct3D_Init(window, SCREENW, SCREENH, false);
	DirectInput_Init(window);
	image_ball = LoadTexture("ball.png");
	if (!image_ball)
	{
		MessageBox(window, "Error loading ball", "Error", 0);
		return false;
	}
	image_bucket = LoadTexture("bucket.png");
	if (!image_bucket)
	{
		MessageBox(window, "Error loading bucket", "Error", 0);
		return false;
	}
	image_kun = LoadTexture("kun.png");
	if (!image_kun)
	{
		MessageBox(window, "Error loading kun", "Error", 0);
		return false;
	}

	BackGround = LoadSurface("BackGround.png");
	if (!BackGround)
	{
		MessageBox(window, "Error loading BackGround", "Error", 0);
		return false;
	}
	/*ball_surf = LoadSurface("ball.png");
	if (!ball_surf)
	{
		MessageBox(window, "Error loading bomb", "Error", 0);
		return false;
	}
	kun_surf = LoadSurface("kun.png");
	if (!kun_surf)
	{
		MessageBox(window, "Error loading kun", "Error", 0);
		return false;
	}
	bucket_surf = LoadSurface("bucket.png");
	if (!bucket_surf)
	{
		MessageBox(window, "Error loading bucket", "Error", 0);
		return false;
	}*/
	d3ddev->GetBackBuffer(0, 0, D3DBACKBUFFER_TYPE_MONO, &backbuffer);

	srand((unsigned int)time(NULL));
	score = 0;
	a = 1.5; 
	b = 0.5;
	ball.reset();
	kun.reset();
	while (fabs(ball.x - kun.x) < 140||ball.x < 90||ball.x > 934 )
	{
		ball.reset();
		kun.reset();
	}

	bucket.x = (SCREENW - (Image2Wid / 2)) / 2;
	bucket.y = SCREENH - Image2Hei;
	return true;	
}

void Game_Run(HWND window)
{
	if (!d3ddev)	return;
	DirectInput_Update();
	ball.y += a;
	kun.y += b;
	
	
	//使用鼠标移动篮子
	int mx = Mouse_X();
	if (mx < 0)
		bucket.x -=5.0f;
	else if (mx > 0)
		bucket.x += 5.0f;
	//使用键盘移动篮子
	if (Key_Down(DIK_LEFT))	bucket.x -= 5.0f;
	else if (Key_Down(DIK_RIGHT))	bucket.x += 5.0f;
	//确保篮球能阻碍篮子运动
	if (ball.y + Image1Hei > bucket.y&&bucket.x < ball.x+Image1Wid&&bucket.x+Image2Wid>ball.x + Image1Wid&&bucket.x>ball.x)
		bucket.x = ball.x+Image1Wid;
	if (ball.y + Image1Hei > bucket.y&&bucket.x + Image2Wid > ball.x&&bucket.x<ball.x&&bucket.x+Image2Wid<ball.x+Image1Wid)
		bucket.x = ball.x - Image2Wid;
	//判断篮子是否接到篮球以及篮球是否落地
	if (ball.y + Image1Hei > SCREENH)
	{
		UINT nRet = MessageBox(NULL, "请你出去你个假粉丝！（是否重试？）", "律师函警告！", MB_OKCANCEL | MB_ICONERROR);
		if (nRet == IDOK)
		{
			Game_Init(window);
		}
		else if (nRet == IDCANCEL)
			gameover = true;
	}																//篮球落地
	int bx = ball.x + Image1Wid;
	int by = ball.y + Image1Hei; 
	if (bucket.x<ball.x && bucket.x+Image2Wid> bx && by>bucket.y)
	{
		score++;
		a += 0.1;
		b += 0.2;
		ostringstream os;
		os << APPTITLE << "[Ikun指数：" << score << "]";
		string scoreStr = os.str();
		SetWindowText(window, scoreStr.c_str());
		ball.reset();
		while (fabs(ball.x - kun.x) < 140 || ball.x < 90 || ball.x > 934)
			ball.reset();
	}																//接到篮球
	//判断是否接到坤坤以及坤坤是否落地
	int cx = kun.x + Image1Wid;
	int cy = kun.y + Image1Hei;
	if (bucket.x<kun.x && bucket.x + Image2Wid> cx && cy > bucket.y && kun.y<bucket.y)
	{
		UINT nRet = MessageBox(NULL, "请你出去你个假粉丝！（是否重试？）", "律师函警告！", MB_OKCANCEL | MB_ICONERROR);
		if (nRet == IDOK)
		{
			Game_Init(window);
		}
		else if (nRet == IDCANCEL)
			gameover = true;
	}																//接到坤坤
	if (kun.y + Image1Hei > SCREENH)
	{
		kun.reset();
		while (fabs(ball.x - kun.x) < 140)
		{
			kun.reset();
		}
	}																//坤坤落地
	//确保篮子在窗口内
	if (bucket.x < 0)	bucket.x = SCREENW - Image2Wid;
	if (bucket.x + Image2Wid > SCREENW)	bucket.x = 0;
	
	DrawSurface(backbuffer, 0, 0, BackGround);
	
	//开始渲染
	if (d3ddev->BeginScene())
	{
		

		D3DXVECTOR3 _ball(ball.x, ball.y,0);
		D3DXVECTOR3 _kunkun(kun.x, kun.y,0);
		D3DXVECTOR3 _bucket(bucket.x, bucket.y, 0);
		sprite->Begin(D3DXSPRITE_ALPHABLEND);
		sprite->Draw(image_ball, NULL, NULL, &_ball, D3DCOLOR_XRGB(255, 255, 255));
		sprite->Draw(image_kun, NULL, NULL, &_kunkun, D3DCOLOR_XRGB(255, 255, 255));
		sprite->Draw(image_bucket, NULL, NULL, &_bucket, D3DCOLOR_XRGB(255, 255, 255));
		sprite->End();

		d3ddev->EndScene();
		d3ddev->Present(NULL, NULL, NULL, NULL);
	}
	if (Key_Down(DIK_ESCAPE))
		gameover = true;
}
void Game_End()
{
	image_ball->Release();
	image_bucket->Release();
	image_kun->Release();
	DirectInput_End();
	Direct3D_End();
}




