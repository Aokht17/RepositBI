import collections, sys
from Bio import Seq, SeqIO


def an_str(km):
    """
    obviously, makes reverse complement
    """
    return Seq.reverse_complement(km)


def kmers(seq, k):
    """
    makes all possible k-mers from the seq
    """
    for i in range(len(seq) - k + 1):
        yield seq[i:i + k]


def fw(km):
    """
    yield all forward neighbors of the given k-mer, which can stand after
    """
    for x in 'ACGT':
        yield km[1:] + x


def bw(km):
    """
    yield all forward neighbors of the given k-mer, which can stand before
    """
    for x in 'ACGT':
        yield x + km[:-1]


def graph(fn, k, limit=1):
    """
    creates a dictionary that keeps track of all k-mers' and their reversed pairs coverage
    fn: fastq-file(s) in a list
    k: the length of k-mer
    limit: the threshold <= that low coverage k-mers will be deleted, default=1
    """
    d = collections.defaultdict(int)
    for f in fn:
        reads = SeqIO.parse(f, 'fastq')
        for read in reads:
            seq_l = str(read.seq).split('N')
            for seq in seq_l:
                for km in kmers(seq, k):
                    d[km] += 1
                seq = an_str(seq)
                for km in kmers(seq, k):
                    d[km] += 1

    d1 = [x for x in d if d[x] <= limit]
    for x in d1:
        del d[x]

    return d


def contig_forward(d, km):
    """
    walks along the de Bruijn graph in the forward direction
    """
    c_fw = [km]

    while True:
        if sum(x in d for x in fw(c_fw[-1])) != 1:
            break

        cand = [x for x in fw(c_fw[-1]) if x in d][0]
        if cand == km or cand == an_str(km):
            break  # break out of cycles
        if cand == an_str(c_fw[-1]):
            break  # break out of hairpins

        if sum(x in d for x in bw(cand)) != 1:
            break

        c_fw.append(cand)

    return c_fw


def get_contig(d, km):
    """
    finds the contig that the k-mer km belongs to
    """
    c_fw = contig_forward(d, km)

    c_bw = contig_forward(d, an_str(km))

    if km in fw(c_fw[-1]):
        c = c_fw
    else:
        c = [an_str(x) for x in c_bw[-1:0:-1]] + c_fw
    return c[0] + ''.join(x[-1] for x in c[1:]), c


def all_contigs(d):
    """
    add all the k-mers in that contig to the done set
    """
    done = set()
    r = []
    for x in d:
        if x not in done:
            s, c = get_contig(d, x)
            for y in c:
                done.add(y)
                done.add(an_str(y))
            r.append(s)

    return r

def write_out(cs):
    """
    writes output fasta file
    """
    with open ('assembly.fasta', 'w') as output:
        for i,x in enumerate(cs):
            output.write('>contig%d\n%s\n'%(i,x))


# to run from command line
if __name__ == "__main__":
    if len(sys.argv) < 2: exit("args: <k> <reads_1.fq> ...")
    k = int(sys.argv[1])
    d = graph(sys.argv[2:], k, 1)
    cs = all_contigs(d)
    write_out(cs)


# or in PyCharm, for example
def sum_assembly(k, *files):
    """
    aggregated function
    k - the length of k-mers used in assembly
    *files - your reads in fastq format
    """
    d = graph([i for i in files], int(k), 1)
    cs = all_contigs(d)
    write_out(cs)