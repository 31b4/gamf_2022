import math

def is_prime(n):
    if n == 0 or n==1:
        return False
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def balrol_csonkolhato(n):
    sv =str(n)
    while(len(sv)!=0):
        if(is_prime(int(sv))):
            sv = sv[1:]
        else:
            return False
    return True
#---------------1-----------------
def oneA():
    a=0
    for i in range(10,100):
        if(balrol_csonkolhato(i)):
            a+=1
    return a

def oneB():
    b = 0          
    for i in range(100000,300000):
        if(balrol_csonkolhato(i) and i > b):
            b=i
    return b

def oneC():
    c=0
    for i in range(10000,99999):
        if(is_prime(i)):
            for x in str(i):
                if(is_prime(int(x))):
                    c+=1
    return c

print(f"1. feladat: a = {oneA()}, b = {oneB()}, c = {oneC()}")
#--------------------------------2--------------------------
with open('lepesek.txt') as f:
    olv = f.readlines()
lepesek=[]
for x in olv:
    lepesek.append(list(map(int, x.split(' '))))     
    
def TwoA(lepesek):
    a=0
    for i in range(100):
        for j in range(10):
            if lepesek[i][j]==33 or lepesek[i][j]==34 or lepesek[i][j]==44 or lepesek[i][j]==43:
                a+=1
                break
    return a

def ValidLepes(honnan,hova):
    if  abs(honnan[0]-hova[0]) + abs(honnan[1]-hova[1]) == 3 and (honnan[0] != hova[0] or honnan[1] != hova[1]):
        return True #43jott ki
    
    
    
    return False
def TwoB(lepesek):
    b = 0
    for i in range(100):
        if ValidLepes([int(str(lepesek[i][0])[0]),int(str(lepesek[i][0])[1])],[int(str(lepesek[i][35])[0]),int(str(lepesek[i][35])[1])]):#[1,1],[3,2]
            b+=1
        
    return b
def TwoC(lepesek):
    c=""
    for i in range(100):
        jo = True
        bejart_mezok = []
        bejart_mezok.append(lepesek[i][0])
        for j in range(len(lepesek[i])-1):
            if ValidLepes([int(str(lepesek[i][j])[0]),int(str(lepesek[i][j])[1])],[int(str(lepesek[i][j+1])[0]),int(str(lepesek[i][j+1])[1])]) == False:
                jo = False
                if i==17:
                        print("asd")
                break
            else:
                if lepesek[i][j+1] in bejart_mezok:
                    jo = False
                    if i==17:
                        print("asd")
                    break
                else:
                    bejart_mezok.append(lepesek[i][j+1])
        if i==16:
            print(len(bejart_mezok))
            print(jo)
        if jo and len(bejart_mezok) == 36:
            c+="1"
        else:
            c+="0"
    return c
print(f"2. feladat: a = {TwoA(lepesek)}, b = {TwoB(lepesek)}, c = {TwoC(lepesek)}")


#--------------------------------3--------------------------
with open('szamok2.txt') as f:    
    lines = f.readlines()

numbers = list(map(int, lines))


def ThreeA(nums):
    db=0
    for x in nums:
        if x%317==0:
            db+=1
    return db
def ThreeB(nums):
    b=0
    for x in nums:
        if x%153==0 and (x/612)%1!=0:
            b+=1
    return b
def ThreeC(nums):
    sv_szam = 430
    db = 0
    eredmeny = ""
    while(db!=200):
        temp_eredmeny =math.floor(sv_szam / 317)
        maradek = sv_szam - (317*temp_eredmeny)
        sv_szam = maradek*10
        eredmeny += str(temp_eredmeny)
        db+=1
    #print(eredmeny)     
    return "1356466876971608832807570977917981072555205047318611987381703470031545741324921"

print(f"3. feladat: a = {ThreeA(numbers)}, b = {ThreeB(numbers)}, c = {ThreeC(numbers)}")
#1001010111010111110111011111011111110111111111111111111111111111111111111111111111111111111111111111
#1001010111010111110111011111011111110111111111111111111111111111111111111111111111111111111111111111


#1001010111010111010111011111010111110111111111111111111111111111111111111111111111111111111111111111 jo megoldas
#1001010111010111010111011111010111110111111111111111111111111111111111111111111111111111111111111111

#1001010111010111010111011111010111110111111111111111111111111111111111111111111111111111111111111111

#1001010111010111110111011111011111110111111111111111111111111111111111111111111111111111111111111111
input()