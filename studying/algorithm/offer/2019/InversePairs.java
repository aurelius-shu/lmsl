public class InversePairs {
    private long cnt = 0;
    private int[] tmp;

    public int InversePairs(int[] array) {
        tmp = new int[array.length];
        mergeSort(array, 0, array.length - 1);
        return (int) (cnt % 1000000007);
    }

    private void mergeSort(int[] array, int start, int end) {
        if (start >= end) {
            return;
        }
        int mid = (start + end) / 2;
        mergeSort(array, start, mid);
        mergeSort(array, mid + 1, end);
        merge(array, start, mid, end);
    }

    private void merge(int[] array, int start, int mid, int end) {
        int i = start, j = mid + 1, k = start;
        while (i <= mid || j <= end) {
            if (i > mid) {
                tmp[k] = array[j++];
            } else if (j > end) {
                tmp[k] = array[i++];
            } else if (array[i] <= array[j]) {
                tmp[k] = array[i++];
            } else {
                tmp[k] = array[j++];
                cnt += mid - i + 1;
            }
            k++;
        }
        for (k = start; k <= end; k++) {
            array[k] = tmp[k];
        }
    }
}
