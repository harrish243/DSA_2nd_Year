class Solution {
    public void rotate(int[] nums, int k) {
        int[] routatelist = new int[nums.length];
        k = k % nums.length;
        int index = 0;
        for (int i = nums.length - k; i < nums.length; i++) {
            routatelist[index] = nums[i];
            index++;
        }
        for (int j = 0; j < nums.length - k; j++) {
            routatelist[index] = nums[j];
            index++;
        }
        for (int i = 0; i < nums.length; i++) {
            nums[i] = routatelist[i];
        }
    }
}