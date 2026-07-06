use std::collections::HashMap;
impl Solution {
    pub fn subarray_sum(nums: Vec<i32>, k: i32) -> i32 {
        let n: usize = nums.len();
        let mut count: i32 = 0;
        let mut psum: i32 = 0;
        let mut store: HashMap<i32, i32> = HashMap::new();
        store.insert(0,1);
        for num in &nums {
            psum += num;
            let diff: i32 = psum - k;
            if let Some(&freq) = store.get(&diff) {
                count += freq;
            }
            *store.entry(psum).or_insert(0) += 1;
        }
        count
    }
}
