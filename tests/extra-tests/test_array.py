import pytest


def find_max_value(arr):
    if not arr:
        return None  # Return None for an empty array
    max_value = arr[0]  # Initialize max_value with the first element

    # Loop through the array to find the maximum value
    for num in arr:
        if num > max_value:
            max_value = num

    return max_value


# Pytest test case for finding the maximum value in an array
def test_find_max_value():
    # Test with an array of positive numbers
    assert find_max_value([5, 10, 15, 20, 25]) == 25

    # Test with an array of negative numbers
    assert find_max_value([-1, -2, -3, -4, -5]) == -1

    # Test with an array of mixed positive and negative numbers
    assert find_max_value([10, -5, 15, -20, 25]) == 25

    # Test with an empty array
    assert find_max_value([]) is None

    # Test with a single-element array
    assert find_max_value([42]) == 42


if __name__ == "__main__":
    pytest.main()
