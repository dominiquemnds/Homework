#include <iostream>
#include <string>
#include <tuple>

void justForFun();//initilization of method used later

void doSomething(){//simple method declaration
	std::cout<<"Hi Bob\n";
} 

void repeatSomething(int i){//recursion method
 std::cout << i << "\n";
  i++;
  if(i<10) {
    repeatSomething(i);
  }
}

void takeTwo(int k, std::string y){
	std::cout<<k<<" "<<y<<"\n"; //prints both variables taken
	}
	

std::tuple<int, bool> foo(int first, bool second)
{
  return std::make_tuple(first, second);
}

void justForLoop(){
	bool stop=true;
	while(stop==true){
		int x;
		stop=false;
	}
}
int main()
{
	doSomething();
	justForFun();
	int k=0;
	repeatSomething(k);
	takeTwo(5,"Learning is fun!");
	
    int first;
    bool second;
    
    //auto [first, second] =foo(15, true);
    //std:: cout << first << ',' << second <<std:: endl;

	int x=5;
	bool stop=true;
	
	while(stop==true){
	    int x=0;//no conflict with repeating variables
	    std::cout<<x<<std::endl;//new variable is still 0
	    stop=false;
	}
	std::cout<<x;//old varibale is still the same
	return 0;
}

void justForFun(){
	std::cout<<"Isn't this fun?\n";
}
