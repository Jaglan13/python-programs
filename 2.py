def set_operations(s):
    while True:
        print("\nSet Operations:")
        print("1. Length of set")
        print("2. Add element")
        print("3. Remove element")
        print("4. Union of sets")
        print("5. Intersection of sets")
        print("6. Difference of sets")
        print("7. Symmetric difference of sets")
        print("8. Check subset")
        print("9. Check superset")
        print("10. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Length of set:", len(s))
        elif choice == 2:
            element = input("Enter element to add: ")
            s.add(element)
            print("Element added successfully.")
        elif choice == 3:
            element = input("Enter element to remove: ")
            if element in s:
                s.remove(element)
                print("Element removed successfully.")
            else:
                print("Element not found in set.")
        elif choice == 4:
            s2 = eval(input("Enter another set (e.g., {1, 2, 3}): "))
            print("Union of sets:", s.union(s2))
        elif choice == 5:
            s2 = eval(input("Enter another set (e.g., {1, 2, 3}): "))
            print("Intersection of sets:", s.intersection(s2))
        elif choice == 6:
            s2 = eval(input("Enter another set (e.g., {1, 2, 3}): "))
            print("Difference of sets:", s.difference(s2))
        elif choice == 7:
            s2 = eval(input("Enter another set (e.g., {1, 2, 3}): "))
            print("Symmetric difference of sets:", s.symmetric_difference(s2))
        elif choice == 8:
            s2 = eval(input("Enter another set (e.g., {1, 2, 3}): "))
            if s2.issubset(s):
                print("It's a subset.")
            else:
                print("It's not a subset.")
        elif choice == 9:
            s2 = eval(input("Enter another set (e.g., {1, 2, 3}): "))
            if s.issuperset(s2):
                print("It's a superset.")
            else:
                print("It's not a superset.")
        elif choice == 10:
            print("Exiting set operations...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")


def list_operations(lst):
    while True:
        print("\nList Operations:")
        print("1. Length of list")
        print("2. Append element")
        print("3. Remove element")
        print("4. Sort list")
        print("5. Reverse list")
        print("6. Count occurrence of element")
        print("7. Index of element")
        print("8. Clear list")
        print("9. List slicing")
        print("10. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Length of list:", len(lst))
        elif choice == 2:
            element = input("Enter element to append: ")
            lst.append(element)
            print("Element appended successfully.")
        elif choice == 3:
            element = input("Enter element to remove: ")
            if element in lst:
                lst.remove(element)
                print("Element removed successfully.")
            else:
                print("Element not found in list.")
        elif choice == 4:
            lst.sort()
            print("List sorted successfully.")
        elif choice == 5:
            lst.reverse()
            print("List reversed successfully.")
        elif choice == 6:
            element = input("Enter element to count occurrence: ")
            count = lst.count(element)
            print("Count of", element, "is", count)
        elif choice == 7:
            element = input("Enter element to find index: ")
            try:
                index = lst.index(element)
                print("Index of", element, "is", index)
            except ValueError:
                print(element, "not found in list.")
        elif choice == 8:
            lst.clear()
            print("List cleared successfully.")
        elif choice == 9:
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced list:", lst[start:end])
        elif choice == 10:
            print("Exiting list operations...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")


def main():
    while True:
        print("\nMenu:")
        print("1. Set Operations")
        print("2. List Operations")
        print("3. Exit")

        option = int(input("Enter your choice: "))

        if option == 1:
            s = eval(input("Enter a set (e.g., {1, 2, 3}): "))
            set_operations(s)
        elif option == 2:
            lst = eval(input("Enter a list (e.g., [1, 2, 3]): "))
            list_operations(lst)
        elif option == 3:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
