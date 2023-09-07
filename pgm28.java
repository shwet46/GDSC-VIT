public class pgm28 { // Sudoku solver



    public static void main(String[] args) {

        int[][] grid = { { 3, 0, 6, 5, 0, 8, 4, 0, 0 },
                { 5, 2, 0, 0, 0, 0, 0, 0, 0 },
                { 0, 8, 7, 0, 0, 0, 0, 3, 1 },
                { 0, 0, 3, 0, 1, 0, 0, 8, 0 },
                { 9, 0, 0, 8, 6, 3, 0, 0, 5 },
                { 0, 5, 0, 0, 9, 0, 6, 0, 0 },
                { 1, 3, 0, 0, 0, 0, 2, 5, 0 },
                { 0, 0, 0, 0, 0, 0, 0, 7, 4 },
                { 0, 0, 5, 2, 0, 6, 3, 0, 0 } };


                if (solveSudoku(grid)) {
                    printSudoku(grid);
                } else {
                    System.out.println("No solution exists.");
                }
            }

            public static boolean solveSudoku(int[][] board) {
                for (int row = 0; row < 9; row++) {
                    for (int col = 0; col < 9; col++) {
                        if (board[row][col] == 0) {
                            for (int num = 1; num <= 9; num++) {
                                if (isValid(board, row, col, num)) {
                                    board[row][col] = num;
                                    if (solveSudoku(board)) {
                                        return true;
                                    }
                                    board[row][col] = 0;
                                }
                            }
                            return false;
                        }
                    }
                }
                return true;
            }

            public static boolean isValid(int[][] board, int row, int col, int num) {
                for (int i = 0; i < 9; i++) {
                    if (board[row][i] == num || board[i][col] == num || board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == num) {
                        return false;
                    }
                }
                return true;
            }

            public static void printSudoku(int[][] board) {
                for (int row = 0; row < 9; row++) {
                    for (int col = 0; col < 9; col++) {
                        System.out.print(board[row][col] + " ");
                    }
                    System.out.println();
                }
            }
        }
