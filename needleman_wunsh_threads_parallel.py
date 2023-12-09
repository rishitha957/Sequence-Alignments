from concurrent.futures import ThreadPoolExecutor

def scores():
    match = 1
    mismatch = -1
    gap_penalty = -1
    return match, mismatch, gap_penalty

def calculate_score(i, j, seq1, seq2, match, mismatch, gap_penalty, dp_matrix):
    match_score = dp_matrix[i - 1][j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch)
    delete_score = dp_matrix[i - 1][j] + gap_penalty
    insert_score = dp_matrix[i][j - 1] + gap_penalty
    return max(match_score, delete_score, insert_score)

def generate_dp_matrix(seq1, seq2):
    match, mismatch, gap_penalty = scores()
    rows = len(seq1) + 1
    cols = len(seq2) + 1
    dp_matrix = [[0] * cols for _ in range(rows)]

    with ThreadPoolExecutor() as executor:
        futures = []
        for i in range(1, rows):
            for j in range(1, cols):
                futures.append(executor.submit(calculate_score, i, j, seq1, seq2, match, mismatch, gap_penalty, dp_matrix))
        
        for i, future in enumerate(futures):
            row = i // (cols - 1) + 1
            col = i % (cols - 1) + 1
            dp_matrix[row][col] = future.result()

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