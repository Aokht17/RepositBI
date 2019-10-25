print('AGCT'.translate(str.maketrans('AGCT', 'TCGA')))

dna = str(input('vvedite').upper().strip())
dna.split()
complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'U': 'A'}
for s in dna:
    print(complement.get(s, '-'), end='')

