#include <iostream>
#include<bits/stdc++.h>
using namespace std;
class Geeks
{
    // Access specifier
    public:
 
    // Data Members
    //string geekname;
    int a; 
    // Member Functions()
    void printname()
    {
        a= 3;
       printf("DS is awesome");
    }
};
 
int main() {
 
    // Declare an object of class geeks
    Geeks obj1;
 
    // accessing data member
    //obj1.geekname = "Abhi";
 
    // accessing member function
    obj1.printname();
    return 0;
}
