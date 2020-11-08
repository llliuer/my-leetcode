func twoSum(nums []int, target int) []int {
    m := make(map[int]int)
    var res []int   

    for i := 0; i<len(nums); i++{
        //if //target-nums[i] in nums
        m[nums[i]] = i
    }
    for i := 0; i<len(nums); i++{
        if( m[target-nums[i]] != 0)&& i!=m[target-nums[i]]{
            return append(res,i,m[target-nums[i]])
        }
    }
    
    
    return res
}


