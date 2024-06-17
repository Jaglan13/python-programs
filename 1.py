def string_operations(s):
    while True:
        print("\nString Operations:")
        print("1. Length of string")
        print("2. Reverse string")
        print("3. Uppercase")
        print("4. Lowercase")
        print("5. Count vowels")
        print("6. Count consonants")
        print("7. Check palindrome")
        print("8. Replace vowels with '*'")
        print("9. Remove whitespace")
        print("10. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Length of string:", len(s))
        elif choice == 2:
            print("Reversed string:", s[::-1])
        elif choice == 3:
            print("Uppercase:", s.upper())
        elif choice == 4:
            print("Lowercase:", s.lower())
        elif choice == 5:
            vowels = "aeiouAEIOU"
            count = sum(1 for char in s if char in vowels)
            print("Count of vowels:", count)
        elif choice == 6:
            consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
            count = sum(1 for char in s if char in consonants)
            print("Count of consonants:", count)
        elif choice == 7:
            if s == s[::-1]:
                print("String is a palindrome.")
            else:
                print("String is not a palindrome.")
        elif choice == 8:
            vowels = "aeiouAEIOU"
            new_string = ''.join(['*' if char in vowels else char for char in s])
            print("String with vowels replaced:", new_string)
        elif choice == 9:
            print("String with whitespace removed:", s.strip())
        elif choice == 10:
            print("Exiting string operations...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")


def tuple_operations(t):
    while True:
        print("\nTuple Operations:")
        print("1. Length of tuple")
        print("2. Maximum element")
        print("3. Minimum element")
        print("4. Sum of elements")
        print("5. Tuple repetition")
        print("6. Concatenation")
        print("7. Index of element")
        print("8. Count occurrence of element")
        print("9. Tuple slicing")
        print("10. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Length of tuple:", len(t))
        elif choice == 2:
            print("Maximum element:", max(t))
        elif choice == 3:
            print("Minimum element:", min(t))
        elif choice == 4:
            print("Sum of elements:", sum(t))
        elif choice == 5:
            n = int(input("Enter repetition count: "))
            print("Tuple repetition:", t * n)
        elif choice == 6:
            t2 = eval(input("Enter another tuple: "))
            print("Concatenation of tuples:", t + t2)
        elif choice == 7:
            element = input("Enter element to find index: ")
            try:
                index = t.index(element)
                print("Index of", element, "is", index)
            except ValueError:
                print(element, "not found in tuple.")
        elif choice == 8:
            element = input("Enter element to count occurrence: ")
            count = t.count(element)
            print("Count of", element, "is", count)
        elif choice == 9:
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced tuple:", t[start:end])
        elif choice == 10:
            print("Exiting tuple operations...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")


def main():
    while True:
        print("\nMenu:")
        print("1. String Operations")
        print("2. Tuple Operations")
        print("3. Exit")

        option = int(input("Enter your choice: "))

        if option == 1:
            s = input("Enter a string: ")
            string_operations(s)
        elif option == 2:
            t = eval(input("Enter a tuple (e.g., (1, 2, 3)): "))
            tuple_operations(t)
        elif option == 3:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
