dictionary = dict()
mylist = []
number = int(input())

for _ in range(number):
    mylist.append(input())

for index in range(len(mylist)):
    word_list = mylist[index].split()
    for word in word_list:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

result = 0
for key in dictionary:
    if dictionary[key] > 1:
        result += dictionary[key]

print(result)
