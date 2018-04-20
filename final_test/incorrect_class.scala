class Demo(){
	var d:Int;
	var e:Int;
	var f:Int;
	def foo(var a:Int, var b:Int):Int ={
	println(1000);
	return a+b;
	};
};


class Qwer() extends Demo{
	var e:Int;
	var f:Int;
	def foo(var z:Int):Int={
	println(2000);
		return	z + this.d + this.e;
		
	};

};
class Dream() extends Qwer{
	var p:Int;
	def foo(var z:Int):Int={
	println(3000);
	return	this.c+z + this.d + this.e + this.p;
		
	};

};
class True(){
def main(var args:Int)={
    var a: Int=1;
    var b: Int=2;
    var c:Dream = new Dream();
    c.f = 1;
    c.e = 300;
    c.d = 13;
    c.p = 20000;
    var d: Int = c.foo(a);
    println(d);
    return 0;
};
};

