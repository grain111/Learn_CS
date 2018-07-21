public class SLLTest{
  public static void main(String []args){
    System.out.println("Hello from main!");
    SLL lst = new SLL();
    lst.head = new Node(5);
    lst.head.pointer = new Node(14);
    lst.head.pointer.pointer = new Node(64);
    lst.print();
  }
}
