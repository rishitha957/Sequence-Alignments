package nwalgorithm;

public class Nw {
	
	final int match = 0;
	final int mismatch = 1;
	final int gap_penalty = 1;
	
	private String seq1;
	private String seq2;
	private int rows;
	private int cols;
	private int[][] dpMatrix;
	
	public Nw(String seq1, String seq2) {
		this.seq1 = seq1;
		this.seq2 = seq2;
		this.rows = seq1.length();
		this.cols = seq2.length();
		this.dpMatrix = new int[rows][cols];
		// Initialize the elements of the matrix with zeros
		for (int i = 0; i < rows; i++) {
		    for (int j = 0; j < cols; j++) {
		        dpMatrix[i][j] = 0;
		    }
		}
		// Initialize the first row (i=0)
		for (int j = 1; j < cols; j++) {
		    dpMatrix[0][j] = j * this.gap_penalty;
		}
		
		// Initialize the first column (j=0)
		for (int i = 1; i < rows; i++) {
		    dpMatrix[i][0] = i * this.gap_penalty;
		}
		
	}
	
	private int score_function(int i,int j) {
		int match_score = this.dpMatrix[i - 1][j - 1] + this.seq1.charAt(i-1) == this.seq2.charAt(j-1) ? this.match: this.mismatch;
		int delete_score = this.dpMatrix[i - 1][j] + this.gap_penalty;
		int insert_score = this.dpMatrix[i][j-1] + this.gap_penalty;
		return Math.max(Math.max(match_score, delete_score),insert_score);
	}
	
	public void naive(){
		for(int i=1; i< this.rows; i++) {
			for(int j = 1; j < this.cols; j++) {
				this.dpMatrix[i][j] = this.score_function(i, j);
			}
		}
	}
	
	private void horizontal_update(int i, int j) {
		for(int k = j; k < this.cols; k ++) {
			this.dpMatrix[i][k] = this.score_function(i, k);
		}
	}
	
	private void vertical_update(int i, int j) {
		for(int k = i ; k < this.rows; k ++) {
			this.dpMatrix[k][j] = this.score_function(k, j);
		}
	}
	
	public void parallel() {
		for(int i = 1; i < Math.min(this.rows, this.cols); i ++) {
			final int final_i = i;
			Thread thread_horizontal = new Thread(new Runnable() {
				@Override
				public void run() {
					horizontal_update(final_i,final_i);
				}
			});
			
			Thread thread_vertical = new Thread(new Runnable() {
				@Override
				public void run() {
					vertical_update(final_i,final_i);
				}
			});
			
			thread_horizontal.start();
			thread_vertical.start();
		
			
			
		}
	}
	
	public int[][] getDpMatrix(){
		return this.dpMatrix;
	}
	
}
