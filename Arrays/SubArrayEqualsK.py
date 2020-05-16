# def SubArrayEqualsK(nums,k):
#     output = 0
#     cummulativeSum = 0

    
#     for i in range(len(nums)):
#         cummulativeSum = nums[i]
#         for j in range(i+1, len(nums)):
#                        # cummulativeSum = cummulativeSum + nums[i] + nums[j]
#                        #cummulativeSum = 0
#             print(cummulativeSum,' ',output )
#             if (cummulativeSum == k):
#                     output += 1
#             cummulativeSum += nums[j]
                       
                       
#     return output
                    
    
# nums = [3,4,7,2,-3,1,4,2]
# ans = (SubArrayEqualsK(nums, 7))
# print(ans)

# Nick White - SubArray equals K

                            
# def subarraySum(nums,k):
#         d = {0:1}
#         summ = 0
#         count = 0
        
#         for i in range(len(nums)):
#             summ += nums[i]
#             if d.get(summ-k,None) is not None:
#                 count += d[summ-k]
            
#             if d.get(summ,None) is not None:
#                 d[summ] += 1
#             else:
#                 d[summ] = 1
#         return count

# nums = [3,4,7,2,-3,1,4,2]
# ans = subarraySum(nums,7)
# print(ans)