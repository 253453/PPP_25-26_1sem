
class User:
    def __init__(self, uid, name, email):
        self.uid = uid
        self.name = name
        self.email = email

    def __str__(self):
        return f'{self.name} <{self.email}>'

def parse_csv(line):
    parts = line.split(';')
    if len(parts) == 3:
        return User(parts[0], parts[1], parts[2])
    return None

def parse_json(line):
    import json
    obj = json.loads(line)
    uid = str(obj.get('uid', ''))
    name = obj.get('first_name', '') + ' ' + obj.get('last_name', '')
    email = obj.get('contacts', {}).get('email', '')
    return User(uid, name.strip(), email)

def parse_raw(line):
    import re
    email_match = re.search(r'\[([^\]]+)\]', line)
    if email_match:
        email = email_match.group(1)
        name_part = line[:email_match.start()].strip()
        parts = name_part.split()
        if len(parts) == 2:
            name = parts[1] + ' ' + parts[0]  
        else:
            name = name_part
        return User('', name, email)
    return None

users = []

data = [
    'csv 123;Иван Иванов;ivan@example.com',
    'json {"uid":42,"first_name":"Petr","last_name":"Petrov","contacts":{"email":"petr@example.com"}}',
    'raw Иванов Иван [ivanov@example.com]',
    'csv 999;Пётр Петров;bad-email',
]

for line in data:
    if line.startswith('csv '):
        user = parse_csv(line[4:])
    elif line.startswith('json '):
        user = parse_json(line[5:])
    elif line.startswith('raw '):
        user = parse_raw(line[4:])
    else:
        user = None
    if user:
        users.append(user)

print('Пользователи:')
for u in users:
    print(u)


