impl Solution {
    pub fn product_except_self(mut nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut pre: Vec<i32> = Vec::with_capacity(n);
        let mut post: Vec<i32> = Vec::with_capacity(n);
        pre.push(1);
        post.push(1);
        for &num in nums.iter() {
            pre.push(num * pre.last().copied().unwrap());
        }
        for &num in nums.iter().rev() {
            post.push(num * post.last().copied().unwrap());
        }
        pre.pop();
        post.pop();
        post.reverse();
        for i in 0..n {
            nums[i] = pre[i] * post[i];
        }
        return nums
    }
}
