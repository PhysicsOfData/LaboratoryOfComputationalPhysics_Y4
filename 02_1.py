#in ingresso vuole il numero (x), in che base è (base_i) e in che base lo voglio (base_f)
def convertor(x, base_i, base_f):
    if(base_i==10 and base_f==2): #decimal-->binary
        x_f=bin(x)
    
    elif(base_i==10 and base_f==16): #decimal-->hexadecimal
        x_f=hex(x)
        
    elif(base_i==2 and base_f==10):#binary-->decimal
        x_f=int(bin(x),2)
    
    elif(base_i==16 and base_f==10):#hexadecimal-->decimal
        x_f=int(hex(x),16)

    elif(base_i==2 and base_f==16): #binay-->hexadecimal
        x_f=int(bin(x),2)
        x_f=hex(x)

    elif(base_i==16 and base_f==2): #hexadecimal-->binary
        x_f=int(hex(x),16)
        x_f=bin(x)
    print(f"il numero in base {base_f} è {x_f}")

convertor(3,10,16)