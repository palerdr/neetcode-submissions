impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let n = nums.len();
        let tot = 1 << n;
        let mut fin = Vec::with_capacity(tot);

        for mask in 0..tot {
            let mut sub = Vec::new();

            for j in 0..n {
                if ((mask & 1 << j)) != 0 {
                    sub.push(nums[j]);
                }
            }
            fin.push(sub);
        }
        return fin
    }
}
