number = int(input("Which number's table you want? : "))
b = int(input('Till...? : '))
for i in range(1,b+1):
    print(a,"x",i,"=",a*i)
    if i == b+1:
        break
print("Here's your table :)")
