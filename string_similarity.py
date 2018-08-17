# -*- coding: utf-8 -*-


def hamming(string1, string2):
    """
    Hamming distance
    https://en.wikipedia.org/wiki/Hamming_distance
    """
    if len(string1) == len(string2):
        return sum(0 if c1 == c2 else 1 for c1, c2 in zip(string1, string2))


def jaccard(string1, string2):
    """
    Jaccard index
    https://en.wikipedia.org/wiki/Jaccard_index
    """
    set1 = set(string1)
    set2 = set(string2)
    return len(set1.intersection(set2))/len(set1.union(set2))


def overlap(string1, string2):
    """
    Overlap coefficient
    https://en.wikipedia.org/wiki/Overlap_coefficient
    """
    set1 = set(string1)
    set2 = set(string2)
    return len(set1.intersection(set2))/min(len(set1), len(set2))


def levenshtein(string1, string2):
    """
    Levenshtein distance
    https://en.wikipedia.org/wiki/Levenshtein_distance
    """
    # This one is hard... probably will be done in
    # Clojure as it's 4clojure's 101st problem.
    pass
