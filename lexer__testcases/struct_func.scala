package tr;

class T(var g: Char,var h: Int,var i: Char,var j: Short,var k: Double,Array[Char] l,var m: Char){
  var a: Char=g;
  var b: Int=h;
  var c: Char=i;
  var d: Short=j;
  var e: Double=k;
  Array[Char] name[10]=l;
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
int main (){
    var k: T = new T('a',47114711,'c',1234,3.141592897932,'*',"abc")
    return 0;
};
}
