#which one is greatest value
a=int(input("enter first num: ",))
b=int(input("enter second num: ",))
c=int(input("enter third num: ",))
if a>b and a>c:
  print("a is greatest value number")
elif b<a and b<c:
  print("b is greatest value no")
else:
  print("c is greatest value num")

#odd or even
a=int(input("enter the value of a: "))
if a % 2 ==0:
   print("a is even number")
else:
  print("a is odd number")

#uppercase or lowercase
char = input("Enter a character: ")

if char.isupper():
    print("Character is uppercase")
else:
    print("Character is lowercase")

#number or character
A = input("Enter value of A: ")

if A.isalpha():
    print("A is a character")
else:
    print("A is a number")





