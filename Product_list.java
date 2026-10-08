class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] productlist = new int[nums.length];
        int total = 1;
        for (int i = 0; i < nums.length; i++) {
            productlist[i] = total;
            total = total * nums[i];
        }
        total = 1;
        for (int j = nums.length - 1; j >= 0; j--) {

            productlist[j] = productlist[j] * total;
            total = total * nums[j];
        }
        return productlist;
    }
}