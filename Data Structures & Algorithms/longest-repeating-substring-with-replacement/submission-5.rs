use std::cmp::max;
impl Solution {
    pub fn character_replacement(s: String, k: i32) -> i32 {
        let s_bytes = s.as_bytes(); 
        let mut counts = [0; 26]; 
        let mut max_freq = 0;
        let mut l = 0;
        let mut max_len = 0;
        for r in 0..s_bytes.len() {
            let r_idx = (s_bytes[r] - b'A') as usize;
            counts[r_idx] += 1;
            max_freq = max(max_freq, counts[r_idx]);
            if (r - l + 1) as i32 - max_freq > k {
                let l_idx = (s_bytes[l] - b'A') as usize;
                counts[l_idx] -= 1;
                l += 1;
            }
            max_len = max(max_len, (r - l + 1) as i32);
        }
        max_len
    }
}
