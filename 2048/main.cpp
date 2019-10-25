/*W D N M D*/
#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdlib>
#include<conio.h>
#include<time.h>
using namespace std;

int _array[4][4] = { 0 };				// A global array designed for save datas 


//
void _Isrand(int times)
{
	srand((unsigned)time(NULL));
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (_array[i][j] == 0)
			{
				switch (rand() % 2)
				{
				case(0):_array[i][j] = 0; break;
				case(1): 
				{
					switch (rand() % 2)
					{
					case(0):_array[i][j] = 2; times--; break;
					case(1):_array[i][j] = 4; times--; break;
					}break;
				}
				}
			}
			if (!times)
				break;
		}
		if(!times)
			break;
	}
}

//To control the position of block
void logic_up()
{	
	for (int i = 0; i < 4; i++)				
	{
		int k = 0;
		for (int j = 0; j < 4; j++)
		{
			if (_array[j][i] != 0)
			{
				_array[k][i] = _array[j][i];
				if (k != j)
				{
					_array[j][i] = 0;
				}
				k++;
			}
		}
		for (int j = 0; j < 3; j++)				
		{
			if (_array[j][i] == _array[j + 1][i])
			{
				_array[j][i] = 2 * _array[j][i];
				_array[j + 1][i] = 0;
			}
		}
		k = 0;									
		for (int j = 0; j < 4; j++)
		{
			if (_array[j][i] != 0)
			{
				_array[k][i] = _array[j][i];
				if (k != j)
				{
					_array[j][i] = 0;
				}
				k++;
			}
		}
	}
}
void logic_down()
{
	for (int i = 0; i < 4; i++)				
	{
		int k = 3;
		for (int j = 3; j >= 0; j--)
		{
			if (_array[j][i] != 0)
			{
				_array[k][i] = _array[j][i];
				if (k != j)
				{
					_array[j][i] = 0;
				}
				k--;
			}
		}
		for (int j = 3; j > 0; j--)				
		{
			if (_array[j][i] == _array[j - 1][i])
			{
				_array[j][i] = 2 * _array[j][i];
				_array[j - 1][i] = 0;
			}
		}
		k = 3;									
		for (int j = 3; j >= 0; j--)
		{
			if (_array[j][i] != 0)
			{
				_array[k][i] = _array[j][i];
				if (k != j)
				{
					_array[j][i] = 0;
				}
				k--;
			}
		}
	}
}
void logic_left()
{
	for (int i = 0; i < 4; i++)				
	{
		int k = 0;
		for (int j = 0; j < 4; j++)
		{
			if (_array[i][j] != 0)
			{
				_array[i][k] = _array[i][j];
				if (k != j)
				{
					_array[i][j] = 0;
				}
				k++;
			}
		}
		for (int j = 0; j < 3; j++)				
		{
			if (_array[i][j] == _array[i][j + 1])
			{
				_array[i][j] = 2 * _array[i][j];
				_array[i][j + 1] = 0;
			}
		}
		k = 0;									
		for (int j = 0; j < 4; j++)
		{
			if (_array[i][j] != 0)
			{
				_array[i][k] = _array[i][j];
				if (k != j)
				{
					_array[i][j] = 0;
				}
				k++;
			}
		}
	}
}
void logic_right()
{
	for (int i = 0; i < 4; i++)				
	{
		int k = 3;
		for (int j = 3; j >= 0; j--)
		{
			if (_array[i][j] != 0)
			{
				_array[i][k] = _array[i][j];
				if (k != j)
				{
					_array[i][j] = 0;
				}
				k--;
			}
		}
		for (int j = 3; j > 0; j--)				
		{
			if (_array[i][j] == _array[i][j - 1])
			{
				_array[i][j] = 2 * _array[i][j];
				_array[i][j - 1] = 0;
			}
		}
		k = 3;									
		for (int j = 3; j >= 0; j--)
		{
			if (_array[i][j] != 0)
			{
				_array[i][k] = _array[i][j];
				if (k != j)
				{
					_array[i][j] = 0;
				}
				k--;
			}
		}
	}
}
//To help display display_helperction show datas beautifully
char* display_helper(int num)
{
	char* display_space = new char[5];				//open up memory to save space
	int temp = num / 10;
	int bit = 0;
	if (temp < 1)				
	{
		bit = 4;
	}
	else if (temp >= 1 && temp < 10)
	{
		bit = 3;
	}
	else if (temp >= 10 && temp < 100)
	{
		bit = 2;
	}
	else if (temp >= 100)
	{
		bit = 1;
	}
	switch (bit)
	{
	case(1):strcpy(display_space, " "); break;
	case(2):strcpy(display_space, "  "); break;
	case(3):strcpy(display_space, "   "); break;
	case(4):strcpy(display_space, "    "); break;
	}
	//char* s = display_space;
	
	return display_space;
}
//To display the datas in global array
void display()
{
	system("cls");
	cout << display_helper(_array[0][0])<< _array[0][0] << '|' << display_helper(_array[0][1]) << _array[0][1] << '|' << display_helper(_array[0][2]) << _array[0][2] << '|' << display_helper(_array[0][3]) << _array[0][3] << endl;
	cout << "-  -  -  -  -  -  -  -  -" << endl;
	cout << display_helper(_array[1][0]) << _array[1][0] << '|' << display_helper(_array[1][1]) << _array[1][1] << '|' << display_helper(_array[1][2]) << _array[1][2] << '|' << display_helper(_array[1][3]) << _array[1][3] << endl;
	cout << "-  -  -  -  -  -  -  -  -" << endl;
	cout << display_helper(_array[2][0]) << _array[2][0] << '|' << display_helper(_array[2][1]) << _array[2][1] << '|' << display_helper(_array[2][2]) << _array[2][2] << '|' << display_helper(_array[2][3]) << _array[2][3] << endl;
	cout << "-  -  -  -  -  -  -  -  -" << endl;
	cout << display_helper(_array[3][0]) << _array[3][0] << '|' << display_helper(_array[3][1]) << _array[3][1] << '|' << display_helper(_array[3][2]) << _array[3][2] << '|' << display_helper(_array[3][3]) << _array[3][3] << endl;
	cout << "-  -  -  -  -  -  -  -  -" << endl;
}

//Judge if the player has won
bool if_win()
{
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (_array[i][j] == 2048)
				return true;
			else
				return false;
		}
	}
}


//Control the run of the game
int main()
{
	while (1)
	{
		int _first = 1;
		while (1)
		{
			int ch = 0;
			if (_first)				//judge if it is at the begining of the game
			{
				_Isrand(2);
				display();
				_first = 0;
			}
			while (!_kbhit());
			ch = _getch();
			if (ch == 119 || ch == 115 || ch == 97 || ch == 100 || ch == 27)
			{
				int temp_array[4][4];
				int flag = 0;
				for(int i=0;i<4;i++)
				{
					for(int j=0;j<4;j++)
					{
						temp_array[i][j] = _array[i][j];
					}
				}
				switch (ch)
				{
				case(119):logic_up(); break;		
				case(115):logic_down(); break;	
				case(97):logic_left(); break;	
				case(100):logic_right(); break;	
				case(27):return 1; break;		
				}
				for(int i=0;i<4;i++)
				{
					for(int j=0;j<4;j++)
					{
						if(temp_array[i][j] != _array[i][j])
							flag = 1;
					}
				}
				if(flag)
				{
					if (if_win())
					{
						system("cls");
						cout << "Congratulation!!!(Press to continue)" << endl;
						while (!_kbhit());
						ch = _getch();				//clear buffer ,in case it affects the next game								
						memset(_array, 0, sizeof(_array));				//init array to prepare for the next game			
						break;
					}
					_Isrand(1);
					display();
				}
				else
				{
					system("cls");
					cout << "WDNMD!!!(Press to continue)" << endl;
					while (!_kbhit());
					ch = _getch();									
					memset(_array, 0, sizeof(_array));				
					break;
				}
			}
			
			
		}

	}
	return 0;
}