import Inputs

def main():
    users = Inputs.get_users()
    print("\nUser Information:")
    for user in users:
        print(f"Index: {user.index}, Name: {user.name}, Chip Count: {user.chip_count}")

if __name__ == "__main__":
    main()
