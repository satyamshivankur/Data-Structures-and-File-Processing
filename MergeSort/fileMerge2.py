import random,pickle
from fileMerge1 import Record
from fileMerge3 import sortByBlocks
from fileMerge4 import merge
def writeRecord():
    '''
    OBJECTIVE :  To write records a givenFile
    INPUT PARAMETERS :
            fileName: Name of the file
            N: Number of Records to be written
    OUTPUT :
            None
    '''
    N=int(input('Enter number of records to be written: '))
    f=open('mainFile.txt','wb')
    keyList,i=[],1
    while i<=N:
        key=random.randint(1000000,2000000+N+1)
        if key not in keyList:
            keyList.append(key)
            nonKey=str(key)*10
            ob=Record(key,nonKey)
            pickle.dump(ob,f)
            i+=1

    f.close()
    
def display(lower,upper):
    '''
    OBJECTIVE :  To display records of sorted file "f1.txt" given lower and upper range
    INPUT PARAMETERS :
            lower: lower limit for the range to display records
            upper: upper limit for the range to display records
    OUTPUT :
            None
    '''
    f1=open('file1.txt','rb')
    ob=pickle.load(f1)
    size=f1.tell()
    i=lower
    f1.seek(size*(lower-1))
    for i in range(lower,upper+1):
        ob=pickle.load(f1)
        print('\nRecord Number:'+str(i)+':')
        print(ob)

    f1.close()

def main():
    writeRecord()
    sortByBlocks()
    lower=int(input('Enter lower limit:'))
    upper=int(input('Enter upper limit:'))
    display(lower,upper)

if __name__=='__main__':
    main()

