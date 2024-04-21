"""
Write a function to get the frequency of all the elements in a list, returned as a dictionary.
assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})
"""
def freq_count(lst):
    freq_dict = {}
    for i in lst:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    return freq_dict

# Testing the function
assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})
print("Test passed!")</s>