class Demo(){
var d:Int;
var e:Int;
var f:Int;
def foo(var a:Int, var b:Int):Int ={
    a = 1;
	println(a);
return a+b;
println(10000);
};
};
class Qwer() extends Demo{
	var e:Int;
	var f:Int;
	def foo2(var z:Int):Int={
	//return z;
		return	z + this.d + this.e;
		
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
	var c:Qwer = new Qwer();
    c.f = 123;
	c.e=4;
c.d = 23;
    var d: Int = c.foo2(a);
    println(d);
    //var c: Int =foo(a,b);
	println(20000);
//	println(c);
    return 0;
};
};

// 1 20000 3
