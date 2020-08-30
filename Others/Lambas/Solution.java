import java.util.List;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

class Student {
    String name;
    int age;
    public Student() {}
    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }
}

class Sortbyage implements Comparator<Student> {
    public int compare(Student a, Student b) {
        return a.age - b.age;
    }
}

class Solution {
    public static void main(String[] args) {
        Solution s = new Solution();
        List<Student> res = new ArrayList<>();
        res.add(new Student("Mina", 23));
        res.add(new Student("Miyouyi", 22));
    

        // Arrays.sort(res, (a, b) -> a.age - b.age);
        Collections.sort(res, new Sortbyage());

        for (Student student: res) {
            System.out.println(student.name);
        }
    }
}