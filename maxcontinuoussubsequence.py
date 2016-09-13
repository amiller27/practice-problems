#!/usr/bin/env python

'''
Maximal Contiguous Subsequence
Question:
    Given a sequence of numbers, find the contiguous subsequence with the largest sum
'''

import itertools
import numpy as np

def mcs(s):
    s_prime = [s[0]]
    for i in s[1:]:
        if s_prime[-1] * i < 0:
            s_prime.append(i)
        else:
            s_prime[-1] += i

    if s_prime[0] < 0:
        s_prime = s_prime[1:]
    if s_prime[-1] < 0:
        s_prime = s_prime[:-1]

    take_left = [[i, s_prime[2*i]] for i in range((len(s_prime)+1)/2)]
    for i in range(1, (len(s_prime)+1)/2):
        if take_left[i-1][1] + s_prime[2*i - 1] > 0:
            take_left[i][0] = take_left[i-1][0]
            take_left[i][1] += take_left[i-1][1] + s_prime[2*i - 1]

    take_right = [[i, s_prime[2*i]] for i in range((len(s_prime)+1)/2)]
    for i in range(len(s_prime)/2-1, -1, -1):
        if take_right[i+1][1] + s_prime[2*i + 1] > 0:
            take_right[i][0] = take_right[i+1][0]
            take_right[i][1] += take_right[i+1][1] + s_prime[2*i + 1]

    results = [None for i in range((len(s_prime)+1)/2)]
    for i in range((len(s_prime)+1)/2):
        results[i] = [take_left[i][0], take_right[i][0], take_left[i][1]+take_right[i][1]-s_prime[2*i]]
    return max(r[2] for r in results)

def total(s, pair):
    return sum(s[pair[0]:pair[1]+1])

def slow_mcs(s):
    return max(total(s, pair) for pair in itertools.combinations(range(len(s)), 2))

if __name__ == '__main__':
    std = 500
    size = 1000
    while True:
        test = list(np.random.normal(0, std, size))
        res = [mcs(test), slow_mcs(test)]
        if abs(res[0] - res[1])/res[1] > 1e-10:
            print test, res
