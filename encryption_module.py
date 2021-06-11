from random import randrange
def encrypt():

    x = open("movie_list.txt","r")
    text = x.readlines()

    values = list(range(32,65+27+32))
    key = dict()

    for letter in range(32,65+27+32):
        val = randrange(0,len(values))
        key[chr(letter)] = values[val]
        values.pop(val)

    

    for y in range(len(text)):
        s = ""
        for z in range(len(text[y])):
            if text[y][z] == "\n":
                continue
            s += chr(key[text[y][z]])
        text[y] = s+"\n"
    x.close()

    f = open("movie_list.txt","w")
    for b in text:
        f.write(b)

    key_file = open("key.txt","w+")
    for value in key.values():
        key_file.write(str(value) + "\n")

def decrypt(text):
    y = open("key.txt","r")
    keys = y.readlines()

    rev_dict = dict()
    asci = 32
    for x in keys:
      
        rev_dict[int(x)] = chr(asci)
        asci += 1

    y.close()
    

    h = open("key.txt","w")
    h.write("")
    h.close()

    for d in range(len(text)):
        s = ""
        for z in range(len(text[d])):
            if text[d][z] == "\n":
                continue
            s += rev_dict[ord(text[d][z])]
           
        text[d] = s
    
   
    return (text)


def decrypt_file(text):
    x = open("movie_list.txt","w")
    for y in text:

        x.write(y)
        x.write("\n")

#encrypter
def encrypter_with_key():
    text_file = input("enter file to be encrypted: ")
    x = open(text_file,"r",)
    text = x.readlines()

    key = {'a':'h','b':'d','c':'s','d':'n','e':'a','f':'i','g':'q','h':'k','i':'e','j':'y','k':'u','l':'j','m':'o','n':'t','o':'c','p':'w','q':'m','r':'b','s':'r','t':'f','u':'l','v':'x','w':'p','x':'g','y':'z','z':'v',' ':' '}
    for y in range(len(text)):
        s = ""
        for z in range(len(text[y])):
            if text[y][z] == "\n":
                break
            s += key[text[y][z]]
        text[y] = s


    x.close()
    y = open(text_file,"w+")
    for z in text:
        y.write(z)
        y.write("\n")
    y.close()

#decrypter
def decrypter_with_key():
    dec_file = input("enter file to be decrypted: ")
    password = input("enter password: ")
    if password == "sample password":
        z = open(dec_file,"r")
        enc = z.readlines()
        dec_key = {'h':'a','d':'b','s':'c','n':'d','a':'e','i':'f','q':'g','k':'h','e':'i','y':'j','u':'k','j':'l','o':'m','t':'n','c':'o','w':'p','m':'q',"b":"r",'r':'s','f':'t','l':'u','x':'v','p':'w','g':'x','z':'y','v':'z',' ':' '}
        final = []
        for x in enc:
            sent = ""
            for y in x:
                if y == "\n":
                    break 
                sent += dec_key[y]
            final += [sent+"\n"]
        z.close()
        h = open(dec_file,"w+")
        for d in final:
            h.write(d)
        h.close()

from nltk.corpus import words
word_list = words.words()

def ord_value_promote_decrypt():

    terminate = False
    space = False


    inp = str(input("enter a word: "))
    out = ""

    if " " in inp: 
        space = True
    if space == False:
        while terminate == False:
            for x in range(-26,27):
                for y in range(0,len(inp)):
                    out += chr(ord(inp[y])+x)
                if out in word_list:
                    terminate = True
                    print (out)
                out = ""

    else:
        lim = inp.index(" ")
        new_str = ""
        
        while terminate == False:
            for a in range(-26,27):
                    for b in range(0,lim):
                        new_str += chr(ord(inp[b])+a)
                    if new_str in word_list:
                        terminate = True
                        c = a
                        
                        
                        out = new_str
                        out += " "
                    new_str = ""
        for d in range(lim+1,len(inp)):
            if inp[d] != " ":
                out += chr(ord(inp[d])+c)
            else:
                out += " "
        print (out)