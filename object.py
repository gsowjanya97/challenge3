object = {'a':{'b':{'c':'d'}}}

def getvalue(value,s):
    while(value != None):
        try:
            key=list(value.keys())[0]    #Get the first key of dictionary
            if (s==key):
                print(value.get(key))
                break                   #If the key matches, provide output of value and exit the loop
            value=value.get(key)        #Else start again with the nested dictionary
        except:
            print("Key not found")      #When reached at the end of dictionary, avoid exceptions
            break
        
        
getvalue(object, 'c')                   #Example object and key sent in function
