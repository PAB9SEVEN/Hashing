from cryptography.fernet import Fernet

f=open('cryptic.txt','r')
#f.write("hello this is the message which need to be encrypted for security reasons")
text=f.read()
#print text

f.close()
#this is to generate the key using fernet

key=Fernet.generate_key()
f=Fernet(key)
token=f.encrypt(text)
#print token
file=open('decryptic.txt','w')
file.write(token)
file.close()

#print f.decrypt(token)


#print text

