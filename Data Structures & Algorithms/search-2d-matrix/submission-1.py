class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Holes
        #[target, target, target]
        
        if matrix == None:
            return False

        new_matrix = []

        for i in range(len(matrix)):
            #internal_list_index
            ili = len(matrix[i])-1 

            if matrix[i][0] <= target and matrix[i][ili] >= target:
                if matrix[i][0] == target or matrix[i][ili] == target: return True
                #new_matrix.append(matrix[i])
                new_matrix = matrix[i]
        
        # binary search
        print(new_matrix)
        L,R = 0, len(new_matrix) - 1
        while L<=R:
            mid = (L+R)//2
            #print(mid, new_matrix[mid], L, R)
            if new_matrix[mid] == target:
                return True
            elif new_matrix[mid] < target:
                L = mid + 1
            else:
                R = mid - 1
            
        return False