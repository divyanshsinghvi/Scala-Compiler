class Demo(){
def foo(var a:Int,var b:Int):Int={ 	
  println(a);
  a=a-1;
  b=b-1;
  println(this.foo(a,b));
  return b;
println(10000);
};

def main()={
    var a: Int=2;
    var b: Int=3;
    var c: Int =this.foo(b,a);
	println(20000);
	println(c);
    return 0;
};
};
// 1 20000 3
