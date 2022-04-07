 # nums = [1,2,3,4]
 # pre_product = [1, 1, 2, 6], pre_prod = 1
 # post_product = [24, 12, 4, 1], post_prod = 1
 # res = [24, 12, 8, 6]
 # element-wise multiplication of the two lists


def prod_array(nums):
    n = len(nums)
    res = [1] * n
    
    # update the res with the pre product for each num
    pre_prod = 1 # initiate first pre product value
    for i in range(n):
        res[i] = pre_prod
        pre_prod *= nums[i]

    # update the res with the post product for each num
    post_prod = 1 # initiate first post product value
    for i in reversed(range(n)):
        res[i] *= post_prod
        post_prod *= nums[i]

    return res


# nums = [1,2,3,4]
nums = [-1,1,0,-3,3] # [0, 0, 9, 0, 0]
print(prod_array(nums))
         
