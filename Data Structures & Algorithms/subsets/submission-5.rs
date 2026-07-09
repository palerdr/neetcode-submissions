impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut ret = vec![];
        let mut sub = vec![];
        
        pub fn dfs(i:usize, nums: &Vec<i32>, ret: &mut Vec<Vec<i32>>, sub: &mut Vec<i32>) -> (){
            if i >= nums.len() {
                ret.push(sub.clone());
                return;
            }

            sub.push(nums[i]);
            dfs(i + 1, nums, ret, sub);
            sub.pop();
            dfs(i+1, nums, ret, sub);
            return;
        }

    dfs(0, &nums, &mut ret, &mut sub);
    return ret
    }
}
