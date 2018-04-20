class demo(){
def main()={
    var i: Int =1;
    var j: Int = 2;
    var d: Int =2;
    var k: Int = 2;
    
    var m3:Array[Int](2,2,2)={1,2,3,4,5,6,7,8};
    
    for(i=0;i<2;i+=1)
    {for(j=0;j<2;j+=1)
      {for(k=0;k<2;k+=1){
        println(m3[i,j,k]);
      };
      };
    };
    
    
    return j;
};
};

//0 2 2 5
