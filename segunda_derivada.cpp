#include <iostream>

using namespace std;

int main(){
float y = 1;
float z = 0;
float h = 0.1;
int N = 10/h;
float x = 0;
 
for(int i=0;i<=N;i++){
  cout << x << " " << y << " " << z << endl;
  z = z-h*y;
  y = y+h*z;
  x = x+h;
}
}
