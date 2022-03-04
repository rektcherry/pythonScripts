f=open('test.txt','w')

f.write('This file was written by Python.\n')

userInput=input('Write something: ')

f.write(str(userInput)+'\n')
f.close()

f=open('test.txt','r')
while True:
    
    textline=f.readline()
    if len(textline)==0:
        break 
    print(textline,end='')
   
f.close()