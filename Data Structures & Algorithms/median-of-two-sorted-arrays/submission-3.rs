impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        let (a, b) = if nums1.len() < nums2.len() { 
            (&nums1[..], &nums2[..]) 
            } else { 
                (&nums2[..], &nums1[..])
                };
        let (n, m) = (a.len(), b.len());
        let total = n + m;
        let half = (total + 1) / 2;
        let (mut l, mut r) = (0, n);

        while l <= r {
            let x = l + (r - l) / 2;
            let y = half - x;
            let almax = if x > 0 { a[x-1] } else { i32::MIN };
            let blmax = if y > 0 { b[y-1] } else { i32::MIN };
            let armin = if x < n { a[x] } else { i32::MAX };
            let brmin = if y < m { b[y] } else { i32::MAX };

            if almax <= brmin && blmax <= armin {
                if total % 2 != 0 {
                    return almax.max(blmax) as f64
                } else {
                    return ((almax.max(blmax) as f64 + armin.min(brmin) as f64) / 2.0) as f64
                }
            } else {
                if almax > brmin {
                    r = x-1;
                } else {
                    l = x+1;
                }
            }
        }
        panic!("The arrays are sorted so this should never happen")
    }
}
