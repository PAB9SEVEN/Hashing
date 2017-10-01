
from crypticmsg import f,key,token
from cryptography.fernet import Fernet

file=open('decryptic.txt','r')
text=file.read()
file.close()
print f.decrypt(token)
'''
here we need to import keys token f=fernet(key) that i the fernet object
as because a particular message can be decrypted using the particular token
required for encrypting the msg
'''
