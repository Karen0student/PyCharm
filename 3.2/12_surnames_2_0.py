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

flag = False
sorted(dictionary)
print(dictionary)
#for key in dictionary:
for key in sorted(dictionary.keys()):
    if dictionary[key] > 1:
        print(f"{key} - {dictionary[key]}")
        flag = True
if flag is False:
    print("Однофамильцев нет")
