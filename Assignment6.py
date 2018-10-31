for c in range(-20, 20):
    for d in range(-20, 20):
        for e in range(-20, 20):
            for f in range(-20, 20):
                if(((c*e)-(d*f)==5) and ((d*e)+(c*f)==0)):
                   print("("+str(c)+" + "+str(d)+"i) x "+
                         "("+str(e)+" + "+str(f)+"i)")
                
                
