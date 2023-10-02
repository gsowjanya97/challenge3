object = {'a':{'b':{'c':'d'}}}

def getvalue(value,s):
    while(value != None):
        try:
            key=list(value.keys())[0]   #Get the first key of dictionary
            if (s==key):
                print(value.get(key))   #If the key matches, provide output of the value and exit the loop
                break                   
            value=value.get(key)        #Else, start again with the next nested dictionary
        except:
            print("Key not found")      #Avoid exceptions when reached the end of dictionary
            break
        
        
getvalue(object, 'c')                   #Example object and key sent in function
