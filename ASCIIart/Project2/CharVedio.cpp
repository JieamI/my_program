#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>
#include<Windows.h>
#include<iostream>
#include<conio.h>
#include <mmsystem.h>
#pragma comment(lib,"WinMM.Lib")
#pragma comment(lib, "Winmm.lib")
#include "cvedio.h"
using namespace std;

void CharVedio::Play()
{
	music(MusicPath);
	clock_t start = clock();
	for (int i = 0; i < TotalNum;)
	{
		int time;
		if (i % 30 == 0)
			time = 43;
		else
			time = 33;
		clock_t end = clock();
		if ((double)(end - start) / CLOCKS_PER_SEC * 1000 >= time)
		{
			view(i);
			i++;
			start += time;
		}
	}
}
void CharVedio::music(char *name)
{
	TCHAR shortName[50 * 8] = { 0 };
	GetShortPathName(name, shortName, sizeof(shortName) / sizeof(TCHAR));
	TCHAR cmd[MAX_PATH + 10];
	wsprintf(cmd, "play %s", name);
	
mciSendString(cmd, NULL, 0, NULL);
}
void CharVedio::view(int i)
{
		system("color 0A");
		HANDLE hout;
		COORD coord;
		coord.X = 0;
		coord.Y = 0;
		hout = GetStdHandle(STD_OUTPUT_HANDLE);
		SetConsoleCursorPosition(hout, coord);
		FILE*fp;
		char name[10];
		char path[100] = { 0 };
		strcat(path, VedioPath);
		int size;
		_itoa(i, name, 10);
		strcat(path, name);
		strcat(path, VedioNameTail);
		fp = fopen(path, "r");
		fseek(fp, 0L, 2);
		size = ftell(fp) + 1;
		fseek(fp, 0L, 0);
		char *buffer = (char*)malloc(size * sizeof(char));
		fread(buffer, SizeOfTxt, 1, fp);
		buffer[SizeOfTxt] = 0;
		cout << buffer;
		free(buffer);
		fclose(fp);
}
void CharVedio::SetTxtSize(int size)
{
	SizeOfTxt = size;
}
CharVedio::CharVedio(char *musicpath, char *vedioPath, char * vedioNameTail, int total)
{
	TotalNum = total;
	MusicPath = musicpath;
	VedioPath = vedioPath;
	VedioNameTail = vedioNameTail;
}