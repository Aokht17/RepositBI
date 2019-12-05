def global_alignment(fast_file, match_score, mismatch_score, gap):
    """
    performs global alignment of 2 sequences by Needleman-Wunsch algorithm
    :param fast_file: the full path to your fasta file
    :return: total score and aligned strings in a tuple
    """
    from Bio import SeqIO
    pi = list(SeqIO.parse(fast_file, 'fasta'))
    Q = pi[0]
    R = pi[1]
    dp = [[0 for x in range(len(Q) + 1)] for y in range(len(R) + 1)]  # nested list
    direction = [['$' for x in range(len(Q) + 1)] for y in range(len(R) + 1)]

    for i in range(len(R) + 1):
        dp[i][0] = gap * i
        direction[i][0] = 'up'

    for j in range(len(Q) + 1):
        dp[0][j] = gap * j
        direction[0][j] = 'left'

    direction_map = {0: 'diagonal', 1: 'up', 2: 'left'}

    for i in range(1, len(R) + 1):
        for j in range(1, len(Q) + 1):
            if R[i - 1] == Q[j - 1]:
                no_gap = dp[i - 1][j - 1] + match_score
            else:
                no_gap = dp[i - 1][j - 1] + mismatch_score

            gap_in_query = dp[i - 1][j] + gap
            gap_in_ref = dp[i][j - 1] + gap

            max_score = max([no_gap, gap_in_query, gap_in_ref])
            max_score_index = [no_gap, gap_in_query, gap_in_ref].index(max_score)
            dp[i][j] = max_score
            direction[i][j] = direction_map[max_score_index]

    i = len(R)  # обратный путь
    j = len(Q)

    ref_with_gaps = ''
    query_with_gaps = ''

    while i != 0 or j != 0:
        if direction[i][j] == 'diagonal':
            query_with_gaps = Q[j - 1] + query_with_gaps
            ref_with_gaps = R[i - 1] + ref_with_gaps
            i = i - 1
            j = j - 1
        elif direction[i][j] == 'left':
            ref_with_gaps = '_' + ref_with_gaps
            query_with_gaps = Q[j - 1] + query_with_gaps
            j = j - 1
        elif direction[i][j] == 'up':
            query_with_gaps = '_' + query_with_gaps
            ref_with_gaps = R[i - 1] + ref_with_gaps
            i = i - 1

    return tuple([dp[len(R)][len(Q)], query_with_gaps, ref_with_gaps])


print(global_alignment('my_fasta', -3, 5, -3))
