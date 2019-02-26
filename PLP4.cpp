#include <iostream>
#include <vector>

using namespace std;


int main(){

int x=5;
int y=10;

if (x<y)
	cout<<"The if statement works"<<endl;


if(x<y and x>0)
	cout<<"The multi-conditional if statement works"<<endl;

while(x<y){
	x++;
	cout<<x<<endl;
	}
cout<<"The while statement works"<<endl;
	
do{
	y++;
	cout<<y<<endl;
	
}
while(y<20);

cout<<"The do while works"<<endl;
	
for(int i=0;i<10;i++){
	if(i==9){
		cout<<"This for loop works"<<endl;
	}
}

int arr[] = { 10, 20, 30, 40 }; 

    for (int x : arr) 
        cout << x << endl;
        
cout<<"The for-each loop works"<<endl;


switch(1){
	case 1: cout<<"This switch statement works!";
	break;
	case 2: cout<<"This code shouldn't execute";
	break;
}

}


