import java.util.Arrays;
public class ReverseArray{

public static void main(String[] args){

       // int[][] numbers = {{1,2,3}, {4,5,6}, {7,8,9}};
        int[][] numbers = {{8,6}, {4,5,6}, {7,8,9}};

        for(int index = 0; index < numbers.length; index++){
            int first = 0;
            int second = numbers[index].length - 1;
            while(first < second) {
                int old = numbers[index][first];
                    numbers[index][first] = numbers[index][second];
                    numbers[index][second] = old;
                    first++; second--;

     } 
    }
       
    
       
    // System.out.print(Arrays.deepToString(numbers));
    System.out.print(numbers);

}
}


