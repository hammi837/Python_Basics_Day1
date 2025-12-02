# Solve 5 beginner problems from LeetCode

# qno1: Median of Two Sorted lists
def findmedian(list1: list[int], list2: list[int]) -> float:
    combined = list1 + list2
    combined.sort()
    n = len(combined)
    mid = n // 2
    if n % 2 == 0:
        return (combined[mid - 1] + combined[mid]) / 2
    else:
        return combined[mid]
    
print("median of two sorted list is:",findmedian([1,3,3,4,5,6],[2,3,4]))

# qno2: Longest Substring Without Repeating Characters
def length_of_longest_substring(s: str) -> int:
    char_index = []
    max_length =0
    for char in s:
        if char not in char_index:
            char_index.append(char)
            max_length +=1
    return max_length
print("length of longest substring without repeating characters is:",length_of_longest_substring("abcabcbbd"))



#qno3: Palindrome Number


def find_palindrome(list1:list[int])->None:

     print(list1)
     list2=list1.copy()
     list2.reverse()
     if list1==list2 :
        print("palidrome")
     else:
       print("not palidrome")

find_palindrome([1,2,3,2,1])   

#qno4: Remove Duplicates from Sorted Array

def rem_dublicates(arr):
    seen=set()
    sum=0
    dublicate=set()
    for num in arr:
        if num in seen:
            dublicate.add(num)
            sum+=1
        else:
            seen.add(num)
    print("how many double value in list",sum)
    print("dublicate values are:",dublicate)
    return list(seen)


arr=[1,2,3,4,5,6,7,8,4,3,6,8]
print("values without dublicate",rem_dublicates(arr))


#qno5: find second largest number in list

def secondmax(arr):
    unique=list(set(arr))
    if len(unique)<2:
        return None
    unique.sort(reverse=True)
    return unique[1]
arr=[1,2,3,4,5,6,7,6,54,5,4,5]
print(secondmax(arr))
 








