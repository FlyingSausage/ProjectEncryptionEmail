def decryption(original:int,number:int):
    l =[]
    j=original
    for c in j:
        if c.isdigit():
            cipherDigit(c,number)
        else:
            cipherChar(c,number)
        
        l.append(c)

def cipherDigit(c,n):
    return c-n

def cipherChar(c,n):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    c = letters.index(n)
    a = c-n
    while a < 0:
        a = a + 26
    return letters[a]