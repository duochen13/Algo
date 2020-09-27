import java.util.PriorityQueue;
import java.util.Comparator;

class Greater implements Comparator<Integer> {
    public int compare(Integer a, Integer b) {
        return b - a;
    }
}

class MedianFinder {

    PriorityQueue<Integer> maxHeap = new PriorityQueue<>(new Greater());
    PriorityQueue<Integer> minHeap = new PriorityQueue<>();

    public MedianFinder() {
    }

    public void addNum(int num) {
        maxHeap.add(num);
        minHeap.add(maxHeap.poll());
        if (minHeap.size() > maxHeap.size()) {
            maxHeap.add(minHeap.poll());
        }
    }

    public double findMedian() {
        int N = maxHeap.size() + minHeap.size();
        if (N % 2 == 1) {
            return maxHeap.peek();
        }
        return (minHeap.peek() + maxHeap.peek()) * 0.5;
    }
}


class Solution {

    public static void main(String[] args) {
        System.out.println("Hello!");
        MedianFinder mf = new MedianFinder();
        for (int num : new int[]{1,2,3,4,5}) {
            mf.addNum(num);
            double res = mf.findMedian();
            System.out.println(res);
        }
    }
}