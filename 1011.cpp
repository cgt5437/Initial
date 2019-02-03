#include <cassert>
#include <cstdint>
#include <iostream>
using namespace std;


ulong gcd(ulong a, ulong b);

int main(int argc, char* argv[] )
{
  if( argc != 3 )
  {
    cerr << "Usage: " << argv[0] << " a b" << endl;
    cerr << "  where a and b are two unsigned ints to find the gcd of" << endl;
    cerr << "  both a and b non-negative" << endl;
    return 1;
  }

  ulong a {stoul( argv[1] )};
  ulong b {stoul( argv[2] )};
  assert(a > 0 && b > 0);

  ulong d {gcd(a, b)};
  cout << d << endl;
  return 0;
}
ulong gcd(ulong a, ulong b)
{
    // easy cases
    if (a == b)
    {
        return a;
    }
    if (a == 0)
    {
        return b;
    }
    if (b == 0)
    {
        return a;
    }
    
    //if a is even
    if (~a & 1) 
    {
        if (b & 1) //b is odd
        {
            return gcd(a >>1, b);
        }
        else //if a and b are both even
        {
            return gcd(a >> 1, b >> 1) << 1 ;
        }
    }
  
    if (~b & 1)  //b is even
    {
        return gcd(a, b >> 1);
    }
   
    // both are odd, and swap depending on which is greater
    if (a > b)
    {
        return gcd((a - b) >> 1, b);
    }
    return gcd((b - a) >> 1, a);
}
