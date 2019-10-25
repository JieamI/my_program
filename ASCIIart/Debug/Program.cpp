#include "cvedio.h"
#include<iostream>

int main()
{
	char musicpath[] = "m.wav";
	char vediopath[] = "BA (";
	char tail[] = ").txt";
	int total = 6571;
	CharVedio vedio = CharVedio(musicpath, vediopath, tail, total);
	vedio.SetTxtSize(1920);
	vedio.Play();
	system("pause");
	return 0;
}