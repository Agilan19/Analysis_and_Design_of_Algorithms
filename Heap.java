//Agilan Ampigaipathar (100553054)
import java.util.Arrays;
import java.util.Collections; 

class Main {

  public void BUILD_MAX_HEAP(int[] numbers) {
    for (int i = numbers.length / 2; i > 0; i--) {
      MAX_HEAPIFY(numbers, i, numbers.length - 1);
    }

    for (int i = numbers.length - 1; i > 0; i--) {
      switchNodes(numbers, 0 , i);
      MAX_HEAPIFY(numbers, 0, i-1);
    }
  }

  public void MAX_HEAPIFY(int[] numbers, int i, int k) {
    int j;
     while ((i*2) + 1 <= k) {
        j = (i*2) + 1;
        if (j < k) {
          if (numbers[j] < numbers[j + 1]) {
            j++;
          }
        }

        if (numbers[i] < numbers[j]) {
          switchNodes(numbers, i, j);
          i = j;
        } 
        else { 
          i = k;
        }
     }
  }

  public int HEAP_MAXIMUM(int[] numbers) {
    //The max heap is already created and so the top (first index) will always be the max
    Arrays.sort(numbers);
    return numbers[numbers.length-1];
  }

  public void HEAP_EXTRACT_MAX(int[] numbers, int max) {
    int[] copyArray = null;
    for(int i = 0; i < numbers.length; i++) {
      //Remove the max
      if(numbers[i] == max) {
        //Copy array onto another array
        copyArray = new int[numbers.length - 1];

        for(int index = 0; index < i; index++) {
            copyArray[index] = numbers[index];
        }
        for (int j = i; j < numbers.length - 1; j++) {
            copyArray[j] = numbers[j+1];
        }
        break;
      }
    }
    for (int g = copyArray.length -1; g > 0; g--) {
        System.out.print(copyArray[g] + " ");
    }
    System.out.println("\n");
  }

  public void MAX_HEAP_INSERT(int[] numbers, int newElement) {
    int currentSize = numbers.length;
    int newSize = currentSize + 1;
    int[] tempArray = new int[newSize];
    for (int i = 0; i < currentSize; i++) {
        tempArray[i] = numbers[i];
    }
    tempArray[newSize - 1] = newElement;
    numbers = tempArray;   
    BUILD_MAX_HEAP(numbers);
    Arrays.sort(numbers);
    for (int g = numbers.length -1; g > 0; g--) {
        System.out.print(numbers[g] + " ");
    }
    System.out.print("\n");
  }

  public void switchNodes(int[] numbers, int i, int j) {
    //Rearrange the nodes 
     int temp = 0;
     temp = numbers[i];
     numbers[i] = numbers[j];
     numbers[j] = temp;
} 

  public static void main(String[] args) {
      int[] numbers = {16, 14, 10, 8, 7, 3, 9, 1, 4, 2};
      Main a = new Main();
      a.BUILD_MAX_HEAP(numbers);

      int max = a.HEAP_MAXIMUM(numbers);

    for (int g = numbers.length -1; g > 0; g--) {
        System.out.print(numbers[g] + " ");
    }
    System.out.print("\n");

      System.out.println("The largest in the max heap is: " + max);

      a.HEAP_EXTRACT_MAX(numbers, max);
      a.MAX_HEAP_INSERT(numbers, 12);
  }
}