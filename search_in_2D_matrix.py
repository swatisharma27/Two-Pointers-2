## Brute Force - using Binary Search
class Solution1:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        '''
        TC: O(mlogn) --> m for each row, log n as BS on columns
        AS: O(1)
        '''
        m = len(matrix) # no. of rows
        n = len(matrix[0]) # no. of columns

        for row in range(0, m):
            low = 0
            high = n - 1
            while low <= high:
                mid = low + (high-low)//2
                curr = matrix[row][mid]

                if curr == target:
                    return True
                elif curr > target:
                    high = mid - 1
                else:
                    low = mid + 1

        return False


## Optimal Solution -> Top Right
class Solution2:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        '''
        TC: O(m+n) 
        AS: O(1)
        '''
        m = len(matrix) # no. of rows
        n = len(matrix[0]) # no. of columns

        #top - right
        r = 0
        c = n - 1
        
        while c >= 0 and r < m:

            curr = matrix[r][c]
            if curr == target:
                return True
            elif curr > target:
                c = c - 1
            else:
                r = r + 1

        return False


## Optimal Solution -> Bottom Left
class Solution3:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        '''
        TC: O(m+n) 
        AS: O(1)
        '''
        m = len(matrix) # no. of rows
        n = len(matrix[0]) # no. of columns

        #bottom - left
        r = m - 1
        c = 0
        
        while r >= 0 and c < n:

            curr = matrix[r][c]
            if curr == target:
                return True
            elif curr > target:
                r = r + 1
            else:
                c = c - 1

        return False



if __name__ == "__main__":
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    s1 = Solution1()
    print(s1.searchMatrix(matrix, target))

    s2 = Solution2()
    print(s2.searchMatrix(matrix, target))

    s3 = Solution2()
    print(s3.searchMatrix(matrix, target))