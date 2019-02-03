dna="AGTAAGTGGTTAAAGGTTAGGAAGTT"
counter=0
original=[]

                              
adjusted_length=int(len(dna)/3)
for i in range(0,adjusted_length):
    original.append(dna[i]+dna[i+1]+dna[i+2])
    
   

print(original)
      
    



    
