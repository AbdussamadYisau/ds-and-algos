# def intersect(nums1, nums2):
    # # ans = []
    # nums1.sort()
    # nums2.sort()
    # # for i in range(len(nums1)):
    # #     for j in range(len(nums2)):
    # #         if nums1[i] == nums2[j]:
    # #             ans.append(nums1[i])
    # #             nums2.remove(j)
    # # ans = [x for x in nums1 if x in nums2]   
    # set1 = set(nums1)
    # set2 = set(nums2)    
                
    # return list(set1 & set2)

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