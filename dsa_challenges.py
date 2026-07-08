def filter_and_sort_even(numbers):
    """
    Returns a new list containing only the even numbers sorted in ascending order.
    """
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
    even_numbers.sort()
    return even_numbers

def count_character_frequency(text):
    """
    Returns a dictionary with the lowercase characters and their frequencies.
    """
    frequency = {}
    for char in text.lower():
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

#Example calls
numbers = [3,1,4,7,1,5,9,2,6,8]
print("Sorted even numbers:", filter_and_sort_even(numbers))

text = "This is my task for Basic Data Structures & Algorithms"
print("Character frequencies:", count_character_frequency(text))