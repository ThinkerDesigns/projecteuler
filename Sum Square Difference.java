public class Main {
    public static void main(String[] args) {
        int n = 100;
        int sumOfSquares = 0;
        int squareOfSums = 0;
        for (int i = 0; i < n + 1; i++){
            sumOfSquares = (i * i) + sumOfSquares;
        }
        for (int j = n; j > 0; j--) {
            squareOfSums += j;
        }
        squareOfSums = squareOfSums * squareOfSums;
        System.out.println(squareOfSums - sumOfSquares);
    }
}
