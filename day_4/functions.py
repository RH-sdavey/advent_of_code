class Table:
    def __init__(self, board: list[list]):
        self.board = board
        self.pos = {
            self.board[r_cnt][c_cnt]: (c_cnt, r_cnt, False) for c_cnt in range(5) for r_cnt in range(5)
        }
        self.row_count = [[] for _ in range(5)]
        self.col_count = [[] for _ in range(5)]

    def mark_called_number(self, num: int) -> bool:
        row = self.pos[num][0]
        col = self.pos[num][1]
        self.row_count[row].insert(0, True)
        self.col_count[col].insert(0, True)
        self.pos[num] = (self.pos[num][0], self.pos[num][1], True)
        return self.check_column(col) or self.check_row(row)

    def check_row(self, row: int) -> bool:
        return True if len(self.row_count[row]) == 5 else False

    def check_column(self, col: int) -> bool:
        return True if len(self.col_count[col]) == 5 else False

    def sum_board_score(self) -> int:
        return sum(int(i) for i in self.pos.keys() if not self.pos[i][2])


def read_input_as_list() -> list:
    file = open('./input/input.txt')
    puzzle_input = [line for line in file.read().split('\n\n')]
    return puzzle_input


def parse_content() -> tuple[list, list]:
    content = read_input_as_list()
    called_numbers = content[0]
    tables = [
        Table([row.split() for row in table.split('\n')]) for table in content[1:]
    ]
    return called_numbers, tables


def mark_and_check_boards(tables, num) -> Table:
    for table in tables:
        if num in table.pos:
            if table.mark_called_number(num):
                return table
