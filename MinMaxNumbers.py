def find_largest_smallest(numbers):
    if not numbers:
        return None, None
    return max(numbers), min(numbers)

# Test the function
num_list = [10, 5, 20, 15, 8]
largest, smallest = find_largest_smallest(num_list)
print(f"The largest element is {largest} and the smallest element is {smallest}")
