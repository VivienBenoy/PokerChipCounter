import User.py

def get_users():
    users = []
    num_users = int(input("Enter the number of users at the table: "))

    for i in range(1, num_users + 1):
        name = input(f"Enter the name of user {i}: ")
        chip_count = int(input(f"Enter the chip count for user {i}: "))
        user = User(i, name, chip_count)
        users.append(user)

    return users

