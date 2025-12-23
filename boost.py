#BOOSTED SECTION CHANCE SCRIPT
#MORE POST=LESS CHANCE TO BE BOOSTED\

import random

#inputs
print("input sb post count")
sb=int(input())
print("input hym post count")
hym=int(input())
print("input gh post count")
gh=int(input())
print("input fg post count")
fg=int(input())
print("input ot post count")
ot=int(input())
print("input # of boost")
numboost=input()
print("input date of the next week")
date=input()

total=sb+hym+gh+fg+ot

#calculate initial chance
chance1=1/(sb+1)
chance2=1/(hym+1)
chance3=1/(gh+1)
chance4=1/(fg+1)
chance5=1/(ot+1)
totalchance=chance1+chance2+chance3+chance4+chance5

#ac stands for actual chance
ac1=round(chance1/totalchance*100,2)
ac2=round(chance2/totalchance*100,2)
ac3=round(chance3/totalchance*100,2)
ac4=round(chance4/totalchance*100,2)
ac5=round(chance5/totalchance*100,2)

#for final usage, 0 to ac1 = sb, ac1 to ac2 = hym, ac2 to ac3 = gh, ac3 to ac4 = fg, ac4 to 1 = ot
calcc1=round(ac1,2)
calcc2=round(ac1+ac2,2)
calcc3=round(ac1+ac2+ac3,2)
calcc4=round(ac1+ac2+ac3+ac4,2)
calcc5=round(ac1+ac2+ac3+ac4+ac5,2)
calcd1=round(calcc1+0.01,2)
calcd2=round(calcc2+0.01,2)
calcd3=round(calcc3+0.01,2)
calcd4=round(calcc4+0.01,2)

#display
print(f"It's time for the {numboost} section boost of the season! The chosen section will receive +35% likes in the next week.")
print()
print("(Please note that replies, profile posts and special sections will not be included in section bonuses.)")
print("below is the chance for each section this week:")
print(f"The number of total post is {total}.")
print(f"Suggestion Box: {ac1}% ({sb} posts)")
print(f"Hypixel Minigames Discussions: {ac2}% ({hym} posts)")
print(f"Guides/Help: {ac3}% ({gh} posts)")
print(f"Forum Games: {ac4}% ({fg} posts)")
print(f"Off Topic: {ac5}% ({ot} posts)")
print("meaning from 0 to", calcc1, "Suggestion Box will be the boosted section")
print("from", calcd1, "to", calcc2, "Hypixel Minigames Discussions will be the boosted section")
print("from", calcd2, "to", calcc3, "Guides/Help will be the boosted section")
print("from", calcd3, "to", calcc4, "Forum Games will be the boosted section")
print("from", calcd4, "to", calcc5, "Off Topic will be the boosted section.")
print()

boostedchoice=round(random.random()*100,2)
print(f"The boosted number is {boostedchoice}.")
if boostedchoice<=calcc1:
  print("The boosted section is Suggestion Box Section.")
elif (boostedchoice<=calcc2):
  print("The boosted section is Hypixel Minigames Discussions Section.")
elif (boostedchoice<=calcc3):
  print("The boosted section is Guides/Help Section.")
elif (boostedchoice<=calcc4):
  print("The boosted section is Forum Games Section.")
elif (boostedchoice<=calcc5):
  print("The boosted section is Off Topic Section.")

print(f"This section bonus will last to {date}, which is one week from now.")
