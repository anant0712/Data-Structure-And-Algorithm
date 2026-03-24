def Secondlargest(arr):
    sorted_arr=sorted(set(arr),reverse=True)
    return sorted_arr[1] if len(sorted_arr) >1 else -1


t = int(input("Enter Number of test cases:"))  # Number of test cases
for _ in range(t):
    n = int(input("Enter number of element in an array:"))  # Number of elements in array
    arr = list(map(int, input().split()))[:n]
    print(Secondlargest(arr))
#arr=[2,4,7,9,23,27,35]
#print(Secondlargest(arr))
