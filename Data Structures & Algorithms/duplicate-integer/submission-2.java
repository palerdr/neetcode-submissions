class Solution {
    public boolean hasDuplicate(int[] nums) {
    Set<Integer> dupes = new HashSet<>(); 
    for (int i = 0; i < nums.length; i++){
        if (dupes.contains(nums[i])){
            return true;
        } else {
            dupes.add(nums[i]);
        }
    } 
    return false;
    }
}