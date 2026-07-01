impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let n = temperatures.len();
        let mut stack = Vec::new();
        let mut more = vec![0; n];

        for (i, &temp) in temperatures.iter().enumerate() {
            while !stack.is_empty() && temp > temperatures[stack.last().copied().unwrap()] {
                let j = stack.pop().unwrap();
                more[j] = (i-j) as i32;
            }
            stack.push(i);
        }
        return more
    }
}
