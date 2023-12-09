import numpy as np
from numba import cuda, njit, prange

@njit(parallel=True)
def calculate_vertical_row(dp_matrix, seq1, seq2, match, mismatch, gap_penalty):
    rows, cols = dp_matrix.shape

    for i in prange(1, rows):
        for j in range(1, cols):
            delete_score = dp_matrix[i - 1, j] + gap_penalty
            dp_matrix[i, j] = max(dp_matrix[i,j], delete_score)

@njit(parallel=True)
def calculate_horizontal_row(dp_matrix, seq1, seq2, match, mismatch, gap_penalty):
    rows, cols = dp_matrix.shape

    for j in prange(1, cols):
        for i in range(1, rows):
            insert_score = dp_matrix[i, j - 1] + gap_penalty
            dp_matrix[i, j] = max(dp_matrix[i,j], insert_score)

@njit(parallel=True)
def calculate_diagonal(dp_matrix, seq1, seq2, match, mismatch, gap_penalty):
    rows, cols = dp_matrix.shape

    for line in prange(1, rows + cols):
        start_col = max(0, line - rows)
        count = min(line, (cols - start_col), rows)

        for j in range(0, count):
            i = min(rows, line) - j - 1

            match_score = dp_matrix[i - 1, start_col + j - 1] + (match if seq1[i - 1] == seq2[start_col + j - 1] else mismatch)
            dp_matrix[i, start_col + j] = max(match_score, dp_matrix[i, start_col + j])


def generate_dp_matrix_parallel(seq1, seq2):
    match, mismatch, gap_penalty = 1, -1, -1
    rows, cols = len(seq1) + 1, len(seq2) + 1
    dp_matrix = np.zeros((rows, cols), dtype=np.int32)

    # Initialize the first column
    dp_matrix[1:, 0] = np.arange(1, rows) * gap_penalty
    # Initialize the first row
    dp_matrix[0, 1:] = np.arange(1, cols) * gap_penalty

    # Compute vertical rows in parallel
    calculate_vertical_row(dp_matrix, seq1, seq2, match, mismatch, gap_penalty)

    # Compute horizontal rows in parallel
    calculate_horizontal_row(dp_matrix, seq1, seq2, match, mismatch, gap_penalty)

    # Compute diagonals in parallel
    calculate_diagonal(dp_matrix, seq1, seq2, match, mismatch, gap_penalty)

    return dp_matrix
