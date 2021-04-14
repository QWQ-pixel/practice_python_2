import collections


def f():
    s = input()
    results = collections.Counter(s.lower())
    print(max(results.values()))


f()
