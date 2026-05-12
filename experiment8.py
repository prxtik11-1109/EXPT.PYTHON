#q-1
X = {"a": 3, "b": 1, "c": 2, "d": 5}

# Ascending order
ascending = dict(sorted(X.items(), key=lambda item: item[1]))
print("Ascending:", ascending)

# Descending order
descending = dict(sorted(X.items(), key=lambda item: item[1], reverse=True))
print("Descending:", descending)

#Q-2
X={"a":3,"b":1,"c":2,"d":5}
print("a" in X)

#Q-3
X={"a":3,"b":1,"c":2,"d":5}
Y={"e":12,"&":11,"9":9,"h":7}
X.update
print(X)

#Q-4
X=("jojo","Zo","dyp")
y=list(X)
y.insert(1,"adj")
z=tuple(y)
print(z)

#Q-5
my_tuple=(10,3.14,"hello",True,[1,2,3])
print("Tuple with different data types: ")
print(my_tuple)

#Q-6
a=[1,34,12,50]
X=sum(a)
print(X)

#Q-7
a=[1,34,12,50]
X=max(a)
print(X)

#Q-8
a={1,"adi","jojo"}
a.update({"john,5"})
print(a)

#Q-9
arr=[1,2,45,67]
arr.reverse()
print(arr)

#Q-10
arr=[10,20,30,40,50]
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])


