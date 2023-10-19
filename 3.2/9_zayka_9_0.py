dictionary = dict()
mylist = []
while True:
    string = input()
    if string == '':
        break
    else:
        mylist.append(string)

for index in range(len(mylist)):
    word_list = mylist[index].split()
    for word in word_list:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

for key in dictionary:
    print(f"{key}: {dictionary[key]}")
