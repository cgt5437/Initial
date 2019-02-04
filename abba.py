'''
By Jack (John) Huggins and Christian Thomas. This module contains three methods.
One method takes a words and returns the 'abba' verision of that word, the
other builds a dictionary whose keys are abba words and whose values are a list
of words that fit that abba word, and the last returns a list of matches based
on the cipher text and the abba dictionary.  Also, contains glorious sample code
given by Dr. Bindner.


The turning point for the program is when we found out that 'zdp' was equivalent
to 'who'.  From here the guesses became more and more intuitive and the letters
fell into place.

The final message was "in belgium, i think children who earn merit badges are
known as brussels scouts."
'''

def word2abba(word):
    '''
    This function takes a word and returns the abba version of that word
    '''

    #initialize empty word dictionary
    wordDict = {}

    # create an alphabet string
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    #initialize the new word variable to be accumulated to be the abba word
    newWord = ''

    #initialize the count as zero to be added to throughout the loop
    count = 0

    # go through every character in the given word
    for char in word:
        #if that character is not in wordDict
        if char not in wordDict:
            #the alphabet character (indexed by the current count) will
            #become the value of that character in the wordDict
            wordDict[char] = alphabet[count]
            #add 1 to the count
            count += 1
        #add the wordDict value keyed by the current character to the string
        #newWord
        newWord += wordDict[char]

        
    return newWord

def buildAbbaDictionary(afile):
    '''
    This function takes in a file and returns a dictionary keyed by an
    abba word with values that are every word in the file that fit that
    abba word
    '''

    #open the given file and assign it to the variable infile
    infile = open(afile, 'r')

    #initialize abbaDict
    abbaDict = {}

    #for every line in the file
    for line in infile:
        #stip the line
        line = line.strip()
        #assign the abba form of the word to the variable abbaWord
        abbaWord = word2abba(line)
        #If the abbaWord is in the abbaDict
        if abbaWord in abbaDict:
            #add that word to the list whose key is that abba word
            abbaDict[abbaWord].append(line)
        else:
            #if not, create a key in abbaDict called abbaword and put a
            #list that contains just that word inside
            abbaDict[abbaWord] = [line]
            
    #close the file
    infile.close()

    return abbaDict



#import the regular expression module
import re

def abbaMatches(abbaDict, guessDict, cipherWord):
    '''
    This function returns a list of words that could potentially be a given cipherWord
    '''
    
    
            
    #Assign the abba version of the cipherword to the variable abbaOfCipherWord
    abbaOfCipherWord = word2abba(cipherWord)
    #Assign the list of words inside the abbaDict keyed by abbaOfCipherWord to the
    #variable potential words
    potentialWords = abbaDict[abbaOfCipherWord]


    #Initialize a variable that will come to represent any character in a regular expression
    x = '[^'
    for key in guessDict:
        #add the value of guessDict at that key to x
        x += guessDict[key]
    #End x by adding a closing bracket to it
    x += ']'

    #Initialize an empty string to be accumulated and call it pattern
    pattern = ""
    #for every character in the cipherword
    for ch in cipherWord:
        #if that character is in the guessDict
        if ch in guessDict:
            #Add the guessDict value keyed by that character to pattern
            pattern += guessDict[ch]
        else:
            #Add x to the pattern, which will come to represent any character in a regualar
            #expression
            pattern += x
    #anchor pattern with a dollar sign
    pattern += '$'


    #Initialize and empty list called words
    words = []
    #go through every word in the list of potential words
    for word in potentialWords:
        #if the words matches the given word and the pattern, add it to the list of words
        if (re.search(pattern, word)):
            words.append(word)


    return words






def translate( guessDict, cipherText ):
    for ch in cipherText:
        #if the character does not match this pattern
        if not re.match( '[a-z]$', ch ):
            # print chracter 
            print( ch, end='')
        else:
            #print the guessDict version of the word
            print( guessDict.get( ch, '-' ), end='')
    print()

    print( cipherText )

def tryLetter( guessDict, cipherText, cipherChar, plainChar ):
    cipherChar = cipherChar.lower()

    # If the ciphercharacter is in guessDict
    if cipherChar in guessDict:
        print( cipherChar + " already mapped to " + guessDict[cipherChar] )
        translate( guessDict, cipherText )
        return

    # If the ciphercharacter is not in the cipherText
    if cipherChar not in cipherText:
        print( cipherChar + " does not appear in the ciphertext." )
        translate( guessDict, cipherText )
        return

    # If the ciphercharacter is in guessdict.values()
    if plainChar in guessDict.values():
        print( "Some letter already maps to " + plainChar )
        translate( guessDict, cipherText )
        return

    guessDict[ cipherChar ] = plainChar

    translate( guessDict, cipherText )

def untryLetter( guessDict, cipherText, cipherChar ):
    del guessDict[cipherChar]
    translate( guessDict, cipherText )
  
            
    
    
    
    
    




        
