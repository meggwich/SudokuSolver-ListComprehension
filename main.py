class Sudoku:

    def __init__(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            self.grid = [
                [int(element) if element.isdigit() else element for element in line.split()] 
                for line in file
            ]

    def __str__(self):
        copy = [
                [str(element) if isinstance(element, (int, set)) else element for element in line] 
                for line in self.grid
            ]
        return '\n'.join([' '.join(row) for row in copy])

    def make_sets(self): 
        for i, row in enumerate(self.grid):
            for j, element in enumerate(row):
                if element == '.':
                    column_set = set([el for el in [self.grid[num][j] for num in range(len(self.grid))] if isinstance(el, int)])
                    row_set = set([el1 for el1 in self.grid[i] if isinstance(el1, int)])
                    
                    quadrant = (j // 3, i // 3)
                    square_set = {self.grid[r][e] for r in range(quadrant[1] * 3, (quadrant[1] + 1) * 3)
                                            for e in range(quadrant[0] * 3, (quadrant[0] + 1) * 3)
                                            if isinstance(self.grid[r][e], int)}
                    
                    possible_values = set(range(1, 10)) - column_set - row_set - square_set
                    self.grid[i][j] = possible_values 

        counter = 0
        for h in self.grid:
            for t in h:
                if isinstance(t, set):
                    if not t:
                        return
                    if len(t) == 1:
                        counter += 1
        return counter

    def replace(self):
        for i, row in enumerate(self.grid):
            for j, element in enumerate(row):
                if isinstance(element, set) and len(element) == 1:
                    self.grid[i][j] = list(element)[0]
                if isinstance(element, set) and len(element) > 1:
                    self.grid[i][j] = '.' 

    def solve(self):
        a = 1
        counter = 0
        while a:
            a = self.make_sets()
            self.replace()
            counter += 1
        for i, row in enumerate(self.grid):
            for j, element in enumerate(row):
                if isinstance(element, set):
                    self.grid[i][j] = '.'
        solution = None if a == None else self.count_empty_squares()
        return counter, solution

    def count_empty_squares(self):
        return sum(1 for row in self.grid for element in row if element == '.' or isinstance(element, set))

if __name__ == "__main__":
    for i in range(1, 10):
        s = Sudoku(f'subor{i}.txt')
        print(s.solve())
