def get_subsets(lst):
    if not lst:
        return [[]]
    subsets = get_subsets(lst[1:])
    return subsets + [[lst[0]] + s for s in subsets]

print(get_subsets(['A', 'B', 'C']))
