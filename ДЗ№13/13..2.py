from Bio.Seq import Seq
from Bio.Alphabet import generic_rna
from Bio.Alphabet import RNAAlphabet


class Rna:
    molecular_type = 'nucleic acids'

    def __init__(self,sequence, func_type, sense):
        self.sequence = sequence
        self.func_type = func_type
        self.sense = True

    def into_protein(self):
        """
        returns an encoded protein sequence
        """
        if self.func_type is 'messenger' and self.sense is True:
            return Seq(self.sequence,generic_rna).translate(table='Standard')
        else:
            print('encodes no amino acids')

    def reverse_transcription(self):
        """
        returns the reverse transcript of a given RNA
        """
        return Seq(self.sequence, RNAAlphabet()).back_transcribe().reverse_complement()

    def orf(self):
        """
        returns the index of the first nucleotide in ORF in RNA (-1 if None)
        """
        return self.sequence.find('AUG')


my_seq = Rna('AUCAUGGGGAACUGA', 'messenger', True)
print(my_seq.reverse_transcription())
print(my_seq.into_protein())
print(my_seq.orf())