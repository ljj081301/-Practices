#include "stdafx.h"
#include <iostream>
#include <string>

using namespace std;

int main()
{
	string alpabet;
	int asci[] = { 97, 98, 99 };

	
	while (true)
	{
		int alpa_num = 999;
		cout << "\n알파벳을 입력하세요.(a~z, A~Z):" << endl;
		cin >> alpabet;

		while (true)
		{
			if (alpabet == "a")
			{
				alpa_num = 0;
				break;
			}

			else if (alpabet == "b")
			{
				alpa_num = 1;
				break;
			}

			else if (alpabet == "c")
			{
				alpa_num = 2;
				break;
			}

			else
			{
				cout << "a~z, A~Z의 알파벳만 입력해주세요." << endl;
				cin >> alpabet;
				continue;
			}
		}
		

		cout << alpabet << "의 아스키코드는 " << asci[alpa_num] << "입니다." << endl;
	}

    return 0;
}

