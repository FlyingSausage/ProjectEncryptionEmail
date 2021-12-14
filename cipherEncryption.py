def encryption(msg:str):
    j = []
    s = msg
    num = int(input("Please Enter the number for ciper encryption"))
    for i in range(0,len(s)): 
        n = s[i]
        
        n = n.lower()
        n = cipherChar(n,num)
        
        j.append(n)

def cipherChar(n,num:int):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    c = letters.index(n)
    a = c+num
    while a > 26:
        a = a - 26
    return letters[a]