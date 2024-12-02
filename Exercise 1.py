import random

def displayMenu():
    print("DIFFICULTY LEVEL")
    print("1. Easy")
    print("2. Moderate")
    print("3. Advanced")
    while True:
        try:
            choice = int(input("Select a difficulty level (1-3): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please select a valid difficulty level.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def randomInt(difficulty):
    if difficulty == 1: 
        return random.randint(1, 9)
    elif difficulty == 2:  
        return random.randint(10, 99)
    elif difficulty == 3:  
        return random.randint(1000, 9999)

def decideOperation():
    return random.choice(['+', '-'])

def displayProblem(num1, num2, operation):
    return f"{num1} {operation} {num2} = "

def isCorrect(user_answer, correct_answer):
    return user_answer == correct_answer

def displayResults(score):
    print(f"Your final score is {score} out of 100.")
    if score >= 90:
        print("Grade: A+")
    elif score >= 80:
        print("Grade: A")
    elif score >= 70:
        print("Grade: B")
    elif score >= 60:
        print("Grade: C")
    else:
        print("Grade: F")

def main():
    play_again = 'yes'
    while play_again.lower() == 'yes':
        difficulty = displayMenu()
        score = 0
        
        for _ in range(10):
            num1 = randomInt(difficulty)
            num2 = randomInt(difficulty)
            operation = decideOperation()
            
            if operation == '+':
                correct_answer = num1 + num2
            else:
                correct_answer = num1 - num2

            problem = displayProblem(num1, num2, operation)
            first_attempt = True
            while True:
                try:
                    user_answer = int(input(problem))
                    if isCorrect(user_answer, correct_answer):
                        if first_attempt:
                            score += 10
                        else:
                            score += 5
                        print("Correct!")
                        break
                    else:
                        if first_attempt:
                            print("Incorrect. Try again.")
                            first_attempt = False
                        else:
                            print(f"Incorrect. The correct answer is {correct_answer}.")
                            break
                except ValueError:
                    print("Invalid input. Please enter a number.")

        displayResults(score)
        play_again = input("Would you like to play again? (yes/no): ")

if __name__ == "__main__":
    main()
