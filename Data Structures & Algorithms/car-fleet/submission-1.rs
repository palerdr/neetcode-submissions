impl Solution {
    pub fn car_fleet(target: i32, position: Vec<i32>, speed: Vec<i32>) -> i32 {
        let mut cars: Vec<(f64, f64)> = position.iter()
            .zip(speed.iter())
            .map(|(&p, &s)| (p as f64, s as f64))
            .collect();
        
        cars.sort_by(|a, b| b.0.partial_cmp(&a.0).unwrap());

        let mut stack: Vec<f64> = Vec::new();

        for (pos, spd) in cars.iter() {
            let ttt: f64 = (target as f64 - pos) / spd;

            if stack.is_empty() || ttt > stack.last().copied().unwrap() {
                stack.push(ttt);
            }
        }
        
        return stack.len() as i32
    }
}
