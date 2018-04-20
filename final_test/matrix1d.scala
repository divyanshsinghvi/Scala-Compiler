class demo(){
def foo():Int={
    var d: Int =2;
    
    var m1:Array[Int](4)={1,2,3,4};
    var m2:Array[Int](4)={1,2,3,4};
    var m3:Array[Int](4)={1,2,3,4};
   var i:Int=1;
   var j:Int=2;
   var k:Int=3;
   var l:Int=4;

    for(i=0;i<4;i+=1)
    { 
      var q:Int =i;
      for(j=0;j<4;j+=1)
      {
        var q:Int = d;
        println(q);
      };
      println(q);
    };
    
    for(i=0;i<4;i+=1)
    {
        println(i);

};
    
    return j;
};
};

class test(){
  def main()={
  var d:demo = new demo();
  var l:Int = d.foo();
};};
//0 2 2 5
