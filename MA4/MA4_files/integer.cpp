#include <cstdlib>
// Integer class 

class Integer{
public:
	Integer(int);
	int get();
	void set(int);
	int start_fib();
private:
	int fib(int n);
	int val;
};
 
Integer::Integer(int n){
	val = n;
}
 
int Integer::get(){
	return val;
}
 
void Integer::set(int n){
	val = n;
}

int Integer::start_fib() {
	return fib(val);
}

int Integer::fib(int n) {
	if (n <= 1) {
		return n;
	} else {
		return fib(n - 1) + fib(n - 2);
	}
}


extern "C"{
	Integer* Integer_new(int n) {return new Integer(n);}
	int Integer_get(Integer* integer) {return integer->get();}
	void Integer_set(Integer* integer, int n) {integer->set(n);}
	int Integer_start_fib(Integer* integer) {return integer->start_fib();};
	void Integer_delete(Integer* integer){
		if (integer){
			delete integer;
			integer = nullptr;
			}
		}
	}
	
	// int Integer_fib(Integer* integer, int n) {return };