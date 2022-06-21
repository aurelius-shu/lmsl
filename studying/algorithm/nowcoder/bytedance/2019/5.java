package main.nowcoder.bytedance2019;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[][] matrix = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = in.nextInt();
            }
        }
        in.close();

        int V = 1 << (n - 1);
        int[][] dp = new int[n][V];
        for (int i = 0; i < n; i++) {
            dp[i][0] = matrix[i][0];
        }

        for (int j = 1; j < V; j++) {
            for (int i = 0; i < n; i++) {
                dp[i][j] = Integer.MAX_VALUE;
                if (((j >> (i - 1)) & 1) == 0) {
                    for (int k = 1; k < n; k++) {
                        if (((j >> (k - 1)) & 1) == 1) {
                            dp[i][j] = Math.min(dp[i][j], matrix[i][k] + dp[k][j ^ (1 << (k - 1))]);
                        }
                    }
                }
            }
        }

        System.out.println(dp[0][V - 1]);
    }
}