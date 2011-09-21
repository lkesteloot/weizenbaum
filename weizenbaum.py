#!/usr/bin/python

"""This solves a problem described by Dijkstra in EWD249, pages 83 and 84, due to
Joe Weizenbaum. See README.markdown for more information."""

def find_solution(n):
    # Map from sum of powers to (i,j) tuple.
    s_to_pair = {}

    # Best solution so far.
    min_s = None
    min_pairs = None

    # Cover the triangle below (and at) the 45-degree diagonal. The one above the
    # diagonal is "trivial" because it's just addition's commutativity.
    for i in range(200):
        # This optimization only halves the total running time.
        if min_s is not None and i**n > min_s:
            break

        for j in range(i + 1):
            s = i**n + j**n

            # If we had already found a pair, then we've found one with at least two.
            # Keep track of it if it's the best we've found so far (smallest s).
            if s in s_to_pair and (min_s is None or s < min_s):
                min_s = s
                min_pairs = [s_to_pair[s], (i, j)]
            else:
                # First time we see this sum.
                s_to_pair[s] = (i, j)


    if min_s is not None:
        print "n = %d, s = %d = %d^%d + %d^%d = %d^%d + %d^%d" % (
                n, min_s,
                min_pairs[0][0], n,
                min_pairs[0][1], n,
                min_pairs[1][0], n,
                min_pairs[1][1], n)
    else:
        print "Search space too small for n = %d" % n

def main():
    for n in range(1, 6):
        find_solution(n)

if __name__ == "__main__":
    main()
