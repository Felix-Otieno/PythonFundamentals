def guess_birthday():
    print("Think of your birthday (Day of the month only). I will try to guess it.")
    
    # Series of questions to guess the birthday
    set1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
    set2 = [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31]
    set3 = [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31]
    set4 = [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31]
    set5 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    
    birthday = 0
    
    # Asking the user if their birthday is in each set
    answer = input(f"Is your birthday in this set? {set1} (yes/no): ").lower()
    if answer == "yes":
        birthday += 1

    answer = input(f"Is your birthday in this set? {set2} (yes/no): ").lower()
    if answer == "yes":
        birthday += 2

    answer = input(f"Is your birthday in this set? {set3} (yes/no): ").lower()
    if answer == "yes":
        birthday += 4

    answer = input(f"Is your birthday in this set? {set4} (yes/no): ").lower()
    if answer == "yes":
        birthday += 8

    answer = input(f"Is your birthday in this set? {set5} (yes/no): ").lower()
    if answer == "yes":
        birthday += 16
    
    print(f"Your birthday is on the {birthday}th!")
    
# Run the program
guess_birthday()
