
class T(var g: Char,var h: Int,var i: Char,var j: Short,var k: Double,var l:Array[Char](3) ,var m: Char){
  var a: Char=g;
  var b: Int=h;
  var c: Char=i;
  var d: Int=j;
  var e: Float=k;
  var name:Array[Char](10);
  var f: Char = m;
};

/*
void f (T x)
{
  x.a = 'a';
  x.b = 47114711;
  x.c = 'c';
  x.d = 1234;
  x.e = 3.141592897932;
  x.f = '*';
  x.name = "abc";
}*/

object demo{
def main(args: Array[String](3))={
    var k: T= new T('a',47114711d,'c',1234,3.141592897932d,'*',"abc");
    return 0;
};
};
