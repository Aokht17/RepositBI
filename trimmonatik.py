import argparse
from Bio import SeqIO


parser = argparse.ArgumentParser()
parser.add_argument('--threshold', type=int, default=25, help='threshold quality that would not be cut', required=True)
parser.add_argument('--file', help='reads fastq format', required=True)
parser.add_argument('--out', type=str, required=True)
args = parser.parse_args()


def trimming(f, thresh, outfile):
    """
    trims the edges of the sequence with quality below the threshold
    """
    reads = SeqIO.parse(f, 'fastq')
    for read in reads:
        start = []
        for i in enumerate(read.seq):
            i = i[0]
            if read.letter_annotations["phred_quality"][i] >= thresh:
                start.append(i)
        try:
            sub_rec = read[min(start): max(start)+1]
            with open(outfile) as out:
                out.write(sub_rec.format("fastq"))
        except ValueError:
            pass


if __name__ == "__main__":
    print("***** trimming started *****")
    trimming(args.file, args.threshold, args.out)
    print("***** trimming completed *****")