object = {'a':{'b':{'c':'d'}}}

def getvalue(value,s):
    while(value != None):
        try:
            key=list(value.keys())[0]    #Get Key of dictionay
            if (s==key):
                print(value.get(key))
                break                   #If Key matches, provides output of value
            value=value.get(key)
        except:
            print("Key not found")
            break
        
        
getvalue(object, 'c')                   #Example object and key sent in function
