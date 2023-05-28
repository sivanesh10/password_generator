import random
n=input("Want to generate password? Y/N")
u_caselist="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
l_caselist="abcdefghijklmnopqrstuvwxyz"
digitlist ="0123456789"
symb= "@#$%^&*"
pswd = ""
if n=="Y":
   for i in range(3):

        pswd+=random.choice(u_caselist)
        pswd+=random.choice(l_caselist)
        pswd+=random.choice(digitlist)
        pswd+=random.choice(symb)

else:

    print("check the spelling")
    exit()

print("Here is Your Password")
p=random.sample(pswd,len(pswd))
for i in pswd:
    print(i,end="")
