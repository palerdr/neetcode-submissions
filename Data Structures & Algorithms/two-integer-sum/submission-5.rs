use std::collections::HashMap;
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut store = HashMap::new();
        let n = nums.len();

        for (i, &num) in nums.iter().enumerate() {
            let diff = target - num;

            if let Some(&prev_index) = store.get(&diff) {
                return  vec![prev_index, i as i32]
            }
            else{
                store.insert(num, i as i32);
            }
        }
        vec![]
}
}
