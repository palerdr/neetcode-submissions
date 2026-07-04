impl Solution {
    pub fn product_except_self(mut nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut res : Vec<i32> = vec![1; n];
        for i in 1..n {
            res[i] = res[i - 1] * nums[i - 1];
        }
        let mut postprod: i32 = 1;
        for i in (0..n).rev() {
            res[i] *= postprod;
            postprod *= nums[i];
        }
        res
    }
}
