def possible_permutations(list_):
    if len(list_) <= 1:
        yield list_
    else:
        for i in range(len(list_)):
            for permutation in possible_permutations(list_[:i] + list_[i + 1:]):
                yield [list_[i]] + permutation