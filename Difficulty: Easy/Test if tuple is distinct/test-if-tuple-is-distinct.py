#User function Template for python3
arr = tuple(map(int, input().split()))
r=set(arr)
if len(r)==len(arr):
    print("True")
else:
    print("False")