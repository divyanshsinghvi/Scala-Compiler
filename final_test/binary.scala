class Demo(){

   def binarySearch(var inputArr:Array[Int](7)={}, var len:Int, var key:Int):Int= {
        var start:Int = 0;
        var mid:Int;
        var end:Int = len - 1;
        while (start <= end) {
            mid = (start + end) / 2;
            if (key == inputArr[mid]) {
                return mid;
            };
            if (key < inputArr[mid]) {
                end = mid - 1;
            } else {
                start = mid + 1;
            };
        };
        return -1;
    };
};

class test(){
  
  def main()={
    var arr: Array[Int](7)={11,12,13,14,15,16,17};
    var obj:Demo = new Demo();
    var x : Int = obj.binarySearch(arr,7,16);
    println(x);
    return 0;
};
};
//0 2 2 5
