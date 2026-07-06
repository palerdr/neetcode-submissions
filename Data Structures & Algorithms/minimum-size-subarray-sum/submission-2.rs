impl Solution {
    pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
        let n: usize = nums.len();
        let mut msss: i32 = i32::MAX;
        let mut cs: i32 = 0;

        let mut l: usize = 0;
        for r in 0..n {
            let num: i32 = nums[r];
            cs += num;
            while cs >= target {
                msss = min(msss, (r-l+1) as i32);
                cs -= nums[l];
                l += 1;
            }
        }
        if msss == i32::MAX {0} else {msss}
    }
}
