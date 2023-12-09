import random
import time
import needleman_wunsh as nw
import needleman_wunsh_threads_parallel as nw_tp
import needleman_wunsh_striped_search as nw_striped
import needleman_wunsh_numba as nw_numba 


seq1 = ''.join(random.choice(['a','c','g','t']) for _ in range(10000))
seq2 = ''.join(random.choice(['a','c','g','t']) for _ in range(10000))
print("--------------------Analyzing Vanilla NW----------------------------")
s = time.time()
dp_matrix = nw.generate_dp_matrix(seq1, seq2)
t = time.time()
print("Time taken to construct NW DP matrix:",(t-s),"s")
# s = time.time()
# aligned_seq1, aligned_seq2 = nw.find_alignment(seq1, seq2, dp_matrix)
# t = time.time()
# print("Time taken to find best alignment:",(t-s)*1000,"ms")
print("Alignment score:",dp_matrix[len(seq1)-1][len(seq2)-1])

# print("--------------------Analyzing NW with parallel Threads----------------------")
# s = time.time()
# dp_matrix_tp = nw_tp.generate_dp_matrix(seq1, seq2)
# t = time.time()
# print("Time taken to construct NW DP matrix using thread pool:",(t-s),"s")
# print("Alignment score:",dp_matrix_tp[len(seq1)-1][len(seq2)-1])

# print("--------------------Analysing NW with Striped Search--------------------------")
# s = time.time()
# dp_matrix_striped = nw_striped.generate_dp_matrix_parallel(seq1, seq2)
# t = time.time()
# print("Time taken to construct NW DP matrix using striped search:",(t-s),"s")
# print("Alignment score:",dp_matrix_striped[len(seq1)-1][len(seq2)-1])

print("--------------------Analysing NW with Numba Striped--------------------------")
s = time.time()
dp_matrix_numba = nw_numba.generate_dp_matrix_parallel(seq1, seq2)
t = time.time()
print("Time taken to construct NW DP matrix using numba vectorization and striped search:",(t-s),"s")