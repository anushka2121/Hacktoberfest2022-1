def swap_case(s):
    z=list(s)
    for i in range(0,len(z)):
        if z[i]==z[i].upper():
             z[i]=z[i].lower()
        #if z[i]==z[i].lower():
        else:
             z[i]=z[i].upper()  
    s=''.join(z)            
    return s
