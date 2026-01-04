import random

def game():
    num_comp=random.randint(1,100)
    attempts=0
    print("Welcome to number guessing game!")
    print("i have chosen a number between 1 to 100\n let's see if u can guess!")

    while True:
       num_user= int(input("Enter your guess:"))
       attempts+=1

       if num_user==num_comp:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.") 
        break
       elif abs(num_user - num_comp) <= 5:
            print("🔥 Too close!")
       elif num_user>num_comp:
        print("Too high")
       elif num_user<num_comp: 
        print("Too low")      

def main():
    game()

if __name__ == "__main__":
    main()