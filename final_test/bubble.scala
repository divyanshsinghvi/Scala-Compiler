class Demo(){

   def sort(var arr:Array[Int](7)={}, var len:Int):Int= { 
    var n:Int = len;
    var temp:Int;
    var i:Int;
    var j:Int;
    for(i=0; i < n; i+=1){
        for(j=1; j < (n-i); j+=1){
            var k:Int= j-1;
            if(arr[k] > arr[j]){
                    temp = arr[k];
                    arr[k] = arr[j];
                    arr[j] = temp;
                };
            };
        };
     
     
     return 1;
    };
};

class test(){
  
  def main()={
    var arr: Array[Int](7)={14,12,1,4,15,6,7};
    var obj:Demo = new Demo();
    var x : Int = obj.sort(arr,7);
    var i:Int;
    for(i=0;i<7;i+=1){
      println(arr[i]);
    };
    return 0;
};
};
//0 2 2 5
