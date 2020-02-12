# Challenge 1
list = ["The Walking Dead",
        "Entourage",
        "The Sopranos",
        "The Vampire Diaries"]
for shows in list:
    print(shows)

# Challenge 2
for i in range(25,51):
    print(i)

# Challenge 3
i = 0
for shows in list:
    print(shows, "is in index:", i)
    i += 1

# Challenge 4
numbers = [1, 2, 3]
q = "yes"
while q.lower() == "yes":
    guess = input("Guess a number in the list\n")
    guess = int(guess)
    if (guess == numbers[0] or guess == numbers[1] or guess == numbers[2]):
        print("You guessed correctly!")
        break
    else: 
        print("You guessed wrong")
    q = input("Do you want to continue?\n")

# Challenge 5
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []

for x in list1:
    for y in list2:
        list3.append(x*y)

print(list3)