# CGSeq Final Project

This repository contains the code for the SGSeq final project, which includes few python scripts and a Java implementation of the NW algorithm.

## Structure

- `cgseq_final_project.ipynb`: Used as a playbook to experiment and collaborate (Google Colab).
- `Java/src/nwalgorithm`: Contains the Java implementation of the NW algorithm.
  - `Nw.java`: The main code for the NW algorithm.
  - `Main.java`: Demonstrates how to run the NW algorithm.
- Python Files:
    - `needleman_wunsh.py` - This is has the basic implementation of Needleman Wunsh Algorithm
    - `needleman_wunsh_threads_parallel.py` - Naive parallelization, Experimented with `concurrent.futures` module in Python provides a high-level interface for asynchronously executing functions using threads or processes. But due to dependency issues, the threads were stuck in deadlock, making it never ending.
    - `needleman_wunsh_striped_search.py` - Experimented with improving on naive parallelim, by splitting matix update to parallely run for row, columns and diagonals, still faced issues with thread executions
    - `needleman_wunsh_numba.py` - Finally switched to a more vectorized solution and using the same parallel splitting of matix to update for row, columns and diagonals

## Prerequisites

- Need Python3 installed, and path correctly set 
- Java Development Kit (JDK) to compile and run the Java code.

## Running Python Code

1. Navigate to the root directory of this project.
2. To install all the required libraries execute command `pip3 install -r requirements.txt`
3. Then run `python3 analyze.py` to run various versions of `needleman_wunsh.py` and compare the execution times.

**Note:** hg38Patch2.fa being a huge file we didn't commit on the github, and we ran the analysis on sythentically generated genomes, but `util.py` fetches any 2 closely related same length genomes, and we can cascade these to use with our analyse.py as well as an extra step.


## Compiling and Running the Java Code

### Compilation

1. Navigate to the `Java/src/nwalgorithm` directory.
2. Compile the Java files:
