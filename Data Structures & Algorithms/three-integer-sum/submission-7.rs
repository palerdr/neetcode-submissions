impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut sols = Vec::new();
        let len = nums.len();
        
        // 1. Guard rail for inputs smaller than a triplet
        if len < 3 { return sols; }
        
        nums.sort_unstable(); // Faster than sort() because it doesn't preserve original order of equal elements

        for i in 0..len - 2 {
            let num = nums[i];

            // 2. Pruning: If the smallest number is > 0, a sum of 0 is impossible
            if num > 0 { break; }

            // 3. Skip duplicates for the first element
            if i > 0 && num == nums[i - 1] { continue; }

            // 4. Pruning: If nums[i] plus the two largest numbers is < 0, nums[i] is too small
            if num + nums[len - 1] + nums[len - 2] < 0 { continue; }

            // 5. Pruning: If nums[i] plus the next two numbers is > 0, nums[i] is too large
            if num + nums[i + 1] + nums[i + 2] > 0 { break; }

            let mut l = i + 1;
            let mut r = len - 1;

            while l < r {
                // Using unsafe indexing avoids Rust's internal bounds-checking overhead
                let left_val = unsafe { *nums.get_unchecked(l) };
                let right_val = unsafe { *nums.get_unchecked(r) };
                let sum = num + left_val + right_val;

                if sum == 0 {
                    sols.push(vec![num, left_val, right_val]);
                    l += 1;
                    r -= 1;

                    while l < r && unsafe { *nums.get_unchecked(l) } == left_val { l += 1; }
                    while l < r && unsafe { *nums.get_unchecked(r) } == right_val { r -= 1; }
                } else if sum < 0 {
                    l += 1;
                } else {
                    r -= 1;
                }
            }
        }
        sols
    }
}