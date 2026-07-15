impl Solution {
    pub fn first_missing_positive(mut nums: Vec<i32>) -> i32 {
        let n = nums.len();

        for i in 0..n {
            while nums[i] >= 1 && nums[i] <= n as i32 && nums[i] != (i + 1) as i32 {
                let target_idx = (nums[i] - 1) as usize;
                if nums[target_idx] == nums[i] {
                    break;
                }
                nums.swap(i, target_idx);
            }
        }
        for i in 0..n {
            if nums[i] != (i + 1) as i32 {
                return (i + 1) as i32;
            }
        }
        (n + 1) as i32
    }
}