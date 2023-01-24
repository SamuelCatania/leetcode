class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        out = []
        d = {}
        rows = len(matrix)
        cols = len(matrix[0])
        n_elements = rows * cols
        count = 0
        x = 0
        y = 0

        out.append(matrix[y][x])

        while len(d) != n_elements - 1:

            if count % 2 == 0:

                while x + 1 < cols and (y, x + 1) not in d:
                    d[(y, x)] = 1
                    x += 1
                    out.append(matrix[y][x])

                while y + 1 < rows and (y + 1, x) not in d:
                    d[(y, x)] = 1
                    y += 1
                    out.append(matrix[y][x])

            else:

                while x - 1 >= 0 and (y, x - 1) not in d:
                    d[(y, x)] = 1
                    x -= 1
                    out.append(matrix[y][x])

                while y - 1 >= 0 and (y - 1, x) not in d:
                    d[(y, x)] = 1
                    y -= 1
                    out.append(matrix[y][x])

            count += 1

        return out
