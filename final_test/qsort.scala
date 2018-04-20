class Demo(){
  def quicksort(var x:Array[Int](6)={}, var first:Int, var last:Int):Int={
                var pivot:Int;
                var j:Int;
                var temp:Int;
                var i:Int;
                var f:Int;
                var e:Int;
                var a:Int;

                if(first<last){
                  pivot=first;
                  i=first;
                  j=last+1;

                  while(i<j){
                  while((x[i] <= x[pivot]) && (i <= last)){
                    i= i + 1;};
                  while(x[j]>x[pivot]){
                    j= j - 1;};
                                if(i<j){
                                        temp=x[i];
                                        x[i]=x[j];
                                        x[j]=temp;
                                };
                        };

                        temp=x[pivot];
                        x[pivot]=x[j];
                        x[j]=temp;
                        f = j - 1 ;
                        e = j + 1;

              this.quicksort(x,first,f);
              this.quicksort(x,e,last);

                return 0;
                };
return 0;
};
};
class test(){
   def main()={
    var arr: Array[Int](6)={16,17,13,14,15,1};
    var size:Int = 6;
    var first:Int = 0;
    var l:Int = size - 1;
    var i:Int;
    var obj:Demo = new Demo();
    obj.quicksort(arr,first,l);
    for(i=0;i<size;i+=1){
      println(arr[i]);
                };
    return 0;
};
};
//0 2 2 5
