impl Solution {
    pub fn can_jump(nums: Vec<i32>) -> bool {
        let n: usize = nums.len();
        let mut lgp: usize = n - 1;
        for i in (0..=n-1).rev() {
            if i + (nums[i] as usize) >= lgp {
                lgp = i
            }
        }
        lgp == 0
    }
}
