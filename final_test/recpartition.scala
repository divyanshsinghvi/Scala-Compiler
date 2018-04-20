class ackermann(){
    def Ack(var m:Int,var n:Int):Int={
        var i:Int  = -1;
        var j:Int  = -1;
        if (m>=0 && n>=0) {
            if (m == 0) {
                i = n + 1;
            } 
            else {
              if (n == 0) {
                i = this.Ack(m - 1, 1);
            } else {
                j = this.Ack(m, n - 1);
                i = this.Ack(m - 1, j);
            };
            };
        };
        return i;
    };
    def main()={
        var i:Int= this.Ack(3,4);
        println(i);
        return 0;
    };
};
