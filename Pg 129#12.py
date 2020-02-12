import os 
import csv

# Challenge 1
text = open("text.txt", "r")
print(text.read())
text.close()

# Challenge 2
quest = input("Hi whats your name?\n")
answer = open("Pg 129.txt", "w")
answer.write(quest)
answer.close()

# Challenge 3
movies = [["Top Gun", "Risky Business", "Minority Report"], 
          ["Titanic", "The Revenant", "Inception"],
          ["Training Day", "Man on Fire", "Flight"]]
with open("Pg 129.csv", "w", newline='') as work:
    w = csv.writer(work, delimiter=",")
    w.writerow(movies[0])
    w.writerow(movies[1])
    w.writerow(movies[2])
