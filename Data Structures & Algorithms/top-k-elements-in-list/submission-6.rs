impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut k = k;
        let n: usize = nums.len();
        let mut num_as_idx_freq_as_values: Vec<i32> = vec![0; 2001];
        let mut freq_as_idx_list_as_values: Vec<Vec<i32>> = (0..(n+1)).map(|_| Vec::new()).collect();
        let mut result: Vec<i32> = Vec::new();
        for num in nums{
            let idx = num + 1000;
            num_as_idx_freq_as_values[idx as usize] += 1;
        }
        for (i,freq) in num_as_idx_freq_as_values.iter().enumerate() {
            if *freq == 0 { continue; }
            let num = (i as i32) - 1000;
            freq_as_idx_list_as_values[*freq as usize].push(num as i32);
        }
        while !freq_as_idx_list_as_values.is_empty() && k > 0 {
            let popped = freq_as_idx_list_as_values.pop();
            match popped {
                Some(values) => {
                    let diff = values.len();
                    result.extend(values);
                    k -= diff as i32;
                }
                None => ()
            };
        }
        result
    }
}
