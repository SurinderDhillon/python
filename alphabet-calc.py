import string

# Creating num list to store 1-26 numbers
num = []
for i in range(1,27):
  num.append(i)

# Creating alph list to store a-z alphabet
alph = []
for j in string.ascii_lowercase:
  alph.append(j)

# Joining alph and num
a = dict(zip(alph, num))

# Taking input value
user_value = input("Enter string: ")

# Using while loop to enter only alphabet
while not user_value.isalpha(): 
    print("Please enter alphabet only")
    user_value = input("Enter string: ")  

# Slicing every character
new_string = list(user_value)

# Creating blank list and dictionary
list1 = []
list2 = []
dict1 = {}

# Finding the values of each alphabet
for index, key in enumerate(a):
    for val in new_string:
      if val == key:
        list1.append("%s" % (key))    # Storing into list1
        list2.append("%s" % (a[key])) # Storing into list2
        
# Converting list2 into integer
list2 = list(map(int, list2))

# Merging two list into dictionary
dictionary = dict(zip(list1, list2))

# Printing the result
print("Total of the alphabet is : %s " % (sum(dictionary.values())))
