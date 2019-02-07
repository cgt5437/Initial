#include <climits>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <vector>
#include "matrix.h"
using namespace std;

//Created by Christian Thomas 


uint opt(size_t i,
         uint a,
         Matrix<uint> & memo,
         const vector<uint> & denom);

void dump(const Matrix<uint> & memo, const vector<uint>& denom);
void traceBack(size_t i,
         uint a,
         Matrix<uint> & memo,
         const vector<uint> & denom);
         
int main(int argc, char* argv [])
{
  vector<uint> denom;
  uint n = static_cast<uint>(stoul(argv[1]));
  
  //allows you to take in 4 coin arguments
  
  for(int i=2;i<6;i++)
  {
  uint coinz = static_cast<uint>(stoul(argv[i]));
  
  denom.push_back(coinz);
}



  Matrix<uint> memo (denom.size(), n + 1);

  for( uint coin = 0; coin <denom.size(); coin++ )
  {
    for( uint amount = 0; amount <= n; amount++ )
    {
      memo.at(coin, amount) = UINT_MAX;
    }
  }

  uint result {opt( denom.size(), n, memo, denom )};
  cout << "it takes " << result << " coins" << endl;
  
  cout << endl;

  dump(memo, denom);
  traceBack( denom.size(), n, memo, denom );
  return 0;
}

uint opt( size_t i,
          uint a,
          Matrix<uint> & memo,
          const vector<uint> & denom )
{
  uint w,q;
  uint smallest{UINT_MAX};
  
  //base case of zeros
  for(uint z = 0; z < i; z++)
  {
    memo.at(z,0)=0;
  }
  
  for(w = 0; w < i; w++)
  { 
    for(q = 0; q <= a; q++)
      {
        if(q >= denom[w])
          { 
            for(uint c = w; c<i;c++)
              {
                memo.at(c,q) = memo.at(w,(q-denom[w])) + 1;
              }
          }
      }
  }
  //Checks to make sure you have minimum amount of coins
  for(size_t c = 0;c < i;c++)
  {
    if(memo.at(c,a)<smallest)
    {
      smallest= memo.at(c,a);
      
    }
  
  }
  return smallest;
 
}


void traceBack(size_t i,
          uint a,
          Matrix<uint> & memo,
          const vector<uint> & denom )
{
  uint newA{0};
  uint lowest{UINT_MAX};
  size_t chosen{0};
  for(size_t c = 0;c < i;c++)
  {
    if(memo.at(c,a)<lowest)
    {
      lowest = memo.at(c,a);
      chosen = denom[c];
    }
    
  }
  //subtracts lowest coin amount to ensure lowest coin is used in every subproblem
  newA = a - chosen;
  cout<<"used coin: "<<chosen<<endl;
  
  //if you get 0 you're done
  if(newA == 0)
  {
    cout<<endl;
  }
  //if not 0 redo the memo table and do traceBack to see what coinz were used
  else
  {
    opt(denom.size(), newA, memo, denom );
    traceBack(denom.size() , newA, memo, denom );
  }
  
}


void dump( const Matrix<uint> & memo, const vector<uint>& denom )
{
  for( uint row = 0; row < memo.numrows(); row++ )
  {
    cout << setw(3) << denom.at(row) << ": ";
    for( uint col = 0; col < memo.numcols(); col++ )
    {
      if( memo.at(row, col) == UINT_MAX )
      {
        cout << "  -";
      }
      else
      {
        cout << setw(3) << memo.at(row, col);
      }
    }
    cout << endl;
  }
  cout << endl;
}
