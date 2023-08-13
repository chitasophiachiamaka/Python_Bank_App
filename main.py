import Agent
import Customer

def main():
    print("Welcome to  Chita's Bank Management System for Agents!")

    while True:
        print("0 = Exit the Program")
        print("1. Agent")
        print("2. Customer")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            agent = Agent()
            agent.menu()
        elif choice == "2":
            customer = Customer()
            customer.menu()
        elif choice == "3":
            print("Thank you for using Chita's BanKApp!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
