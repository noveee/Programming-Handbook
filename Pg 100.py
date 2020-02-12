# Challenge 1
string1 = "camus"
print(string1[0])
print(string1[1])
print(string1[2])
print(string1[3])
print(string1[4])

# Challenge 2
a = input("Input something: ")
b = input("Input something else: ")
print("Yesterday I wrote a {}. I sent to {}!".format(a, b))

# Challenge 3
print("aldous Huxley was born in 1894.".capitalize())

# Challenge 4
seperate = "Where now? Who now? When now?".split("?")
print(seperate)

# Challenge 5
listt = ["The", 
         "fox", 
         "jumped", 
         "over", 
         "the", 
         "fence", 
         "."]

fox = " ".join(listt)
fox = fox[0: -2] + "."
print(fox)

# Challenge 6
print("A screaming comes across the sky.".replace("s", "$"))

# Challenge 7
indexing = "Hemingway"
indexing = indexing.index("m")
print(indexing)

# Challenge 8
print("\"I live life faded\"")

# Challenge 9
thrice = "three "
print(thrice+thrice+thrice)
print(thrice * 3)

# Challenge 10
slicing = "It was a bright cold day in April, and the clocks were striking thirteen."
sliced = slicing[0:33]
print(sliced)