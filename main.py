import Inputs

def print_users():
    users = Inputs.get_users()
    print("\nUser Information:")
    for user in users:
        print(f"Index: {user.index}, Name: {user.name}, Chip Count: {user.chip_count}")
    return users    

if __name__ == "__main__":
    users = print_users()
    keep_playing = "y"
    sb = 5
    i=0
    while keep_playing == "y":
        pot = 0
        i = i + 1
        print("------------Round :",i,"-------------------")
        print("\nSmall Blind : \t", sb)
        print("Big Blind : \t", sb*2)
        for user in users:
            print(f"Index: {user.index}, Name: {user.name}, Chip Count: {user.chip_count}")
            print("Removing 5 as tip from each user", user.chip_count)
            user.chip_count = user.chip_count - 5
            print("Removing 5 as tip from each user", user.chip_count)
        
        
        sb = sb *2
        keep_playing = input(f"Do you want to keep playing (y/n): ")
        print_users()
        
    
    

