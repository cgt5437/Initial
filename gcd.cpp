// perform a divide-and-conquer gcd algorithm
// for problem set 1011
// implemented by Your Name Here

#include <cassert>
#include <cstdint>
#include <iostream>
using namespace std;

// the divide-and-conquer algorithm
// @param a one of the values to find the gcd of
// @param b the other value to find the gcd of
// @return the gcd of a and b
ulong get_gcd(ulong a, ulong b);

int main( int argc, char* argv[] )
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

  ulong gcd {get_gcd(a, b)};
  cout << gcd << endl;
  return 0;
}

ulong get_gcd(ulong a, ulong b)
{
  return 0;
}