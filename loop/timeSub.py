import random
import time

correctCount = 0
count = 0
NUMBER_OF_QUESTIONS = 5

startTime = time.time()

while count < NUMBER_OF_QUESTIONS:
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)

    # Ensure number1 is larger than number2 for positive subtraction results
    if number1 < number2:
        number1, number2 = number2, number1
    
    # Properly display the subtraction question and use int() for input
    answer = int(input(f"What is {number1} - {number2}? "))

    if number1 - number2 == answer:
        print("You are correct!")
        correctCount += 1
    else:
        print(f"Your answer is wrong. The correct answer is {number1 - number2}.")
    
    count += 1

endTime = time.time()
testTime = int(endTime - startTime)

print(f"Correct count is {correctCount} out of {NUMBER_OF_QUESTIONS} \nTest time is {testTime} seconds")
