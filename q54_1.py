class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # use i to keep track of (0, len(matrix) * len(matrix[0])):
        # row, col = 0, 0
        # rightBounds = (0, len(matrix[0]) - 1), downBounds = (len(matrix) - 1, len(matrix[0]) - 1), leftBounds = (len(matrix[0]) - 1, 0), upBounds = (0, 0)
        # while i < len(matrix) * len(matrix[0]):
        #   move to the right: while i < len(matrix) * len(matrix[0]) and col < rightBounds[1]:
        #       col += 1, i += 1, res.append(matrix[row][col])
        #   rightBounds = (rightBounds[0] + 1, rightBounds[1] - 1)
        #   move down: while i < len(matrix) * len(matrix[0]) and row < downBounds[0]:
        #       row += 1, i += 1, res.append(matrix[row][col])
        #   downBounds = (downBounds[0] - 1, downBounds[1] - 1)
        #   move left: while i < len(matrix) * len(matrix[0]) and col > leftBounds[1]
        #       col -= 1, i += 1, res.append(matrix[row][col])
        #   leftBounds = (leftBounds[0] - 1, leftBounds[1] + 1)
        #   move up: while i < len(matrix) * len(matrix[0]) and row > upBounds[0] - 1:
        #       row -= 1, i += 1, res.append(matrix[row][col])
        #   upBounds = (upBounds[0] + 1, upBounds[1] + 1)
        i, row, col, res = 0, 0, 0, []
        rightBounds = (0, len(matrix[0]))
        downBounds = (len(matrix), len(matrix[0]))
        leftBounds = (len(matrix), -1)
        upBounds = (0, -1)
        origin = (0, 0)

        while i < len(matrix) * len(matrix[0]):
            row, col = origin[0], origin[1]
            while i < len(matrix) * len(matrix[0]) and col < rightBounds[1]:
                res.append(matrix[row][col])
                col += 1
                i += 1
            rightBounds = (rightBounds[0] + 1, rightBounds[1] - 1)
            row += 1
            col -= 1
            
            while i < len(matrix) * len(matrix[0]) and row < downBounds[0]:
                res.append(matrix[row][col])
                row += 1
                i += 1
            downBounds = (downBounds[0] - 1, downBounds[1] - 1)
            row -= 1
            col -= 1

            while i < len(matrix) * len(matrix[0]) and col > leftBounds[1]:
                res.append(matrix[row][col])
                col -= 1
                i += 1
            leftBounds = (leftBounds[0] - 1, leftBounds[1] + 1)
            print("start", row, col)
            row -= 1
            col += 1
            
            while i < len(matrix) * len(matrix[0]) and row > upBounds[0]:
                print(row, col)
                res.append(matrix[row][col])
                row -= 1
                i += 1
            upBounds = (upBounds[0] + 1, upBounds[1] + 1)
            origin = (origin[0] + 1, origin[1] + 1)
        
        return res
