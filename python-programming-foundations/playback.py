#asks user for input phrase
phrase = str(input("Enter phrase: "))

#output phrase slowed down
slowed = '...'.join(phrase.split())
print(slowed)
