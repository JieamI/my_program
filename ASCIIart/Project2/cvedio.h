#pragma once
class CharVedio
{
public:
	int TotalNum;
	char *MusicPath;
	char *VedioPath;
	char *VedioNameTail;
	int SizeOfTxt;

	CharVedio(char *musicpath, char *vedioPath, char * vedioNameTail, int total);
	void Play();
	void SetTxtSize(int size);
private:
	void music(char *name);
	void view(int i);
};

