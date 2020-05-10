from Bio import SeqIO


def bestOverlap(read1, reads, k_mer):
    """
    returns the reads pair and maximum length of the overlapped pair in reads
    """
    read_a, read_b = None, None
    best_overlap = 0
    for read2 in reads:
        if read1 != read2:  # skip self comparison
            offset = maximum(read1, read2, k_mer)
            if offset > best_overlap:  # skip non-overlapped pairs
                best_overlap = offset
                read_a, read_b = read1, read2
    return [best_overlap, read_a, read_b]


def right_overlap(read1, read2, k_mer):
    """
    counts intersecting nucleotides on the right
    """
    start = 0
    while True:
        start = read1.find(read2[:k_mer], start)
        if start == -1:
            return 0
        elif read2.startswith(read1[start:]):
            return len(read1) - start
        start += 1


def left_overlap(read1, read2, k_mer):
    """
    counts intersecting nucleotides on the left
    """
    start_1 = 0
    while True:
        start_1 = read2.find(read1[:k_mer], start_1)
        if start_1 == -1:
            return 0
        elif read1.startswith(read2[start_1:]):
            return len(read2) - start_1
        start_1 += 1

def maximum(read1, read2, k_mer):
    """
    returns the maximum overlap of two reads
    """
    return max(right_overlap(read1, read2, k_mer), left_overlap(read1, read2, k_mer))


def concatenate(length, read1, read2, reads):
    """
    glues two reads, removes them from the list and adds concatenated
    """
    if read1.startswith(read2[(-length):]):
        reads.append(read2[:(-length)] + read1)
    elif read2.startswith(read1[(-length):]):
        reads.append(read1[:(-length)] + read2)
    reads.remove(read1)
    reads.remove(read2)



def assembly(file, overlap=2):
    """
    sum function for assembly. Writes output in fasta format
    file: your input (fasta)
    overlap: minimum expected overlap length. Default = 2
    """
    reads = [str(i.seq) for i in SeqIO.parse(file, 'fasta')]
    reads = set(reads)
    reads = list(reads)
    while len(reads) != 1:
        for i in reads:
            a = bestOverlap(i, reads, overlap)
            concatenate(int(a[0]), a[1], a[2], reads)

    with open('assembly_naive.fasta', 'w') as output:
        for i, x in enumerate(reads):
            output.write('>contig%d\n%s\n' % (i, x))

assembly('unknown.txt')