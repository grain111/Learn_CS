public class List{
  public static int capacity = 10;
  public static int[] arr = new int[capacity];
  public static int length = 0;

  public static void append(int num){
    if (length == capacity){
      capacity *= 2;
      int[] temp = new int[capacity];
      for (int i = 0; i < length; i++){
        temp[i] = arr[i];
      }
      arr = temp;
    }
    arr[length] = num;
    length++;
  }

  public static int pop(){
    int ans = arr[length - 1];
    length--;
    if (length == capacity / 2){
      capacity /= 2;
      int[] temp = new int[capacity];
      for (int i = 0; i < length; i++){
        temp[i] = arr[i];
      }
      arr = temp;
    }
    return ans;
  }

  public static void main(String[] args) {
    List lst = new List();
    lst.append(5);
    lst.append(7);
    lst.append(7);
    lst.append(7);
    lst.append(7);
    lst.append(7);
    lst.append(7);
    lst.append(7);
    lst.append(7);
    lst.append(7);
    lst.append(7);
    lst.pop();
    lst.append(7);
    System.out.println(lst.capacity);
    System.out.println(lst.length);
    for (int num : lst.arr){
      System.out.println(num);
    }
  }
}
