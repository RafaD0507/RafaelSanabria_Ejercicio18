#include <iostream>

using namespace std;

int main(){
float y = 1;
float h = 0.1;
int N = 3/h;
float x = 0;
 
for(int i=0;i<=N;i++){
  cout << x << " " << y << endl;
  x = x+h;
  y = y-h*y;
  
}
}
