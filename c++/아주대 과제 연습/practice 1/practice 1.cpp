

#include "stdafx.h"
#include "stdlib.h"
#include <iostream>

using namespace std;

int sum(int, int), minuss(int, int), multi(int, int), mok(int, int);


int sum(int n1, int n2)
{
	return n1 + n2;
}

int minuss(int n1, int n2)
{
	return n1 - n2;
}

int multi(int n1, int n2)
{
	return n1 * n2;
}

int mok(int n1, int n2)
{
	return n1 / n2;
}


int main()
{
	int num_1;
	int num_2;
	
	cout << "두 정수의 합, 차, 몫, 나머지를 구하는 프로그램 입니다.\n" << endl;
	cout << "첫번째 정수 입력:";
	cin >> num_1;
	cout << "두번째 정수 입력:";
	cin >> num_2;

	cout << "--------------------" << endl;
	cout << "합 :" << sum(num_1, num_2) << endl;
	cout << "차 :" << minuss(num_1, num_2) << endl;
	cout << "곱 :" << multi(num_1, num_2) << endl;
	cout << "몫 :" << mok(num_1, num_2) << endl;
	cout << "나머지 :" << num_1 % num_2 << endl;
	cout << "--------------------" << endl;

	system("PAUSE");

    return 0;
}

