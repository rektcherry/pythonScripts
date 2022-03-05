## this program reads file pmalli.txt which contains words and numbers
## if pmalli.txt contains palindrome, then it writes it to another file called ptulos.txt
## also prints out if line is number or palindrome or is not a palindrome
#################################################################################################
import os
import sys
cvd = os.getcwd()

def openFileR(): # open the pmalli file to read
    try: 
        f = open(f'{cvd}\pmalli.txt','r')
        return f
    except:
        sys.exit('Can\'t read the fr file. Throws error.')

def openFileW(): # open file to write the palindromes if there is any
    try:
        w=open(f'{cvd}\ptulos.txt','w')
        return w
    except:
        sys.exit('Can\'t read the fw file. Throws error.')    

def readFile(f): # read line from pmalli.txt
    rawLine=f.readline() 
    line = rawLine[0:-1] 
    return line

def main ():
    fr = openFileR()
    fw = openFileW() 
    while True:
        line = readFile(fr) ## go through line by line pmalli.txt 
        if len(line)==0: # stop loop when line has nothing on it (assumes there is no empty lines, could be improved)
            break 
        if (line.isdigit()):
            print('Line \''+line+'\' contains numbers.') # check if contaisn numbers
        if (line[::]==line[::-1]) and (line.isalpha()):
            print('Line \''+line+'\' is palindrome.') # checks if alphapetic and palindrome
            fw.write(line+'\n')            
        if (line[::]!=line[::-1])and (line.isalpha()):
            print('Line \''+line+'\' is not palindrome.') # checks if aplhapetic and not palindrome
    # close the files when done
    fr.close()
    fw.close()
main()
