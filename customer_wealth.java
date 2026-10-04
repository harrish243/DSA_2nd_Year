public class customer_wealth {
    public int wealth(int[][] accounts){
        int max =0;
        for(int[] customer: accounts){
            int sum =0;
            for(int money: customer){
                sum = sum + money;
            }
            if(sum > max){
                max = sum;
            }
        }
        return max;
    }
}
