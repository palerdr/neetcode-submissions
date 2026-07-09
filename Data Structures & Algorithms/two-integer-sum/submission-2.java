class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numbers = new HashMap<>(); //create hashmap
        int small = 0; //initialize smaller
        int large = 0; //initialize larger
        for (int i = 0; i < nums.length; i++){
            int diff = target - nums[i]; //checks hashmap for other term 
            if (numbers.containsKey(diff)){ //if has it update small + large
                small = Math.min (numbers.get(diff),i);
                large = Math.max (numbers.get(diff),i);
            } else {
                numbers.put(nums[i], i); //if doesn't we add to hashmap
            }
        }
        int [] indices = {small,large}; //initialize return array
        return indices;
    }
}
