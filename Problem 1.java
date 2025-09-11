import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int inp = scanner.nextInt();
        int res = 0;
        System.out.println("Enter number: ");
        for(int i = 0; i < inp; i++) {
            if (i % 3 == 0) {
                res += i;
            }
            else if (i % 5 == 0) {
                res += i;
            }
            else {
                continue;
            }
        }
        System.out.println(res);
    }
}
