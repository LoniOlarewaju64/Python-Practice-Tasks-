import random
capitals = { 
    "France": "Paris",
    "Japan": "Tokyo",
    "Egypt": "Cairo",
    "Denmark": "Cophenhagen"
}


country = random.choice(list(capitals.keys())) #Egypt
correct_answer = capitals[country] #Cairo

print(f"What is the capital of {country}?")
guess = input("Your answer: ").strip() # strip() removes whitespace.

if guess.lower() == correct_answer.lower(): # converts test into lowercase:
    print("Correct, good job!") 
else: 
    print(f"Not quite...the capital of {country} is {correct_answer}")