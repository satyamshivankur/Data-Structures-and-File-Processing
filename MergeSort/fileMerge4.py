import pickle,os
import fileMerge3 as C
def merge():
    '''
    OBJECTIVE :  To sort and merge records of f1.txt and f2.txt
    INPUT PARAMETERS :
            None
    OUTPUT :
            None
    '''
    
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
            for i in range(0,C.blocksize*2):
                try:
                    if C.getKey(a)<C.getKey(b):
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
    
