"""
Write a function to find the specified number of largest products from two given lists, selecting one factor from each list.
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
"""

def large_product(list1, list2, n):
    """
    This function takes two lists and an integer n as input and returns a list of the n largest products of two factors from the two lists.
    """
    # Sort the two lists in descending order
    list1.sort(reverse=True)
    list2.sort(reverse=True)

    # Initialize an empty list to store the n largest products
    largest_products = []

    # Iterate through the two lists and find the n largest products
    for i in range(len(list1)):
        for j in range(len(list2)):
            # Calculate the product of the two factors
            product = list1[i] * list2[j]

            # Check if the product is already in the list
            if product not in largest_products:
                # If it's not, add it to the list
                largest_products.append(product)

                # If the list has reached the desired length, break out of the inner loop
                if len(largest_products) == n:
                    break

    return largest_products

# Test the function with the given example
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]<|endoftext|>