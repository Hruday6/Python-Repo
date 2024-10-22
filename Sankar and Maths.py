import java.util.Scanner;
public class DistinctFValues{
    public static void main(String[] args){
        Scanner scanner=new Scanner(System.in);
        int N=scanner.nextInt();
        int distinctCount=(N%2==0) ?(N/2):(N/2+1);
        System.out.println(distinctCount);
    }
}