import random,pickle,os

blocksize=10
class Record:
    def __init__(self,key,nonKey):
        '''
        OBJECTIVE : To initialize an Record object
        INPUT PARAMETERS :
                self : (Implicit) Record object
                key : key value of the object Record
                nonkey : value corresponding to that key
        OUTPUT :
                None
        '''
        self.key=key
        self.nonKey=nonKey

    def __str__(self):
        '''
        OBJECTIVE: To return a string of the values of the object Record
        INPUT PARAMETERS :
                self : (Implicit) Record object
        OUTPUT : 
                a string representing the Record object
        '''
        return 'Key No.:'+str(self.key)+'\nKey Value:'+str(self.nonKey)

    def getKey(self):
        '''
        OBJECTIVE: To get key value of the Record object
        INPUT PARAMETERS:
                 self: (Implicit) Record Object
        OUTPUT :
                 None
        '''
        return self.key
    
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

def sortByBlocks():
    '''
    OBJECTIVE :  To sort and merge records of givwn two files
    INPUT PARAMETERS :
            None
    OUTPUT :
            None
    '''
    f=open('mainFile.txt','rb')
    f1=open('file1.txt','wb')
    f2=open('file2.txt','wb')

    global blocksize
    keepLooping=True
    while keepLooping:
        lst=[]
        for i in range(0,blocksize):
            try:
                ob=pickle.load(f)
                lst.append(ob)
            except EOFError:
                keepLooping=False
        lst.sort(key=lambda Record:Record.getKey())
        for i in lst:
            pickle.dump(i,f1)
        lst=[]
        for i in range(0,blocksize):
            try:
                ob=pickle.load(f)
                lst.append(ob)
            except EOFError:
                keepLooping=False
        lst.sort(key=lambda Record:Record.getKey())
        for i in lst:
            pickle.dump(i,f2)

    f.close()
    f1.close()
    f2.close()

    while True:
        merge()
        if os.path.getsize('file2.txt')==0:
            break
        blocksize*=2
        
def merge():
    
    f1=open('file1.txt','rb')
    f2=open('file2.txt','rb')
    f3=open('file3.txt','wb')
    f4=open('file4.txt','wb')
    a,b=None,None
    keepLooping,flag,check=True,True,0
    while keepLooping:
        f=f3 if flag else f4
        if check==0:
            a=pickle.load(f1)
            b=pickle.load(f2)
            check=1
        else:
            for i in range(0,blocksize*2):
                try:
                    if a.getKey()<b.getKey():
                        pickle.dump(a,f)
                        a=pickle.load(f1)
                    else:
                        pickle.dump(b,f)
                        b=pickle.load(f2)
                except EOFError:
                    break
            while True:
                try:
                    ob=pickle.load(f1)
                    pickle.dump(ob,f)
                except EOFError:
                    keepLooping=False
                    break
            while True:
                try:
                    ob=pickle.load(f2)
                    pickle.dump(ob,f)
                except EOFError:
                    keepLooping=False
                    break
            flag=False if True else flag
    f1.close()
    f2.close()
    f3.close()
    f4.close()

    os.remove('file1.txt')
    os.remove('file2.txt')
    os.rename('file3.txt','file1.txt')
    os.rename('file4.txt','file2.txt')
    
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
