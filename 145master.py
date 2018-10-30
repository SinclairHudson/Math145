import pprint

def order(number, ring):
    for x in range(ring):
        print(str(number)+"^"+str(x)+" = "+str(((number ** x)% ring)))
        if (((number ** x)% ring) == 1) and (x!=0):
            return x
    print("error, no power = 1 (mod n)")
    return -1

def finding_units(n):
    units = []
    primroots = []
    for x in range(n):
        for i in range(n):
            if(((x*i)%n)==1):
                units.append(x)
    print("The units, or Zn*, is the following set:")
    print(units)
    print("the number of units is "+str(len(units)))
    for y in units:
        breaking = 0
        
        for j in range (len(units)-1):
            if((y**j)%n==1 and j != 0):
                breaking = 1
        if(breaking == 0):
            primroots.append(y)
    print("the PRIMITIVE roots of Zn are as follows:")
    print(primroots)
    print("the number of primitive roots is "+str(len(primroots)))
def factors(n):            
    factors = []

    for z in range(1,n+1):
        if(n%z ==0):
            factors.append(z)
            
    print("The factors of "+str(n)+" are:")
    print(factors)
    print(str(n)+" has "+str(len(factors))+" factors.")

ring=17
for number in range(ring):
    print("-------------------------------------------------------------")
    finding_units(ring)
    print(str(number)+" has order of "+str(order(number, ring))+" in Z"+str(ring))
    #factors(number)
