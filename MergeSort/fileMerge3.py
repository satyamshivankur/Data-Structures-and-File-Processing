import pickle,os
from fileMerge4 import merge
blocksize=100
def getKey(record):
        '''
        OBJECTIVE: To get key value of the Record object
        INPUT PARAMETERS:
                 self: (Implicit) Record Object
        OUTPUT :
                 None
        '''
        return record.key
    
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
        lst.sort(key=getKey)
        for i in lst:
            pickle.dump(i,f1)
        lst=[]
        for i in range(0,blocksize):
            try:
                ob=pickle.load(f)
                lst.append(ob)
            except EOFError:
                keepLooping=False
        lst.sort(key=getKey)
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
        

    
