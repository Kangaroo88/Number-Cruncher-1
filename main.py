
import time
import random

print('Number Crunchers! \n')
level = ''
while level != 'easy': #making sure input is easy
  level = input('Please type easy to begin: ')


#Introduction / storyline
username = input('Hey, what is your name? ')
print(' \n9:00 A.M. - It is a hot sunny day. Sarah was sweating and to make it worse, her teacher gave her class an online assessment!')
print('She did not have any time to study! ')
print('It is your job to help her succeed throughout all the levels.')
print('By doing this Sarah promised to buy you an ice cream to cool off!')
print('Sarah clicks the button to start and it says:')

 

# The easy level 
if level == 'easy':
  right = 0 #counting score of correct answers
question = 0 #counting the number of questions in total
print('\nPart A of the asessment: ')
for x in range(100):
  num1 = random.randint(1,100) 
  num2 = random.randint(1,100)
  print ('What is', num1, '+', num2, '=')
  start = time.time()
  
  #Making sure input is valid
  try:
    guess = int(input(""))
  except ValueError:
    print('Please enter another valid answer! ')
    question += 1
    print('What is', num1, '+', num2, '=')
    guess = int(input(""))
  answer = num1 + num2
  if guess == answer: #if the guess is correct
    print('That is correct!')
    right += 1 
    question += 1 
  else:
    print("That is wrong!") #if the guess is wrong
    print('The correct answer is' , answer)
  question += 1
  if right == 5: # if the score is 5, the user can move on
    print ("You correctly completed" , right , "questions! ")
    break
      

    

# The medium level
level = input('\nType next to move to the next page: ')
while level != 'next': #Making sure the input is next
  level = input('Please enter next to begin: ')
if level == 'next': 
  right = 5
print('\nPart B of the assessment: ')
for x in range(100):
  num1 = random.randint(50,100) 
  num2 = random.randint(1,49)
  #making sure num2 isn't greater than num1 or they aren't the same
  print ('What is', num1, '-', num2, '=')
  #making sure guess is a valid input
  try:
    guess = int(input(""))
  except ValueError:
    print('Please enter another valid answer! ')
    question += 1
    print('What is', num1, '-', num2, '=')
    guess = int(input(""))
  answer = num1 - num2
  if guess == answer: #if guess is correct
    print('That is correct!')
    right += 1 #counting score of correct answers
    question += 1
  else:
    print("That is wrong!") #if guess is wrong
    print('The correct answer is' , answer)
    question += 1
  if right == 10: #Once score is equal to 10, user can move on
      print ("You correctly completed" , right , "questions! ")
      break




#Hard level
level = input('\nType next to complete the final page: ')
if level == 'next':
  right = 10
  print('Part C of the assessment: ')
for x in range(12):
  num1 = random.randint(1,12)
  num2 = random.randint(1,12)
  print ('What is', num1, '*', num2, '=')
  #Making sure the input is valid
  try:
      guess = int(input(""))
  except ValueError:
      print('Please enter another valid answer! ')
      question += 1
      print('What is', num1, '*', num2, '=')
      guess = int(input(""))
  answer = num1 * num2   
  if guess == answer: #if guess is correct
    print('That is correct!')
    right += 1 
    question += 1
  else:
    print("That is wrong!") #if guess is wrong
    print('The correct answer is' , answer)
    question += 1
  if right == 15: #Once score is equal to 15, user can move on
    end = time.time()
    length = round(end - start)
    question = (question - 5)
    print("\nYour final score is : " ,right, "out of", question , ". You finished in" , length , "seconds!")
    break
  

      #bad ending
if question > 17:
  print('Keep on trying', username,'! ', 'Remember perserverance is the key to success! No matter how many times you are wrong, keep trying to understand and then hopefully you will!')
  
      #good ending
if question < 18:
  print('Congratulations', username, '! ' 'You did an excellent job on the test. You are granted your ice cream to cool you off!')


    



