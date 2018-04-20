class Demo(){
    def main()={
    var i: Int = 0;
    var b: Int = 3;
    var c: Int = 2;
    var d: Int = 1000;
    var e: Int = 3;
    var f: Int = 2;
    var m: Array[Int](3,3)={};
    var a: Array[Int](2) = {d,c};
    m[1,1]=5555;
	m[1,1]+=1;
	b = m[1,1];
	println(b);
	if (i<=e){
	b = b + f;
        a[i]=a[i]+d;
	println(a[i]);
    };
    if (i<=f){
	b = b + c*f;
        a[i]=a[i]-d;
	println(a[i]);
    } else {
        b = d;
	println(b);
    };
	return 0;  
};
};
