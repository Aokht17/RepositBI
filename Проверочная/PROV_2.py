from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
def complementary_line(stringo):
    """
helper function to search for orf in a complementary chain
    :param stringo: str
    :return: list
    """
    string = ''.join(reversed(stringo.upper()))
    start = [i for i in range(len(string)) if string.startswith('TAC', i)]
    result = []
    for a in start:
        output = str()
        for indx in range(a, len(string), 3):
            current_codon = string[indx:indx + 3]
            if current_codon not in ["ATT", "ACT", "ATC"]:
                output += current_codon
            else:
                output += current_codon
                break
        if len(output) >= 12:
            dna = Seq(output, generic_dna)
            result.append(dna.complement())
    return (result)

# код слегка не доработан, так что выплевывает обертку от complement биопитона для комплементарной цепи

def gene_search(stringo):
    """
    the main function, searches for the orf and writes them from start to stop codon for both chains
    :param stringo: str
    :return: list of str
    """
    string = stringo.upper()
    start = [i for i in range(len(string)) if string.startswith('ATG', i)]
    result = []
    for a in start:
        output = str()
        for indx in range(a, len(string), 3):
            current_codon = string[indx:indx + 3]
            if current_codon not in ["TAA", "TAG", "TGA"]:
                output += current_codon
            else:
                output += current_codon
                break
        if len(output) >= 12:
            result.append(output)
    result.append(complementary_line(string))
    return (result)



print(gene_search('ATGaaatcaATGgggccctttTAAcgtTTAcccgggtttCATaaaCTAaaacccgggtttCAT'))
