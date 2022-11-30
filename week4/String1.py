# str class
# collection of characters
# character - symbol of language
# english -> characters - 256
# alphabets (a-zA-Z) - string
# digits (0 - 9) - numeric type
# symbols (*, & ,# ,? , #) etc
# control(Ctrl, Shift, Alt)
# 256 characters in american english language
# character -> Numeric value
# character value -> ASCII value
# ASCII Value -> Character
# 65 -> A
# 66 -> B
# 67 -> C

# Declare and initialize
# str1 = "PCPS College"
# str2 = 'PCPS College'
# str3 = """PCPS College""" # multiline string
# str4 = '''PCPS College''' # multiline string

# Explore str class
# capitalize(self, /)
# Return a capitalized version of the string
# str1 = "pcps college"
# str2 = str1.capitalize()
# print(str1)
# print(str2)

# casefold(self, /)
# Return a version of the string suitable
# password1 = 'admin'
# password2 = "Admin"
# result = password1 == password2
# print(result)

# pwd1 = password1.casefold()
# pwd2 = password2.casefold()
# result2 = pwd1 == pwd2
# print(result2)

# center(self, width, fillchar = '', /)
# amount = 123.456
# result = str(amount).center(20, '*') # center justified
# result = str(amount).ljust(20, '*') # left justified
# result = str(amount).rjust(20, '*') # right justified
# print(result)

# count(sub[, start[, end]]) -> int
# str1 = """Padding is done using the spaces"""
# str2 = "is"
# result = str1.count(str2)
# print(result)

# Reading text file
# file = open("TheHungerGames.txt")
# str1 = file.read(100)
# str1 = file.readlines()
# str2 = " ".join(str1)
# result = str2.count('the ')
# result1 = str2.count('The ')
# print(result)
# print(result1)
# print(len(str2))
# print(type(str1))
# print(str1)

# list to string
# list1 = ['word1', 'word2', 'word3']
# str2 = " ".join(list1)
# print(len(str2))
# print(str2)

# endswith(suffix[, start[, end]]) -> bool
# str1 = "pcps college."
# result = str1.endswith(';')
# print(result)

# expandtabs(self, /, tabsize=8)
# str1 = "SN\tNAME\tADDRESS"
# str2 = str1.expandtabs(tabsize=20)
# print(str2)
# print(str1)

# find(sub[, start[, end]]) -> int
# str1 = "pcps college, lalitpur"
# str2 = 'l'
# str3 = 'o'

# count = str1.count(str2)

# result1 =str1.find(str3)
# result = str1.find(str2)
# print(result1)
# print(result)

# print(count)

# r1 = str1.find(str2)
# print(r1)
# r2 = str1.find(str2, r1+1)
# print(r2)
# r3 = str1.find(str2, r2+1)
# print(r3)
# r4 = str1.find(str2, r3+1)
# print(r4)

# Automated?
str1 = "pcps college, lalitpur"
str2 = "l"
count = str1.count(str2)
result = -1
results = []
for i in range(count):
    result = str1.find(str2, result+1)
    results.append(result)
    print(result)
    print(results)
    # print(i)