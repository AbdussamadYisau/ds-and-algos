def intersect(nums1, nums2):
    i = 0
    j = 0
    
    result = []

    nums1.sort()
    nums2.sort()

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
            
        else:
            j += 1
    return result

nums1 = [1,2,2,1] # [1,1,2,2]
nums2 = [2,2]

print(intersect(nums1,nums2))