import java.util.*;

class Node {
    
    Node prev;
    Node next;
    int key;
    int val;
    
    public Node() {
        this.key = 0;
        this.val = 0;
        this.prev = null;
        this.next = null;
    }
    
    public Node(int key, int val) {
        this.key = key;
        this.val = val;
        this.prev = null;
        this.next = null;
    }
}


class LRUCache {

    int size;
    int capacity;
    Node start;
    Node end; 
    Map<Integer, Node> memo;
    
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        this.start = new Node();
        this.end = new Node();
        // dummy start and end node
        this.start.next = this.end;
        this.end.prev = this.start;
        this.memo = new HashMap<>();
    }
    
    public void moveNodeToFront(Node node) {
        Node startNextNode = this.start.next;
        this.start.next = node;
        node.prev = this.start;
        node.next = startNextNode;
        startNextNode.prev = node;
    }

    public void deleteLeastUsedNode(Node node) {
        Node prevNode = node.prev;
        Node nextNode = node.next;
        prevNode.next = nextNode;
        nextNode.prev = prevNode;
        // remove key
    }

    public int get(int key) {
        if (!this.memo.containsKey(key))
            return -1;
        System.out.println("Get node: " + Integer.toString(key) + ":" + Integer.toString(this.memo.get(key).val));
        // move the node to the front
        Node node = this.memo.get(key);
        deleteLeastUsedNode(node);
        moveNodeToFront(node);
        return this.memo.get(key).val;
    }
    
    public void put(int key, int value) {
        if (this.memo.containsKey(key)) {
            Node curNode = this.memo.get(key);
            curNode.val = value;
            // rerange linkedlist
            deleteLeastUsedNode(curNode);
            moveNodeToFront(curNode);
        } else {
            Node newNode = new Node(key, value);
            this.memo.put(key, newNode);   
            System.out.println("Insert new node: " + Integer.toString(key) + ":" + Integer.toString(value));
            // add node in the very beginning
            moveNodeToFront(newNode);
            // increment size
            this.size++;
            // out of size
            if (this.size > this.capacity) {
                // delete the least used node
                Node removedNode = this.end.prev;
                System.out.println("removedNode " + Integer.toString(removedNode.key) + ":" + Integer.toString(removedNode.val));
                deleteLeastUsedNode(removedNode);
                // decrement size
                this.size--;
                // remove key
                this.memo.remove(removedNode.key);
            }
            
        }
    }

    public void printData() {
        Node node = this.start;
        while (node != null) {
            System.out.print(Integer.toString(node.key) + " ");
            node = node.next;
        }
        System.out.println("");
    }
}

public class Solution {


    public static void main(String[] args) {

        Solution s = new Solution();
        LRUCache cache = new LRUCache(2);
        cache.put(1,1);
        cache.put(2,2);
        cache.printData();
        cache.get(1);
        cache.printData();
        cache.put(3,3);
        cache.printData();
        cache.get(2);
        cache.printData();
        // go over size
        cache.put(4,4);
        cache.printData();
        cache.get(1);
        cache.printData();
        cache.get(3);
        cache.printData();
        cache.get(4);
        cache.printData();

    }
}