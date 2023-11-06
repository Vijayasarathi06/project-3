##stone paper sicessor
import random
while True:
  player=str(input("enter the choice of rock, paper and scissors:"))
  computer=random.choice(["rock","paper","scissors"])
  if player==computer:
    print("tie")
  elif player=="rock":
    if computer=="paper":
      print(f"you loss {computer} covers {player}")
    else:
      print(f"you win {player} smashed {computer}")
  elif player=="paper":
    if computer=="scissors":
      print(f"you loss {computer} cut {player}")
    else:
      print(f"you win {player} coveded {computer}")
  elif player=="scissors":
    if computer=="rock":
      print(f"you loss {computer} smashed {player}")
    else:
      print(f"you win {player} cut {computer}")
  else:
    print("check the spelling")
####
####palindrom number
num=int(input("enter the value of number"))
y=num
result=0
while(y>0):
    x=y%10
    result=result*10+x
    y=y//10
if num==result:
    print(result)
else:
    print("False")
##Stars
stop=int(input("enter the stop value"))
for i in range(stop):
    for j in range(i):
        print(" ",end="")
    for k in range(stop-i):
        print("*",end=" ") 
    print("")





















