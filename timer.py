import time

## type a number of seconds
seconds = int(input("Enter the number of seconds: "))

#starts loop
while seconds >= 0:
  #seperates times into hours, minutes and seconds
  mins,secs = divmod(seconds, 60)
  print(f"\r{mins:02}:{secs:02}", end="")

  #countdown motion
  time.sleep(1)
  seconds -=1

print("\n TIMES UP !!!")