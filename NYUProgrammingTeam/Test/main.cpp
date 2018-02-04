#include<stdio.h>
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

struct Letter{
    char c;
    int value;
};

string int_to_str(long long int num)
{
    stringstream ss;

    ss << num;

    return ss.str();
}

int main()
{
    int n; //number of tests
    cin >> n;
    int groups = 0;
    int magL = 0;
    int mag = 0;
    for(int i = 0; i < n; i++){
        magL = mag;
        cin >> mag;
        if(mag != magL){
            groups++;
        }
    }
    cout << groups;

    return 0;
}


