from random import randint

#enryption fuction
def encrypt(text,key):
    result=""
    for i in range(len(text)):
        ch=text[i]
        if(ch.isupper()):#chek uper case of text s
            alph=ord(ch)-65
            ke=key[alph].upper()
            result += ke
        else:#lower case of text
            if ch==" ":
                result += " "
            else:
                alph=ord(ch)-97
                ke=key[alph].lower()
                result += ke
    return result

#decrption function
def decrypt(text,key):
    result=""
    for i in range(len(text)):
        ch=text[i]
        if (ch.isupper()): #uper case text 
            k=key.upper()
            alph=k.find(ch)
            result += chr(alph+65)
        else: #lower case text 
            if ch==" ":
                result += " "
            else:
                k=key.lower()
                alph=k.find(ch)
                result += chr(alph+97)
    return result


# here start the main function
key=""
a=[]
while(len(key)!=26):
 value = randint(0,25)
 if value in a:
     continue 
 else:
     a.append(value)
     key +=chr(value+65)
     
while(1):
 ch=int(input("1.Encryption   2.Decryption  0.for exit:"))
 if ch==1:
     text = input(("enter the text for Plain Text:"))
     print("Key:",key)
     print("messege Plain Text:",text)
     print("messege cipher Text:" + encrypt(text,key))#call encryption function 
 elif ch==2:
     text = input(("enter the text for cipher Text:"))
     print("key=",key)
     print("messege Pain Text:" + decrypt(text,key))#call decryption function 
     print("messege cipher text:",text)
 elif ch==0:
     print("Exit")
     break
 else:
     print("enter the correct choise") 