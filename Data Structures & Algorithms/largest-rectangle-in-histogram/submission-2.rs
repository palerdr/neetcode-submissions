impl Solution {
    pub fn largest_rectangle_area(mut heights: Vec<i32>) -> i32 {
        heights.push(-1);
        let n = heights.len();
        let area = |left, right, height_idx| {
            return ((right - left + 1) as i32) * heights[height_idx]
        };
        let mut stack = Vec::with_capacity(n);
        let mut largest_area: i32 = 0;

        for i in 0..n {
            while let Some(&t) = stack.last() { 
                if heights[i] >= heights[t] {
                    break;
                }
                let j = stack.pop().unwrap();
                let l = if let Some(&prev_idx) = stack.last() {
                    prev_idx + 1
                } else {
                    0
                };
                let r = i - 1;
                largest_area = largest_area.max(area(l,r,j));
            }
            stack.push(i);
        }
        return largest_area;
    }
}
