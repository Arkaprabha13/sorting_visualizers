#include <iostream>
#include <fstream>
#include <windows.h>  // For Sleep function
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <thread>  // For this_thread
#include <chrono>

using namespace std;

// Function to save sorting steps
void saveStep(const vector<int>& arr) {
    ofstream outfile("steps.txt", ios::app);  // Append mode
    for (int num : arr) {
        outfile << num << " ";
    }
    outfile << "\n";
    outfile.close();
}

// Bubble Sort Algorithm
void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                saveStep(arr);
                Sleep(500);  // Sleep for 500 milliseconds
            }
        }
    }
}

// Insertion Sort Algorithm
void insertionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
            saveStep(arr);
            Sleep(500);  // Sleep for 500 milliseconds
        }
        arr[j + 1] = key;
        saveStep(arr);
    }
}

// Selection Sort Algorithm
void selectionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        swap(arr[i], arr[min_idx]);
        saveStep(arr);
        Sleep(500);  // Sleep for 500 milliseconds
    }
}

// Heap Sort Algorithm (Not Stable)
void heapify(vector<int>& arr, int n, int i) {
    int largest = i;
    int l = 2 * i + 1;
    int r = 2 * i + 2;

    if (l < n && arr[l] > arr[largest])
        largest = l;

    if (r < n && arr[r] > arr[largest])
        largest = r;

    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

void heapSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    for (int i = n - 1; i >= 0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
        saveStep(arr);
        Sleep(500);  // Sleep for 500 milliseconds
    }
}

// Merge Sort Algorithm (Stable)
void merge(vector<int>& arr, int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;

    vector<int> L(n1);
    vector<int> R(n2);

    for (int i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    int i = 0;
    int j = 0;
    int k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k++] = L[i++];
        } else {
            arr[k++] = R[j++];
        }
    }

    while (i < n1) {
        arr[k++] = L[i++];
    }

    while (j < n2) {
        arr[k++] = R[j++];
    }

    saveStep(arr);
}

void mergeSort(vector<int>& arr, int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
        Sleep(500);  // Sleep for 500 milliseconds
    }
}

// Quick Sort Algorithm (Not Stable)
int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = (low - 1);

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
            saveStep(arr);
            Sleep(500);  // Sleep for 500 milliseconds
        }
    }

    swap(arr[i + 1], arr[high]);
    saveStep(arr);
    Sleep(500);  // Sleep for 500 milliseconds

    return (i + 1);
}

void quickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// Main Function
int main() {
    // Read input from input.txt
    ifstream infile("input.txt");
    if (!infile.is_open()) {
        cerr << "Failed to open input.txt\n";
        return 1;
    }

    string line;
    getline(infile, line);  // Read array
    stringstream ss(line);
    vector<int> arr;
    int num;
    while (ss >> num) {
        arr.push_back(num);
        if (ss.peek() == ',') ss.ignore();
    }

    string algo;
    getline(infile, algo);  // Read sorting algorithm
    infile.close();

    // Clear previous steps
    ofstream outfile("steps.txt");
    outfile.close();

    // Choose sorting algorithm
    if (algo == "Bubble Sort") {
        bubbleSort(arr);
    } else if (algo == "Insertion Sort") {
        insertionSort(arr);
    } else if (algo == "Selection Sort") {
        selectionSort(arr);
    } else if (algo == "Heap Sort") {
        heapSort(arr);
    } else if (algo == "Merge Sort") {
        mergeSort(arr, 0, arr.size() - 1);
    } else if (algo == "Quick Sort") {
        quickSort(arr, 0, arr.size() - 1);
    } else {
        cerr << "Unknown sorting algorithm: " << algo << "\n";
        return 1;
    }

    cout << "Sorting complete. Check steps.txt for visualization.\n";
    return 0;
}
