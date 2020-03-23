from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Alphabet import generic_dna


def personal_ribosome(fasta_way, codon='Standard'):
    """
    a generator for line-by-line translation of fasta files into protein sequences
    :param fasta_way: file path
    :param codon: codon table, 'Standard' by default
    """
    with open(fasta_way) as file:
        sequences = [str(record.seq) for record in SeqIO.parse(file, 'fasta')]
        for stroka in sequences:
            row = Seq(stroka, generic_dna)
            yield row.translate(table=codon)
        



for i in personal_ribosome('my_fasta'):
    print(i)

