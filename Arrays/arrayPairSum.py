# Given an integer array, output all the unique pairs that sum up to a specific value k.

# So the input:

# pair_sum([1,3,2,2],4)

# would return 2 pairs:

#  (1,3)
#  (2,2)
	

def uniqueTwoSum(arr, sum):
  ans, comp = set(), set()
  for n in arr:
    c = sum-n
    if c in comp:
      res = (n, c) if n > c else (c, n)
      if res not in ans:
        ans.add(res)
    comp.add(n)
  print(ans)
  return len(ans)





arr = [1,5,7,-1,5]
n = len(arr)
sum = 6


print(uniqueTwoSum(arr,sum))

print()
