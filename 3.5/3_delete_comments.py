from sys import stdin
my_list = []
for line in stdin:
    print_text = ""
    for word in line.split():
        if "#" in word:
            my_list.append(print_text)
            break
        else:
            print_text += word + " "
    # if string != my_list[-1]:
print("\n".join(my_list))






# from sys import stdin
# my_list = []
# for line in stdin:
#     my_list.append(line.rstrip("\n"))
#
# for index in range(len(my_list)):
#     print_text = ""
#     for word in my_list[index].split():
#         if "#" in word:
#             print(print_text)
#             break
#         else:
#             print_text += word + " "
#     # if string != my_list[-1]:




# old
# from sys import stdin
# my_list = []
# for line in stdin:
#     my_list.append(line.rstrip("\n"))
# print()
# for string in my_list:
#     for word in string:
#         if string[0] == "#":
#             break
#         if word == "#":
#             if string != my_list[-1]:
#                 print()
#             break
#         else:
#             print(word, end="")
