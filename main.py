from crud_oprations import CRUD

def main():
    crud = CRUD()
    while True:
        print("\n1. Create\n2. Read\n3. Update\n4. Delete\n5. Display All\n6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            key = input("Enter key: ")
            value = input("Enter value: ")
            crud.create(key, value)
        elif choice == '2':
            key = input("Enter key to read: ")
            print(crud.read(key))
        elif choice == '3':
            key = input("Enter key to update: ")
            value = input("Enter new value: ")
            crud.update(key, value)
        elif choice == '4':
            key = input("Enter key to delete: ")
            crud.delete(key)
        elif choice == '5':
            crud.display_all()
        elif choice == '6':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
