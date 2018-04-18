#include <bits/stdc++.h>
using namespace std;
 
//Base class
class Parent
{
    public:
      int id_p=5;
};
  
// Sub class inheriting from Base Class(Parent)
class Child : public Parent
{
    public:
};
 
//main function
int main() 
   {
      
        Child obj1;
          
        // An object of class child has all data members
        // and member functions of class parent
        printf("%d",obj1.id_p);
//        cout << "Child id is " <<  obj1.id_c << endl;
//       cout << "Parent id is " <<  obj1.id_p << endl;
         
        return 0;
   } 
