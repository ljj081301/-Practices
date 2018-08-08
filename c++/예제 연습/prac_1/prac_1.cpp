
//https://www.acmicpc.net/step

#include "stdafx.h"
#include <iostream>
#include <stdlib.h>
#include <Windows.h>

using namespace std;

void num_sprint() //N 찍기
{
	int i;
	cout << "정수를 입력하세요.:";
	cin >> i;

	for (int n = 3; n>0; n--)
	{
		cout << i << endl;
		i++;
		Sleep(400);
	}

	Sleep(1000);

	for (i > 0; i--;)
	{
		cout << i << endl;
		Sleep(50);
	}
}


void gugudan() //구구단
{
	int dan;
	cout << "구구단 몇단을 실행할까요?:";
	cin >> dan;

	for (int gop = 1; gop < 10; gop++)
	{
		cout << dan << " * " << gop << " = " << dan * gop << endl;
	}

}

void star_sprint() //별 찍기
{
	int star_count;
	cout << "별을 몇줄 만들까요?:";
	cin >> star_count;

	for (star_count > 0; star_count--;) {

		for (int n = 0; n < star_count; n++); {
			cout << "★";
		}

		cout << endl;
	}
}

int main() //실행 희망시 주석표시 제거할 것
{
	cout << "for문 관련 예제 모음" << endl;


	//////////

	num_sprint();

	gugudan();

	star_sprint();

	//////////


	system("PAUSE");

	return 0;
}