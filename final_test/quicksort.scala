class Demo(){
  def partition(var arr:Array[Int](7)={},var start:Int,var end:Int):Int={
      var pivot:Int = start;
      var down: Int = start+1;
      var up: Int = end;
      var temp:Int;
      while(1){
      while(down <= end && arr[down] <= arr[pivot]){
        down +=1;
      };
      while(up > start && arr[up] >= arr[pivot]){
        up -=1;
      };
      if(down<up){
        temp = arr[down];
        arr[down] = arr[up];
        arr[up] = temp;
      }else{
      break;
      };
      };
        temp = arr[pivot];
        arr[pivot] = arr[up];
        arr[up] = temp;
      return up;

  };



  def Sort(var arr:Array[Int](7)={},var start:Int,var end:Int):Int={
      var pivot:Int;
      var temp:Int;
      println(100);
      if(start < end){
        if(start == end-1){
            if(arr[start] > arr[end]){
                temp = arr[start];
                arr[start] = arr[end];
                arr[end]=temp;
            //println(1); 
            }else{
              pivot = this.partition(arr,start,end);
              this.Sort(arr,start,pivot-1);
              this.Sort(arr,pivot+1,end);

            };
      };
  };
  return 0;
};
};
class test(){
  
  def main()={
    var arr: Array[Int](7)={18,12,14,13,15,1,17};
    var obj:Demo = new Demo();
    var i:Int;
    var x : Int = obj.Sort(arr,0,6);
    for(i=0;i<7;i+=1){
    println(arr[i]);};
    return 0;
};
};
//0 2 2 5
