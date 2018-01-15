def to_rna(dna_strand):
    translator = "".maketrans("GCTA", "CGAU")
    correct_values= ["G","C","T","A"]
    for char in dna_strand:
        if char not in correct_values:
            raise ValueError("Wrong input")

    return dna_strand.translate(translator)


