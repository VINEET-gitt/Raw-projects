# TAKE GREETINGS FROM PYTHON
import time 
name = input("Enter your name : ")
current_time = time.strftime("%I:%M %p")
hrs = int(time.strftime("%H"))
if (hrs >= 0 and hrs < 12):
    print(f"Good morning {name}.")
elif (hrs >= 12 and hrs < 17):
    print(f"Good afternoon {name}.")
elif (hrs >= 17 and hrs < 21):
    print(f"Good evening {name}.")
elif (hrs >= 21 and hrs < 24):
    print(f"Good night {name}.")
print("It's been",current_time)
