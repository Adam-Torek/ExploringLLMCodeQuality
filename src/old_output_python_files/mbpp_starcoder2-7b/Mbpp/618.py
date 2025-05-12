"""
Write a function to divide two lists element wise.
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
"""
def div_list(a,b):
    return [float(a[i])/b[i] for i in range(len(a))]

"""
Write a function to calculate the mean of a list.
assert mean_list([1,2,3,4,5])==3.0
"""
def mean_list(a):
    return sum(a)/len(a)

"""
Write a function to calculate the median of a list.
assert median_list([1,2,3,4,5])==3.0
assert median_list([1,2,3,4,5,6])==3.5
"""
def median_list(a):
    a.sort()
    if len(a)%2==0:
        return (a[len(a)/2]+a[len(a)/2-1])/2.0
    else:
        return a[len(a)/2]

"""
Write a function to calculate the mode of a list.
assert mode_list([1,2,3,4,5])==1
assert mode_list([1,2,3,4,5,5])==5
"""
def mode_list(a):
    b=list(set(a))
    c=[a.count(i) for i in b]
    return b[c.index(max(c))]

"""
Write a function to calculate the standard deviation of a list.
assert stdev_list([1,2,3,4,5])==1.5811388300841898
"""
def stdev_list(a):
    mean=mean_list(a)
    return (sum([(i-mean)**2 for i in a])/len(a))**0.5

"""
Write a function to calculate the variance of a list.
assert variance_list([1,2,3,4,5])==2.0
"""
def variance_list(a):
    return stdev_list(a)**2

"""
Write a function to calculate the range of a list.
assert range_list([1,2,3,4,5])==4
"""
def range_list(a):
    return max(a)-min(a)

"""
Write a function to calculate the interquartile range of a list.
assert iqr_list([1,2,3,4,5])==1.0
assert iqr_list([1,2,3,4,5,6])==2.0
"""
def iqr_list(a):
    a.sort()
    if len(a)%2==0:
        return median_list(a[len(a)/2:])-median_list(a[:len(a)/2])
    else:
        return median_list(a[len(a)/2+1:])-median_list(a[:len(a)/2])

"""
Write a function to calculate the skewness of a list.
assert skewness_list([1,2,3,4,5])==0.0
assert skewness_list([1,2,3,4,5,6])==0.5773502691896257
"""
def skewness_list(a):
    mean=mean_list(a)
    stdev=stdev_list(a)
    return sum([(i-mean)/stdev**3 for i in a])/len(a)

"""
Write a function to calculate the kurtosis of a list.
assert kurtosis_list([1,2,3,4,5])==-1.2
assert kurtosis_list([1,2,3,4,5,6])==-0.6
"""
def kurtosis_list(a):
    mean=mean_list(a)
    stdev=stdev_list(a)
    return sum([(i-mean)/stdev**4 for i in a])/len(a)

"""
Write a function to calculate the z-score of each value in a list.
assert zscore_list([1,2,3,4,5])==[-1.4638501161659793, -0.8783100653643068