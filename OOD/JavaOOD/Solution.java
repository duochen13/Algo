

/*
1. interface & abstract class

interface A{
    final val (built-in default)
    // abstract method, all methods declared here must be implemented by the classes that implements this class
    void greetings()
}

abstract class B {
    // 1. some lines of code you want to share among related classes
    // 2. Define non-static, non-final vars
    final var
    non-final var
    // implementation
}

C implements A
D extends B

*/

import java.io.*;

abstract class University {
    String name = "";

    University(String name) { this.name = name; }

    // default non-abstract methods
    public void introduction() {
        System.out.println("name intro: " + this.name);
    }

    //abstract methods declaration
    abstract public void greetings();
}


class Department extends University {
    int size;
    String department_name = "";

    Department(String name, String department_name, int size) { 
        super(name);
        this.size = size; 
        this.department_name = department_name; 
    }

    @Override
    public void greetings() {
        System.out.println("University: " + this.name + ", Department: " + this.department_name + ", size: " + this.size);
    }

}

interface Animal {
    // abstract method
    int size = 2;
    void greetings();
}

class Cat implements Animal {
    String name = "";
    
    Cat(String name) { this.name = name; }
    
    @Override
    public void greetings() { System.out.println("Cat: " + this.name + " miao~"); }
}


class Solution {
    public static void main(String[] args) {
        Solution s = new Solution();
        Department d = new Department("Umich", "EECS", 1000);
        d.introduction();
        d.greetings();
        
    }
}