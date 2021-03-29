def revword (word:str)->str:
    n= len(word)
    NW=''
    while n>0:
        NW+=word[n-1]
        n-=1
    NW=NW.rstrip()
    return NW.lower()

def countword()->int:
    txt=open('text.txt')
    txt=txt.read().split()
    counter=0
    word=txt[0]
    for mila in txt:
        if revword(mila)==word:
            counter+=1
    return counter+1