object demo{
def main(var a:Int=2)={
    var i: Int =1;
    var j: Int = 2;
    var d: Int =2;
    for (i= 0;i<= 2; i=i+2){
	println(i);
        if (i>=2){
		var a:Int =3;
		var b:Int =2;
		a+= b;
            println(a);
        }
        else{
		d  += i;
            println(d);
        };
    };
    return j;
};
};
//0 2 2 5
