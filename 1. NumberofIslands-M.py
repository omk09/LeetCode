


# Complexity 
    #   time O(n*m)
    #   space O(n*m) stack fro BFS 

# Algorithm: 
    # iterate over the matri 
    # find the '1', then BFS to find how big this island is, turn the '1' found to '0' while doing BFS
    # everytime you find an island increment the numberOfIslands 


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def islandBFS(grid, row, col):

            if(row >= len(grid) or row<0 or col<0 or col>=len(grid[0]) or grid[row][col]=='0'):
                return
            grid[row][col] = '0';
            islandBFS(grid, row+1, col);
            islandBFS(grid, row-1, col);
            islandBFS(grid, row, col+1);
            islandBFS(grid, row, col-1);
            return 
            
            
            
        if(len(grid) == 0):
            return 0 

        numIslands = 0; 

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (grid[row][col] == '1'):
                    numIslands+=1; 
                    islandBFS(grid, row, col); 
                
        return numIslands; 
    
    

