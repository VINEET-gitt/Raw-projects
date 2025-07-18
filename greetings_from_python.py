# TAKE GREETINGS FROM PYTHON
import time 
n = input("Enter your name : ")
a = time.strftime("%I:%M %p")
a1 = int(time.strftime("%H"))
if (a1 >= 0 and a1 < 12):
    print("Good morning",n)
elif (a1 >= 12 and a1 < 17):
    print("Good afternoon",n)
elif (a1 >= 17 and a1 < 21):
    print("Good evening",n)
elif (a1 >= 21 and a1 < 24):
    print("Good night",n)
print("It's been",a)