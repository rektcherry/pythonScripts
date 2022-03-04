from concurrent.futures import process
## this program reads file pmalli.txt which contains words and numbers
## if pmalli.txt contains palindrome, then it writes it to another file called ptulos.txt
## also prints out if line is number or palindrome or is not a palindrome
#################################################################################################

def openFileR(): # open the pmalli file to read
    try: 
        f=open('.\palindrome\pmalli.txt','r')
        return f
    except:
        process.exit(0) 
        return print('Can\'t read the file. Throws error.')
def openFileW(): # open file to write the palindromes if there is any
    try:
        w=open('.\palindrome\ptulos.txt','w')
        return w
    except:
        process.exit(0) 
        return print('Can\'t read the file. Throws error.')    

fr = openFileR()
fw = openFileW() 

def readFile(f): # read line from pmalli.txt
    rawLine=f.readline() 
    line = rawLine[0:-1] 
    return line

while True:
    line = readFile(fr) ## go through line by line pmalli.txt 
    if len(line)==0:
        break 
    if (line.isdigit()):
        print('Line \''+line+'\' contains numbers.') # check if contaisn numbers
        continue
    if (line[::]==line[::-1]) and (line.isalpha()):
        print('Line \''+line+'\' is palindrome.') # checks if alphapetic and palindrome
        fw.write(line+'\n') 
        continue           
    if (line[::]!=line[::-1])and (line.isalpha()):
        print('Line \''+line+'\' is not palindrome.') # checks if aplhapetic and not palindrome
        continue
# close the files when done
fr.close()
fw.close()