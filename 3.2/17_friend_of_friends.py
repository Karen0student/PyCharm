# Create an empty dictionary to store friends of each person
people = {}

# Read names and build the list of friends
while True:
    line = input()
    if not line:
        break

    person1, person2 = line.split()

    # Add person2 to the list of friends of person1
    if person1 in people:
        people[person1].append(person2)
    else:
        people[person1] = [person2]

print(people)
# Create a set to store 2nd level friends
level_2_friends = {}

# Find 2nd level friends for each person
for person in people:
    level_1_friends = people[person]  # list
    level_2_friends[person] = set()  # set

    # Iterate through level 1 friends and add their friends to level 2
    for friend in level_1_friends:
        if friend in people:
            level_2_friends[person].update(people[friend])

# Sort the results and print them
for person in sorted(level_2_friends.keys()):
    friends = sorted(level_2_friends[person])
    print(f"{person}: {', '.join(friends)}")
