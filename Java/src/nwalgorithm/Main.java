package nwalgorithm;

import java.util.Random;

public class Main {
	public static void main(String[] args) {
		String seq1 = generateRandomString(20000);
		String seq2 = generateRandomString(20000);
		

		Nw nw_naive = new Nw(seq1,seq2);
		Nw nw_parallel = new Nw(seq1,seq2);
		long starting_time = System.currentTimeMillis();
		nw_naive.naive();
		long ending_time = System.currentTimeMillis();
		
		System.out.print("naive: " + starting_time);
		
		starting_time = System.currentTimeMillis();
		nw_parallel.parallel();
		ending_time = System.currentTimeMillis();
		System.out.print("parallel: " + starting_time);
		
	}
	
	public static String generateRandomString(int length) {
		String characters = "acgt";
        StringBuilder randomString = new StringBuilder();

        Random random = new Random();

        for (int i = 0; i < length; i++) {
            int randomIndex = random.nextInt(characters.length());
            char randomChar = characters.charAt(randomIndex);
            randomString.append(randomChar);
        }

        return randomString.toString();
	}
	
	public static void printMatrix(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println(); // Move to the next line after each row
        }
    }
}
