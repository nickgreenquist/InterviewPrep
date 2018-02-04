/*
 * C++ Program to Convert Decimal to Binary Value
 */
 
 #include<iostream>
 #include <string>
 #include <stdlib.h>
 using namespace std;
  
 void binary(int num)
 {
     int rem;
  
     if (num <= 1)
     {
         cout << num;
         return;
     }
     rem = num % 2;
     binary(num / 2);
     cout << rem;
 }
  
 int main()
 {
     int dec, bin;
     string line;
     cin >> line;

     while(!line.empty()) {
        line >> dec;
        binary(dec);
        cout << endl;
        cin >> line;
     }
     return 0;
 }