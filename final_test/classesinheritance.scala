class Cake(){
        var flavor:Int; 
        def Cake(var flavor:Int):Int={
            this.flavor=flavor;
		return 0;
        };       
        def bake():Int={
            println(this.flavor);
		return 0;
        };
        def frost():Int={
            println(this.flavor);
		return 0;
        };
   };
class Dream(){
	def main()={
	var c:Cake = new Cake();
	c.flavor = 10;
	println(c.flavor);
	c.Cake(4);
	println(c.flavor);	
	return c;
	};
};
