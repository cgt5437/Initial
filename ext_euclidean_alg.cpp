// perform Euclid's extended algorithm

// implemented by Christian Thomas

#include <cstdint>
#include <iostream>
using namespace std;

/**
 * how many bits are needed to encode x?
 * @param x a value whose highest bit will be determined
 * @return the position of the highest bit needed to encode x
 */
long how_many_bits( long x, long y );

long ext_euc( long a, long b, long & x, long & y, long & d); 

int main( int argc, char* argv[] )
{
  if( argc != 3 )
  {
    cerr << "Usage: " << argv[0] << " a b" << endl;
    cerr << "  where a and b are two unsigned ints to find the gcd of" << endl;
    return 1;
  }

  long a {stol( argv[1] )};
  long b {stol( argv[2] )};

  long x;
  long y;
  long d;
  long n;
  
  
  
  n = how_many_bits( a,b );
  
  
  d = ext_euc( a, b, x, y, d);
  cerr << "x: " << x << "  y: " << y << "  d: " << d << endl;
  
  if(d==1){
    cout<<"relatively prime:yes"<<endl;
  }
  else{
    cout<<"relatively prime:no"<<endl;
  }

  cout <<"How many bits: "<< n <<  endl;
 
  return 0;
}

long ext_euc(long a, long b, long &x, long &y, long &d) {
 
  if(b == 0) {
    x = 1;
    y = 0;
    return a;
    }

    long x1; 
    long y1;
    long gcd = ext_euc(b, a % b, x1, y1, d);
    
   
    x = y1;  
    y = x1 - (a / b) * y1;
  
    
    return gcd;
}



long how_many_bits( long x, long y )
{
  long count_bits {0};
  long a;
  //find largest
  if(x > y)
  {
    a = x;
  }
  else
  {
    a = y;
  }
  while( a > 0 )
  {
    a >>= 1;
    count_bits++;
  }
  return count_bits;
  
}
