impl Solution {
    pub fn can_partition(nums: Vec<i32>) -> bool {
        let total: usize = nums.iter().map(|&x| x as usize).sum();
        if total % 2 != 0 {
            return false;
        }
        let target = total / 2;

        // Each u64 holds 64 bits. We need enough blocks to hold 'target' bits.
        let mut dp = vec![0u64; (target / 64) + 1];
        dp[0] = 1; // 0th bit is set (a sum of 0 is possible)

        for &num_i32 in &nums {
            let num = num_i32 as usize;
            
            // How many full 64-bit blocks we are shifting by
            let block_shift = num / 64;
            // The remaining bits to shift within the block
            let bit_shift = num % 64;

            // We must iterate backwards to prevent reusing the same number
            for i in (block_shift..dp.len()).rev() {
                // 1. Shift the bits from the corresponding old block
                let mut shifted = dp[i - block_shift] << bit_shift;

                // 2. Handle the "carry" bits from the block before it
                // If we shifted by 2 bits, the top 2 bits of the previous block 
                // need to spill over into the bottom of this current block.
                if bit_shift > 0 && i > block_shift {
                    shifted |= dp[i - block_shift - 1] >> (64 - bit_shift);
                }

                // 3. Take it or Leave it (Bitwise OR)
                dp[i] |= shifted;
            }
        }

        // Check if the target bit is 1
        let target_block = target / 64;
        let target_bit = target % 64;
        
        (dp[target_block] & (1 << target_bit)) != 0
    }
}