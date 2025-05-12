"""
Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
"""
import math

def count_binary_seq(n):
    if n == 1:
        return 2
    else:
        return 2 * count_binary_seq(n-1)

def count_binary_seq_helper(n, count, current_sum, target_sum):
    if n == 0:
        if current_sum == target_sum:
            count += 1
        return count
    else:
        count = count_binary_seq_helper(n-1, count, current_sum, target_sum)
        current_sum += 1
        if current_sum == target_sum:
            count += 1
        return count

def count_binary_seq_helper_optimized(n, count, current_sum, target_sum):
    if n == 0:
        if current_sum == target_sum:
            count += 1
        return count
    else:
        count = count_binary_seq_helper_optimized(n-1, count, current_sum, target_sum)
        current_sum += 1
        if current_sum == target_sum:
            count += 1
        return count

def count_binary_seq_optimized(n):
    if n == 1:
        return 2
    else:
        return count_binary_seq_helper_optimized(n-1, 0, 0, 0)

def count_binary_seq_optimized_helper(n, count, current_sum, target_sum):
    if n == 0:
        if current_sum == target_sum:
            count += 1
        return count
    else:
        count = count_binary_seq_optimized_helper(n-1, count, current_sum, target_sum)
        current_sum += 1
        if current_sum == target_sum:
            count += 1
        return count

def count_binary_seq_optimized_helper_optimized(n, count, current_sum, target_sum):
    if n == 0:
        if current_sum == target_sum:
            count += 1
        return count
    else:
        count = count_binary_seq_optimized_helper_optimized(n-1, count, current_sum, target_sum)
        current_sum += 1
        if current_sum == target_sum:
            count += 1
        return count

def count_binary_seq_optimized_optimized(n):
    if n == 1:
        return 2
    else:
        return count_binary_seq_optimized_helper_optimized(n-1, 0, 0, 0)

def count_binary_seq_optimized_optimized_helper(n, count, current_sum, target_sum):
    if n == 0:
        if current_sum == target_sum:
            count += 1
        return count
    else:
        count = count_binary_seq_optimized_optimized_helper(n-1, count, current_sum, target_sum)
        current_sum += 1
        if current_sum == target_sum:
            count += 1
        return count

def count_binary_seq_optimized_optimized_helper_optimized(n, count, current_sum, target_sum):
    if n == 0:
        if current_sum == target_sum:
            count += 1
        return count
    else:
        count = count_binary_seq_optimized_optimized_helper_optimized(n-1, count, current_sum, target_sum)
        current_sum += 1
        if current_sum == target_sum:
            count += 1
        return count

def count_binary_seq_optimized_optimized_optimized(n):
    if n == 1:
        return 2
    else:
        return count_binary_seq_optimized_optimized_helper_optimized(n-1, 0, 0, 0)

def count_binary_seq_optimized_optimized_optimized_helper(n, count, current_sum, target_sum):
    if n == 0:
        if current_sum == target_sum:
            count += 1
        return count
    else:
        count = count_binary_seq_optimized_optimized_optimized_helper(n-1, count, current_sum, target_sum)
        current_sum += 1
        if current_sum == target_sum: