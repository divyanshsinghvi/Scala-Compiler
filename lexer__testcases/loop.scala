
object demo{
def main(args: Array[String](3))={
	
	var i:Int;
	var j:Int;
	var k:Int;
	var res:Int;
	for(res = 0,i=0; i < 10; i=i+1){
		for(j = 0; j < 10; j=j+1){
			for(k = 0; k < 10; k=k+1){
				res += 1;
				println(res);
				break;
			};
		};
	};

	println(res);
};
};
