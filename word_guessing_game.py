import random

print("Welcome to the Word Guessing Game!")
words = ["home", "tode", "four", "nest"]
word = random.choice(words)
turns = 5
right_ans = set()
all_ans = ""
print(f"Guess the correct word. It has {len(word)} letters.")

while turns > 0:
  ask = input("Guess a character: ")
  all_ans += ask

  for i in word:
    if i in all_ans:
      print(i, end = " ")
      right_ans.add(i)

    else:
      print("_", end = " ")

  if ask not in word:
    turns = turns - 1
    print("\nIncorrect guess! Remaining attempts:", {turns})
    
  if turns == 0:
    break

  if right_ans == (q:=set(word)):
    print(f"Congratulations, you guessed the word \'{word}\'")
    break
    
if right_ans != q:
  print("You lost.")