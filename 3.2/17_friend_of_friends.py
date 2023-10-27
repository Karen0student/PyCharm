friends_level_1 = {}

while (line := input()) != "":
    pair = line.split()
    friends_level_1.setdefault(pair[0], set()).add(pair[1])
    friends_level_1.setdefault(pair[1], set()).add(pair[0])
friends_level_2 = {}
for person, friends in friends_level_1.items():
    friends_level_2_set = set()
    for friend_1 in friends:
        friends_level_2_set = friends_level_2_set.union(friends_level_1[friend_1])
    for friend_2 in friends_level_2_set:
        friends_level_2.setdefault(person, set())
        if friend_2 not in friends_level_1[person] and friend_2 != person:
            friends_level_2[person].add(friend_2)

friend_sorted_keys = sorted(friends_level_2.keys())
for person in friend_sorted_keys:
    print(f'{person}: ', end="")
    print(', '.join(sorted(friends_level_2[person])))
