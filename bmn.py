import sys, collections, argparse
from Bio import Seq, SeqIO
import logging


logging.basicConfig(filename='DBG_log.log', filemode='w', format='%(asctime)s: %(message)s',
                    datefmt='%H:%M:%S', level=logging.INFO)
logger = logging.getLogger(__name__)

def reverse_comp(km):
    """
    obviously, makes reverse complement
    km: given seq
    """
    return Seq.reverse_complement(km)


def kmers(seq, k):
    """
    makes all possible k-mers from the seq
    seq: given seq
    k: the length of k-mers
    """
    for i in range(len(seq) - k + 1):
        yield seq[i:i + k]


def forward_further(km):
    """
    yield all forward neighbors of the given k-mer, which can stand after
    km: given k-mer
    """
    for x in 'ACGT':
        yield km[1:] + x


def forward_before(km):
    """
    yield all forward neighbors of the given k-mer, which can stand before
    km: given k-mer
    """
    for x in 'ACGT':
        yield x + km[:-1]


def graph(fn, k, limit=3):
    """
    creates a dictionary that keeps track of all k-mers' and their reversed pairs coverage
    fn: fastq-file(s) in a list
    k: the length of k-mer
    limit: the threshold > that low coverage k-mers will be deleted, default=3
    """
    dict_of_kmer = collections.defaultdict(int)
    for f in fn:
        format = str(f).split('.')[-1]
        if format is 'fq' or format is 'fastq':  # rather primitive format recognition
            reads = SeqIO.parse(f, 'fastq')
        else:
            reads = SeqIO.parse(f, 'fasta')
        for read in reads:
            seq_l = str(read.seq).split('N')
            for seq in seq_l:
                for km in kmers(seq, k):
                    dict_of_kmer[km] += 1
                seq = reverse_comp(seq)
                for km in kmers(seq, k):
                    dict_of_kmer[km] += 1

    d1 = [x for x in dict_of_kmer if dict_of_kmer[x] <= limit] # filtering k-mers with low coverage
    for x in d1:
        del dict_of_kmer[x]
    logger.info('Filering k-mers with coverage lower than %s', limit)
    return dict_of_kmer


def contig_forward(d, km):
    """
    walks along the de Bruijn graph in the forward direction
    d: dictionary of k-mers and coverage from graph function
    """
    c_fw = [km]

    while True:
        if sum(x in d for x in forward_further(c_fw[-1])) != 1:
            break

        cand = [x for x in forward_further(c_fw[-1]) if x in d][0]
        if cand == km or cand == reverse_comp(km):
            break  # break out of cycles
        elif cand == reverse_comp(c_fw[-1]):
            break  # break out of hairpins

        elif sum(x in d for x in forward_before(cand)) != 1:
            break

        c_fw.append(cand)

    return c_fw


def get_contig(d, km):
    """
    finds the contig that the k-mer km belongs to
    d: dictionary of k-mers and coverage from graph function
    km: k-mer
    """
    c_fw = contig_forward(d, km)

    c_bw = contig_forward(d, reverse_comp(km))

    if km in forward_further(c_fw[-1]):
        c = c_fw
    else:
        c = [reverse_comp(x) for x in c_bw[-1:0:-1]] + c_fw
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
                done.add(reverse_comp(y))
            r.append(s)

    return r

def write_out(cs):
    """
    writes output fasta file
    """
    with open('assembly.fasta', 'w') as output:
        for i,x in enumerate(cs):
            output.write('>contig%d\n%s\n'%(i,x))
            logger.debug('%s contigs is done', i)

# to run from command line
#if __name__ == "__main__":
    #if len(sys.argv) < 2: exit("args: <k> <reads_1.fq> ...")
    #k = int(sys.argv[1])
    #d = graph(sys.argv[2:], k, 1)
    #cs = all_contigs(d)
    #write_out(cs)


# or in PyCharm, for example
def sum_assembly(k, *files):
    """
    aggregated function
    k - the length of k-mers used in assembly
    *files - your reads in fasta or fastq format
    """
    d = graph([i for i in files], int(k))
    logger.info('***We started assembly with kmer=%s***', k)
    cs = all_contigs(d)
    write_out(cs)
    logger.info('***Completed***')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--kmer', type=int, default=25, help='the length of k-mers used in assembly', required=False)
    parser.add_argument('--files', nargs='+', help='reads in fasta or fastq format', required=True)
    args = parser.parse_args()
    sum_assembly(args.kmer, args.files)

    #d = graph([i for i in args.files], args.k)
    #cs = all_contigs(d)
    #write_out(cs)