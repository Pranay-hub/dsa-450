#!/usr/bin/env python3
"""Generate complete DSA 450 problems.json"""
import json, re

def slug(name):
    s = re.sub(r'[^a-z0-9]+', '-', name.lower().strip()).strip('-')
    return s

P = []

def add(topic, problem, difficulty, status, notes, py, cpp, java, explanation, algorithm, tc, sc, viz_type="none", viz_data={}):
    P.append({
        "id": slug(problem),
        "topic": topic,
        "problem": problem,
        "difficulty": difficulty,
        "status": status,
        "notes": notes,
        "solution": {"python": py, "cpp": cpp, "java": java},
        "explanation": explanation,
        "algorithm": algorithm,
        "timeComplexity": tc,
        "spaceComplexity": sc,
        "visualization": {"type": viz_type, "data": viz_data}
    })

# ===================== ARRAYS =====================
add("Array","Reverse the array","Easy","solved","Swap first and last moving inward",
"def reverse(arr):\n    left, right = 0, len(arr)-1\n    while left < right:\n        arr[left], arr[right] = arr[right], arr[left]\n        left += 1; right -= 1\n    return arr",
"void reverse(vector<int>& arr) {\n    int l=0,r=arr.size()-1;\n    while(l<r) swap(arr[l++],arr[r--]);\n}",
"void reverse(int[] arr) {\n    int l=0,r=arr.length-1;\n    while(l<r){int t=arr[l];arr[l]=arr[r];arr[r]=t;l++;r--;}\n}",
"Two pointers swap from ends inward.","Two Pointers","O(n)","O(1)")

add("Array","Find the maximum and minimum element in an array","Easy","solved","Compare elements pairwise",
"def getMinMax(arr):\n    mn=mx=arr[0]\n    for x in arr[1:]:\n        if x<mn: mn=x\n        if x>mx: mx=x\n    return mn,mx",
"pair<int,int> getMinMax(vector<int>& a){\n    int mn=a[0],mx=a[0];\n    for(int i=1;i<a.size();i++){mn=min(mn,a[i]);mx=max(mx,a[i]);}\n    return{mn,mx};\n}",
"int[] getMinMax(int[] a){\n    int mn=a[0],mx=a[0];\n    for(int i=1;i<a.length;i++){mn=Math.min(mn,a[i]);mx=Math.max(mx,a[i]);}\n    return new int[]{mn,mx};\n}",
"Linear scan tracking min and max.","Linear Scan","O(n)","O(1)")

add("Array","Find the Kth max and min element of an array","Medium","pending","Use min-heap of size k",
"import heapq\ndef kthSmallest(arr,k):\n    h=[]\n    for x in arr:\n        heapq.heappush(h,-x)\n        if len(h)>k: heapq.heappop(h)\n    return -h[0]",
"int kthSmallest(vector<int> a,int k){\n    priority_queue<int> pq;\n    for(int x:a){pq.push(x);if(pq.size()>k)pq.pop();}\n    return pq.top();\n}",
"int kthSmallest(int[] a,int k){\n    PriorityQueue<Integer> pq=new PriorityQueue<>(Collections.reverseOrder());\n    for(int x:a){pq.offer(x);if(pq.size()>k)pq.poll();}\n    return pq.poll();\n}",
"Maintain a max-heap of size k. The root is the kth smallest.","Heap","O(n log k)","O(k)")

add("Array","Sort an array of 0s 1s and 2s","Easy","solved","Dutch National Flag",
"def sort012(arr):\n    lo,hi=0,len(arr)-1\n    mid=0\n    while mid<=hi:\n        if arr[mid]==0: arr[lo],arr[mid]=arr[mid],arr[lo];lo+=1;mid+=1\n        elif arr[mid]==1: mid+=1\n        else: arr[mid],arr[hi]=arr[hi],arr[mid];hi-=1",
"void sort012(vector<int>& a){\n    int lo=0,mi=0,hi=a.size()-1;\n    while(mi<=hi){\n        if(a[mi]==0)swap(a[lo++],a[mi++]);\n        else if(a[mi]==1)mi++;\n        else swap(a[mi],a[hi--]);\n    }\n}",
"void sort012(int[] a){\n    int lo=0,mi=0,hi=a.length-1;\n    while(mi<=hi){\n        if(a[mi]==0){int t=a[lo];a[lo]=a[mi];a[mi]=t;lo++;mi++;}\n        else if(a[mi]==1)mi++;\n        else{int t=a[mi];a[mi]=a[hi];a[hi]=t;hi--;}\n    }\n}",
"Dutch National Flag: partition into three regions using three pointers.","Dutch National Flag","O(n)","O(1)","sorting",{"array":[2,0,1,2,1,0],"algorithm":"dutch-flag"})

add("Array","Move all negative elements to one side of the array","Easy","solved","Partition like quicksort",
"def rearrange(arr):\n    j=0\n    for i in range(len(arr)):\n        if arr[i]<0: arr[i],arr[j]=arr[j],arr[i];j+=1",
"void rearrange(vector<int>& a){\n    int j=0;\n    for(int i=0;i<a.size();i++)if(a[i]<0)swap(a[i],a[j++]);\n}",
"void rearrange(int[] a){\n    int j=0;\n    for(int i=0;i<a.length;i++)if(a[i]<0){int t=a[i];a[i]=a[j];a[j]=t;j++;}\n}",
"Partition all negatives to the left using a swap pointer.","Partition","O(n)","O(1)")

add("Array","Union and Intersection of two sorted arrays","Easy","pending","Merge technique",
"def unionArrays(a,b):\n    i=j=0;r=[]\n    while i<len(a) and j<len(b):\n        if a[i]<b[j]:\n            if not r or r[-1]!=a[i]:r.append(a[i])\n            i+=1\n        elif a[i]>b[j]:\n            if not r or r[-1]!=b[j]:r.append(b[j])\n            j+=1\n        else:\n            if not r or r[-1]!=a[i]:r.append(a[i])\n            i+=1;j+=1\n    while i<len(a):\n        if not r or r[-1]!=a[i]:r.append(a[i])\n        i+=1\n    while j<len(b):\n        if not r or r[-1]!=b[j]:r.append(b[j])\n        j+=1\n    return r",
"vector<int> unionArr(vector<int>& a,vector<int>& b){\n    int i=0,j=0;vector<int>r;\n    while(i<a.size()&&j<b.size()){\n        if(a[i]<b[j]){if(r.empty()||r.back()!=a[i])r.push_back(a[i]);i++;}\n        else if(a[i]>b[j]){if(r.empty()||r.back()!=b[j])r.push_back(b[j]);j++;}\n        else{if(r.empty()||r.back()!=a[i])r.push_back(a[i]);i++;j++;}\n    }\n    while(i<a.size()){if(r.empty()||r.back()!=a[i])r.push_back(a[i]);i++;}\n    while(j<b.size()){if(r.empty()||r.back()!=b[j])r.push_back(b[j]);j++;}\n    return r;\n}",
"ArrayList<Integer> unionArr(int[] a,int[] b){\n    ArrayList<Integer>r=new ArrayList<>();\n    int i=0,j=0;\n    while(i<a.length&&j<b.length){\n        if(a[i]<b[j]){if(r.isEmpty()||r.get(r.size()-1)!=a[i])r.add(a[i]);i++;}\n        else if(a[i]>b[j]){if(r.isEmpty()||r.get(r.size()-1)!=b[j])r.add(b[j]);j++;}\n        else{if(r.isEmpty()||r.get(r.size()-1)!=a[i])r.add(a[i]);i++;j++;}\n    }\n    while(i<a.length){if(r.isEmpty()||r.get(r.size()-1)!=a[i])r.add(a[i]);i++;}\n    while(j<b.length){if(r.isEmpty()||r.get(r.size()-1)!=b[j])r.add(b[j]);j++;}\n    return r;\n}",
"Merge technique: advance pointer of smaller element, skip duplicates for union, match for intersection.","Two Pointers","O(m+n)","O(1)")

add("Array","Cyclically rotate an array by one","Easy","solved","Store last, shift right, place at front",
"def rotate(arr):\n    last=arr[-1]\n    for i in range(len(arr)-1,0,-1): arr[i]=arr[i-1]\n    arr[0]=last",
"void rotate(vector<int>& a){\n    int last=a.back();\n    for(int i=a.size()-1;i>0;i--)a[i]=a[i-1];\n    a[0]=last;\n}",
"void rotate(int[] a){\n    int last=a[a.length-1];\n    for(int i=a.length-1;i>0;i--)a[i]=a[i-1];\n    a[0]=last;\n}",
"Store last element, shift all right by 1, place stored element at index 0.","In-place Rotation","O(n)","O(1)")

add("Array","Largest sum contiguous subarray","Medium","solved","Kadane's algorithm",
"def maxSubArray(arr):\n    msf=meh=float('-inf')\n    for x in arr:\n        meh+=x\n        if msf<meh: msf=meh\n        if meh<0: meh=0\n    return msf",
"int maxSubArray(vector<int>& a){\n    int msf=INT_MIN,meh=0;\n    for(int x:a){meh+=x;msf=max(msf,meh);if(meh<0)meh=0;}\n    return msf;\n}",
"int maxSubArray(int[] a){\n    int msf=Integer.MIN_VALUE,meh=0;\n    for(int x:a){meh+=x;if(msf<meh)msf=meh;if(meh<0)meh=0;}\n    return msf;\n}",
"Kadane's: track running sum, reset to 0 when negative. Max running sum is the answer.","Kadane's Algorithm","O(n)","O(1)","dp-table",{"description":"Running max sum","rows":["meh","msf"],"cols":["index"]})

add("Array","Minimise the maximum difference between heights","Medium","solved","Sort and adjust by k",
"def getMinDiff(arr,k):\n    arr.sort()\n    ans=arr[-1]-arr[0]\n    s,b=arr[0]+k,arr[-1]-k\n    if s>b: s,b=b,s\n    for i in range(1,len(arr)-1):\n        sub=arr[i]-k\n        add=arr[i]+k\n        if sub>=s or add<=b: continue\n        if add-s<=b-sub: s=sub\n        else: b=add\n    return min(ans,b-s)",
"int getMinDiff(vector<int>& a,int k){\n    sort(a.begin(),a.end());\n    int ans=a.back()-a[0];\n    int s=a[0]+k,b=a.back()-k;\n    if(s>b)swap(s,b);\n    for(int i=1;i<a.size()-1;i++){\n        int sub=a[i]-k,add=a[i]+k;\n        if(sub>=s||add<=b)continue;\n        if(add-s<=b-sub)s=sub;else b=add;\n    }\n    return min(ans,b-s);\n}",
"int getMinDiff(int[] a,int k){\n    Arrays.sort(a);\n    int ans=a[a.length-1]-a[0];\n    int s=a[0]+k,b=a[a.length-1]-k;\n    if(s>b){int t=s;s=b;b=t;}\n    for(int i=1;i<a.length-1;i++){\n        int sub=a[i]-k,add=a[i]+k;\n        if(sub>=s||add<=b)continue;\n        if(add-s<=b-sub)s=sub;else b=add;\n    }\n    return Math.min(ans,b-s);\n}",
"Sort array. Try to minimize range by adjusting elements with +/-k toward the middle.","Sorting + Greedy","O(n log n)","O(1)")

add("Array","Minimum number of Jumps to reach end of an array","Medium","solved","Greedy: track farthest reachable",
"def minJumps(arr):\n    n=len(arr)\n    if n<=1:return 0\n    if arr[0]==0:return -1\n    j=ce=f=0\n    for i in range(n-1):\n        f=max(f,i+arr[i])\n        if i==ce:\n            j+=1;ce=f\n            if ce>=n-1:break\n    return j if ce>=n-1 else -1",
"int minJumps(vector<int>& a){\n    int n=a.size();if(n<=1)return 0;\n    if(a[0]==0)return -1;\n    int j=0,ce=0,f=0;\n    for(int i=0;i<n-1;i++){\n        f=max(f,i+a[i]);\n        if(i==ce){j++;ce=f;if(ce>=n-1)break;}\n    }\n    return ce>=n-1?j:-1;\n}",
"int minJumps(int[] a){\n    int n=a.length;if(n<=1)return 0;\n    if(a[0]==0)return -1;\n    int j=0,ce=0,f=0;\n    for(int i=0;i<n-1;i++){\n        f=Math.max(f,i+a[i]);\n        if(i==ce){j++;ce=f;if(ce>=n-1)break;}\n    }\n    return ce>=n-1?j:-1;\n}",
"Greedy: track farthest reachable. When current jump range ends, increment jumps and extend range.","Greedy","O(n)","O(1)")

add("Array","Find duplicate in an array of N+1 Integers","Medium","solved","Floyd's cycle detection",
"def findDuplicate(arr):\n    s=f=arr[0]\n    while True:\n        s=arr[s];f=arr[arr[f]]\n        if s==f:break\n    s=arr[0]\n    while s!=f: s=arr[s];f=arr[f]\n    return s",
"int findDuplicate(vector<int>& a){\n    int s=a[0],f=a[0];\n    do{s=a[s];f=a[a[f]];}while(s!=f);\n    s=a[0];while(s!=f){s=a[s];f=a[f];}\n    return s;\n}",
"int findDuplicate(int[] a){\n    int s=a[0],f=a[0];\n    do{s=a[s];f=a[a[f]];}while(s!=f);\n    s=a[0];while(s!=f){s=a[s];f=a[f];}\n    return s;\n}",
"Treat array as linked list. Find cycle using slow/fast pointers. Reset one pointer to start and advance both one step to find cycle entry (the duplicate).","Floyd's Cycle","O(n)","O(1)")

add("Array","Merge 2 sorted arrays without using Extra space","Medium","solved","Gap method",
"def merge(a,b):\n    n,m=len(a),len(b)\n    gap=(n+m+1)//2\n    while gap>0:\n        i=0\n        while i+gap<n+m:\n            j=i+gap\n            x=a[i] if i<n else b[i-n]\n            y=a[j] if j<n else b[j-n]\n            if x>y:\n                if i<n and j<n: a[i],a[j]=a[j],a[i]\n                elif i<n: a[i],b[j-n]=b[j-n],a[i]\n                else: b[i-n],b[j-n]=b[j-n],b[i-n]\n            i+=1\n        if gap==1:break\n        gap=(gap+1)//2",
"void merge(vector<int>& a,vector<int>& b){\n    int n=a.size(),m=b.size(),gap=(n+m+1)/2;\n    while(gap>0){\n        for(int i=0;i+gap<n+m;i++){\n            int j=i+gap;\n            int ai=(i<n)?a[i]:b[i-n],aj=(j<n)?a[j]:b[j-n];\n            if(ai>aj){\n                if(i<n&&j<n)swap(a[i],a[j]);\n                else if(i<n)swap(a[i],b[j-n]);\n                else swap(b[i-n],b[j-n]);\n            }\n        }\n        if(gap==1)break;gap=(gap+1)/2;\n    }\n}",
"void merge(int[] a,int[] b){\n    int n=a.length,m=b.length,gap=(n+m+1)/2;\n    while(gap>0){\n        for(int i=0;i+gap<n+m;i++){\n            int j=i+gap;\n            int ai=(i<n)?a[i]:b[i-n],aj=(j<n)?a[j]:b[j-n];\n            if(ai>aj){\n                if(i<n&&j<n){int t=a[i];a[i]=a[j];a[j]=t;}\n                else if(i<n){int t=a[i];a[i]=b[j-n];b[j-n]=t;}\n                else{int t=b[i-n];b[i-n]=b[j-n];b[j-n]=t;}\n            }\n        }\n        if(gap==1)break;gap=(gap+1)/2;\n    }\n}",
"Shell sort-like gap method: compare elements at distance gap across both arrays. Reduce gap until 1.","Gap Method","O((n+m)log(n+m))","O(1)")

add("Array","Kadane's Algo [V.V.V.V.V IMP]","Medium","solved","Kadane's with subarray bounds",
"def kadane(arr):\n    msf=meh=float('-inf')\n    start=end=s=0\n    for i,x in enumerate(arr):\n        meh+=x\n        if msf<meh: msf=meh;start=s;end=i\n        if meh<0: meh=0;s=i+1\n    return msf,start,end",
"struct Result{int sum,start,end;};\nResult kadane(vector<int>& a){\n    int msf=INT_MIN,meh=0,start=0,end=0,s=0;\n    for(int i=0;i<a.size();i++){\n        meh+=a[i];\n        if(msf<meh){msf=meh;start=s;end=i;}\n        if(meh<0){meh=0;s=i+1;}\n    }\n    return{msf,start,end};\n}",
"int[] kadane(int[] a){\n    int msf=Integer.MIN_VALUE,meh=0,start=0,end=0,s=0;\n    for(int i=0;i<a.length;i++){\n        meh+=a[i];\n        if(msf<meh){msf=meh;start=s;end=i;}\n        if(meh<0){meh=0;s=i+1;}\n    }\n    return new int[]{msf,start,end};\n}",
"Kadane's algorithm tracking start and end indices of the maximum subarray.","Kadane's Algorithm","O(n)","O(1)")

add("Array","Merge Intervals","Medium","solved","Sort by start, merge overlapping",
"def merge(intervals):\n    intervals.sort()\n    m=[intervals[0]]\n    for s,e in intervals[1:]:\n        if m[-1][1]>=s: m[-1][1]=max(m[-1][1],e)\n        else: m.append([s,e])\n    return m",
"vector<vector<int>> merge(vector<vector<int>>& a){\n    sort(a.begin(),a.end());\n    vector<vector<int>>r;int n=a.size();\n    r.push_back(a[0]);\n    for(int i=1;i<n;i++){\n        if(r.back()[1]>=a[i][0])r.back()[1]=max(r.back()[1],a[i][1]);\n        else r.push_back(a[i]);\n    }\n    return r;\n}",
"int[][] merge(int[][] a){\n    Arrays.sort(a,(x,y)->x[0]-y[0]);\n    ArrayList<int[]>r=new ArrayList<>();\n    r.add(a[0]);\n    for(int i=1;i<a.length;i++){\n        if(r.get(r.size()-1)[1]>=a[i][0])\n            r.get(r.size()-1)[1]=Math.max(r.get(r.size()-1)[1],a[i][1]);\n        else r.add(a[i]);\n    }\n    return r.toArray(new int[0][]);\n}",
"Sort by start time. Merge each interval with previous if they overlap.","Sorting + Merge","O(n log n)","O(n)")

add("Array","Next Permutation","Medium","solved","Find dip from right, swap, reverse suffix",
"def nextPermutation(arr):\n    n=len(arr)\n    i=n-2\n    while i>=0 and arr[i]>=arr[i+1]: i-=1\n    if i>=0:\n        j=n-1\n        while arr[j]<=arr[i]: j-=1\n        arr[i],arr[j]=arr[j],arr[i]\n    l,r=i+1,n-1\n    while l<r: arr[l],arr[r]=arr[r],arr[l];l+=1;r-=1",
"void nextPermutation(vector<int>& a){\n    int n=a.size(),i=n-2;\n    while(i>=0&&a[i]>=a[i+1])i--;\n    if(i>=0){int j=n-1;while(a[j]<=a[i])j--;swap(a[i],a[j]);}\n    reverse(a.begin()+i+1,a.end());\n}",
"void nextPermutation(int[] a){\n    int n=a.length,i=n-2;\n    while(i>=0&&a[i]>=a[i+1])i--;\n    if(i>=0){int j=n-1;while(a[j]<=a[i])j--;int t=a[i];a[i]=a[j];a[j]=t;}\n    int l=i+1,r=n-1;\n    while(l<r){int t=a[l];a[l]=a[r];a[r]=t;l++;r--;}\n}",
"Find rightmost decreasing element. Swap with next larger to its right. Reverse the suffix.","Two Pointers","O(n)","O(1)")

add("Array","Count Inversion","Hard","pending","Modified merge sort",
"def countInv(arr):\n    if len(arr)<=1:return arr,0\n    mid=len(arr)//2\n    l,li=countInv(arr[:mid])\n    r,ri=countInv(arr[mid:])\n    m,mi=mergeCount(l,r)\n    return m,li+ri+mi\n\ndef mergeCount(a,b):\n    res=[];i=j=inv=0\n    while i<len(a) and j<len(b):\n        if a[i]<=b[j]:res.append(a[i]);i+=1\n        else:res.append(b[j]);j+=1;inv+=len(a)-i\n    res+=a[i:]+b[j:]\n    return res,inv",
"long long merge(vector<int>& a,vector<int>& t,int l,int m,int r){\n    int i=l,j=m,k=l;long long inv=0;\n    while(i<m&&j<=r){\n        if(a[i]<=a[j])t[k++]=a[i++];\n        else{t[k++]=a[j++];inv+=m-i;}\n    }\n    while(i<m)t[k++]=a[i++];\n    while(j<=r)t[k++]=a[j++];\n    for(i=l;i<=r;i++)a[i]=t[i];\n    return inv;\n}\nlong long mergeSort(vector<int>& a,vector<int>& t,int l,int r){\n    long long inv=0;\n    if(l<r){int m=(l+r)/2;\n        inv+=mergeSort(a,t,l,m);\n        inv+=mergeSort(a,t,m+1,r);\n        inv+=merge(a,t,l,m+1,r);\n    }\n    return inv;\n}",
"long long merge(int[] a,int[] t,int l,int m,int r){\n    int i=l,j=m,k=l;long inv=0;\n    while(i<m&&j<=r){\n        if(a[i]<=a[j])t[k++]=a[i++];\n        else{t[k++]=a[j++];inv+=m-i;}\n    }\n    while(i<m)t[k++]=a[i++];\n    while(j<=r)t[k++]=a[j++];\n    System.arraycopy(t,l,a,l,r-l+1);\n    return inv;\n}\nlong mergeSort(int[] a,int[] t,int l,int r){\n    long inv=0;\n    if(l<r){int m=(l+r)/2;\n        inv+=mergeSort(a,t,l,m);inv+=mergeSort(a,t,m+1,r);\n        inv+=merge(a,t,l,m+1,r);\n    }\n    return inv;\n}",
"During merge sort's merge step, when right element is smaller than left, all remaining left elements form inversions.","Modified Merge Sort","O(n log n)","O(n)","sorting",{"array":[2,4,1,3,5],"algorithm":"merge-sort"})

add("Array","Best time to buy and Sell stock","Easy","solved","Track min price, compute max profit",
"def maxProfit(p):\n    mn=float('inf');mp=0\n    for x in p:\n        mn=min(mn,x)\n        mp=max(mp,x-mn)\n    return mp",
"int maxProfit(vector<int>& p){\n    int mn=INT_MAX,mp=0;\n    for(int x:p){mn=min(mn,x);mp=max(mp,x-mn);}\n    return mp;\n}",
"int maxProfit(int[] p){\n    int mn=Integer.MAX_VALUE,mp=0;\n    for(int x:p){mn=Math.min(mn,x);mp=Math.max(mp,x-mn);}\n    return mp;\n}",
"Track minimum price seen so far. At each day, calculate profit if selling now.","Single Pass","O(n)","O(1)")

add("Array","Find all pairs with given sum","Easy","solved","Hash map complement count",
"def countPairs(arr,k):\n    c=0;d={}\n    for x in arr:\n        c+=d.get(k-x,0)\n        d[x]=d.get(x,0)+1\n    return c",
"int countPairs(vector<int>& a,int k){\n    unordered_map<int,int>d;int c=0;\n    for(int x:a){c+=d[k-x];d[x]++;}\n    return c;\n}",
"int countPairs(int[] a,int k){\n    HashMap<Integer,Integer>d=new HashMap<>();int c=0;\n    for(int x:a){c+=d.getOrDefault(k-x,0);d.merge(x,1,Integer::sum);}\n    return c;\n}",
"For each element, check if complement exists in map and add its count.","Hash Map","O(n)","O(n)")

add("Array","Find common elements in 3 sorted arrays","Easy","solved","Three pointer merge",
"def common(a,b,c):\n    i=j=k=0;r=[]\n    while i<len(a) and j<len(b) and k<len(c):\n        if a[i]==b[j]==c[k]:\n            if not r or r[-1]!=a[i]:r.append(a[i])\n            i+=1;j+=1;k+=1\n        elif a[i]<=b[j] and a[i]<=c[k]:i+=1\n        elif b[j]<=c[k]:j+=1\n        else:k+=1\n    return r",
"vector<int> common(vector<int>& a,vector<int>& b,vector<int>& c){\n    int i=j=k=0;vector<int>r;\n    while(i<a.size()&&j<b.size()&&k<c.size()){\n        if(a[i]==b[j]&&b[j]==c[k]){\n            if(r.empty()||r.back()!=a[i])r.push_back(a[i]);\n            i++;j++;k++;\n        }else if(a[i]<=b[j]&&a[i]<=c[k])i++;\n        else if(b[j]<=c[k])j++;\n        else k++;\n    }\n    return r;\n}",
"ArrayList<Integer> common(int[] a,int[] b,int[] c){\n    int i=j=k=0;ArrayList<Integer>r=new ArrayList<>();\n    while(i<a.length&&j<b.length&&k<c.length){\n        if(a[i]==b[j]&&b[j]==c[k]){\n            if(r.isEmpty()||r.get(r.size()-1)!=a[i])r.add(a[i]);\n            i++;j++;k++;\n        }else if(a[i]<=b[j]&&a[i]<=c[k])i++;\n        else if(b[j]<=c[k])j++;\n        else k++;\n    }\n    return r;\n}",
"Three pointers advance the smallest. When all match, record and advance all.","Three Pointers","O(n1+n2+n3)","O(1)")

add("Array","Rearrange array in alternating positive and negative items","Medium","solved","Right rotation for misplaced",
"def rearrange(arr):\n    for i in range(len(arr)):\n        if i%2==0:\n            if arr[i]>=0:continue\n            else:\n                j=i+1\n                while j<len(arr) and arr[j]<0:j+=1\n                if j==len(arr):return\n                arr[i+1:j+1]=[arr[j]]+arr[i+1:j]\n        else:\n            if arr[i]<0:continue\n            else:\n                j=i+1\n                while j<len(arr) and arr[j]>=0:j+=1\n                if j==len(arr):return\n                arr[i+1:j+1]=[arr[j]]+arr[i+1:j]\n    return arr",
"void rearrange(vector<int>& a){\n    for(int i=0;i<a.size();i++){\n        if(i%2==0){if(a[i]<0){\n            int j=i+1;while(j<a.size()&&a[j]<0)j++;\n            if(j==a.size())return;\n            int t=a[j];for(int k=j;k>i;k--)a[k]=a[k-1];a[i]=t;\n        }}else{if(a[i]>=0){\n            int j=i+1;while(j<a.size()&&a[j]>=0)j++;\n            if(j==a.size())return;\n            int t=a[j];for(int k=j;k>i;k--)a[k]=a[k-1];a[i]=t;\n        }}\n    }\n}",
"void rearrange(int[] a){\n    for(int i=0;i<a.length;i++){\n        if(i%2==0){if(a[i]<0){\n            int j=i+1;while(j<a.length&&a[j]<0)j++;\n            if(j==a.length)return;\n            int t=a[j];for(int k=j;k>i;k--)a[k]=a[k-1];a[i]=t;\n        }}else{if(a[i]>=0){\n            int j=i+1;while(j<a.length&&a[j]>=0)j++;\n            if(j==a.length)return;\n            int t=a[j];for(int k=j;k>i;k--)a[k]=a[k-1];a[i]=t;\n        }}\n    }\n}",
"Find misplaced elements and right-rotate them into correct position.","Right Rotation","O(n^2)","O(1)")

add("Array","Find if there is any subarray with sum equal to 0","Easy","solved","Prefix sum + hash set",
"def hasZeroSum(arr):\n    s=set();ps=0\n    for x in arr:\n        ps+=x\n        if ps==0 or ps in s:return True\n        s.add(ps)\n    return False",
"bool hasZeroSum(vector<int>& a){\n    unordered_set<int>s;int ps=0;\n    for(int x:a){ps+=x;if(ps==0||s.count(ps))return true;s.insert(ps);}\n    return false;\n}",
"boolean hasZeroSum(int[] a){\n    HashSet<Integer>s=new HashSet<>();int ps=0;\n    for(int x:a){ps+=x;if(ps==0||s.contains(ps))return true;s.add(ps);}\n    return false;\n}",
"If prefix sum repeats or is zero, a zero-sum subarray exists.","Prefix Sum + Hashing","O(n)","O(n)")

add("Array","Find factorial of a large number","Medium","pending","Digit-by-digit array multiplication",
"def factorial(n):\n    r=[1]\n    for x in range(2,n+1):\n        c=0\n        for i in range(len(r)):\n            p=r[i]*x+c\n            r[i]=p%10;c=p//10\n        while c:r.append(c%10);c//=10\n    r.reverse()\n    return ''.join(map(str,r))",
"string factorial(int n){\n    vector<int>r;int i;\n    r.push_back(1);\n    for(int x=2;x<=n;x++){\n        int c=0;\n        for(int i=0;i<r.size();i++){int p=r[i]*x+c;r[i]=p%10;c=p/10;}\n        while(c){r.push_back(c%10);c/=10;}\n    }\n    reverse(r.begin(),r.end());\n    string s;for(int d:r)s+=to_string(d);\n    return s;\n}",
"String factorial(int n){\n    ArrayList<Integer>r=new ArrayList<>();\n    r.add(1);\n    for(int x=2;x<=n;x++){\n        int c=0;\n        for(int i=0;i<r.size();i++){int p=r.get(i)*x+c;r.set(i,p%10);c=p/10;}\n        while(c>0){r.add(c%10);c/=10;}\n    }\n    StringBuilder sb=new StringBuilder();\n    for(int i=r.size()-1;i>=0;i--)sb.append(r.get(i));\n    return sb.toString();\n}",
"Store digits in array, multiply each by next number handling carry. Reverses at end.","Array Digit Multiplication","O(n*d)","O(d)")

add("Array","Maximum product subarray","Medium","solved","Track max and min product (negatives flip)",
"def maxProd(arr):\n    mx=mn=res=arr[0]\n    for x in arr[1:]:\n        if x<0: mx,mn=mn,mx\n        mx=max(x,mx*x)\n        mn=min(x,mn*x)\n        res=max(res,mx)\n    return res",
"int maxProd(vector<int>& a){\n    int mx=a[0],mn=a[0],res=a[0];\n    for(int i=1;i<a.size();i++){\n        if(a[i]<0)swap(mx,mn);\n        mx=max(a[i],mx*a[i]);mn=min(a[i],mn*a[i]);\n        res=max(res,mx);\n    }\n    return res;\n}",
"int maxProd(int[] a){\n    int mx=a[0],mn=a[0],res=a[0];\n    for(int i=1;i<a.length;i++){\n        if(a[i]<0){int t=mx;mx=mn;mn=t;}\n        mx=Math.max(a[i],mx*a[i]);mn=Math.min(a[i],mn*a[i]);\n        res=Math.max(res,mx);\n    }\n    return res;\n}",
"Track both max and min product at each position. Swap on negative since neg*neg can be max.","DP Tracking","O(n)","O(1)")

add("Array","Find longest consecutive subsequence","Medium","solved","Hash set, only start from sequence beginnings",
"def longestCons(arr):\n    s=set(arr)\n    ml=0\n    for x in s:\n        if x-1 not in s:\n            c=1\n            while x+c in s:c+=1\n            ml=max(ml,c)\n    return ml",
"int longestCons(vector<int>& a){\n    unordered_set<int>s(a.begin(),a.end());int ml=0;\n    for(int x:s){\n        if(!s.count(x-1)){\n            int c=1;while(s.count(x+c))c++;\n            ml=max(ml,c);\n        }\n    }\n    return ml;\n}",
"int longestCons(int[] a){\n    HashSet<Integer>s=new HashSet<>();for(int x:a)s.add(x);int ml=0;\n    for(int x:s){\n        if(!s.contains(x-1)){\n            int c=1;while(s.contains(x+c))c++;\n            ml=Math.max(ml,c);\n        }\n    }\n    return ml;\n}",
"For each element that starts a sequence (num-1 not in set), count consecutive elements. O(n) total.","Hash Set","O(n)","O(n)")

add("Array","Find elements that appear more than n/k times","Medium","solved","Frequency map + filter",
"def moreThanNdK(arr,k):\n    t=len(arr)//k\n    f={}\n    for x in arr:f[x]=f.get(x,0)+1\n    return [k for k,v in f.items() if v>t]",
"vector<int> moreThanNdK(vector<int>& a,int k){\n    int t=a.size()/k;unordered_map<int,int>f;vector<int>r;\n    for(int x:a)f[x]++;\n    for(auto&p:f)if(p.second>t)r.push_back(p.first);\n    return r;\n}",
"ArrayList<Integer> moreThanNdK(int[] a,int k){\n    int t=a.length/k;HashMap<Integer,Integer>f=new HashMap<>();\n    for(int x:a)f.merge(x,1,Integer::sum);\n    ArrayList<Integer>r=new ArrayList<>();\n    for(var e:f.entrySet())if(e.getValue()>t)r.add(e.getKey());\n    return r;\n}",
"Count frequencies, filter elements exceeding n/k threshold.","Frequency Counting","O(n)","O(n)")

add("Array","Maximum profit by buying and selling a share atmost twice","Hard","solved","Four-state DP",
"def maxProfit2(p):\n    fb=fs=sb=ss=float('-inf'),0,float('-inf'),0\n    for x in p:\n        ss=max(ss,sb+x)\n        sb=max(sb,fs-x)\n        fs=max(fs,fb+x)\n        fb=max(fb,-x)\n    return fs[1]",
"int maxProfit(vector<int>& p){\n    int fb=INT_MIN,fs=0,sb=INT_MIN,ss=0;\n    for(int x:p){ss=max(ss,sb+x);sb=max(sb,fs-x);fs=max(fs,fb+x);fb=max(fb,-x);}\n    return fs;\n}",
"int maxProfit(int[] p){\n    int fb=Integer.MIN_VALUE,fs=0,sb=Integer.MIN_VALUE,ss=0;\n    for(int x:p){ss=Math.max(ss,sb+x);sb=Math.max(sb,fs-x);fs=Math.max(fs,fb+x);fb=Math.max(fb,-x);}\n    return fs;\n}",
"Track four states: first_buy, first_sell, second_buy, second_sell. Update in reverse order.","State Machine DP","O(n)","O(1)")

add("Array","Find whether an array is a subset of another array","Easy","solved","Hash set lookup",
"def isSubset(a,b):\n    s=set(a)\n    return all(x in s for x in b)",
"bool isSubset(vector<int>& a,vector<int>& b){\n    unordered_set<int>s(a.begin(),a.end());\n    for(int x:b)if(!s.count(x))return false;\n    return true;\n}",
"boolean isSubset(int[] a,int[] b){\n    HashSet<Integer>s=new HashSet<>();for(int x:a)s.add(x);\n    for(int x:b)if(!s.contains(x))return false;\n    return true;\n}",
"Add all of array1 to set, check every element of array2 exists.","Hash Set","O(m+n)","O(m)")

add("Array","Find the triplet that sum to a given value","Medium","solved","Sort + two pointer",
"def triplet(arr,t):\n    arr.sort()\n    for i in range(len(arr)-2):\n        l,r=i+1,len(arr)-1\n        while l<r:\n            s=arr[i]+arr[l]+arr[r]\n            if s==t:return(arr[i],arr[l],arr[r])\n            elif s<t:l+=1\n            else:r-=1\n    return None",
"vector<int> triplet(vector<int>& a,int t){\n    sort(a.begin(),a.end());\n    for(int i=0;i<a.size()-2;i++){\n        int l=i+1,r=a.size()-1;\n        while(l<r){\n            int s=a[i]+a[l]+a[r];\n            if(s==t)return{a[i],a[l],a[r]};\n            else if(s<t)l++;else r--;\n        }\n    }\n    return{};\n}",
"int[] triplet(int[] a,int t){\n    Arrays.sort(a);\n    for(int i=0;i<a.length-2;i++){\n        int l=i+1,r=a.length-1;\n        while(l<r){\n            int s=a[i]+a[l]+a[r];\n            if(s==t)return new int[]{a[i],a[l],a[r]};\n            else if(s<t)l++;else r--;\n        }\n    }\n    return new int[]{};\n}",
"Sort array, fix one element, use two pointers to find remaining two.","Sorting + Two Pointers","O(n^2)","O(1)")

add("Array","Trapping Rain water problem","Hard","solved","Prefix/suffix max arrays",
"def trap(h):\n    n=len(h)\n    l=[0]*n;r=[0]*n\n    l[0]=h[0]\n    for i in range(1,n):l[i]=max(l[i-1],h[i])\n    r[n-1]=h[n-1]\n    for i in range(n-2,-1,-1):r[i]=max(r[i+1],h[i])\n    return sum(min(l[i],r[i])-h[i] for i in range(n))",
"int trap(vector<int>& h){\n    int n=h.size();vector<int>l(n),r(n);\n    l[0]=h[0];for(int i=1;i<n;i++)l[i]=max(l[i-1],h[i]);\n    r[n-1]=h[n-1];for(int i=n-2;i>=0;i--)r[i]=max(r[i+1],h[i]);\n    int w=0;for(int i=0;i<n;i++)w+=min(l[i],r[i])-h[i];\n    return w;\n}",
"int trap(int[] h){\n    int n=h.length;int[]l=new int[n],r=new int[n];\n    l[0]=h[0];for(int i=1;i<n;i++)l[i]=Math.max(l[i-1],h[i]);\n    r[n-1]=h[n-1];for(int i=n-2;i>=0;i--)r[i]=Math.max(r[i+1],h[i]);\n    int w=0;for(int i=0;i<n;i++)w+=Math.min(l[i],r[i])-h[i];\n    return w;\n}",
"Water at position i = min(max_left, max_right) - height[i]. Precompute prefix/suffix max.","Prefix/Suffix Max","O(n)","O(n)")

add("Array","Chocolate Distribution problem","Easy","solved","Sort + sliding window of size m",
"def chocDist(arr,m):\n    arr.sort()\n    d=float('inf')\n    for i in range(m-1,len(arr)):\n        d=min(d,arr[i]-arr[i-m+1])\n    return d",
"int chocDist(vector<int>& a,int m){\n    sort(a.begin(),a.end());int d=INT_MAX;\n    for(int i=m-1;i<a.size();i++)d=min(d,a[i]-a[i-m+1]);\n    return d;\n}",
"int chocDist(int[] a,int m){\n    Arrays.sort(a);int d=Integer.MAX_VALUE;\n    for(int i=m-1;i<a.length;i++)d=Math.min(d,a[i]-a[i-m+1]);\n    return d;\n}",
"Sort array, slide window of size m, find minimum difference between first and last in window.","Sorting + Sliding Window","O(n log n)","O(1)","sorting",{"array":[7,3,2,4,9,12,56],"algorithm":"quicksort"})

# ===================== MATRIX (10) =====================
add("Matrix","Spirally traverse a matrix","Medium","solved","Four boundary pointers",
"def spiral(mat):\n    if not mat:return[]\n    t,b,l,r=0,len(mat)-1,0,len(mat[0])-1\n    res=[]\n    while t<=b and l<=r:\n        for i in range(l,r+1):res.append(mat[t][i])\n        t+=1\n        for i in range(t,b+1):res.append(mat[i][r])\n        r-=1\n        if t<=b:\n            for i in range(r,l-1,-1):res.append(mat[b][i])\n            b-=1\n        if l<=r:\n            for i in range(b,t-1,-1):res.append(mat[i][l])\n            l+=1\n    return res",
"vector<int> spiral(vector<vector<int>>& m){\n    if(m.empty())return{};\n    int t=0,b=m.size()-1,l=0,r=m[0].size()-1;\n    vector<int>res;\n    while(t<=b&&l<=r){\n        for(int i=l;i<=r;i++)res.push_back(m[t][i]);t++;\n        for(int i=t;i<=b;i++)res.push_back(m[i][r]);r--;\n        if(t<=b){for(int i=r;i>=l;i--)res.push_back(m[b][i]);b--;}\n        if(l<=r){for(int i=b;i>=t;i--)res.push_back(m[i][l]);l++;}\n    }\n    return res;\n}",
"ArrayList<Integer> spiral(int[][] m){\n    ArrayList<Integer>r=new ArrayList<>();\n    int t=0,b=m.length-1,l=0,r=m[0].length-1;\n    while(t<=b&&l<=r){\n        for(int i=l;i<=r;i++)r.add(m[t][i]);t++;\n        for(int i=t;i<=b;i++)r.add(m[i][r]);r--;\n        if(t<=b){for(int i=r;i>=l;i--)r.add(m[b][i]);b--;}\n        if(l<=r){for(int i=b;i>=t;i--)r.add(m[i][l]);l++;}\n    }\n    return r;\n}",
"Maintain four boundaries (top,bottom,left,right). Traverse in order: right, down, left, up, shrinking boundaries.","Four Pointers","O(m*n)","O(1)","none",{})

add("Matrix","Search an element in a matrix","Medium","solved","Binary search treating 2D as 1D",
"def searchMatrix(mat,t):\n    if not mat:return False\n    m,n=len(mat),len(mat[0])\n    lo,hi=0,m*n-1\n    while lo<=hi:\n        mid=(lo+hi)//2\n        v=mat[mid//n][mid%n]\n        if v==t:return True\n        elif v<t:lo=mid+1\n        else:hi=mid-1\n    return False",
"bool searchMatrix(vector<vector<int>>& m,int t){\n    if(m.empty())return false;\n    int r=m.size(),c=m[0].size();\n    int lo=0,hi=r*c-1;\n    while(lo<=hi){\n        int mid=(lo+hi)/2;int v=m[mid/c][mid%c];\n        if(v==t)return true;else if(v<t)lo=mid+1;else hi=mid-1;\n    }\n    return false;\n}",
"boolean searchMatrix(int[][] m,int t){\n    int r=m.length,c=m[0].length;\n    int lo=0,hi=r*c-1;\n    while(lo<=hi){\n        int mid=(lo+hi)/2;int v=m[mid/c][mid%c];\n        if(v==t)return true;else if(v<t)lo=mid+1;else hi=mid-1;\n    }\n    return false;\n}",
"Flatten 2D matrix into virtual 1D and binary search. Map index back to row/col.","Binary Search","O(log(m*n))","O(1)","none",{})

add("Matrix","Median in a row-wise sorted Matrix","Hard","solved","Binary search on answer range",
"def countLess(mat,x):\n    c=0\n    for row in mat:\n        lo,hi=0,len(row)-1\n        while lo<=hi:\n            mid=(lo+hi)//2\n            if row[mid]<=x:lo=mid+1\n            else:hi=mid-1\n        c+=lo\n    return c\n\ndef median(mat):\n    r,c=len(mat),len(mat[0])\n    lo,hi=0,2000\n    while lo<hi:\n        mid=(lo+hi)//2\n        if countLess(mat,mid)<(r*c+1)//2:lo=mid+1\n        else:hi=mid\n    return lo",
"int countLess(vector<vector<int>>& m,int x){\n    int c=0;for(auto&r:m){\n        int lo=0,hi=r.size()-1;\n        while(lo<=hi){int mid=(lo+hi)/2;if(r[mid]<=x)lo=mid+1;else hi=mid-1;}\n        c+=lo;\n    }\n    return c;\n}\nint median(vector<vector<int>>& m){\n    int r=m.size(),c=m[0].size();int lo=0,hi=2000;\n    while(lo<hi){\n        int mid=(lo+hi)/2;\n        if(countLess(m,mid)<(r*c+1)/2)lo=mid+1;else hi=mid;\n    }\n    return lo;\n}",
"int countLess(int[][] m,int x){\n    int c=0;for(int[]r:m){\n        int lo=0,hi=r.length-1;\n        while(lo<=hi){int mid=(lo+hi)/2;if(r[mid]<=x)lo=mid+1;else hi=mid-1;}\n        c+=lo;\n    }\n    return c;\n}\nint median(int[][] m){\n    int r=m.length,c=m[0].length;int lo=0,hi=2000;\n    while(lo<hi){\n        int mid=(lo+hi)/2;\n        if(countLess(m,mid)<(r*c+1)/2)lo=mid+1;else hi=mid;\n    }\n    return lo;\n}",
"Binary search on answer range [0,2000]. Count elements <= mid. Adjust search based on count vs (m*n+1)/2.","Binary Search on Answer","O(32*m*logn)","O(1)","none",{})

add("Matrix","Row with max 1s","Easy","solved","Start from top-right, move left on 1, down on 0",
"def maxOnes(mat):\n    r,c=len(mat),len(mat[0])\n    i,j=0,c-1\n    best=-1\n    while i<r and j>=0:\n        if mat[i][j]==1:\n            best=i;j-=1\n        else:i+=1\n    return best",
"int maxOnes(vector<vector<int>>& m){\n    int r=m.size(),c=m[0].size();\n    int i=0,j=c-1,best=-1;\n    while(i<r&&j>=0){\n        if(m[i][j]==1){best=i;j--;}\n        else i++;\n    }\n    return best;\n}",
"int maxOnes(int[][] m){\n    int r=m.length,c=m[0].length;\n    int i=0,j=c-1,best=-1;\n    while(i<r&&j>=0){\n        if(m[i][j]==1){best=i;j--;}\n        else i++;\n    }\n    return best;\n}",
"Start from top-right corner. Move left when seeing 1, move down when seeing 0.","Staircase Search","O(m+n)","O(1)","none",{})

add("Matrix","Print elements in sorted order from a row-column wise sorted matrix","Medium","solved","Min-heap of size k (number of columns)",
"import heapq\ndef sortedMatrix(mat):\n    r,c=len(mat),len(mat[0])\n    h=[(mat[i][0],i,0) for i in range(r)]\n    heapq.heapify(h)\n    res=[]\n    while h:\n        v,i,j=heapq.heappop(h)\n        res.append(v)\n        if j+1<c: heapq.heappush(h,(mat[i][j+1],i,j+1))\n    return res",
"vector<int> sortedMatrix(vector<vector<int>>& m){\n    priority_queue<tuple<int,int,int>,vector<tuple<int,int,int>>,greater<>>pq;\n    int r=m.size(),c=m[0].size();\n    for(int i=0;i<r;i++)pq.push({m[i][0],i,0});\n    vector<int>res;\n    while(!pq.empty()){\n        auto[v,i,j]=pq.top();pq.pop();\n        res.push_back(v);\n        if(j+1<c)pq.push({m[i][j+1],i,j+1});\n    }\n    return res;\n}",
"ArrayList<Integer> sortedMatrix(int[][] m){\n    PriorityQueue<int[]>pq=new PriorityQueue<>((a,b)->a[0]-b[0]);\n    int r=m.length,c=m[0].length;\n    for(int i=0;i<r;i++)pq.offer(new int[]{m[i][0],i,0});\n    ArrayList<Integer>res=new ArrayList<>();\n    while(!pq.isEmpty()){\n        int[]cur=pq.poll();\n        res.add(cur[0]);\n        if(cur[2]+1<c)pq.offer(new int[]{m[cur[1]][cur[2]+1],cur[1],cur[2]+1});\n    }\n    return res;\n}",
"Min-heap with first element of each row. Pop smallest, push next element from same row.","Min Heap","O(r*c*logr)","O(r)","none",{})

add("Matrix","Find a specific pair in matrix","Medium","solved","Suffix max matrix then find max diff",
"def findPair(mat):\n    r,c=len(mat),len(mat[0])\n    mx=[[0]*c for _ in range(r)]\n    mx[r-1][c-1]=mat[r-1][c-1]\n    for j in range(c-2,-1,-1):mx[r-1][j]=max(mat[r-1][j],mx[r-1][j+1])\n    for i in range(r-2,-1,-1):mx[i][c-1]=max(mat[i][c-1],mx[i+1][c-1])\n    for i in range(r-2,-1,-1):\n        for j in range(c-2,-1,-1):\n            mx[i][j]=max(mat[i][j],mx[i+1][j],mx[i][j+1])\n    ans=float('-inf')\n    for i in range(r-1):\n        for j in range(c-1):\n            ans=max(ans,mx[i+1][j+1]-mat[i][j])\n    return ans",
"int findPair(vector<vector<int>>& m){\n    int r=m.size(),c=m[0].size();\n    vector<vector<int>>mx(r,vector<int>(c));\n    mx[r-1][c-1]=m[r-1][c-1];\n    for(int j=c-2;j>=0;j--)mx[r-1][j]=max(m[r-1][j],mx[r-1][j+1]);\n    for(int i=r-2;i>=0;i--)mx[i][c-1]=max(m[i][c-1],mx[i+1][c-1]);\n    for(int i=r-2;i>=0;i--)for(int j=c-2;j>=0;j--)\n        mx[i][j]=max({m[i][j],mx[i+1][j],mx[i][j+1]});\n    int ans=INT_MIN;\n    for(int i=0;i<r-1;i++)for(int j=0;j<c-1;j++)\n        ans=max(ans,mx[i+1][j+1]-m[i][j]);\n    return ans;\n}",
"int findPair(int[][] m){\n    int r=m.length,c=m[0].length;int[][]mx=new int[r][c];\n    mx[r-1][c-1]=m[r-1][c-1];\n    for(int j=c-2;j>=0;j--)mx[r-1][j]=Math.max(m[r-1][j],mx[r-1][j+1]);\n    for(int i=r-2;i>=0;i--)mx[i][c-1]=Math.max(m[i][c-1],mx[i+1][c-1]);\n    for(int i=r-2;i>=0;i--)for(int j=c-2;j>=0;j--)\n        mx[i][j]=Math.max(m[i][j],Math.max(mx[i+1][j],mx[i][j+1]));\n    int ans=Integer.MIN_VALUE;\n    for(int i=0;i<r-1;i++)for(int j=0;j<c-1;j++)\n        ans=Math.max(ans,mx[i+1][j+1]-m[i][j]);\n    return ans;\n}",
"Build suffix max matrix from bottom-right. Then find max(mat[j]-mat[i]) where j is strictly after i.","Suffix Max","O(m*n)","O(m*n)","none",{})

add("Matrix","Rotate matrix by 90 degrees","Medium","solved","Transpose then reverse each row",
"def rotate90(mat):\n    n=len(mat)\n    for i in range(n):\n        for j in range(i,n):\n            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]\n    for row in mat:row.reverse()\n    return mat",
"void rotate90(vector<vector<int>>& m){\n    int n=m.size();\n    for(int i=0;i<n;i++)for(int j=i;j<n;j++)swap(m[i][j],m[j][i]);\n    for(int i=0;i<n;i++)reverse(m[i].begin(),m[i].end());\n}",
"void rotate90(int[][] m){\n    int n=m.length;\n    for(int i=0;i<n;i++)for(int j=i;j<n;j++){int t=m[i][j];m[i][j]=m[j][i];m[j][i]=t;}\n    for(int i=0;i<n;i++){int l=0,r=n-1;while(l<r){int t=m[i][l];m[i][l]=m[i][r];m[i][r]=t;l++;r--;}}\n}",
"Transpose the matrix (swap [i][j] with [j][i]), then reverse each row.","Transpose + Reverse","O(n^2)","O(1)","none",{})

add("Matrix","Kth smallest element in a row-column wise sorted matrix","Medium","solved","Binary search on answer",
"def countLe(mat,x):\n    c=0\n    for row in mat:\n        lo,hi=0,len(row)-1\n        while lo<=hi:\n            mid=(lo+hi)//2\n            if row[mid]<=x:lo=mid+1\n            else:hi=mid-1\n        c+=lo\n    return c\n\ndef kthSmallest(mat,k):\n    r,c=len(mat),len(mat[0])\n    lo,hi=mat[0][0],mat[-1][-1]\n    while lo<hi:\n        mid=(lo+hi)//2\n        if countLe(mat,mid)<k:lo=mid+1\n        else:hi=mid\n    return lo",
"int kthSmallest(vector<vector<int>>& m,int k){\n    int r=m.size(),c=m[0].size();\n    int lo=m[0][0],hi=m[r-1][c-1];\n    while(lo<hi){\n        int mid=(lo+hi)/2,cnt=0;\n        for(auto&row:m){\n            int l=0,h=row.size()-1;\n            while(l<=h){int md=(l+h)/2;if(row[md]<=mid)l=md+1;else h=md-1;}\n            cnt+=l;\n        }\n        if(cnt<k)lo=mid+1;else hi=mid;\n    }\n    return lo;\n}",
"int kthSmallest(int[][] m,int k){\n    int r=m.length,c=m[0].length;\n    int lo=m[0][0],hi=m[r-1][c-1];\n    while(lo<hi){\n        int mid=(lo+hi)/2,cnt=0;\n        for(int[]row:m){\n            int l=0,h=row.length-1;\n            while(l<=h){int md=(l+h)/2;if(row[md]<=mid)l=md+1;else h=md-1;}\n            cnt+=l;\n        }\n        if(cnt<k)lo=mid+1;else hi=mid;\n    }\n    return lo;\n}",
"Binary search on value range. Count elements <= mid. Adjust search based on count vs k.","Binary Search","O(log(MAX)*m*logn)","O(1)","none",{})

add("Matrix","Common elements in all rows of a given matrix","Medium","solved","Hash map with row counts",
"def commonElements(mat):\n    r,c=len(mat),len(mat[0])\n    d={}\n    for i in range(r):\n        for j in range(c):\n            d[mat[i][j]]=d.get(mat[i][j],0)+1\n    res=[]\n    for k,v in d.items():\n        if v==r:res.append(k)\n    return res",
"vector<int> commonElements(vector<vector<int>>& m){\n    int r=m.size(),c=m[0].size();\n    unordered_map<int,int>d;vector<int>res;\n    for(int i=0;i<r;i++)for(int j=0;j;j++)d[m[i][j]]++;\n    for(auto&p:d)if(p.second==r)res.push_back(p.first);\n    return res;\n}",
"ArrayList<Integer> commonElements(int[][] m){\n    int r=m.length,c=m[0].length;\n    HashMap<Integer,Integer>d=new HashMap<>();\n    for(int i=0;i<r;i++)for(int j=0;j<c;j++)d.merge(m[i][j],1,Integer::sum);\n    ArrayList<Integer>res=new ArrayList<>();\n    for(var e:d.entrySet())if(e.getValue()==r)res.add(e.getKey());\n    return res;\n}",
"Count occurrences of each element across all rows. Elements appearing in all rows are common.","Hash Map","O(m*n)","O(m*n)","none",{})

# ===================== STRINGS (43) =====================
add("String","Reverse a String","Easy","solved","Two pointer swap",
"def reverse(s):\n    s=list(s)\n    l,r=0,len(s)-1\n    while l<r:s[l],s[r]=s[r],s[l];l+=1;r-=1\n    return ''.join(s)",
"string reverse(string s){\n    int l=0,r=s.size()-1;\n    while(l<r)swap(s[l++],s[r--]);\n    return s;\n}",
"static String reverse(String s){\n    char[]a=s.toCharArray();\n    int l=0,r=a.length-1;\n    while(l<r){char t=a[l];a[l]=a[r];a[r]=t;l++;r--;}\n    return new String(a);\n}",
"Two pointers swap from ends.","Two Pointers","O(n)","O(1)","none",{})

add("String","Check whether a String is Palindrome","Easy","solved","Two pointer comparison",
"def isPalin(s):\n    l,r=0,len(s)-1\n    while l<r:\n        if s[l]!=s[r]:return False\n        l+=1;r-=1\n    return True",
"bool isPalin(string s){\n    int l=0,r=s.size()-1;\n    while(l<r)if(s[l++]!=s[r--])return false;\n    return true;\n}",
"static boolean isPalin(String s){\n    int l=0,r=s.length()-1;\n    while(l<r)if(s.charAt(l++)!=s.charAt(r--))return false;\n    return true;\n}",
"Compare characters from both ends moving inward.","Two Pointers","O(n)","O(1)","none",{})

add("String","Find Duplicate Characters in a string","Easy","solved","Frequency count",
"def findDup(s):\n    d={}\n    for c in s:d[c]=d.get(c,0)+1\n    return {k:v for k,v in d.items() if v>1}",
"map<char,int> findDup(string s){\n    map<char,int>d;\n    for(char c:s)d[c]++;\n    map<char,int>r;\n    for(auto&p:d)if(p.second>1)r[p.first]=p.second;\n    return r;\n}",
"static HashMap<Character,Integer> findDup(String s){\n    HashMap<Character,Integer>d=new HashMap<>();\n    for(char c:s.toCharArray())d.merge(c,1,Integer::sum);\n    HashMap<Character,Integer>r=new HashMap<>();\n    for(var e:d.entrySet())if(e.getValue()>1)r.put(e.getKey(),e.getValue());\n    return r;\n}",
"Count character frequencies using a map, filter those with count > 1.","Frequency Count","O(n)","O(k) where k is charset","none",{})

add("String","Write a program to print all permutations of a given string","Medium","solved","Backtracking with swap",
"def permute(s,l,r):\n    if l==r:print(''.join(s))\n    else:\n        for i in range(l,r+1):\n            s[l],s[i]=s[i],s[l]\n            permute(s,l+1,r)\n            s[l],s[i]=s[i],s[l]",
"void permute(string&s,int l,int r){\n    if(l==r)cout<<s<<endl;\n    else{for(int i=l;i<=r;i++){\n        swap(s[l],s[i]);permute(s,l+1,r);swap(s[l],s[i]);\n    }}\n}",
"static void permute(char[] s,int l,int r){\n    if(l==r)System.out.println(new String(s));\n    else{for(int i=l;i<=r;i++){\n        char t=s[l];s[l]=s[i];s[i]=t;\n        permute(s,l+1,r);\n        t=s[l];s[l]=s[i];s[i]=t;\n    }}\n}",
"Backtracking: swap each character with current position, recurse on remaining, backtrack.","Backtracking","O(n*n!)","O(n)","none",{})

add("String","Check if two strings are anagrams","Easy","solved","Character frequency comparison",
"def areAnagram(a,b):\n    if len(a)!=len(b):return False\n    d={}\n    for c in a:d[c]=d.get(c,0)+1\n    for c in b:d[c]=d.get(c,0)-1\n    return all(v==0 for v in d.values())",
"bool areAnagram(string a,string b){\n    if(a.size()!=b.size())return false;\n    int d[256]={0};\n    for(char c:a)d[c]++;for(char c:b)d[c]--;\n    for(int i=0;i<256;i++)if(d[i]!=0)return false;\n    return true;\n}",
"static boolean areAnagram(String a,String b){\n    if(a.length()!=b.length())return false;\n    int[]d=new int[256];\n    for(char c:a.toCharArray())d[c]++;for(char c:b.toCharArray())d[c]--;\n    for(int x:d)if(x!=0)return false;\n    return true;\n}",
"Count characters in both strings. If all counts match, they are anagrams.","Frequency Count","O(n)","O(1) fixed charset","none",{})

add("String","Count and Say problem","Medium","solved","Iterative run-length encoding",
"def countAndSay(n):\n    s='1'\n    for _ in range(1,n):\n        res='';c=1\n        for i in range(1,len(s)):\n            if s[i]==s[i-1]:c+=1\n            else:res+=str(c)+s[i-1];c=1\n        res+=str(c)+s[-1]\n        s=res\n    return s",
"string countAndSay(int n){\n    string s=\"1\";\n    for(int i=1;i<n;i++){\n        string r=\"\";int c=1;\n        for(int j=1;j<s.size();j++){\n            if(s[j]==s[j-1])c++;\n            else{r+=to_string(c)+s[j-1];c=1;}\n        }\n        r+=to_string(c)+s.back();s=r;\n    }\n    return s;\n}",
"static String countAndSay(int n){\n    String s=\"1\";\n    for(int i=1;i<n;i++){\n        StringBuilder r=new StringBuilder();int c=1;\n        for(int j=1;j<s.length();j++){\n            if(s.charAt(j)==s.charAt(j-1))c++;\n            else{r.append(c).append(s.charAt(j-1));c=1;}\n        }\n        r.append(c).append(s.charAt(s.length()-1));s=r.toString();\n    }\n    return s;\n}",
"Iteratively build result by reading previous string as groups of same characters (count + digit).","Run-Length Encoding","O(n*m)","O(m)","none",{})

add("String","Longest Palindromic Substring","Hard","solved","Expand around center",
"def longestPalin(s):\n    n=len(s)\n    start,maxl=0,1\n    def expand(l,r):\n        while l>=0 and r<n and s[l]==s[r]:l-=1;r+=1\n        return r-l-1\n    for i in range(n):\n        l1=expand(i,i)\n        l2=expand(i,i+1)\n        ml=max(l1,l2)\n        if ml>maxl:maxl=ml;start=i-ml//2\n    return s[start:start+maxl]",
"string longestPalin(string s){\n    int n=s.size(),start=0,maxl=1;\n    auto expand=[&](int l,int r){\n        while(l>=0&&r<n&&s[l]==s[r]){l--;r++;}\n        return r-l-1;\n    };\n    for(int i=0;i<n;i++){\n        int l1=expand(i,i),l2=expand(i,i+1);\n        int ml=max(l1,l2);\n        if(ml>maxl){maxl=ml;start=i-ml/2;}\n    }\n    return s.substr(start,maxl);\n}",
"static String longestPalin(String s){\n    int n=s.length(),start=0,maxl=1;\n    for(int i=0;i<n;i++){\n        int l1=expand(s,i,i),l2=expand(s,i,i+1);\n        int ml=Math.max(l1,l2);\n        if(ml>maxl){maxl=ml;start=i-ml/2;}\n    }\n    return s.substring(start,start+maxl);\n}\nstatic int expand(String s,int l,int r){\n    while(l>=0&&r<s.length()&&s.charAt(l)==s.charAt(r)){l--;r++;}\n    return r-l-1;\n}",
"For each index, expand outward checking for odd and even length palindromes.","Expand Around Center","O(n^2)","O(1)","none",{})

add("String","Longest Repeating Subsequence","Medium","solved","LCS with i!=j constraint",
"def lrs(s):\n    n=len(s)\n    dp=[[0]*(n+1) for _ in range(n+1)]\n    for i in range(1,n+1):\n        for j in range(1,n+1):\n            if s[i-1]==s[j-1] and i!=j:\n                dp[i][j]=dp[i-1][j-1]+1\n            else:dp[i][j]=max(dp[i-1][j],dp[i][j-1])\n    return dp[n][n]",
"int lrs(string s){\n    int n=s.size();vector<vector<int>>dp(n+1,vector<int>(n+1,0));\n    for(int i=1;i<=n;i++)for(int j=1;j<=n;j++){\n        if(s[i-1]==s[j-1]&&i!=j)dp[i][j]=dp[i-1][j-1]+1;\n        else dp[i][j]=max(dp[i-1][j],dp[i][j-1]);\n    }\n    return dp[n][n];\n}",
"static int lrs(String s){\n    int n=s.length();int[][]dp=new int[n+1][n+1];\n    for(int i=1;i<=n;i++)for(int j=1;j<=n;j++){\n        if(s.charAt(i-1)==s.charAt(j-1)&&i!=j)dp[i][j]=dp[i-1][j-1]+1;\n        else dp[i][j]=Math.max(dp[i-1][j],dp[i][j-1]);\n    }\n    return dp[n][n];\n}",
"Modified LCS: find longest subsequence that appears twice with different indices (i!=j).","2D DP","O(n^2)","O(n^2)","dp-table",{"description":"LCS table with i!=j constraint","rows":["char"],"cols":["char"]})

add("String","Longest Common Substring","Medium","solved","2D DP tracking max length",
"def lcs(a,b):\n    m,n=len(a),len(b)\n    dp=[[0]*(n+1) for _ in range(m+1)]\n    ml=0\n    for i in range(1,m+1):\n        for j in range(1,n+1):\n            if a[i-1]==b[j-1]:\n                dp[i][j]=dp[i-1][j-1]+1\n                ml=max(ml,dp[i][j])\n    return ml",
"int lcs(string a,string b){\n    int m=a.size(),n=b.size(),ml=0;\n    vector<vector<int>>dp(m+1,vector<int>(n+1,0));\n    for(int i=1;i<=m;i++)for(int j=1;j<=n;j++){\n        if(a[i-1]==b[j-1]){dp[i][j]=dp[i-1][j-1]+1;ml=max(ml,dp[i][j]);}\n    }\n    return ml;\n}",
"static int lcs(String a,String b){\n    int m=a.length(),n=b.length(),ml=0;int[][]dp=new int[m+1][n+1];\n    for(int i=1;i<=m;i++)for(int j=1;j<=n;j++){\n        if(a.charAt(i-1)==b.charAt(j-1)){dp[i][j]=dp[i-1][j-1]+1;ml=Math.max(ml,dp[i][j]);}\n    }\n    return ml;\n}",
"2D DP: dp[i][j] = length of longest common substring ending at a[i-1] and b[j-1]. Reset to 0 on mismatch.","2D DP","O(m*n)","O(m*n)","dp-table",{"description":"Common substring lengths","rows":["string A chars"],"cols":["string B chars"]})

add("String","Word Break Problem","Hard","solved","DP + dictionary lookup",
"def wordBreak(s,wordDict):\n    wd=set(wordDict)\n    n=len(s)\n    dp=[False]*(n+1)\n    dp[0]=True\n    for i in range(1,n+1):\n        for j in range(i):\n            if dp[j] and s[j:i] in wd:\n                dp[i]=True;break\n    return dp[n]",
"bool wordBreak(string s,vector<string>& wd){\n    unordered_set<string>dict(wd.begin(),wd.end());\n    int n=s.size();vector<bool>dp(n+1,false);dp[0]=true;\n    for(int i=1;i<=n;i++)for(int j=0;j<i;j++){\n        if(dp[j]&&dict.count(s.substr(j,i-j))){dp[i]=true;break;}\n    }\n    return dp[n];\n}",
"static boolean wordBreak(String s,String[] wd){\n    HashSet<String>dict=new HashSet<>(Arrays.asList(wd));\n    int n=s.length();boolean[]dp=new boolean[n+1];dp[0]=true;\n    for(int i=1;i<=n;i++)for(int j=0;j<i;j++){\n        if(dp[j]&&dict.contains(s.substring(j,i))){dp[i]=true;break;}\n    }\n    return dp[n];\n}",
"dp[i] = can we segment s[0:i] using dictionary words. Check all possible splits.","1D DP","O(n^2)","O(n)","dp-table",{"description":"Can s[0:i] be segmented","rows":["True/False"],"cols":["index"]})

add("String","Minimum number of swaps to make strings equal","Easy","solved","Count mismatch pairs",
"def minSwaps(s1,s2):\n    xy=yx=0\n    for a,b in zip(s1,s2):\n        if a=='x' and b=='y':xy+=1\n        elif a=='y' and b=='x':yx+=1\n    return (xy+1)//2+(yx+1)//2 if (xy+yx)%2==0 else -1",
"int minSwaps(string s1,string s2){\n    int xy=0,yx=0;\n    for(int i=0;i<s1.size();i++){\n        if(s1[i]=='x'&&s2[i]=='y')xy++;\n        else if(s1[i]=='y'&&s2[i]=='x')yx++;\n    }\n    if((xy+yx)%2!=0)return -1;\n    return xy/2+yx/2+xy%2+yx%2;\n}",
"static int minSwaps(String s1,String s2){\n    int xy=0,yx=0;\n    for(int i=0;i<s1.length();i++){\n        if(s1.charAt(i)=='x'&&s2.charAt(i)=='y')xy++;\n        else if(s1.charAt(i)=='y'&&s2.charAt(i)=='x')yx++;\n    }\n    if((xy+yx)%2!=0)return -1;\n    return xy/2+yx/2+xy%2+yx%2;\n}",
"Count 'x'/'y' and 'y'/'x' mismatches. Same-type mismatches need 1 swap each (pairs). Different types need 1 swap per pair.","Greedy","O(n)","O(1)","none",{})

add("String","Check if strings are rotations of each other","Easy","solved","Concatenate and check substring",
"def areRotation(a,b):\n    return len(a)==len(b) and b in a+a",
"bool areRotation(string a,string b){\n    return a.size()==b.size()&&(a+a).find(b)!=string::npos;\n}",
"static boolean areRotation(String a,String b){\n    return a.length()==b.length()&&(a+a).contains(b);\n}",
"If b is a rotation of a, then b must be a substring of a+a.","String Matching","O(n)","O(n)","none",{})

add("String","Longest Prefix Suffix (KMP LPS)","Medium","solved","Compute LPS array",
"def computeLPS(pat):\n    n=len(pat)\n    lps=[0]*n\n    length=0;i=1\n    while i<n:\n        if pat[i]==pat[length]:\n            length+=1;lps[i]=length;i+=1\n        else:\n            if length!=0:length=lps[length-1]\n            else:lps[i]=0;i+=1\n    return lps",
"vector<int> computeLPS(string pat){\n    int n=pat.size(),len=0;\n    vector<int>lps(n,0);int i=1;\n    while(i<n){\n        if(pat[i]==pat[len]){lps[i++]=++len;}\n        else{if(len!=0)len=lps[len-1];else lps[i++]=0;}\n    }\n    return lps;\n}",
"static int[] computeLPS(String pat){\n    int n=pat.length(),len=0;int[]lps=new int[n];int i=1;\n    while(i<n){\n        if(pat.charAt(i)==pat.charAt(len)){lps[i++]=++len;}\n        else{if(len!=0)len=lps[len-1];else lps[i++]=0;}\n    }\n    return lps;\n}",
"Build LPS array by comparing prefix with suffix. On mismatch, fall back to previous LPS value.","KMP Pattern","O(n)","O(n)","none",{})

add("String","Roman Number to Integer","Easy","solved","Right to left, add or subtract",
"def romanToInt(s):\n    d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}\n    r=d[s[-1]]\n    for i in range(len(s)-2,-1,-1):\n        if d[s[i]]<d[s[i+1]]:r-=d[s[i]]\n        else:r+=d[s[i]]\n    return r",
"int romanToInt(string s){\n    unordered_map<char,int>d={{'I',1},{'V',5},{'X',10},{'L',50},{'C',100},{'D',500},{'M',1000}};\n    int r=d[s.back()];\n    for(int i=s.size()-2;i>=0;i--){\n        if(d[s[i]]<d[s[i+1]])r-=d[s[i]];else r+=d[s[i]];\n    }\n    return r;\n}",
"static int romanToInt(String s){\n    HashMap<Character,Integer>d=new HashMap<>();\n    d.put('I',1);d.put('V',5);d.put('X',10);d.put('L',50);d.put('C',100);d.put('D',500);d.put('M',1000);\n    int r=d.get(s.charAt(s.length()-1));\n    for(int i=s.length()-2;i>=0;i--){\n        if(d.get(s.charAt(i))<d.get(s.charAt(i+1)))r-=d.get(s.charAt(i));else r+=d.get(s.charAt(i));\n    }\n    return r;\n}",
"Traverse right to left. Add value if current >= next, subtract otherwise.","Linear Scan","O(n)","O(1)","none",{})

add("String","Longest Common Prefix","Easy","solved","Vertical scanning",
"def longestCommonPrefix(strs):\n    if not strs:return ''\n    for i in range(len(strs[0])):\n        c=strs[0][i]\n        for s in strs[1:]:\n            if i>=len(s) or s[i]!=c:return strs[0][:i]\n    return strs[0]",
"string longestCommonPrefix(vector<string>& strs){\n    if(strs.empty())return \"\";\n    for(int i=0;i<strs[0].size();i++){\n        char c=strs[0][i];\n        for(int j=1;j<strs.size();j++)\n            if(i>=strs[j].size()||strs[j][i]!=c)return strs[0].substr(0,i);\n    }\n    return strs[0];\n}",
"static String longestCommonPrefix(String[] strs){\n    if(strs.length==0)return \"\";\n    for(int i=0;i<strs[0].length();i++){\n        char c=strs[0].charAt(i);\n        for(int j=1;j<strs.length;j++)\n            if(i>=strs[j].length()||strs[j].charAt(i)!=c)return strs[0].substring(0,i);\n    }\n    return strs[0];\n}",
"Compare character at position i across all strings. Stop when mismatch found.","Vertical Scan","O(S) total chars","O(1)","none",{})

add("String","Rabin-Karp Algorithm","Medium","solved","Rolling hash pattern matching",
"def rabinKarp(text,pat):\n    n,m=len(text),len(pat)\n    d,q=256,101\n    h=pow(d,m-1)%q\n    p=t=0\n    res=[]\n    for i in range(m):\n        p=(d*p+ord(pat[i]))%q\n        t=(d*t+ord(text[i]))%q\n    for i in range(n-m+1):\n        if p==t:\n            if text[i:i+m]==pat:res.append(i)\n        if i<n-m:\n            t=(d*(t-ord(text[i])*h)+ord(text[i+m]))%q\n    return res",
"vector<int> rabinKarp(string text,string pat){\n    int n=text.size(),m=pat.size(),d=256,q=101;\n    int h=(int)pow(d,m-1)%q,p=0,t=0;vector<int>res;\n    for(int i=0;i<m;i++){p=(d*p+pat[i])%q;t=(d*t+text[i])%q;}\n    for(int i=0;i<=n-m;i++){\n        if(p==t&&text.substr(i,m)==pat)res.push_back(i);\n        if(i<n-m){t=(d*(t-text[i]*h)+text[i+m])%q;if(t<0)t+=q;}\n    }\n    return res;\n}",
"static ArrayList<Integer> rabinKarp(String text,String pat){\n    int n=text.length(),m=pat.length(),d=256,q=101;\n    int h=(int)Math.pow(d,m-1)%q,p=0,t=0;ArrayList<Integer>res=new ArrayList<>();\n    for(int i=0;i<m;i++){p=(d*p+pat.charAt(i))%q;t=(d*t+text.charAt(i))%q;}\n    for(int i=0;i<=n-m;i++){\n        if(p==t&&text.substring(i,i+m).equals(pat))res.add(i);\n        if(i<n-m){t=(d*(t-text.charAt(i)*h)+text.charAt(i+m))%q;if(t<0)t+=q;}\n    }\n    return res;\n}",
"Compute hash of pattern and sliding window. Match hash first, then verify characters on hash hit.","Rolling Hash","O(n+m) average","O(1)","none",{})

add("String","Check if a string is subsequence of another","Easy","solved","Two pointer",
"def isSubsequence(s,t):\n    i=j=0\n    while i<len(s) and j<len(t):\n        if s[i]==t[j]:i+=1\n        j+=1\n    return i==len(s)",
"bool isSubsequence(string s,string t){\n    int i=0,j=0;\n    while(i<s.size()&&j<t.size()){\n        if(s[i]==t[j])i++;\n        j++;\n    }\n    return i==s.size();\n}",
"static boolean isSubsequence(String s,String t){\n    int i=0,j=0;\n    while(i<s.length()&&j<t.length()){\n        if(s.charAt(i)==t.charAt(j))i++;\n        j++;\n    }\n    return i==s.length();\n}",
"Two pointers: advance first pointer only on match. If first pointer reaches end, s is subsequence.","Two Pointers","O(n)","O(1)","none",{})

add("String","Edit Distance","Hard","solved","2D DP on two strings",
"def editDist(a,b):\n    m,n=len(a),len(b)\n    dp=[[0]*(n+1) for _ in range(m+1)]\n    for i in range(m+1):dp[i][0]=i\n    for j in range(n+1):dp[0][j]=j\n    for i in range(1,m+1):\n        for j in range(1,n+1):\n            if a[i-1]==b[j-1]:dp[i][j]=dp[i-1][j-1]\n            else:dp[i][j]=1+min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])\n    return dp[m][n]",
"int editDist(string a,string b){\n    int m=a.size(),n=b.size();\n    vector<vector<int>>dp(m+1,vector<int>(n+1));\n    for(int i=0;i<=m;i++)dp[i][0]=i;\n    for(int j=0;j<=n;j++)dp[0][j]=j;\n    for(int i=1;i<=m;i++)for(int j=1;j<=n;j++){\n        if(a[i-1]==b[j-1])dp[i][j]=dp[i-1][j-1];\n        else dp[i][j]=1+min({dp[i][j-1],dp[i-1][j],dp[i-1][j-1]});\n    }\n    return dp[m][n];\n}",
"static int editDist(String a,String b){\n    int m=a.length(),n=b.length();int[][]dp=new int[m+1][n+1];\n    for(int i=0;i<=m;i++)dp[i][0]=i;\n    for(int j=0;j<=n;j++)dp[0][j]=j;\n    for(int i=1;i<=m;i++)for(int j=1;j<=n;j++){\n        if(a.charAt(i-1)==b.charAt(j-1))dp[i][j]=dp[i-1][j-1];\n        else dp[i][j]=1+Math.min(dp[i][j-1],Math.min(dp[i-1][j],dp[i-1][j-1]));\n    }\n    return dp[m][n];\n}",
"dp[i][j] = min operations to convert a[0:i] to b[0:j]. Options: insert, delete, replace.","2D DP","O(m*n)","O(m*n)","dp-table",{"description":"Edit distance table","rows":["string A"],"cols":["string B"]})

add("String","Find next greater number with same set of digits","Medium","solved","Next permutation approach",
"def nextGreater(n):\n    s=list(str(n))\n    i=len(s)-2\n    while i>=0 and s[i]>=s[i+1]:i-=1\n    if i<0:return -1\n    j=len(s)-1\n    while s[j]<=s[i]:j-=1\n    s[i],s[j]=s[j],s[i]\n    s[i+1:]=reversed(s[i+1:])\n    return int(''.join(s))\nimport re",
"int nextGreater(int n){\n    string s=to_string(n);int i=s.size()-2;\n    while(i>=0&&s[i]>=s[i+1])i--;\n    if(i<0)return -1;\n    int j=s.size()-1;while(s[j]<=s[i])j--;\n    swap(s[i],s[j]);\n    reverse(s.begin()+i+1,s.end());\n    int r=stoll(s);\n    return r>INT_MAX?-1:r;\n}",
"static long nextGreater(int n){\n    char[]s=Long.toString(n).toCharArray();int i=s.length-2;\n    while(i>=0&&s[i]>=s[i+1])i--;\n    if(i<0)return -1;\n    int j=s.length-1;while(s[j]<=s[i])j--;\n    char t=s[i];s[i]=s[j];s[j]=t;\n    int l=i+1,r=s.length-1;\n    while(l<r){t=s[l];s[l]=s[r];s[r]=t;l++;r--;}\n    long val=Long.parseLong(new String(s));\n    return val>Integer.MAX_VALUE?-1:val;\n}",
"Apply next permutation algorithm on the digit array of the number.","Two Pointers","O(d) d=digits","O(d)","none",{})

add("String","Minimum Window Substring","Hard","solved","Sliding window with character count",
"def minWindow(s,t):\n    from collections import Counter\n    need=Counter(t)\n    missing=len(t)\n    start=0,end=0,best=(0,float('inf'))\n    for i,c in enumerate(s):\n        if need[c]>0:missing-=1\n        need[c]-=1\n        while missing==0:\n            if i-start<best[1]-best[0]:best=(start,i)\n            need[s[start]]+=1\n            if need[s[start]]>0:missing+=1\n            start+=1\n    return s[best[0]:best[1]+1] if best[1]!=float('inf') else ''",
"string minWindow(string s,string t){\n    vector<int>need(128,0);\n    for(char c:t)need[c]++;\n    int missing=t.size(),start=0,bestStart=0,bestLen=INT_MAX;\n    for(int i=0;i<s.size();i++){\n        if(--need[s[i]]>=0)missing--;\n        while(missing==0){\n            if(i-start<bestLen){bestStart=start;bestLen=i-start;}\n            if(++need[s[start++]]>0)missing++;\n        }\n    }\n    return bestLen==INT_MAX?\"\":s.substr(bestStart,bestLen);\n}",
"static String minWindow(String s,String t){\n    int[]need=new int[128];\n    for(char c:t.toCharArray())need[c]++;\n    int missing=t.length(),start=0,bestStart=0,bestLen=Integer.MAX_VALUE;\n    for(int i=0;i<s.length();i++){\n        if(--need[s.charAt(i)]>=0)missing--;\n        while(missing==0){\n            if(i-start<bestLen){bestStart=start;bestLen=i-start;}\n            if(++need[s.charAt(start++)]>0)missing++;\n        }\n    }\n    return bestLen==Integer.MAX_VALUE?\"\":s.substring(bestStart,bestStart+bestLen);\n}",
"Sliding window: expand right to include all chars of t, shrink left to find minimum window.","Sliding Window","O(n)","O(1) charset","none",{})

# Remaining strings...
add("String","Longest Substring Without Repeating Characters","Medium","solved","Sliding window + hash set",
"def longestUnique(s):\n    d={};ml=0;st=0\n    for i,c in enumerate(s):\n        if c in d and d[c]>=st:st=d[c]+1\n        d[c]=i;ml=max(ml,i-st+1)\n    return ml",
"int longestUnique(string s){\n    unordered_map<char,int>d;int ml=0,st=0;\n    for(int i=0;i<s.size();i++){\n        if(d.count(s[i])&&d[s[i]]>=st)st=d[s[i]]+1;\n        d[s[i]]=i;ml=max(ml,i-st+1);\n    }\n    return ml;\n}",
"static int longestUnique(String s){\n    HashMap<Character,Integer>d=new HashMap<>();int ml=0,st=0;\n    for(int i=0;i<s.length();i++){\n        if(d.containsKey(s.charAt(i))&&d.get(s.charAt(i))>=st)st=d.get(s.charAt(i))+1;\n        d.put(s.charAt(i),i);ml=Math.max(ml,i-st+1);\n    }\n    return ml;\n}",
"Sliding window with map. On repeat, jump start past last occurrence.","Sliding Window + Hash Map","O(n)","O(min(n,charset))","none",{})

add("String","Count palindromic subsequence of length k","Hard","solved","3D DP",
"def countPalSubseq(s,k):\n    n=len(s)\n    dp=[[[0]*(k+1) for _ in range(n)] for _ in range(n)]\n    for i in range(n):dp[i][i][1]=1\n    for length in range(2,n+1):\n        for i in range(n-length+1):\n            j=i+length-1\n            if s[i]==s[j]:\n                for l in range(1,k+1):dp[i][j][l]+=dp[i+1][j-1][l-1]\n            for l in range(1,k+1):dp[i][j][l]+=dp[i+1][j][l]+dp[i][j-1][l]-dp[i+1][j-1][l]\n    return dp[0][n-1][k]",
"int countPalSubseq(string s,int k){\n    int n=s.size();\n    vector<vector<vector<int>>>dp(n,vector<vector<int>>(n,vector<int>(k+1,0)));\n    for(int i=0;i<n;i++)dp[i][i][1]=1;\n    for(int len=2;len<=n;len++)for(int i=0;i<=n-len;i++){\n        int j=i+len-1;\n        if(s[i]==s[j])for(int l=1;l<=k;l++)dp[i][j][l]+=dp[i+1][j-1][l-1];\n        for(int l=1;l<=k;l++)dp[i][j][l]+=dp[i+1][j][l]+dp[i][j-1][l]-dp[i+1][j-1][l];\n    }\n    return dp[0][n-1][k];\n}",
"static int countPalSubseq(String s,int k){\n    int n=s.length();\n    int[][][]dp=new int[n][n][k+1];\n    for(int i=0;i<n;i++)dp[i][i][1]=1;\n    for(int len=2;len<=n;len++)for(int i=0;i<=n-len;i++){\n        int j=i+len-1;\n        if(s.charAt(i)==s.charAt(j))for(int l=1;l<=k;l++)dp[i][j][l]+=dp[i+1][j-1][l-1];\n        for(int l=1;l<=k;l++)dp[i][j][l]+=dp[i+1][j][l]+dp[i][j-1][l]-dp[i+1][j-1][l];\n    }\n    return dp[0][n-1][k];\n}",
"3D DP: dp[i][j][l] = count of palindromic subsequences of length l in s[i:j].","3D DP","O(n^2*k)","O(n^2*k)","dp-table",{"description":"3D DP table for palindromic subsequence count","rows":["start index"],"cols":["end index"]})

add("String","String to Integer (atoi)","Medium","solved","Parse with state handling",
"def myAtoi(s):\n    s=s.lstrip()\n    if not s:return 0\n    sign=-1 if s[0]=='-' else 1\n    if s[0] in '+-':s=s[1:]\n    res=0\n    for c in s:\n        if not c.isdigit():break\n        res=res*10+int(c)\n        if res*sign>2**31-1:return 2**31-1\n        if res*sign<-2**31:return -2**31\n    return res*sign",
"int myAtoi(string s){\n    int i=0,n=s.size(),sign=1;\n    while(i<n&&s[i]==' ')i++;\n    if(i<n&&(s[i]=='+'||s[i]=='-')){sign=(s[i]=='-')?-1:1;i++;}\n    long res=0;\n    while(i<n&&isdigit(s[i])){\n        res=res*10+(s[i]-'0');\n        if(res*sign>INT_MAX)return INT_MAX;\n        if(res*sign<INT_MIN)return INT_MIN;\n        i++;\n    }\n    return res*sign;\n}",
"static int myAtoi(String s){\n    int i=0,n=s.length(),sign=1;\n    while(i<n&&s.charAt(i)==' ')i++;\n    if(i<n&&(s.charAt(i)=='+'||s.charAt(i)=='-')){sign=(s.charAt(i)=='-')?-1:1;i++;}\n    long res=0;\n    while(i<n&&Character.isDigit(s.charAt(i))){\n        res=res*10+(s.charAt(i)-'0');\n        if(res*sign>Integer.MAX_VALUE)return Integer.MAX_VALUE;\n        if(res*sign<Integer.MIN_VALUE)return Integer.MIN_VALUE;\n        i++;\n    }\n    return(int)(res*sign);\n}",
"Skip whitespace, handle sign, parse digits one by one, clamp to 32-bit integer range.","Linear Parse","O(n)","O(1)","none",{})

add("String","Implement Strstr()","Easy","solved","KMP algorithm",
"def strStr(haystack,needle):\n    if not needle:return 0\n    n,m=len(haystack),len(needle)\n    lps=[0]*m\n    length,i=0,1\n    while i<m:\n        if needle[i]==needle[length]:length+=1;lps[i]=length;i+=1\n        else:\n            if length!=0:length=lps[length-1]\n            else:lps[i]=0;i+=1\n    i=j=0\n    while i<n:\n        if haystack[i]==needle[j]:i+=1;j+=1\n        if j==m:return i-j\n        elif i<n and haystack[i]!=needle[j]:\n            if j!=0:j=lps[j-1]\n            else:i+=1\n    return -1",
"int strStr(string h,string p){\n    int n=h.size(),m=p.size();\n    vector<int>lps(m,0);\n    for(int i=1,len=0;i<m;){\n        if(p[i]==p[len])lps[i++]=++len;\n        else if(len)len=lps[len-1];\n        else lps[i++]=0;\n    }\n    for(int i=0,j=0;i<n;){\n        if(h[i]==p[j]){i++;j++;}\n        if(j==m)return i-j;\n        if(i<n&&h[i]!=p[j]){if(j)j=lps[j-1];else i++;}\n    }\n    return -1;\n}",
"static int strStr(String h,String p){\n    int n=h.length(),m=p.length();int[]lps=new int[m];\n    for(int i=1,len=0;i<m;){\n        if(p.charAt(i)==p.charAt(len))lps[i++]=++len;\n        else if(len>0)len=lps[len-1];\n        else lps[i++]=0;\n    }\n    for(int i=0,j=0;i<n;){\n        if(h.charAt(i)==p.charAt(j)){i++;j++;}\n        if(j==m)return i-j;\n        if(i<n&&h.charAt(i)!=p.charAt(j)){if(j>0)j=lps[j-1];else i++;}\n    }\n    return -1;\n}",
"KMP pattern matching with LPS array for efficient skip on mismatch.","KMP","O(n+m)","O(m)","none",{})

add("String","KMP Algorithm for pattern searching","Medium","solved","Same as strStr but returns all positions",
"def kmpSearch(text,pat):\n    n,m=len(text),len(pat)\n    lps=[0]*m\n    length,i=0,1\n    while i<m:\n        if pat[i]==pat[length]:length+=1;lps[i]=length;i+=1\n        else:\n            if length!=0:length=lps[length-1]\n            else:lps[i]=0;i+=1\n    res=[]\ni=j=0\n    while i<n:\n        if text[i]==pat[j]:i+=1;j+=1\n        if j==m:res.append(i-j);j=lps[j-1]\n        elif i<n and text[i]!=pat[j]:\n            if j!=0:j=lps[j-1]\n            else:i+=1\n    return res",
"vector<int> kmpSearch(string t,string p){\n    int n=t.size(),m=p.size();\n    vector<int>lps(m,0);\n    for(int i=1,len=0;i<m;){\n        if(p[i]==p[len])lps[i++]=++len;\n        else if(len)len=lps[len-1];else lps[i++]=0;\n    }\n    vector<int>res;\n    for(int i=0,j=0;i<n;){\n        if(t[i]==p[j]){i++;j++;}\n        if(j==m){res.push_back(i-j);j=lps[j-1];}\n        if(i<n&&t[i]!=p[j]){if(j)j=lps[j-1];else i++;}\n    }\n    return res;\n}",
"static ArrayList<Integer> kmpSearch(String t,String p){\n    int n=t.length(),m=p.length();int[]lps=new int[m];\n    for(int i=1,len=0;i<m;){\n        if(p.charAt(i)==p.charAt(len))lps[i++]=++len;\n        else if(len>0)len=lps[len-1];else lps[i++]=0;\n    }\n    ArrayList<Integer>res=new ArrayList<>();\n    for(int i=0,j=0;i<n;){\n        if(t.charAt(i)==p.charAt(j)){i++;j++;}\n        if(j==m){res.add(i-j);j=lps[j-1];}\n        if(i<n&&t.charAt(i)!=p.charAt(j)){if(j>0)j=lps[j-1];else i++;}\n    }\n    return res;\n}",
"Build LPS array for pattern, then scan text using LPS for efficient backtracking.","KMP","O(n+m)","O(m)","none",{})

# I need to continue with ALL remaining problems...
# Let me generate the rest programmatically from the spreadsheet data
print(f"Manually defined: {len(P)} problems")
