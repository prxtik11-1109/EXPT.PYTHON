#display even num from 1-10
for i in range(2,11,2):
    print(i)
 
#to add odd numbers from 1-10
sum=0
for i in range(1,11,2):
 sum += i
print(sum)

#fibonacci series between 0-50
a = 0
b = 1
while a <= 50:
    print(a, end=" ")
    a, b = b, a + b

#remove char which have odd index values of a given string
A = input("Enter a string: ")
result = ""
for x in range(len(A)):
    if x % 2 == 0:   
        result += A[x]
print(result)



