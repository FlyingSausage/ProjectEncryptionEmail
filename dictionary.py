import os, json
def createDict():
    dict = {}
    chars = 'abcdefghijklmnopqrstuvwxyz'
    digits = '1234567890'
    print('Start fullfilling character for new dictionary codebook: \n')
    for c in chars:
        d = input(f"assigning {c} to: ")
        while d in dict.values():
            d = input(f"assigning {c} to: ")
        dict[c] = d

    print('Start fulling digits for new dictionary codebook: \n')
    for i in digits: 
        j = input(f"assiging {i} to：")
        while j in dict.values():
            j = input(f"assiging {i} to：")
        dict[i] = j
    
    dirname = os.path.dirname(__file__)
    filename = input("dictionary file name: ")
    filename = os.path.join(dirname,filename)

    f = open(filename, 'w')
    json.dump(dict,f)
    f.close()
    return "Dictionary Created"

def encryption(msg:str):
    #import json file
    filename = input('input the codebook json filename: ')
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname,filename)
    f = open(filename)
    dict = json.load(f)

    s = '' #initialize s with an empty string
    for c in msg: #convert msg character by character with the dictionary imported
        if c != ' ':
            c = c.lower()
            a = dict[c]
            s = s + a
        else:
            s = s + c
    
    f.close()
    return s

def decryption(msg:str):
    #import json file
    filename = input('input the codebook json filename: ')
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname,filename)
    f = open(filename)
    dict = json.load(f)

    s = '' #initialize s with an empty string
    for c in msg: #convert msg character by character with the dictionary imported
        if c != ' ':
            c = c.lower()
            a = findkey(dict,c)
            s = s + a
        else:
            s = s + c
    
    f.close()
    return s

def findkey(d:dict, s):
    for key,value in d.items():
        if s == value:
            return key


