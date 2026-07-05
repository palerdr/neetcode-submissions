impl Solution {
    pub fn can_jump(nums: Vec<i32>) -> bool {
        let n:usize = nums.len();
        if n <= 1 {true}
        else{
            let mut k:usize = 0;
            while nums[k] != 0 {
                let jump:usize = nums[k] as usize;
                if k + jump >= n - 1 {return true} 
                let mut br:usize = 0;
                let mut bri:usize = 0;
                for idx in k+1..k+jump+1 {
                    let reach:usize = idx + (nums[idx] as usize);
                    if reach > br {
                        br = reach;
                        bri = idx;
                    }
                }
                k = bri;
            }
            return false
        }
    }
}
