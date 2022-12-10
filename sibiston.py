
currency={"USD":81,"EUR":84,"INR":1,"Pound":97,"Chinese yuan":11.41,"Brazillian Real":15,"Russia's Rubal:,"Canadian dollar":}
def convert(c1,a,c2):
    if(c2=="INR"):
        print("The currency in",c1,"After converting into %s is"%c2,(a*currency[c1]))
    elif(c1=="INR"):
        print("The currency in",c1," After converting into %s is"%c2,(a/currency[c2]))
    else:
        print("The currency in",c1," After converting into %s is"%c2,(a/currency[c2])*currency[c1])
print("--------------------------------")
print("| currency converter |")
print("--------------------------------")
for M in currency.keys():
     print(M)
c1=input("Enter The Currency: ")
a=int(input("Amount: "))
c2=input("Enter The Currency you want to convert to: ")
convert(c1,a,c2)
print("--Vise-Versa--".center(130,"-"))
convert(c2,a,c1)