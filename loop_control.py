#loop control statement = change loops execution from its sequence
#break, pass, continue = get out of the loop entirely, does nothing, skip to next iteration

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# phone_number = input("Write you number down: ")

# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end = "")

for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)