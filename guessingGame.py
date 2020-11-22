import random
count = [1, 2, 3, 4, 5]
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
store = int(random.uniform(1, 9))
for c in count:
    user = int(input("Enter your guess "))
    if(user > store):
        print("Your number is very high")
    elif(user < store):
        print("Your number is very low")
    elif(user == store):
        print("Your number is right")
        break
