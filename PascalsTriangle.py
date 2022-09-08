# https://leetcode.com/problems/pascals-triangle/solution/


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]] 
         
        for i in range(1, numRows): 
            temp = []
            temp.append(1)

            for j in range(len(ans[-1])-1): 
                temp.append(ans[-1][j]+ans[-1][j+1])

            temp.append(1)
            ans.append(temp)
        return ans



