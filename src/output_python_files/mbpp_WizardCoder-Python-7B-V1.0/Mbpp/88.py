"""
Write a function to get the frequency of all the elements in a list, returned as a dictionary.
assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})
"""
def freq_count(lst):
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

print(freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]))