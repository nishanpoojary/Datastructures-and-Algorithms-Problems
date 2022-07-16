# python3

EPS = 1e-6
PRECISION = 6

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col

def read_data():
    size = int(input())
    a = []
    b = []
    for _ in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)

def select_pivot_element(pivot, a, used_rows):
    while used_rows[pivot.row] or a[pivot.row][pivot.col] == 0:
        pivot.row += 1
    return pivot

# swap row to top of non-pivot rows
def swap_lines(a, b, used_rows, pivot):
    a[pivot.col], a[pivot.row] = a[pivot.row], a[pivot.col]
    b[pivot.col], b[pivot.row] = b[pivot.row], b[pivot.col]
    used_rows[pivot.col], used_rows[pivot.row] = used_rows[pivot.row], used_rows[pivot.col]
    pivot.row = pivot.col

def process_pivot_element(a, b, pivot, used_rows):
    scale = a[pivot.row][pivot.col]
    if scale != 1:
        for i in range(len(a)):
            a[pivot.row][i] /= scale
        b[pivot.row] /= scale
    for i in range(len(a)):
        if i != pivot.row:
            multiple = a[i][pivot.col]
            for j in range(len(a)):
                a[i][j] -= a[pivot.row][j] * multiple
            b[i] -= b[pivot.row] * multiple
    used_rows[pivot.row] = True


def solve_equation(equation):
    a = equation.a
    b = equation.b
    size = len(a)
    used_rows = [False] * size
    for i in range(size):
        pivot = Position(0, i)
        pivot = select_pivot_element(pivot, a, used_rows)
        swap_lines(a, b, used_rows, pivot)
        process_pivot_element(a, b, pivot, used_rows)
    return b

def print_column(column):
    for e in column:
        print("{0:.6f}".format(e), end=' ')


if __name__ == '__main__':
    matrix = read_data()
    solution = solve_equation(matrix)
    print_column(solution)
    exit(0)