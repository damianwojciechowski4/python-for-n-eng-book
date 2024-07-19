integer= int("10")
print(integer)

#binary
binary = bin(10)
print(f"Binary '10': {binary}")

#hexadecimal
hexadecimal = hex(10)
print(f"Hexa '10': {hexadecimal}")

#list
# converts argument to a list
list1 = list("Hello")   
print(list1)

#set
## Converts an argument into a set of unordered, unique and unchagable items
set1 = set("Hello")
print(set1)

#tuple
tuple_2 = tuple (["1","2","3","4"])
print(f"Tuple: {tuple_2}")


#str
string1 = str(10)
print(string1)

#isdigit
test1="a".isdigit()
print(f"Is digit: {test1}")
test2="3".isdigit()
print(f"Is digit: {test2}")

#isalpha - allows to check whether a string contains only alphabetic characters
test3="Hello".isalpha()
print(f"Is alphabetic: {test3}")

test4 = "a1234-  ".isalpha()
print(f"Is alphabetic: {test4}")


#isalnum - checks whether a string contains of letters or numbers ONLY 
# for example no spaces
test5 = "asdasfa1asd  ".isalnum()
print(f"Is alphanumeric: {test5}")

test6 = "asdasfa1asd".isalnum()
print(f"Is alphanumeric: {test6}")

