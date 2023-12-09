from concurrent.futures import ThreadPoolExecutor

def scores():
    match = 1
    mismatch = -1
    gap_penalty = -1
    return match, mismatch, gap_penalty

def calculate_vertical_row(i, seq1, seq2, match, mismatch, gap_penalty, dp_matrix):
    for j in range(1, len(seq2)):
        delete_score = dp_matrix[i - 1][j] + gap_penalty
        dp_matrix[i][j] = max(dp_matrix[i][j], delete_score)

def calculate_horizontal_row(j, seq1, seq2, match, mismatch, gap_penalty, dp_matrix):
    for i in range(1, len(seq1)):
        insert_score = dp_matrix[i][j - 1] + gap_penalty
        dp_matrix[i][j] = max(dp_matrix[i][j], insert_score)

def calculate_diagonal(start, end, seq1, seq2, match, mismatch, gap_penalty, dp_matrix):
    rows = len(seq2)
    cols = len(seq1)

    for line in range(1, rows + cols):
        start_col = max(0, line - rows)
        count = min(line, (cols - start_col), rows)

        for j in range(0, count):
            i = min(rows, line) - j - 1

            match_score = dp_matrix[i - 1][start_col + j - 1] + (match if seq1[i - 1] == seq2[start_col + j - 1] else mismatch)
            dp_matrix[i][start_col + j] = max(match_score, dp_matrix[i][start_col + j])

def generate_dp_matrix_parallel(seq1, seq2):
    match, mismatch, gap_penalty = scores()
    rows = len(seq1)
    cols = len(seq2)
    dp_matrix = [[0] * cols for _ in range(rows)]

    with ThreadPoolExecutor() as executor:
        futures = []

        for i in range(1, rows):
            dp_matrix[i][0] = i * gap_penalty
        for j in range(1, cols):
            dp_matrix[0][j] = j * gap_penalty

        # Compute vertical rows in parallel
        for i in range(1,rows):
            futures.append(executor.submit(calculate_vertical_row, i, seq1, seq2, match, mismatch, gap_penalty, dp_matrix))

        # Compute horizontal rows in parallel
        for j in range(1, cols):
            futures.append(executor.submit(calculate_horizontal_row, j, seq1, seq2, match, mismatch, gap_penalty, dp_matrix))

        # Compute diagonals in parallel
        num_diagonals = rows + cols - 2
        chunk_size = num_diagonals // executor._max_workers + 1
        for i in range(0, num_diagonals, chunk_size):
            end = min(i + chunk_size, num_diagonals)
            futures.append(executor.submit(calculate_diagonal, i, end, seq1, seq2, match, mismatch, gap_penalty, dp_matrix))

        # Wait for all tasks to complete
        for future in futures:
            future.result()

    return dp_matrix

