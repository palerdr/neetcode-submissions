impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut sols = Vec::new();
        nums.sort();

        for (i, &num) in nums.iter().enumerate() {
            if i > 0 && num == nums[i-1] {
                continue
            } else {
                let (mut l, mut r) = (i+1, nums.len()-1);
                let target = -num;
                while l <  r {
                    let eq = nums[l] + nums[r];
                    if eq == target {
                        sols.push(vec![nums[l], nums[r], nums[i]]);
                        r -= 1;
                        l += 1;
                        while l<r && nums[l] == nums[l-1] {
                            l+=1;
                        }
                        while l<r && nums[r] == nums[r+1] {
                            r-=1;
                        }
                    } else {
                        if eq > target {
                            r -= 1;
                        } else {
                            l += 1;
                        }
                    }
                }
            }
        }
        return sols
    }
}
