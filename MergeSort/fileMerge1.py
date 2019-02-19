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




