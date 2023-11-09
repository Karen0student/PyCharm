import json
users_json = input()
updates_json = input()

with open(users_json, encoding='utf-8') as users_file:
    users_data = json.load(users_file)
with open(updates_json, encoding='utf-8') as updates_file:
    updates_data = json.load(updates_file)

for update in updates_data:
    for user in users_data:
        if user["name"] == update["name"]:
            for key, value in update.items():
                if key in user and value > user[key]:
                    user[key] = value
                elif key not in user:
                    user[key] = value

updated_users_data = dict()
for user in users_data:
    key = user['name']
    user.pop('name')
    updated_users_data[key] = user

with open(users_json, 'w', encoding='utf-8') as users_file:
    json.dump(updated_users_data, users_file, indent=4)
