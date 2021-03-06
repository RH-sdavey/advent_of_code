# Input Data:
# 7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

# After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners,
# After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:
# Finally, 24 is drawn:
# 22 13 17 11  0         3 15  0  2 22      **14 21 17 24  4**
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
# At this point, the third board wins because it has at least one complete row or column of marked
# numbers (in this case, the entire top row is marked: 14 21 17 24 4).

# The score of the winning board can now be calculated.
# Start by finding the sum of all unmarked numbers on that board;
# in this case, the sum is 188.
# Then, multiply that sum by the number that was just called when the board won, 24,
# to get the final score, 188 * 24 = 4512.

from day_4.functions import parse_content, mark_and_check_boards


def main():
    called_numbers, tables = parse_content()
    for num in called_numbers.split(','):
        winning_table = mark_and_check_boards(tables, num)
        if winning_table:
            return int(num) * int(winning_table.sum_board_score())


if __name__ == '__main__':
    print(main())  # -> 25023
