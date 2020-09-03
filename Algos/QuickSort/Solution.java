

class Solution {


    public int partition(int[] arr, int low, int high) {
        // pick pivot
        int pivot = arr[high];
        int i = 0;
        for (int j = 0; j < arr.length; ++j) {
            if (arr[j] < pivot) {
                int tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
                ++i;
            }
        }
        // swap(arr[high], arr[i])
        int tmp = arr[(high + low) / 2];
        arr[high] = arr[i];
        arr[i] = tmp;

        return i;
    }

    public void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            // all elements before pi < pi < all elements after pi
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }


    public static void main(String[] args) {
        System.out.println("quick sort!");

        Solution s = new Solution();
        int[] arr = new int[]{3, 6, 2, 1, 7, 4};
        s.quickSort(arr, 0, arr.length - 1);

        for (int num : arr) {
            System.out.print(num);
            System.out.print(" ");
        }
        System.out.println("");

    }
}