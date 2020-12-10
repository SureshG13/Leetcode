// Leetcode link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
// Suresh G --> java

class Solution
 {
 public int[] twoSum(int[] nu, int target)
  {
    int i=0;
    int j=nu.length-1;
    int[] ans = new int[2];
    while (i<j)
      {
          if(nu[i]+nu[j]==target)
              {
                  ans[0]=i+1;
                  ans[1]=j+1;
                   break;
              }
          if(nu[i]+nu[j]>target)
              {
                  j--;
              }
          else
              {
                  i++;
              }
      }
 return ans;
   }
 }
