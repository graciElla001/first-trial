#useless trivia
#ee cummings never uses uper case!!!

name = input("Hi, what's your name?")

print("\nIf poet ee cummings were to email you, he'd address you as", name.lower())
print("But if ee were crazy, he'd call you", name.upper())

called = name * 5
print ('\nIf a small child wants to get your attention')
print ('your name would be:')
print(called)

age = input("How old are you??")
age = int(age)
seconds = age * 365 * 24 * 60 * 60
print("\nYou are over", seconds, "seconds old")

weight = input("What is your present body mass index?")
weight = int(weight)
moon_weight = weight/6
print ("\nDo you know that on the moon, you would weigh only", moon_weight, "Pounds")
sun_weight = weight * 27.1
print ("\nDo you know that on the sun, you will weigh", sun_weight, "(but uhhm not for too long)")


input('\nPress the enter key to exit.')
