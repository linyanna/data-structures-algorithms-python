
# Question 1
expenses = [2200, 2350, 2600, 2130, 2190]

#1
answer1 = expenses[1]-expenses[0]

#2
total = 0
for i in range(3):
  total += expenses[i]
answer2 = total

#3
spent2000 = False
for i in expenses:
  if i==2000:
    spend2000 = True
answer3 = spent2000

#4
expenses.append(1980)
answer4 = expenses

#5
expenses[3] -= 200
answer5 = expenses

# Print Answers
print("answer 1: ", answer1, "\nanswer2: ", answer2, "\nanswer3: ", answer3, "\nanswer4: ",  answer4,  "\nanswer5: ",  answer5)
