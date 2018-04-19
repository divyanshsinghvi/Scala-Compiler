class Demo(){
var aaaaa:Int;
def foo(var a:Int, var b:Int):Int ={
    //a = 1;
	println(a);
return a+b;
println(10000);
};

def foo2(var a:Int, var b:Int):Int ={
    //a = 1;
	var w:Int=this.foo(a,b);
	println(this.aaaaa);
return w;
println(10000);
};
};
class True(){
def main(var args:Int)={
    var a: Int=5;
    var b: Int=2;
    var k: Demo = new Demo();
    k.aaaaa = 1;
    var c: Int =k.foo2(a,b);
	println(20000);
	println(c);
    return 0;
};
};
// 1 20000 3
