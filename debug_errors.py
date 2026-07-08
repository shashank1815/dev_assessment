def calculate_average(numbers):
    try:
        total = 0

        for i in range(len(numbers)):
            total += numbers[i]
        return total / len(numbers)
    except ZeroDivisionError:
        print("Error: Cannot calculate average of an empty list.")
        return None
def get_list_element(my_list, index):
    try:
        if not isinstance(my_list, list):
            raise TypeError
        return my_list[index]
    except IndexError:
        print("Error: Index is out of bounds.")
        return None
    except TypeError:
        print("Error: Input is not a list.")
        return None
    
# Example data
data1 = [10, 20, 30, 40, 50]
data2 = [5,15]
data3 = []
print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}")
print()

sample_list = [100,200,300]
print(get_list_element(sample_list, 1))
print(get_list_element(sample_list, 5))
print(get_list_element("Hello", 0))