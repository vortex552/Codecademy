import random

name = ""
question = "Will I win the lottery?"
answer = ""

if name == "":
  print(question)
elif question == "":
  print("Are you losers going to ask me a question sometime this decade or do I need to wait till the next decade arrives...")
else:
  print(str(name) + " asks: " + str(question))


random_number = random.randint(1, 11)
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
 answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "That question sucks ass."
elif random_number == 11:
  answer = "Jesus, what loser is writing these questions?"
else:
  print("Error")

print("Magic 8-Ball's answer: " + answer)
