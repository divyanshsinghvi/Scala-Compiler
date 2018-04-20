class Demo(){
def foo(var a:Int, var b:Int):Int ={
	if(a == 0)
	{return 0;
	};
	var c:Int = this.foo(a-1,b-1);
	println(c);
	return a+b;
};
};

class test(){
def main()={
    var a: Int=5;
    var b: Int=4;
    var d:Demo = new Demo();
    var c: Int =d.foo(10,10);
	println(c);
    return 0;
};
};
// 1 20000 3
