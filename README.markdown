Weizenbaum
==========

Copyright 2011 Lawrence Kesteloot.

This solves a problem described by Dijkstra in EWD249, pages 83 and 84, due to
Joe Weizenbaum:

> Make a program that, for given positive integer _n_, determines the smallest number
> _s_ that can be decomposed into the sum of two n-th powers in at least two non-trivially
> different ways.

He doesn't say so, but the base of the powers can't be negative (or the search space
would be too large?).

He describes a fast algorithm based on some table lookup that I don't understand.
The brute-force method below takes 44 ms in Python on a laptop. Ours makes use
of a hash table, which perhaps he didn't want to use (in 1969).

The i^n + j^n = s equation describes a super circle at the origin. We search the
arc between 0 and 45 degrees (inclusive) for integer coordinates. We do the search
backwards, first looking for integer coordinates and keeping track of the radius^n
value, which we call s.

