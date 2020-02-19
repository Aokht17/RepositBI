from Bio.Seq import Seq
from Bio.Alphabet import generic_dna


def personal_ribosome(fasta_way, codon='Standard'):
    """
    a generator for line-by-line translation of fasta files into protein sequences
    :param fasta_way: file path
    :param codon: codon table, 'Standard' by default
    """
    with open(fasta_way) as file:
        for stroka in file:
            if not stroka.startswith('>'):
                row = Seq(stroka, generic_dna)
                yield row.translate(table=codon)



for i in personal_ribosome('my_fasta'):
    print(i)

