first = int(input("\nEnter a first number: "))
last = int(input("\nEnter a last number: "))
skips = int(input("You want it to count in: "))
for i in range(first, last, skips):
    print (i)

input("\nPress the enter key to exit")

