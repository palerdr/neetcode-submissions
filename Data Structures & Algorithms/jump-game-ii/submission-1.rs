impl Solution {
    pub fn jump(nums: Vec<i32>) -> i32 {
        let n : usize = nums.len();
        if n <= 1 {
            0
        } else {
        let mut jumps : i32 = 0;
        let mut current_jump_end : usize = 0;
        let mut farthest : usize = 0;
        for i in 0..n-1 {
            farthest = max(farthest, i + (nums[i] as usize));
            if i == current_jump_end {
                jumps += 1;
                current_jump_end = farthest;
                if current_jump_end >= n - 1 {
                    break;
                }
            }
        }
        jumps
        }}
}
