#Password Generator Project
import random
# import shuffle
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
alet= int(input("How many letters would you like in your password?\n")) 
asym = int(input(f"How many symbols would you like?\n"))
anum = int(input(f"How many numbers would you like?\n"))

# alet = 5
# anum = 3
# asym = 2


llet = len(letters) -1
lnum = len(numbers) -1
lsym = len(symbols) -1

# print (llet)
# print(lnum)
# print(lsym)

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

pass1 = ("")



for let in range (1 , alet+1):
  rlet = random.randint(1 , llet)
  # print (letters[rlet])
  pass1 += letters[rlet]


for num in range (1 , anum+1):
  rnum = random.randint(1 , lnum)
  # print (numbers[rnum])
  pass1 += numbers[rnum]

for sym in range (1 , asym+1):
  rsym = random.randint(1 , lsym)
  # print (symbols[rsym])
  pass1 += symbols[rsym]

pass1 = str(pass1)

print(pass1)

plst1 = list(pass1)

# print(plst1)

random.shuffle(plst1)

# print(plst1)

pass2 =("")

for i in plst1:
  pass2 += i 
  # print (pass2)



print (pass2)
















#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P