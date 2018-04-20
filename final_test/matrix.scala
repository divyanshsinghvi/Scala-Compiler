class demo(){
def main():Int={
    var i: Int =1;
    var j: Int = 2;
    var d: Int =2;
    
    var m1:Array[Int](2,2)={1,2,3,4};
    var m2:Array[Int](2,2)={100,200,300,400}; 
    var m3:Array[Int](2,2)={1,1,1,1}; 
    
    for(i=0;i<2;i+=1)
    {for(j=0;j<2;j+=1)
      {
        d = m1[i,j]*m2[i,j];
        m3[i,j] += d;
        println(m3[i,j]);

      };
    };
    
    
    return j;
};
};

//0 2 2 5
