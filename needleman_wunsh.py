def scores():
    match = 1
    mismatch = -1
    gap_penalty = -1
    return match, mismatch, gap_penalty

def generate_dp_matrix(seq1, seq2):
    match, mismatch, gap_penalty = scores()
    rows = len(seq1) + 1
    cols = len(seq2) + 1
    dp_matrix = [[0] * cols for _ in range(rows)]

    for i in range(1, rows):
        dp_matrix[i][0] = i * gap_penalty
    for j in range(1, cols):
        dp_matrix[0][j] = j * gap_penalty

    for i in range(1, rows):
        for j in range(1, cols):
            match_score = dp_matrix[i - 1][j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch)
            delete_score = dp_matrix[i - 1][j] + gap_penalty
            insert_score = dp_matrix[i][j - 1] + gap_penalty
            dp_matrix[i][j] = max(match_score, delete_score, insert_score)

    return dp_matrix

def find_alignment(seq1, seq2, score_matrix):
    match, mismatch, gap_penalty = scores()
    rows = len(seq1) + 1
    cols = len(seq2) + 1
    alignment1 = []
    alignment2 = []
    i, j = rows - 1, cols - 1
    while i > 0 or j > 0:
        current_score = score_matrix[i][j]
        diagonal_score = score_matrix[i - 1][j - 1] if i > 0 and j > 0 else float('-inf')
        up_score = score_matrix[i - 1][j] if i > 0 else float('-inf')
        left_score = score_matrix[i][j - 1] if j > 0 else float('-inf')

        if i > 0 and j > 0 and current_score == diagonal_score + (match if seq1[i - 1] == seq2[j - 1] else mismatch):
            alignment1.insert(0, seq1[i - 1])
            alignment2.insert(0, seq2[j - 1])
            i -= 1
            j -= 1
        elif i > 0 and current_score == up_score + gap_penalty:
            alignment1.insert(0, seq1[i - 1])
            alignment2.insert(0, '-')
            i -= 1
        elif j > 0:
            alignment1.insert(0, '-')
            alignment2.insert(0, seq2[j - 1])
            j -= 1

    aligned_seq1 = ''.join(alignment1)
    aligned_seq2 = ''.join(alignment2)

    return aligned_seq1, aligned_seq2
