def q_a(fastq_file,new_fasta, min_numb=50):
    """
reads lines above the specified length from the fastq file and translates to fasta format
    :param fastq_file: file path
    :param new_fasta: file path
    :param min_numb: the min length of sequence (default=50)
    """
    from Bio import SeqIO
    seqs = []
    uuu = SeqIO.parse(fastq_file, 'fastq')
    for lines in uuu:
        if len(lines) >= min_numb:
            seqs.append(lines)
    SeqIO.write(seqs, new_fasta, 'fasta')


q_a('sample.fastq', 'my_fasta', 50)
