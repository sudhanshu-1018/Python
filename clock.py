time=input("what is the time?(ex-15:00)")
  
if time>="00:00" and time<"12:00":
    print("good morning")
elif time>="12:00" and time<"15:00":
    print("good afternoon")
elif time>="15:00" and time<"19:00":
    print("good evening")
elif time>="19:00" and time<"00:00":
    print("good night")
else:
    print("invalid time")




import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hours = int(time.strftime('%H'))
# hours=int(input("Enter the hour:"))
minutes = int(time.strftime('%M'))
if hours >=0 and hours<12:
    print("good morning")
elif hours >= 12 and hours<15:
    print("good afternoon")
elif hours >= 15 and hours<19:
    print("good evening")
else:
    print("good night")
