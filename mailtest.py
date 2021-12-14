import mymail,os, importlib

sender = input('please enter YOUR email address: ')
receiver = input('please enter RECEIVER"s email addresss')
msgpath = input('Do you enter a message now or import the message from a text file, enter:\n 1: enter\n 2: import text file\n ')
dirname = os.path.dirname(__file__)
msg = ''
if msgpath == '1':
    msg = input('please enter your message: ')
elif msgpath == '2':
    filename = input('please enter your text filename include extension. make sure your file is in the same folder of this py file')
    filename = os.path.join(dirname,filename)
    f = open(filename,'r',encoding='UTF-8')
    msg = msg.join(f.readlines())

if input("Do you want to encrypt your message?\n 1 for yes \n2 for no: ") == 1:
    fname = input("Enter the filename of the encryption py file including extension: ")
    encryptionModule = importlib.import_module(fname, package = None)
    encryptionModule.encryption(msg) #The encryption files must have encryption method exactly called encryption

header = input('please enter your Subject: ')
From = input('Please enter sender name that will be displayed: ')

email = mymail.mymail(sender,receiver,msg,header,From)

email.sendMail()


