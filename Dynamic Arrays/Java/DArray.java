import java.util.*;

public class DArray{
  public static void main(String[] args) {
    int[] arr = new int[1];
    arr[0] = 6;
    System.out.println(arr[0]);

    List<Integer> lst = new ArrayList<Integer>(10);
    lst.add(5);
    lst.add('a');
    System.out.println(lst.get(0));
    System.out.println(lst.get(1));
  }
}
