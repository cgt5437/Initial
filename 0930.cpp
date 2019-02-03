#include <fstream>
#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;
size_t HashTable(string word)
  
{
   size_t seed = 131; 
   unsigned long hash = 0;
   for(int i = 0; i < word.length(); i++)
   {
      hash = (hash * seed) + word[i];
   }
   return hash % 99173;
}

size_t hash_320( const string & key, size_t table_size )
{
  size_t hash_val = 0;
  for( auto character : key )
  {
    hash_val = 37 * hash_val + static_cast< unsigned char >( character );
  }
  return hash_val % table_size;
}

int main()
{
  ifstream word_file;
  word_file.open("/usr/share/dict/words");
  vector<int> g1;
  g1.push_back(4);
  g1.at(0);
  size_t tmp1 {0};
  size_t tmp2 {0};
  size_t collisions1 {0};
  size_t collisions2 {0};
  string word;
  while( word_file >> word )
  {
    tmp1 = hash_320(word, 99173);
    tmp2 = HashTable(word);
    for( auto i = 0; i < g1.size(); i++)
  {
    if(tmp1 == g1.at(i))
    {
      collisions1++;
    }
    if(tmp2 == g1.at(i))
    {
      collisions2++;
    }
  } 
    g1.push_back(tmp1);
    
  }
  cout << collisions1 << endl;
  cout << collisions2 << endl;
  
  word_file.close();
  return 0;
}




