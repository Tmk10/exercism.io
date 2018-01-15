def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        differences = len([a for a in zip(strand_a, strand_b) if a[0] != a[1]])
        return differences
    else:
        raise ValueError(" Strands have different length")
