object Demo {
    def main(args: Array[String])={
    var i: Int = 0;
    Array[Int] a={1,2,3};
    if (i<=3){
        a[i]=a[i]+1;
    };
    if (i>=2){
        a[i]=a[i]-1;
    } else {
        a[i] = 1;
    };
  };
}