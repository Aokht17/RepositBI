import numpy as np
from Bio import SeqIO


def match(a, b, match_score, mismatch_score, gap):
    if a == b:
        return match_score
    elif a == '-' or b == '-':
        return gap
    else:
        return mismatch_score


def global_alignment(fast_file, match_score, mismatch_score, gap):
    """
        performs global alignment of 2 sequences by Needleman-Wunsch algorithm
        :param fast_file: the full path to your fasta file
        :return: total score and aligned strings
        """
    pi = list(SeqIO.parse(fast_file, 'fasta'))
    s1 = pi[0]
    s2 = pi[1]

    m, n = len(s1), len(s2)
    matrix = np.zeros((m + 1, n + 1))

    for i in range(m + 1):
        matrix[i][0] = gap * i
    for j in range(n + 1):
        matrix[0][j] = gap * j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            diag = matrix[i - 1][j - 1] + match(s1[i - 1], s2[j - 1], match_score, mismatch_score, gap)
            delete = matrix[i - 1][j] + gap
            insert = matrix[i][j - 1] + gap
            matrix[i][j] = max(diag, delete, insert)

    align1, align2 = '', ''
    i, j = m, n

    # Traceback
    while i > 0 and j > 0:
        score_current = matrix[i][j]
        score_diag = matrix[i - 1][j - 1]
        score_left = matrix[i][j - 1]
        score_up = matrix[i - 1][j]

        if score_current == score_diag + match(s1[i - 1], s2[j - 1], match_score, mismatch_score, gap):
            a1, a2 = s1[i - 1], s2[j - 1]
            i, j = i - 1, j - 1
        elif score_current == score_up + gap:
            a1, a2 = s1[i - 1], '-'
            i -= 1
        elif score_current == score_left + gap:
            a1, a2 = '-', s2[j - 1]
            j -= 1
        align1 += a1
        align2 += a2

    while i > 0:
        a1, a2 = s1[i - 1], '-'
        align1 += a1
        align2 += a2
        i -= 1

    while j > 0:
        a1, a2 = '-', s2[j - 1]
        align1 += a1
        align2 += a2
        j -= 1

    align1 = align1[::-1]
    align2 = align2[::-1]
    seqN = len(align1)
    sym = ''
    seq_score = 0
    for i in range(seqN):
        a1 = align1[i]
        a2 = align2[i]
        if a1 == a2:
            sym += a1
            seq_score += match(a1, a2, match_score, mismatch_score, gap)

        else:
            seq_score += match(a1, a2, match_score, mismatch_score, gap)
            sym += ' '

    return seq_score, align1, align2


print(global_alignment('my_fasta', 1, -1, -1))
