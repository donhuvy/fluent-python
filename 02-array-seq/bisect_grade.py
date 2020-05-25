'''
Ref: https://docs.python.org/3/library/bisect.html
'''

import bisect

def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    # bisect.biset_left would be the wrong one to use here :)
    i = bisect.bisect(breakpoints, score)
    return grades[i]

if __name__ == "__main__":
    scores = [33, 99, 77, 70, 89, 90, 100]
    for score in scores:
        print(f"{score} -> {grade(score)}")
