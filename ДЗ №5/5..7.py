print('AGCT'.translate(str.maketrans('AGCT', 'TCGA')))

dna = str(input('vvedite').upper().strip())
complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'U': 'A'}
for s in dna[::-1]:
    print(complement.get(s, '-'), end='')

