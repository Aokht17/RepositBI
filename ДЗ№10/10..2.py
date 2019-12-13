def how_distributed(your_fasta):
    """
 creates a histogram and fit a kernel density estimate for distribution of lines' length in fasta file
    :param your_fasta: full path
    :return: none
    """
    import seaborn as sns
    from Bio import SeqIO
    u = list(SeqIO.parse(your_fasta, 'fasta'))
    app = []
    for line in u:
        app.append(len(line))
    sns.distplot(tuple(app))
    return
