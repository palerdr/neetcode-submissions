impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut fin: Vec<Vec<i32>>= Vec::new();
        let mut sub: Vec<i32> = Vec::new();

        fn dfs(i:usize, nums:&Vec<i32>, res: &mut Vec<Vec<i32>>, tmp: &mut Vec<i32>) {
            if i >= nums.len() {
                res.push(tmp.clone());
                return
            } else {
                tmp.push(nums[i]);
                dfs(i+1, nums, res, tmp);
                tmp.pop();
                dfs(i+1, nums, res, tmp);
                return
            }
        }
        dfs(0, &nums, &mut fin, &mut sub);
        return fin
    }
}
