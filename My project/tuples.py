# python tuples
# access
# newtuples=[1,2,3,"arfin","false"]
# print(newtuples[2])
# # negative indexing
# print(newtuples[-4])

# # range of tuples
# newtuples=("apple","banana","cherry","orrange","kiwi","melon","mango")
# print(newtuples[2:5])

# upldate tuples
# newtuples=("apple","banana","cherry","orrange","kiwi","melon","mango")
# a= list(newtuples)
# a.insert(3,"papaya")
# newtuples= tuple(a)
# print(newtuples)

# unpack tuple
# fruits =("apple","banana","cherry","orrange","kiwi","melon","mango")
# (a,b,c,*d)= fruits
# print(a,b,d)

# loop tuple with for loop

# fruits=("apple","banana","cherry","orrange","kiwi","melon","mango")
# for i in fruits:
#     print (i)

# loop with range
# fruits=("apple","banana","cherry","orrange","kiwi","melon","mango")
# for i in range(len(fruits)):
#     print(fruits[i])

# while loop
# fruits=("apple","banana","cherry","orrange","kiwi","melon","mango")
# x=0
# while x<len(fruits):
#     print (fruits[x])
#     x = x + 1

# join tuples
# tuples1 =(1,2,23,4,)
# tuples2 = (5,6,7,8,9)
#
# tuples3 = tuples1 + tuples2
# print (tuples3)


# # multiply tuplea
# fruits =("apples","banana", "cherry")
# b = fruits*3
# print(b)

# tuples mathods count
# fruits = ('apples', 'banana', 'cherry', 'apples', 'banana', 'cherry', 'apples')
# apples= fruits.count("apples")
# print (apples)

# tuples mathod index
# index= ('banana', 'cherry', 'apples', 'banana', 'cherry')
# f= index.index('apples')
# print (f)