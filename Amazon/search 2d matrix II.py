class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #target at top right corner O(m + n)
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0: return False
        row, col = 0, len(matrix[0])-1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target: return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False





# class Point {
#     int x;
#     int y;
# }
#
# Point isInMatrix(int[][] matrix, int target){
#     int row = matrix.length;
#     int column = matrix[0].length;
#     int r = 0;
#     int c = column - 1;
#     while (r < row && c >= 0){
#         if (matrix[r][c] == target){
#             return new Point(r,c);
#         }
#         if (matrix[r][c] > target){
#             c--;
#         } else {
#             r++;
#         }
#     }
#     return new Point(-1,-1);
# }