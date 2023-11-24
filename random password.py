import string
import random
str1 = list(string.ascii_lowercase)
str2 = list(string.ascii_uppercase)
str3 = list(string.digits)
str4 = list(string.punctuation)
input1 = input("How many characters do you want in your password? ")
while True:
    try:
        characters_number = int(input1)
        if characters_number < 8:
            print("Your number should be at least 8.")
            input1 = input("Please, Enter your number again: ")
        else:
            break
    except:
        print("Please, Enter numbers only.")
        input1 = input("How many characters do you want in your password? ")
random.shuffle(str1)
random.shuffle(str2)
random.shuffle(str3)
random.shuffle(str4)
part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))
result = []
for x in range(part1):
    result.append(str1[x])
    result.append(str2[x])
for x in range(part2):
    result.append(str3[x])
    result.append(str4[x])
random.shuffle(result)
password = "".join(result)
print("Strong Password: ", password)