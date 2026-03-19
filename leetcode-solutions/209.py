class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
      int minlen= INT_MAX;
      int n= nums.size();
      int sum=0;
      int low=0;
      for ( int high=0; high< n ; high++){
        sum+=nums[high];
        
      
      while ( sum>= target){
        int currentmin = high-low+1;
       minlen= min(minlen, currentmin);
        sum-=nums[low];
        low++;
}
      }
    
      return(minlen == INT_MAX )? 0 : minlen; 
    }
};
