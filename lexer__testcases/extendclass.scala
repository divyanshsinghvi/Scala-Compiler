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
	var c:Int;
	var p:Int;
	def foo(var z:Int):Int={
//return z+ this.e;
	println(3000);
	return z + this.e+this.p;
	//	return	z + this.d + this.e + this.p+this.c;
		
	};

};
class True(){
var a: Int;
var b: Int;
var c: Int;
def main(var args:Int)={
    var a: Int=5;
    var b: Int=4;
    var r: Int =1;
    var x: Int =1;
	var c:Dream = new Dream();
    c.f = 123;
	c.e=4;
c.d = 23;
c.p = 212;
c.c = 13;
    var d: Int = c.foo(a);
    println(d);
    //var c: Int =foo(a,b);
	println(20000);
//	println(c);
    return 0;
};
};

// 1 20000 3
