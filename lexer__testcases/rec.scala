object Demo{
def foo(var a:Int, var b:Int):Int ={
	if(a == 0)
	{return 0;
	};
	var c:Int = foo(a-1,b-1);
	println(10000);
	return c;
};
def main()={
    var a: Int=5;
    var b: Int=4;
    var c: Int =foo(10,10);
	println(20000);
	println(c);
    return 0;
};
};
// 1 20000 3
