# zip(*iterable) = combine element from two or more iterables. create zip object with paired elements stored in tuples for ewachj element

usernames = ["Chris", "Dude", "Bro"]
passwords = ("qwerty123", "abc123", "password")
login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]

users = zip(usernames, passwords, login_date)

print(type(users))

# for key, value in users.items():
#     print(key + " : " + value)

for i in users:
    print(i)