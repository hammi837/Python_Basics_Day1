


def remove_duplicates(items: list[int]) -> list[int]:
    unique_list: list[int] = []

    for item in items:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list





def feq_counter(s: str) -> dict[str:int]:
    word=s.split()
    freq: dict[str:int]={}
    for char in word:
        if char in freq:
            freq[char]+=21
        else:
            freq[char]=1
    return freq





print("\n====== MAIN MENU ======")
print("Enter 1 for word-frequency counter")
print("Enter 2 for list duplicate remover")
print("Enter 3 for  Exit the program")
while True:
        option = input("Choose an option: ")
        if option == "1":
            print("frequency of each word:",feq_counter(input("enter your string:")))
        elif option == "2":
            n = int(input("How many numbers? "))
            nums = []
            for i in range(n):
               num = int(input(f"Enter number {i+1}: "))
               nums.append(num)
            print(nums)
            print("list after removing dublicate:",remove_duplicates(nums))
        elif option == "3":
            print("Exiting program!")
            break
        else:
            print("Invalid choice. Please try again.")





