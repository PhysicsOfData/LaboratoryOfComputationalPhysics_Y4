s="Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Mickey instead of the number and for the multiples of five print Mouse. \
For numbers which are multiples of both three and five print MickeyMouse"

alph=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","x","z")
ALPH=("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","Y","X","Z")

"""restituisce il numero di volte in cui lettera si ripete"""
def count(s,minusc, maiusc): 
    i=j=0
    while(i<len(s)):
        if(s[i]==minusc or s[i]==maiusc ):
            j+=1  
        i+=1
    return j

k=0
while(k<len(alph)):
    a = count(s,alph[k],ALPH[k])
    print("la lettera %s si ripete %d volte" %(alph[k],a))
    k+=1