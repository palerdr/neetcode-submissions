use std::collections::HashMap;

impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        let mut store: HashMap<i32, i32> = HashMap::new();
        let mut longest_cons: i32 = 0;
        for &num in nums.iter() {
            if store.contains_key(&num){
                continue
            } else {
            let lt: i32 = store.get(&(num-1)).copied().unwrap_or(0);
            let rt: i32 = store.get(&(num+1)).copied().unwrap_or(0);
            let tot: i32 = lt + rt + 1;
            longest_cons = max(longest_cons, tot);
            store.insert(num, tot);
            store.insert(num-lt, tot);
            store.insert(num+rt, tot);
            }
        }
        longest_cons
    }
}
