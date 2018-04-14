public class SLL {
Node head = null;

  void pushFront(float val) {
    Node newNode = new Node(val);
    if (head == null){
      head = newNode;
    } else{
      newNode.pointer = head;
      head = newNode;
    }

  }

   void print(){
    Node node = head;
    while (true){
      System.out.println(node.val);
      node = node.pointer;
      if (node == null){
        break;
      }
    }

  }

  public static void main(String []args) {
    System.out.println("Hello from main!");
    SLL lst = new SLL();
    lst.head = new Node(5);
    lst.head.pointer = new Node(14);
    lst.head.pointer.pointer = new Node(64);
    lst.print();
  }
}

class Node {
  float val;
  Node pointer = null;
  Node(float value){
    this.val = value;
  }
}
