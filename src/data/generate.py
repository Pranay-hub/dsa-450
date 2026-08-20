import json
import re

def slug(name):
    s = name.lower().strip()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    s = s.strip('-')
    return s

problems = []

# ============================================================
# ARRAYS (36 problems)
# ============================================================

problems.append({
    "id": slug("Reverse the array"),
    "topic": "Array",
    "problem": "Reverse the array",
    "difficulty": "Easy",
    "status": "solved",
    "notes": "Swap first and last elements moving inward",
    "solution": {
        "python": "def reverse(arr):\n    left, right = 0, len(arr) - 1\n    while left < right:\n        arr[left], arr[right] = arr[right], arr[left]\n        left += 1\n        right -= 1\n    return arr",
        "cpp": "#include <vector>\nusing namespace std;\nvoid reverse(vector<int>& arr) {\n    int left = 0, right = arr.size() - 1;\n    while (left < right) {\n        swap(arr[left], arr[right]);\n        left++;\n        right--;\n    }\n}",
        "java": "public static void reverse(int[] arr) {\n    int left = 0, right = arr.length - 1;\n    while (left < right) {\n        int temp = arr[left];\n        arr[left] = arr[right];\n        arr[right] = temp;\n        left++;\n        right--;\n    }\n}"
    },
    "explanation": "Use two pointers starting from both ends of the array. Swap elements at left and right pointers, then move inward until they meet. This reverses the array in-place.",
    "algorithm": "Two Pointers",
    "timeComplexity": "O(n)",
    "spaceComplexity": "O(1)",
    "visualization": {"type": "none", "data": {}}
})

problems.append({
    "id": slug("Find the maximum and minimum element in an array"),
    "topic": "Array",
    "problem": "Find the maximum and minimum element in an array",
    "difficulty": "Easy",
    "status": "solved",
    "notes": "Compare elements pairwise to reduce comparisons",
    "solution": {
        "python": "def getMinMax(arr):\n    if len(arr) % 2 == 0:\n        mx = max(arr[0], arr[1])\n        mn = min(arr[0], arr[1])\n        i = 2\n    else:\n        mx = mn = arr[0]\n        i = 1\n    while i < len(arr) - 1:\n        if arr[i] < arr[i + 1]:\n            mx = max(mx, arr[i + 1])\n            mn = min(mn, arr[i])\n        else:\n            mx = max(mx, arr[i])\n            mn = min(mn, arr[i + 1])\n        i += 2\n    return mn, mx",
        "cpp": "#include <vector>\n#include <algorithm>\nusing namespace std;\npair<int,int> getMinMax(vector<int>& arr) {\n    int mn = arr[0], mx = arr[0];\n    for (int i = 1; i < arr.size(); i++) {\n        mx = max(mx, arr[i]);\n        mn = min(mn, arr[i]);\n    }\n    return {mn, mx};\n}",
        "java": "public static int[] getMinMax(int[] arr) {\n    int mn = arr[0], mx = arr[0];\n    for (int i = 1; i < arr.length; i++) {\n        mx = Math.max(mx, arr[i]);\n        mn = Math.min(mn, arr[i]);\n    }\n    return new int[]{mn, mx};\n}"
    },
    "explanation": "Iterate through the array once, keeping track of the minimum and maximum values seen so far. Compare each element against current min and max.",
    "algorithm": "Linear Scan",
    "timeComplexity": "O(n)",
    "spaceComplexity": "O(1)",
    "visualization": {"type": "none", "data": {}}
})

problems.append({
    "id": slug("Find the Kth max and min element of an array"),
    "topic": "Array",
    "problem": "Find the \"Kth\" max and min element of an array",
    "difficulty": "Medium",
    "status": "pending",
    "notes": "Use min-heap or quickselect",
    "solution": {
        "python": "import heapq\ndef kthSmallest(arr, k):\n    heapq.heapify(arr)\n    for _ in range(k - 1):\n        heapq.heappop(arr)\n    return heapq.heappop(arr)\n\ndef kthLargest(arr, k):\n    return kthSmallest(arr[:], len(arr) - k + 1)",
        "cpp": "#include <vector>\n#include <queue>\nusing namespace std;\nint kthSmallest(vector<int> arr, int k) {\n    priority_queue<int> pq;\n    for (int x : arr) {\n        pq.push(x);\n        if (pq.size() > k) pq.pop();\n    }\n    return pq.top();\n}",
        "java": "public static int kthSmallest(int[] arr, int k) {\n    PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());\n    for (int x : arr) {\n        pq.offer(x);\n        if (pq.size() > k) pq.poll();\n    }\n    return pq.poll();\n}"
    },
    "explanation": "Use a min-heap of size k. For kth smallest, iterate and maintain heap of k smallest elements. The root of the heap is the kth smallest. For kth largest, use k' = n-k+1.",
    "algorithm": "Heap",
    "timeComplexity": "O(n log k)",
    "spaceComplexity": "O(k)",
    "visualization": {"type": "none", "data": {}}
})

problems.append({
    "id": slug("Sort an array of 0s 1s and 2s"),
    "topic": "Array",
    "problem": "Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo",
    "difficulty": "Easy",
    "status": "solved",
    "notes": "Count 0s, 1s, 2s and overwrite",
    "solution": {
        "python": "def sort012(arr):\n    lo, mid, hi = 0, 0, len(arr) - 1\n    while mid <= hi:\n        if arr[mid] == 0:\n            arr[lo], arr[mid] = arr[mid], arr[lo]\n            lo += 1\n            mid += 1\n        elif arr[mid] == 1:\n            mid += 1\n        else:\n            arr[mid], arr[hi] = arr[hi], arr[mid]\n            hi -= 1\n    return arr",
        "cpp": "#include <vector>\nusing namespace std;\nvoid sort012(vector<int>& arr) {\n    int lo = 0, mid = 0, hi = arr.size() - 1;\n    while (mid <= hi) {\n        if (arr[mid] == 0) swap(arr[lo++], arr[mid++]);\n        else if (arr[mid] == 1) mid++;\n        else swap(arr[mid], arr[hi--]);\n    }\n}",
        "java": "public static void sort012(int[] arr) {\n    int lo = 0, mid = 0, hi = arr.length - 1;\n    while (mid <= hi) {\n        if (arr[mid] == 0) { int t = arr[lo]; arr[lo] = arr[mid]; arr[mid] = t; lo++; mid++; }\n        else if (arr[mid] == 1) mid++;\n        else { int t = arr[mid]; arr[mid] = arr[hi]; arr[hi] = t; hi--; }\n    }\n}"
    },
    "explanation": "Dutch National Flag algorithm: maintain three pointers - lo (boundary of 0s), mid (current element), hi (boundary of 2s). Partition array in single pass.",
    "algorithm": "Dutch National Flag / Three Pointers",
    "timeComplexity": "O(n)",
    "spaceComplexity": "O(1)",
    "visualization": {"type": "sorting", "data": {"array": [2, 0, 1, 2, 1, 0], "algorithm": "dutch-national-flag"}}
})

problems.append({
    "id": slug("Move all negative elements to one side of the array"),
    "topic": "Array",
    "problem": "Move all the negative elements to one side of the array",
    "difficulty": "Easy",
    "status": "solved",
    "notes": "Two pointer approach: swap negative to left",
    "solution": {
        "python": "def rearrange(arr):\n    j = 0\n    for i in range(len(arr)):\n        if arr[i] < 0:\n            arr[i], arr[j] = arr[j], arr[i]\n            j += 1\n    return arr",
        "cpp": "#include <vector>\nusing namespace std;\nvoid rearrange(vector<int>& arr) {\n    int j = 0;\n    for (int i = 0; i < arr.size(); i++) {\n        if (arr[i] < 0) swap(arr[i], arr[j++]);\n    }\n}",
        "java": "public static void rearrange(int[] arr) {\n    int j = 0;\n    for (int i = 0; i < arr.length; i++) {\n        if (arr[i] < 0) { int t = arr[i]; arr[i] = arr[j]; arr[j] = t; j++; }\n    }\n}"
    },
    "explanation": "Use a partition pointer j. When we find a negative element at i, swap it with arr[j] and advance j. This is essentially the partition step of quicksort.",
    "algorithm": "Partition / Two Pointers",
    "timeComplexity": "O(n)",
    "spaceComplexity": "O(1)",
    "visualization": {"type": "none", "data": {}}
})

problems.append({
    "id": slug("Union and Intersection of two sorted arrays"),
    "topic": "Array",
    "problem": "Find the Union and Intersection of the two sorted arrays.",
    "difficulty": "Easy",
    "status": "pending",
    "notes": "Use merge technique from merge sort",
    "solution": {
        "python": "def findUnion(a, b):\n    i, j = 0, 0\n    union = []\n    while i < len(a) and j < len(b):\n        if a[i] < b[j]:\n            if not union or union[-1] != a[i]: union.append(a[i])\n            i += 1\n        elif a[i] > b[j]:\n            if not union or union[-1] != b[j]: union.append(b[j])\n            j += 1\n        else:\n            if not union or union[-1] != a[i]: union.append(a[i])\n            i += 1\n            j += 1\n    while i < len(a):\n        if not union or union[-1] != a[i]: union.append(a[i])\n        i += 1\n    while j < len(b):\n        if not union or union[-1] != b[j]: union.append(b[j])\n        j += 1\n    return union\n\ndef findIntersection(a, b):\n    i, j = 0, 0\n    inter = []\n    while i < len(a) and j < len(b):\n        if a[i] < b[j]: i += 1\n        elif a[i] > b[j]: j += 1\n        else:\n            if not inter or inter[-1] != a[i]: inter.append(a[i])\n            i += 1\n            j += 1\n    return inter",
        "cpp": "#include <vector>\nusing namespace std;\nvector<int> findUnion(vector<int>& a, vector<int>& b) {\n    int i = 0, j = 0;\n    vector<int> res;\n    while (i < a.size() && j < b.size()) {\n        if (a[i] < b[j]) { if (res.empty() || res.back() != a[i]) res.push_back(a[i]); i++; }\n        else if (a[i] > b[j]) { if (res.empty() || res.back() != b[j]) res.push_back(b[j]); j++; }\n        else { if (res.empty() || res.back() != a[i]) res.push_back(a[i]); i++; j++; }\n    }\n    while (i < a.size()) { if (res.empty() || res.back() != a[i]) res.push_back(a[i]); i++; }\n    while (j < b.size()) { if (res.empty() || res.back() != b[j]) res.push_back(b[j]); j++; }\n    return res;\n}",
        "java": "public static ArrayList<Integer> findUnion(int[] a, int[] b) {\n    ArrayList<Integer> res = new ArrayList<>();\n    int i = 0, j = 0;\n    while (i < a.length && j < b.length) {\n        if (a[i] < b[j]) { if (res.isEmpty() || res.get(res.size()-1) != a[i]) res.add(a[i]); i++; }\n        else if (a[i] > b[j]) { if (res.isEmpty() || res.get(res.size()-1) != b[j]) res.add(b[j]); j++; }\n        else { if (res.isEmpty() || res.get(res.size()-1) != a[i]) res.add(a[i]); i++; j++; }\n    }\n    while (i < a.length) { if (res.isEmpty() || res.get(res.size()-1) != a[i]) res.add(a[i]); i++; }\n    while (j < b.length) { if (res.isEmpty() || res.get(res.size()-1) != b[j]) res.add(b[j]); j++; }\n    return res;\n}"
    },
    "explanation": "Use merge technique like merge sort. For union: include element if it appears in either array (skip duplicates). For intersection: include only when elements match in both arrays.",
    "algorithm": "Two Pointers / Merge",
    "timeComplexity": "O(m + n)",
    "spaceComplexity": "O(1) excluding output",
    "visualization": {"type": "none", "data": {}}
})

problems.append({
    "id": slug("Cyclically rotate an array by one"),
    "topic": "Array",
    "problem": "Write a program to cyclically rotate an array by one.",
    "difficulty": "Easy",
    "status": "solved",
    "notes": "Store last element, shift all right by 1, put last at index 0",
    "solution": {
        "python": "def rotate(arr):\n    last = arr[-1]\n    for i in range(len(arr) - 1, 0, -1):\n        arr[i] = arr[i - 1]\n    arr[0] = last\n    return arr",
        "cpp": "#include <vector>\nusing namespace std;\nvoid rotate(vector<int>& arr) {\n    int last = arr.back();\n    for (int i = arr.size() - 1; i > 0; i--)\n        arr[i] = arr[i - 1];\n    arr[0] = last;\n}",
        "java": "public static void rotate(int[] arr) {\n    int last = arr[arr.length - 1];\n    for (int i = arr.length - 1; i > 0; i--)\n        arr[i] = arr[i - 1];\n    arr[0] = last;\n}"
    },
    "explanation": "Store the last element. Shift all elements one position to the right (from end to start). Place the stored last element at position 0.",
    "algorithm": "In-place Rotation",
    "timeComplexity": "O(n)",
    "spaceComplexity": "O(1)",
    "visualization": {"type": "none", "data": {}}
})

problems.append({
    "id": slug("Largest sum contiguous subarray"),
    "topic": "Array",
    "problem": "find Largest sum contiguous Subarray [V. IMP]",
    "difficulty": "Medium",
    "status": "solved",
    "notes": "Kadane's algorithm",
    "solution": {
        "python": "def maxSubArray(arr):\n    max_so_far = float('-inf')\n    max_ending_here = 0\n    for i in range(len(arr)):\n        max_ending_here += arr[i]\n        if max_so_far < max_ending_here:\n            max_so_far = max_ending_here\n        if max_ending_here < 0:\n            max_ending_here = 0\n    return max_so_far",
        "cpp": "#include <vector>\n#include <algorithm>\nusing namespace std;\nint maxSubArray(vector<int>& arr) {\n    int max_so_far = INT_MIN, max_ending_here = 0;\n    for (int i = 0; i < arr.size(); i++) {\n        max_ending_here += arr[i];\n        max_so_far = max(max_so_far, max_ending_here);\n        if (max_ending_here < 0) max_ending_here = 0;\n    }\n    return max_so_far;\n}",
        "java": "public static int maxSubArray(int[] arr) {\n    int maxSoFar = Integer.MIN_VALUE, maxEndingHere = 0;\n    for (int i = 0; i < arr.length; i++) {\n        maxEndingHere += arr[i];\n        if (maxSoFar < maxEndingHere) maxSoFar = maxEndingHere;\n        if (maxEndingHere < 0) maxEndingHere = 0;\n    }\n    return maxSoFar;\n}"
    },
    "explanation": "Kadane's algorithm: iterate through array maintaining a running sum. If running sum becomes negative, reset it to 0 (start a new subarray). Track the maximum sum seen.",
    "algorithm": "Kadane's Algorithm",
    "timeComplexity": "O(n)",
    "spaceComplexity": "O(1)",
    "visualization": {"type": "dp-table", "data": {"description": "Running max sum at each position", "rows": ["max_ending_here", "max_so_far"], "cols": ["index values"]}}
})

problems.append({
    "id": slug("Minimise the maximum difference between heights"),
    "topic": "Array",
    "problem": "Minimise the maximum difference between heights [V.IMP]",
    "difficulty": "Medium",
    "status": "solved",
    "notes": "Sort array, add k to smaller, subtract k from larger, find min diff",
    "solution": {
        "python": "def getMinDiff(arr, k):\n    n = len(arr)\n    if n == 1: return 0\n    arr.sort()\n    ans = arr[-1] - arr[0]\n    small, big = arr[0] + k, arr[-1] - k\n    if small > big: small, big = big, small\n    for i in range(1, n - 1):\n        subtract = arr[i] - k\n        add = arr[i] + k\n        if subtract >= small and add <= big: continue\n        if add - small <= big - subtract: small = subtract\n        else: big = add\n    return min(ans, big - small)",
        "cpp": "#include <vector>\n#include <algorithm>\nusing namespace std;\nint getMinDiff(vector<int>& arr, int k) {\n    int n = arr.size();\n    sort(arr.begin(), arr.end());\n    int ans = arr[n-1] - arr[0];\n    int small = arr[0] + k, big = arr[n-1] - k;\n    if (small > big) swap(small, big);\n    for (int i = 1; i < n - 1; i++) {\n        int sub = arr[i] - k, add = arr[i] + k;\n        if (sub >= small || add <= big) continue;\n        if (add - small <= big - sub) small = sub;\n        else big = add;\n    }\n    return min(ans, big - small);\n}",
        "java": "public static int getMinDiff(int[] arr, int k) {\n    int n = arr.length;\n    Arrays.sort(arr);\n    int ans = arr[n-1] - arr[0];\n    int small = arr[0] + k, big = arr[n-1] - k;\n    if (small > big) { int t = small; small = big; big = t; }\n    for (int i = 1; i < n - 1; i++) {\n        int sub = arr[i] - k, add = arr[i] + k;\n        if (sub >= small || add <= big) continue;\n        if (add - small <= big - sub) small = sub;\n        else big = add;\n    }\n    return Math.min(ans, big - small);\n}"
    },
    "explanation": "Sort the array. After sorting, modify each element by +/- k. Try to minimize the range between max and min by adjusting elements closer to the middle. Track the best possible min difference.",
    "algorithm": "Sorting + Greedy",
    "timeComplexity": "O(n log n)",
    "spaceComplexity": "O(1)",
    "visualization": {"type": "none", "data": {}}
})

problems.append({
    "id": slug("Minimum number of Jumps to reach end of an array"),
    "topic": "Array",
    "problem": "Minimum no. of Jumps to reach end of an array",
    "difficulty": "Medium",
    "status": "solved",
    "notes": "Greedy: track farthest reachable position",
    "solution": {
        "python": "def minJumps(arr):\n    n = len(arr)\n    if n <= 1: return 0\n    if arr[0] == 0: return -1\n    jumps = 0\n    current_end = 0\n    farthest = 0\n    for i in range(n - 1):\n        farthest = max(farthest, i + arr[i])\n        if i == current_end:\n            jumps += 1\n            current_end = farthest\n            if current_end >= n - 1: break\n    return jumps if current_end >= n - 1 else -1",
        "cpp": "#include <vector>\n#include <algorithm>\nusing namespace std;\nint minJumps(vector<int>& arr) {\n    int n = arr.size();\n    if (n <= 1) return 0;\n    if (arr[0] == 0) return -1;\n    int jumps = 0, curEnd = 0, farthest = 0;\n    for (int i = 0; i < n - 1; i++) {\n        farthest = max(farthest, i + arr[i]);\n        if (i == curEnd) {\n            jumps++;\n            curEnd = farthest;\n            if (curEnd >= n - 1) break;\n        }\n    }\n    return curEnd >= n - 1 ? jumps : -1;\n}",
        "java": "public static int minJumps(int[] arr) {\n    int n = arr.length;\n    if (n <= 1) return 0;\n    if (arr[0] == 0) return -1;\n    int jumps = 0, curEnd = 0, farthest = 0;\n    for (int i = 0; i < n - 1; i++) {\n        farthest = Math.max(farthest, i + arr[i]);\n        if (i == curEnd) {\n            jumps++;\n            curEnd = farthest;\n            if (curEnd >= n - 1) break;\n        }\n    }\n    return curEnd >= n - 1 ? jumps : -1;\n}"
    },
    "explanation": "Greedy approach: track the farthest reachable position. When we reach the end of current jump range, increment jumps and extend range to farthest we can reach.",
    "algorithm": "Greedy",
    "timeComplexity": "O(n)",
    "spaceComplexity": "O(1)",
    "visualization": {"type": "none", "data": {}}
})

problems.append({
    "id": slug("Find duplicate in an array of N+1 Integers"),
    "topic": "Array",
    "problem": "find duplicate in an array of N+1 Integers",
    "difficulty": "Medium",
    "status": "solved",
    "notes": "Floyd's cycle detection or index marking",
    "solution": {
        "python": "def findDuplicate(arr):\n    slow = arr[0]\n    fast = arr[0]\n    while True:\n        slow = arr[slow]\n        fast = arr[arr[fast]]\n        if slow == fast: break\n    slow = arr[0]\n    while slow != fast:\n        slow = arr[slow]\n        fast = arr[fast]\n    return slow",
        "cpp": "#include <vector>\nusing namespace std;\nint findDuplicate(vector<int>& arr) {\n    int slow = arr[0], fast = arr[0];\n    do { slow = arr[slow]; fast = arr[arr[fast]]; } while (slow != fast);\n    slow = arr[0];\n    while (slow != fast) { slow = arr[slow]; fast = arr[fast]; }\n    return slow;\n}",
        "java": "public static int findDuplicate(int[] arr) {\n    int slow = arr[0], fast = arr[0];\n    do { slow = arr[slow]; fast = arr[arr[fast]]; } while (slow != fast);\n    slow = arr[0];\n    while (slow != fast) { slow = arr[slow]; fast = arr[fast]; }\n    return slow;\n}"
    },
    "explanation": "Floyd's cycle detection: treat array as a linked list where arr[i] is next node. Find cycle entry point using slow/fast pointers. The meeting point after resetting one pointer to start and moving both one step at a time gives the duplicate.",
    "algorithm": "Floyd's Cycle Detection",
    "timeComplexity": "O(n)",
    "spaceComplexity": "O(1)",
    "visualization": {"type": "none", "data": {}}
})

problems.append({
    "id": slug("Merge 2 sorted arrays without using Extra space"),
    "topic": "Array",
    "problem": "Merge 2 sorted arrays without using Extra space.",
    "difficulty": "Medium",
    "status": "solved",
    "notes": "Gap method or start from end of arr1 and beginning of arr2",
    "solution": {
        "python": "def merge(arr1, arr2):\n    n, m = len(arr1), len(arr2)\n    gap = (n + m + 1) // 2\n    while gap > 0:\n        i = 0\n        while i + gap < n + m:\n            j = i + gap\n            a = arr1[i] if i < n else arr2[i - n]\n            b = arr1[j] if j < n else arr2[j - n]\n            if a > b:\n                if i < n and j < n: arr1[i], arr1[j] = arr1[j], arr1[i]\n                elif i < n and j >= n: arr1[i], arr2[j - n] = arr2[j - n], arr1[i]\n                else: arr2[i - n], arr2[j - n] = arr2[j - n], arr2[i - n]\n            i += 1\n        if gap == 1: break\n        gap = (gap + 1) // 2\n    arr1.sort()\n    arr2.sort()",
        "cpp": "#include <vector>\n#include <algorithm>\nusing namespace std;\nvoid merge(vector<int>& a, vector<int>& b) {\n    int n = a.size(), m = b.size();\n    int gap = (n + m + 1) / 2;\n    while (gap > 0) {\n        for (int i = 0; i + gap < n + m; i++) {\n            int j = i + gap;\n            int ai = (i < n) ? a[i] : b[i - n];\n            int aj = (j < n) ? a[j] : b[j - n];\n            if (ai > aj) {\n                if (i < n && j < n) swap(a[i], a[j]);\n                else if (i < n) swap(a[i], b[j - n]);\n                else swap(b[i - n], b[j - n]);\n            }\n        }\n        if (gap == 1) break;\n        gap = (gap + 1) / 2;\n    }\n}",
        "java": "public static void merge(int[] a, int[] b) {\n    int n = a.length, m = b.length;\n    int gap = (n + m + 1) / 2;\n    while (gap > 0) {\n        for (int i = 0; i + gap < n + m; i++) {\n            int j = i + gap;\n            int ai = (i < n) ? a[i] : b[i - n];\n            int aj = (j < n) ? a[j] : b[j - n];\n            if (ai > aj) {\n                if (i < n && j < n) { int t = a[i]; a[i] = a[j]; a[j] = t; }\n                else if (i < n) { int t = a[i]; a[i] = b[j-n]; b[j-n] = t; }\n                else { int t = b[i-n]; b[i-n] = b[j-n]; b[j-n] = t; }\n            }\n        }\n        if (gap == 1) break;\n        gap = (gap + 1) / 2;\n    }\n}"
    },
    "explanation": "Shell sort-like gap method: start with gap = (n+m)/2, compare elements at distance gap across both arrays and swap if needed. Reduce gap until 1. Then do a final pass with gap=1.",
    "algorithm": "Gap Method",
    "timeComplexity": "O((n+m) log(n+m))",
    "spaceComplexity": "O(1)",
    "visualization": {"type": "none", "data": {}}
})

problems.append({
    "id": slug("Kadanes Algorithm"),
    "topic": "Array",
    "problem": "Kadane's Algo [V.V.V.V.V IMP]",
    "difficulty": "Medium",
    "status": "solved",
    "notes": "Same as largest sum contiguous subarray",
    "solution": {
        "python": "def kadane(arr):\n    max_so_far = float('-inf')\n    max_ending_here = 0\n    start, end, s = 0, 0, 0\n    for i in range(len(arr)):\n        max_ending_here += arr[i]\n        if max_so_far < max_ending_here:\n            max_so_far = max_ending_here\n            start = s\n            end = i\n        if max_ending_here < 0:\n            max_ending_here = 0\n            s = i + 1\n    return max_so_far, start, end",
        "cpp": "#include <vector>\n#include <climits>\nusing namespace std;\nstruct Result { int sum, start, end; };\nResult kadane(vector<int>& arr) {\n    int maxSoFar = INT_MIN, maxEndingHere = 0;\n    int start = 0, end = 0, s = 0;\n    for (int i = 0; i < arr.size(); i++) {\n        maxEndingHere += arr[i];\n        if (maxSoFar < maxEndingHere) {\n            maxSoFar = maxEndingHere;\n            start = s; end = i;\n        }\n        if (maxEndingHere < 0) { maxEndingHere = 0; s = i + 1; }\n    }\n    return {maxSoFar, start, end};\n}",
        "java": "public static int[] kadane(int[] arr) {\n    int maxSoFar = Integer.MIN_VALUE, maxEndingHere = 0;\n    int start = 0, end = 0, s = 0;\n    for (int i = 0; i < arr.length; i++) {\n        maxEndingHere += arr[i];\n        if (maxSoFar < maxEndingHere) { maxSoFar = maxEndingHere; start = s; end = i; }\n        if (maxEndingHere < 0) { maxEndingHere = 0; s = i + 1; }\n    }\n    return new int[]{maxSoFar, start, end};\n}"
    },
    "explanation": "Kadane's algorithm with subarray tracking: maintain running sum, reset when negative. Track start and end indices of the maximum subarray.",
    "algorithm": "Kadane's Algorithm",
    "timeComplexity": "O(n)",
    "spaceComplexity": "O(1)",
    "visualization": {"type": "none", "data": {}}
})

problems.append({
    "id": slug("Merge Intervals"),
    "topic": "Array",
    "problem": "Merge Intervals",
    "difficulty": "Medium",
    "status": "solved",
    "notes": "Sort by start, merge overlapping",
    "solution": {
        "python": "def merge(intervals):\n    intervals.sort(key=lambda x: x[0])\n    merged = [intervals[0]]\n    for i in range(1, len(intervals)):\n        if merged[-1][1] >= intervals[i][0]:\n            merged[-1][1] = max(merged[-1][1], intervals[i][1])\n        else:\n            merged.append(intervals[i])\n    return merged",
        "cpp": "#include <vector>\n#include <algorithm>\nusing namespace std;\nvector<vector<int>> merge(vector<vector<int>>& intervals) {\n    sort(intervals.begin(), intervals.end());\n    vector<vector<int>> merged;\n    merged.push_back(intervals[0]);\n    for (int i = 1; i < intervals.size(); i++) {\n        if (merged.back()[1] >= intervals[i][0])\n            merged.back()[1] = max(merged.back()[1], intervals[i][1]);\n        else merged.push_back(intervals[i]);\n    }\n    return merged;\n}",
        "java": "public static int[][] merge(int[][] intervals) {\n    Arrays.sort(intervals, (a, b) -> a[0] - b[0]);\n    ArrayList<int[]> merged = new ArrayList<>();\n    merged.add(intervals[0]);\n    for (int i = 1; i < intervals.length; i++) {\n        if (merged.get(merged.size()-1)[1] >= intervals[i][0])\n            merged.get(merged.size()-1)[1] = Math.max(merged.get(merged.size()-1)[1], intervals[i][1]);\n        else merged.add(intervals[i]);\n    }\n    return merged.toArray(new int[0][]);\n}"
    },
    "explanation": "Sort intervals by start time. Iterate through, merging each interval with the previous if they overlap (current start <= previous end). Otherwise add as new interval.",
    "algorithm": "Sorting + Merge",
    "timeComplexity": "O(n log n)",
    "spaceComplexity": "O(n)",
    "visualization": {"type": "none", "data": {}}
})

problems.append({
    "id": slug("Next Permutation"),
    "topic": "Array",
    "problem": "Next Permutation",
    "difficulty": "Medium",
    "status": "solved",
    "notes": "Find first decreasing from right, swap with next larger, reverse suffix",
    "solution": {
        "python": "def nextPermutation(arr):\n    n = len(arr)\n    i = n - 2\n    while i >= 0 and arr[i] >= arr[i + 1]:\n        i -= 1\n    if i >= 0:\n        j = n - 1\n        while arr[j] <= arr[i]:\n            j -= 1\n        arr[i], arr[j] = arr[j], arr[i]\n    left, right = i + 1, n - 1\n    while left < right:\n        arr[left], arr[right] = arr[right], arr[left]\n        left += 1\n        right -= 1\n    return arr",
        "cpp": "#include <vector>\n#include <algorithm>\nusing namespace std;\nvoid nextPermutation(vector<int>& arr) {\n    int n = arr.size(), i = n - 2;\n    while (i >= 0 && arr[i] >= arr[i + 1]) i--;\n    if (i >= 0) {\n        int j = n - 1;\n        while (arr[j] <= arr[i]) j--;\n        swap(arr[i], arr[j]);\n    }\n    reverse(arr.begin() + i + 1, arr.end());\n}",
        "java": "public static void nextPermutation(int[] arr) {\n    int n = arr.length, i = n - 2;\n    while (i >= 0 && arr[i] >= arr[i + 1]) i--;\n    if (i >= 0) {\n        int j = n - 1;\n        while (arr[j] <= arr[i]) j--;\n        int t = arr[i]; arr[i] = arr[j]; arr[j] = t;\n    }\n    int left = i + 1, right = n - 1;\n    while (left < right) {\n        int t = arr[left]; arr[left] = arr[right]; arr[right] = t;\n        left++; right--;\n    }\n}"
    },
    "explanation": "Find the rightmost element arr[i] that is smaller than arr[i+1]. Find the smallest element to the right of i that is larger than arr[i], swap them. Reverse the suffix after i.",
    "algorithm": "Two Pointers",
    "timeComplexity": "O(n)",
    "spaceComplexity": "O(1)",
    "visualization": {"type": "none", "data": {}}
})

problems.append({
    "id": slug("Count Inversions"),
    "topic": "Array",
    "problem": "Count Inversion",
    "difficulty": "Hard",
    "status": "pending",
    "notes": "Modified merge sort",
    "solution": {
        "python": "def mergeSort(arr, temp, left, right):\n    mid = (left + right) // 2\n    inv_count = 0\n    if left < right:\n        inv_count += mergeSort(arr, temp, left, mid)\n        inv_count += mergeSort(arr, temp, mid + 1, right)\n        inv_count += merge(arr, temp, left, mid + 1, right)\n    return inv_count\n\ndef merge(arr, temp, left, mid, right):\n    i, j, k = left, mid, left\n    inv_count = 0\n    while i <= mid - 1 and j <= right:\n        if arr[i] <= arr[j]:\n            temp[k] = arr[i]; i += 1\n        else:\n            temp[k] = arr[j]; j += 1\n            inv_count += mid - i\n        k += 1\n    while i <= mid - 1: temp[k] = arr[i]; i += 1; k += 1\n    while j <= right: temp[k] = arr[j]; j += 1; k += 1\n    for i in range(left, right + 1): arr[i] = temp[i]\n    return inv_count\n\ndef countInversions(arr):\n    temp = [0] * len(arr)\n    return mergeSort(arr, temp, 0, len(arr) - 1)",
        "cpp": "#include <vector>\nusing namespace std;\nlong long merge(vector<int>& arr, vector<int>& temp, int left, int mid, int right) {\n    int i = left, j = mid, k = left;\n    long long inv = 0;\n    while (i < mid && j <= right) {\n        if (arr[i] <= arr[j]) temp[k++] = arr[i++];\n        else { temp[k++] = arr[j++]; inv += mid - i; }\n    }\n    while (i < mid) temp[k++] = arr[i++];\n    while (j <= right) temp[k++] = arr[j++];\n    for (i = left; i <= right; i++) arr[i] = temp[i];\n    return inv;\n}\nlong long mergeSort(vector<int>& arr, vector<int>& temp, int l, int r) {\n    long long inv = 0;\n    if (l < r) {\n        int m = (l + r) / 2;\n        inv += mergeSort(arr, temp, l, m);\n        inv += mergeSort(arr, temp, m + 1, r);\n        inv += merge(arr, temp, l, m + 1, r);\n    }\n    return inv;\n}",
        "java": "static long merge(int[] arr, int[] temp, int left, int mid, int right) {\n    int i = left, j = mid, k = left; long inv = 0;\n    while (i < mid && j <= right) {\n        if (arr[i] <= arr[j]) temp[k++] = arr[i++];\n        else { temp[k++] = arr[j++]; inv += mid - i; }\n    }\n    while (i < mid) temp[k++] = arr[i++];\n    while (j <= right) temp[k++] = arr[j++];\n    System.arraycopy(temp, left, arr, left, right - left + 1);\n    return inv;\n}\nstatic long mergeSort(int[] arr, int[] temp, int l, int r) {\n    long inv = 0;\n    if (l < r) {\n        int m = (l + r) / 2;\n        inv += mergeSort(arr, temp, l, m);\n        inv += mergeSort(arr, temp, m + 1, r);\n        inv += merge(arr, temp, l, m + 1, r);\n    }\n    return inv;\n}"
    },
    "explanation": "Modified merge sort: during merge step, when right element is smaller than left, all remaining left elements form inversions. Count them as (mid - i).",
    "algorithm": "Modified Merge Sort",
    "timeComplexity": "O(n log n)",
    "spaceComplexity": "O(n)",
    "visualization": {"type": "sorting", "data": {"array": [2, 4, 1, 3, 5], "algorithm": "merge-sort"}}
})

problems.append({
    "id": slug("Best time to Buy and Sell Stock"),
    "topic": "Array",
    "problem": "Best time to buy and Sell stock",
    "difficulty": "Easy",
    "status": "solved",
    "notes": "Track minimum price, compute max profit at each step",
    "solution": {
        "python": "def maxProfit(prices):\n    min_price = float('inf')\n    max_profit = 0\n    for price in prices:\n        min_price = min(min_price, price)\n        max_profit = max(max_profit, price - min_price)\n    return max_profit",
        "cpp": "#include <vector>\n#include <algorithm>\nusing namespace std;\nint maxProfit(vector<int>& prices) {\n    int minPrice = INT_MAX, maxProfit = 0;\n    for (int p : prices) {\n        minPrice = min(minPrice, p);\n        maxProfit = max(maxProfit, p - minPrice);\n    }\n    return maxProfit;\n}",
        "java": "public static int maxProfit(int[] prices) {\n    int minPrice = Integer.MAX_VALUE, maxProfit = 0;\n    for (int p : prices) {\n        minPrice = Math.min(minPrice, p);\n        maxProfit = Math.max(maxProfit, p - minPrice);\n    }\n    return maxProfit;\n}"
    },
    "explanation": "Track the minimum price seen so far. At each step, calculate profit if selling at current price. Return the maximum profit across all days.",
    "algorithm": "Single Pass / Greedy",
    "timeComplexity": "O(n)",
    "spaceComplexity": "O(1)",
    "visualization": {"type": "none", "data": {}}
})

problems.append({
    "id": slug("Find all pairs on integer array whose sum is equal to given number"),
    "topic": "Array",
    "problem": "find all pairs on integer array whose sum is equal to given number",
    "difficulty": "Easy",
    "status": "solved",
    "notes": "Use hash map to find complement",
    "solution": {
        "python": "def findPairs(arr, target):\n    count = 0\n    seen = {}\n    for num in arr:\n        complement = target - num\n        if complement in seen:\n            count += seen[complement]\n        seen[num] = seen.get(num, 0) + 1\n    return count",
        "cpp": "#include <vector>\n#include <unordered_map>\nusing namespace std;\nint findPairs(vector<int>& arr, int target) {\n    unordered_map<int,int> seen;\n    int count = 0;\n    for (int num : arr) {\n        int comp = target - num;\n        if (seen.count(comp)) count += seen[comp];\n        seen[num]++;\n    }\n    return count;\n}",
        "java": "public static int findPairs(int[] arr, int target) {\n    HashMap<Integer,Integer> seen = new HashMap<>();\n    int count = 0;\n    for (int num : arr) {\n        int comp = target - num;\n        if (seen.containsKey(comp)) count += seen.get(comp);\n        seen.merge(num, 1, Integer::sum);\n    }\n    return count;\n}"
    },
    "explanation": "For each element, check if its complement (target - num) exists in the hash map. If yes, add the count of that complement. Then add current element to map.",
    "algorithm": "Hash Map",
    "timeComplexity": "O(n)",
    "spaceComplexity": "O(n)",
    "visualization": {"type": "none", "data": {}}
})

problems.append({
    "id": slug("Find common elements In 3 sorted arrays"),
    "topic": "Array",
    "problem": "find common elements In 3 sorted arrays",
    "difficulty": "Easy",
    "status": "solved",
    "notes": "Three pointer approach",
    "solution": {
        "python": "def findCommon(a, b, c):\n    i, j, k = 0, 0, 0\n    result = []\n    while i < len(a) and j < len(b) and k < len(c):\n        if a[i] == b[j] == c[k]:\n            if not result or result[-1] != a[i]:\n                result.append(a[i])\n            i += 1; j += 1; k += 1\n        elif a[i] <= b[j] and a[i] <= c[k]: i += 1\n        elif b[j] <= a[i] and b[j] <= c[k]: j += 1\n        else: k += 1\n    return result",
        "cpp": "#include <vector>\nusing namespace std;\nvector<int> findCommon(vector<int>& a, vector<int>& b, vector<int>& c) {\n    int i = 0, j = 0, k = 0;\n    vector<int> res;\n    while (i < a.size() && j < b.size() && k < c.size()) {\n        if (a[i] == b[j] && b[j] == c[k]) {\n            if (res.empty() || res.back() != a[i]) res.push_back(a[i]);\n            i++; j++; k++;\n        } else if (a[i] <= b[j] && a[i] <= c[k]) i++;\n        else if (b[j] <= a[i] && b[j] <= c[k]) j++;\n        else k++;\n    }\n    return res;\n}",
        "java": "public static ArrayList<Integer> findCommon(int[] a, int[] b, int[] c) {\n    int i = 0, j = 0, k = 0;\n    ArrayList<Integer> res = new ArrayList<>();\n    while (i < a.length && j < b.length && k < c.length) {\n        if (a[i] == b[j] && b[j] == c[k]) {\n            if (res.isEmpty() || res.get(res.size()-1) != a[i]) res.add(a[i]);\n            i++; j++; k++;\n        } else if (a[i] <= b[j] && a[i] <= c[k]) i++;\n        else if (b[j] <= a[i] && b[j] <= c[k]) j++;\n        else k++;\n    }\n    return res;\n}"
    },
    "explanation": "Three pointers, one for each array. Advance the pointer pointing to the smallest value. When all three match, record the common element and advance all three.",
    "algorithm": "Three Pointers",
    "timeComplexity": "O(n1 + n2 + n3)",
    "spaceComplexity": "O(1) excluding output",
    "visualization": {"type": "none", "data": {}}
})

problems.append({
    "id": slug("Rearrange array in alternating positive and negative items"),
    "topic": "Array",
    "problem": "Rearrange the array in alternating positive and negative items with O(1) extra space",
    "difficulty": "Medium",
    "status": "solved",
    "notes": "Right rotation for misplaced elements",
    "solution": {
        "python": "def rearrange(arr):\n    outofplace = -1\n    for index in range(len(arr)):\n        if outofplace >= 0:\n            if (arr[outofplace] >= 0 and arr[index] < 0) or (arr[outofplace] < 0 and arr[index] >= 0):\n                arr[outofplace:index+1] = [arr[index]] + arr[outofplace:index] + arr[index+1:]\n                if index - outofplace >= 2:\n                    outofplace += 2\n                else:\n                    outofplace = -1\n        if outofplace == -1:\n            if (arr[index] >= 0 and index % 2 == 0) or (arr[index] < 0 and index % 2 == 1):\n                continue\n            else:\n                outofplace = index\n    return arr",
        "cpp": "#include <vector>\n#include <algorithm>\nusing namespace std;\nvoid rotate(vector<int>& arr, int start, int end) {\n    int tmp = arr[end];\n    for (int i = end; i > start; i--) arr[i] = arr[i-1];\n    arr[start] = tmp;\n}\nvoid rearrange(vector<int>& arr) {\n    int outofplace = -1;\n    for (int i = 0; i < arr.size(); i++) {\n        if (outofplace >= 0) {\n            if ((arr[outofplace] >= 0 && arr[i] < 0) || (arr[outofplace] < 0 && arr[i] >= 0)) {\n                rotate(arr, outofplace, i);\n                if (i - outofplace >= 2) outofplace += 2;\n                else outofplace = -1;\n            }\n        }\n        if (outofplace == -1) {\n            if ((arr[i] >= 0 && i % 2 == 0) || (arr[i] < 0 && i % 2 == 1)) continue;\n            else outofplace = i;\n        }\n    }\n}",
        "java": "public static void rearrange(int[] arr) {\n    int outofplace = -1;\n    for (int i = 0; i < arr.length; i++) {\n        if (outofplace >= 0) {\n            if ((arr[outofplace] >= 0 && arr[i] < 0) || (arr[outofplace] < 0 && arr[i] >= 0)) {\n                int tmp = arr[i];\n                for (int j = i; j > outofplace; j--) arr[j] = arr[j-1];\n                arr[outofplace] = tmp;\n                if (i - outofplace >= 2) outofplace += 2;\n                else outofplace = -1;\n            }\n        }\n        if (outofplace == -1) {\n            if ((arr[i] >= 0 && i % 2 == 0) || (arr[i] < 0 && i % 2 == 1)) continue;\n            else outofplace = i;\n        }\n    }\n}"
    },
    "explanation": "Find the first out-of-place element (wrong sign for its position). Right-rotate it into its correct position. Repeat until all elements are in correct alternating positions.",
    "algorithm": "Right Rotation",
    "timeComplexity": "O(n^2)",
    "spaceComplexity": "O(1)",
    "visualization": {"type": "none", "data": {}}
})

problems.append({
    "id": slug("Find if there is any subarray with sum equal to 0"),
    "topic": "Array",
    "problem": "Find if there is any subarray with sum equal to 0",
    "difficulty": "Easy",
    "status": "solved",
    "notes": "Prefix sum with hash set",
    "solution": {
        "python": "def subArrayExists(arr):\n    s = set()\n    prefix_sum = 0\n    for num in arr:\n        prefix_sum += num\n        if prefix_sum == 0 or prefix_sum in s:\n            return True\n        s.add(prefix_sum)\n    return False",
        "cpp": "#include <vector>\n#include <unordered_set>\nusing namespace std;\nbool subArrayExists(vector<int>& arr) {\n    unordered_set<int> s;\n    int prefix = 0;\n    for (int num : arr) {\n        prefix += num;\n        if (prefix == 0 || s.count(prefix)) return true;\n        s.insert(prefix);\n    }\n    return false;\n}",
        "java": "public static boolean subArrayExists(int[] arr) {\n    HashSet<Integer> s = new HashSet<>();\n    int prefix = 0;\n    for (int num : arr) {\n        prefix += num;\n        if (prefix == 0 || s.contains(prefix)) return true;\n        s.add(prefix);\n    }\n    return false;\n}"
    },
    "explanation": "Compute prefix sums. If any prefix sum repeats or equals zero, there exists a subarray with sum 0. Use a hash set for O(1) lookups.",
    "algorithm": "Prefix Sum + Hashing",
    "timeComplexity": "O(n)",
    "spaceComplexity": "O(n)",
    "visualization": {"type": "none", "data": {}}
})

problems.append({
    "id": slug("Find factorial of a large number"),
    "topic": "Array",
    "problem": "Find factorial of a large number",
    "difficulty": "Medium",
    "status": "pending",
    "notes": "Store digits in array, multiply digit by digit",
    "solution": {
        "python": "def factorial(n):\n    res = [1]\n    for x in range(2, n + 1):\n        carry = 0\n        for i in range(len(res)):\n            prod = res[i] * x + carry\n            res[i] = prod % 10\n            carry = prod // 10\n        while carry:\n            res.append(carry % 10)\n            carry //= 10\n    res.reverse()\n    return ''.join(map(str, res))",
        "cpp": "#include <string>\n#include <vector>\n#include <algorithm>\nusing namespace std;\nstring factorial(int n) {\n    vector<int> res;\n    res.push_back(1);\n    for (int x = 2; x <= n; x++) {\n        int carry = 0;\n        for (int i = 0; i < res.size(); i++) {\n            int prod = res[i] * x + carry;\n            res[i] = prod % 10;\n            carry = prod / 10;\n        }\n        while (carry) { res.push_back(carry % 10); carry /= 10; }\n    }\n    reverse(res.begin(), res.end());\n    string s;\n    for (int d : res) s += to_string(d);\n    return s;\n}",
        "java": "public static String factorial(int n) {\n    ArrayList<Integer> res = new ArrayList<>();\n    res.add(1);\n    for (int x = 2; x <= n; x++) {\n        int carry = 0;\n        for (int i = 0; i < res.size(); i++) {\n            int prod = res.get(i) * x + carry;\n            res.set(i, prod % 10);\n            carry = prod / 10;\n        }\n        while (carry > 0) { res.add(carry % 10); carry /= 10; }\n    }\n    StringBuilder sb = new StringBuilder();\n    for (int i = res.size() - 1; i >= 0; i--) sb.append(res.get(i));\n    return sb.toString();\n}"
    },
    "explanation": "Store the result as an array of digits (reverse order). Multiply each digit by the next number, handling carry. This handles arbitrarily large factorials.",
    "algorithm": "Array Digit Multiplication",
    "timeComplexity": "O(n * d) where d is digits in result",
    "spaceComplexity": "O(d)",
    "visualization": {"type": "none", "data": {}}
})

problems.append({
    "id": slug("Maximum product subarray"),
    "topic": "Array",
    "problem": "find maximum product subarray",
    "difficulty": "Medium",
    "status": "solved",
    "notes": "Track both max and min (negative can become positive)",
    "solution": {
        "python": "def maxProduct(arr):\n    n = len(arr)\n    maxVal = arr[0]\n    minVal = arr[0]\n    result = arr[0]\n    for i in range(1, n):\n        if arr[i] < 0:\n            maxVal, minVal = minVal, maxVal\n        maxVal = max(arr[i], maxVal * arr[i])\n        minVal = min(arr[i], minVal * arr[i])\n        result = max(result, maxVal)\n    return result",
        "cpp": "#include <vector>\n#include <algorithm>\nusing namespace std;\nint maxProduct(vector<int>& arr) {\n    int n = arr.size();\n    int maxVal = arr[0], minVal = arr[0], result = arr[0];\n    for (int i = 1; i < n; i++) {\n        if (arr[i] < 0) swap(maxVal, minVal);\n        maxVal = max(arr[i], maxVal * arr[i]);\n        minVal = min(arr[i], minVal * arr[i]);\n        result = max(result, maxVal);\n    }\n    return result;\n}",
        "java": "public static int maxProduct(int[] arr) {\n    int maxVal = arr[0], minVal = arr[0], result = arr[0];\n    for (int i = 1; i < arr.length; i++) {\n        if (arr[i] < 0) { int t = maxVal; maxVal = minVal; minVal = t; }\n        maxVal = Math.max(arr[i], maxVal * arr[i]);\n        minVal = Math.min(arr[i], minVal * arr[i]);\n        result = Math.max(result, maxVal);\n    }\n    return result;\n}"
    },
    "explanation": "Track both max and min product at each position (since negative*negative = positive, min can become max). Swap them when encountering negative numbers.",
    "algorithm": "Dynamic Programming (Tracking)",
    "timeComplexity": "O(n)",
    "spaceComplexity": "O(1)",
    "visualization": {"type": "none", "data": {}}
})

problems.append({
    "id": slug("Find longest consecutive subsequence"),
    "topic": "Array",
    "problem": "Find longest consecutive subsequence",
    "difficulty": "Medium",
    "status": "solved",
    "notes": "Use hash set, check if element is start of sequence",
    "solution": {
        "python": "def longestConsecutive(arr):\n    s = set(arr)\n    max_len = 0\n    for num in s:\n        if num - 1 not in s:\n            curr = num\n            curr_len = 1\n            while curr + 1 in s:\n                curr += 1\n                curr_len += 1\n            max_len = max(max_len, curr_len)\n    return max_len",
        "cpp": "#include <vector>\n#include <unordered_set>\n#include <algorithm>\nusing namespace std;\nint longestConsecutive(vector<int>& arr) {\n    unordered_set<int> s(arr.begin(), arr.end());\n    int maxLen = 0;\n    for (int num : s) {\n        if (s.find(num - 1) == s.end()) {\n            int curr = num, len = 1;\n            while (s.count(curr + 1)) { curr++; len++; }\n            maxLen = max(maxLen, len);\n        }\n    }\n    return maxLen;\n}",
        "java": "public static int longestConsecutive(int[] arr) {\n    HashSet<Integer> s = new HashSet<>();\n    for (int x : arr) s.add(x);\n    int maxLen = 0;\n    for (int num : s) {\n        if (!s.contains(num - 1)) {\n            int curr = num, len = 1;\n            while (s.contains(curr + 1)) { curr++; len++; }\n            maxLen = Math.max(maxLen, len);\n        }\n    }\n    return maxLen;\n}"
    },
    "explanation": "Add all elements to a set. For each element that is the start of a sequence (num-1 not in set), count consecutive elements. Only start counting from sequence beginnings for O(n) total.",
    "algorithm": "Hash Set",
    "timeComplexity": "O(n)",
    "spaceComplexity": "O(n)",
    "visualization": {"type": "none", "data": {}}
})

problems.append({
    "id": slug("Find elements that appear more than n/k times"),
    "topic": "Array",
    "problem": "Given an array of size n and a number k, find all elements that appear more than \" n/k \" times.",
    "difficulty": "Medium",
    "status": "solved",
    "notes": "Use dictionary to count frequencies",
    "solution": {
        "python": "def moreThanNdK(arr, k):\n    threshold = len(arr) // k\n    freq = {}\n    for num in arr:\n        freq[num] = freq.get(num, 0) + 1\n    return [num for num, count in freq.items() if count > threshold]",
        "cpp": "#include <vector>\n#include <unordered_map>\nusing namespace std;\nvector<int> moreThanNdK(vector<int>& arr, int k) {\n    int threshold = arr.size() / k;\n    unordered_map<int,int> freq;\n    for (int x : arr) freq[x]++;\n    vector<int> res;\n    for (auto& p : freq) if (p.second > threshold) res.push_back(p.first);\n    return res;\n}",
        "java": "public static ArrayList<Integer> moreThanNdK(int[] arr, int k) {\n    int threshold = arr.length / k;\n    HashMap<Integer,Integer> freq = new HashMap<>();\n    for (int x : arr) freq.merge(x, 1, Integer::sum);\n    ArrayList<Integer> res = new ArrayList<>();\n    for (var e : freq.entrySet()) if (e.getValue() > threshold) res.add(e.getKey());\n    return res;\n}"
    },
    "explanation": "Count frequencies using a hash map. Filter elements whose count exceeds n/k. Simple frequency counting approach.",
    "algorithm": "Hash Map / Frequency Counting",
    "timeComplexity": "O(n)",
    "spaceComplexity": "O(n)",
    "visualization": {"type": "none", "data": {}}
})

problems.append({
    "id": slug("Maximum profit by buying and selling a share atmost twice"),
    "topic": "Array",
    "problem": "Maximum profit by buying and selling a share atmost twice",
    "difficulty": "Hard",
    "status": "solved",
    "notes": "Track four states: first buy, first sell, second buy, second sell",
    "solution": {
        "python": "def maxProfit(prices):\n    if not prices: return 0\n    first_buy, first_sell = float('-inf'), 0\n    second_buy, second_sell = float('-inf'), 0\n    for p in prices:\n        second_sell = max(second_sell, second_buy + p)\n        second_buy = max(second_buy, first_sell - p)\n        first_sell = max(first_sell, first_buy + p)\n        first_buy = max(first_buy, -p)\n    return first_sell",
        "cpp": "#include <vector>\n#include <algorithm>\nusing namespace std;\nint maxProfit(vector<int>& prices) {\n    int fb = INT_MIN, fs = 0, sb = INT_MIN, ss = 0;\n    for (int p : prices) {\n        ss = max(ss, sb + p);\n        sb = max(sb, fs - p);\n        fs = max(fs, fb + p);\n        fb = max(fb, -p);\n    }\n    return fs;\n}",
        "java": "public static int maxProfit(int[] prices) {\n    int fb = Integer.MIN_VALUE, fs = 0, sb = Integer.MIN_VALUE, ss = 0;\n    for (int p : prices) {\n        ss = Math.max(ss, sb + p);\n        sb = Math.max(sb, fs - p);\n        fs = Math.max(fs, fb + p);\n        fb = Math.max(fb, -p);\n    }\n    return fs;\n}"
    },
    "explanation": "Track four states: first_buy, first_sell, second_buy, second_sell. At each price, update states in order: second_sell, second_buy, first_sell, first_buy. The order matters to avoid using a transaction twice.",
    "algorithm": "State Machine DP",
    "timeComplexity": "O(n)",
    "spaceComplexity": "O(1)",
    "visualization": {"type": "none", "data": {}}
})

problems.append({
    "id": slug("Find whether an array is a subset of another array"),
    "topic": "Array",
    "problem": "Find whether an array is a subset of another array",
    "difficulty": "Easy",
    "status": "solved",
    "notes": "Sort and binary search, or use hash set",
    "solution": {
        "python": "def isSubset(a, b):\n    s = set(a)\n    for x in b:\n        if x not in s:\n            return False\n    return True",
        "cpp": "#include <vector>\n#include <unordered_set>\nusing namespace std;\nbool isSubset(vector<int>& a, vector<int>& b) {\n    unordered_set<int> s(a.begin(), a.end());\n    for (int x : b) if (!s.count(x)) return false;\n    return true;\n}",
        "java": "public static boolean isSubset(int[] a, int[] b) {\n    HashSet<Integer> s = new HashSet<>();\n    for (int x : a) s.add(x);\n    for (int x : b) if (!s.contains(x)) return false;\n    return true;\n}"
    },
    "explanation": "Add all elements of the first array to a hash set. Check if every element of the second array exists in the set.",
    "algorithm": "Hash Set",
    "timeComplexity": "O(m + n)",
    "spaceComplexity": "O(m)",
    "visualization": {"type": "none", "data": {}}
})

problems.append({
    "id": slug("Find the triplet that sum to a given value"),
    "topic": "Array",
    "problem": "Find the triplet that sum to a given value",
    "difficulty": "Medium",
    "status": "solved",
    "notes": "Sort, fix one element, two-pointer for remaining two",
    "solution": {
        "python": "def findTriplet(arr, target):\n    arr.sort()\n    n = len(arr)\n    for i in range(n - 2):\n        left, right = i + 1, n - 1\n        while left < right:\n            curr_sum = arr[i] + arr[left] + arr[right]\n            if curr_sum == target:\n                return (arr[i], arr[left], arr[right])\n            elif curr_sum < target:\n                left += 1\n            else:\n                right -= 1\n    return None",
        "cpp": "#include <vector>\n#include <algorithm>\nusing namespace std;\nvector<int> findTriplet(vector<int>& arr, int target) {\n    sort(arr.begin(), arr.end());\n    for (int i = 0; i < arr.size() - 2; i++) {\n        int l = i + 1, r = arr.size() - 1;\n        while (l < r) {\n            int sum = arr[i] + arr[l] + arr[r];\n            if (sum == target) return {arr[i], arr[l], arr[r]};\n            else if (sum < target) l++;\n            else r--;\n        }\n    }\n    return {};\n}",
        "java": "public static int[] findTriplet(int[] arr, int target) {\n    Arrays.sort(arr);\n    for (int i = 0; i < arr.length - 2; i++) {\n        int l = i + 1, r = arr.length - 1;\n        while (l < r) {\n            int sum = arr[i] + arr[l] + arr[r];\n            if (sum == target) return new int[]{arr[i], arr[l], arr[r]};\n            else if (sum < target) l++;\n            else r--;\n        }\n    }\n    return new int[]{};\n}"
    },
    "explanation": "Sort the array. For each element, use two pointers (left and right) to find two elements that sum to (target - arr[i].)",
    "algorithm": "Sorting + Two Pointers",
    "timeComplexity": "O(n^2)",
    "spaceComplexity": "O(1)",
    "visualization": {"type": "none", "data": {}}
})

problems.append({
    "id": slug("Trapping Rain water problem"),
    "topic": "Array",
    "problem": "Trapping Rain water problem",
    "difficulty": "Hard",
    "status": "solved",
    "notes": "Prefix max left and suffix max right",
    "solution": {
        "python": "def trap(height):\n    n = len(height)\n    if n < 3: return 0\n    left = [0] * n\n    right = [0] * n\n    left[0] = height[0]\n    for i in range(1, n):\n        left[i] = max(left[i-1], height[i])\n    right[n-1] = height[n-1]\n    for i in range(n-2, -1, -1):\n        right[i] = max(right[i+1], height[i])\n    water = 0\n    for i in range(n):\n        water += min(left[i], right[i]) - height[i]\n    return water",
        "cpp": "#include <vector>\n#include <algorithm>\nusing namespace std;\nint trap(vector<int>& height) {\n    int n = height.size();\n    vector<int> left(n), right(n);\n    left[0] = height[0];\n    for (int i = 1; i < n; i++) left[i] = max(left[i-1], height[i]);\n    right[n-1] = height[n-1];\n    for (int i = n-2; i >= 0; i--) right[i] = max(right[i+1], height[i]);\n    int water = 0;\n    for (int i = 0; i < n; i++) water += min(left[i], right[i]) - height[i];\n    return water;\n}",
        "java": "public static int trap(int[] height) {\n    int n = height.length;\n    int[] left = new int[n], right = new int[n];\n    left[0] = height[0];\n    for (int i = 1; i < n; i++) left[i] = Math.max(left[i-1], height[i]);\n    right[n-1] = height[n-1];\n    for (int i = n-2; i >= 0; i--) right[i] = Math.max(right[i+1], height[i]);\n    int water = 0;\n    for (int i = 0; i < n; i++) water += Math.min(left[i], right[i]) - height[i];\n    return water;\n}"
    },
    "explanation": "For each position, water trapped = min(max_left, max_right) - height[i]. Precompute prefix max (left) and suffix max (right) arrays.",
    "algorithm": "Prefix/Suffix Max",
    "timeComplexity": "O(n)",
    "spaceComplexity": "O(n)",
    "visualization": {"type": "none", "data": {}}
})

problems.append({
    "id": slug("Chocolate Distribution problem"),
    "topic": "Array",
    "problem": "Chocolate Distribution problem",
    "difficulty": "Easy",
    "status": "solved",
    "notes": "Sort and find minimum difference in window of size m",
    "solution": {
        "python": "def findMinDiff(arr, m):\n    arr.sort()\n    min_diff = float('inf')\n    for i in range(m - 1, len(arr)):\n        min_diff = min(min_diff, arr[i] - arr[i - m + 1])\n    return min_diff",
        "cpp": "#include <vector>\n#include <algorithm>\n#include <climits>\nusing namespace std;\nint findMinDiff(vector<int>& arr, int m) {\n    sort(arr.begin(), arr.end());\n    int minDiff = INT_MAX;\n    for (int i = m - 1; i < arr.size(); i++)\n        minDiff = min(minDiff, arr[i] - arr[i - m + 1]);\n    return minDiff;\n}",
        "java": "public static int findMinDiff(int[] arr, int m) {\n    Arrays.sort(arr);\n    int minDiff = Integer.MAX_VALUE;\n    for (int i = m - 1; i < arr.length; i++)\n        minDiff = Math.min(minDiff, arr[i] - arr[i - m + 1]);\n    return minDiff;\n}"
    },
    "explanation": "Sort the array. The optimal distribution is m consecutive elements in sorted order. Slide a window of size m and find the minimum difference between first and last in each window.",
    "algorithm": "Sorting + Sliding Window",
    "timeComplexity": "O(n log n)",
    "spaceComplexity": "O(1)",
    "visualization": {"type": "sorting", "data": {"array": [7, 3, 2, 4, 9, 12, 56], "algorithm": "quicksort"}}
})

# I need to continue with all remaining problems...
# This script is just a starting point - I'll write a complete generation script

print(f"Partial count: {len(problems)}")
