object Demo {
    def main(args: Array[String](2))={
    var i: Int = 0;
    var b: Int = 3;
    var c: Int = 2;
    var d: Int = 1;
    var e: Int = 3;
    var f: Int = 2;

    var a: Array[Int](2) = {d,c};
    if (i<=e){
	b = b + f;
        a[i]=a[i]+d;
	println(a[i]);
    };
    if (i>=f){
	b = b + c*f;
        a[i]=a[i]-d;
	println(a[i]);
    } else {
        b = d;
	println(b);
    };
  };
};
