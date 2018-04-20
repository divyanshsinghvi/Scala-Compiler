class Demo(){
def foo(var a:Int, var b:Int,var c:Int,var d:Int,var e:Int,var f:Int, var g:Int,var h:Int,var i:Int,var j:Int):Int ={
	return a+b+c+d+e+f+g+h+i+j;
};
};

class test(){
def main()={
    var a: Int=5;
    var b: Int=4;
    var d:Demo = new Demo();
    var c: Int =d.foo(1,2,3,4,5,6,7,8,9,10);
	println(c);
    return 0;
};
};
// 1 20000 3
