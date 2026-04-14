fruits=["apple","mango","banana","grapes","papaya"]
print("apple" in fruits)
print("banana" not in fruits                                                                   )


fruits=["apple","mango","banana","grapes","papaya"]
print(fruits[1])
print(fruits[-2])
print(fruits[:3])


fruits=["apple","mango","banana","grapes","papaya"]
fruits[2] = "orange"
fruits.append("pineapple")
fruits.insert(1,"kiwi")
del fruits[4]
print(fruits)


list1=["apple","mango","banana"]
list2=["grapes","papaya"]
 
print(list1 + list2)
print(list1 * 2)
print(len(list2))
print(max(list2))
print(min(list1))
