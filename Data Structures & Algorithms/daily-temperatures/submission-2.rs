impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let n = temperatures.len();
        let mut stack = Vec::with_capacity(n);
        let mut more = vec![0; n];

        for (i, &temp) in temperatures.iter().enumerate() {
            while let Some(&last_idx) = stack.last() {
                if temp > unsafe { *temperatures.get_unchecked(last_idx) } {
                    stack.pop();
                    more[last_idx] = (i - last_idx) as i32;
                } else {
                    break;
                }
            }
            stack.push(i);
        }
        
        more
    }
}