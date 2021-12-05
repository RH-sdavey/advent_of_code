# you're on a submarine, down and up affect your depth,
# The submarine seems to already have a planned course (your puzzle input).
# forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2
# Your horizontal position and depth both start at 0.
# The steps above would then modify them as follows:
# forward 5 adds 5 to your horizontal position, a total of 5.
# down 5 adds 5 to your depth, resulting in a value of 5.
# forward 8 adds 8 to your horizontal position, a total of 13.
# up 3 decreases your depth by 3, resulting in a value of 2.
# down 8 adds 8 to your depth, resulting in a value of 10.
# forward 2 adds 2 to your horizontal position, a total of 15.
# After following these instructions, you would have a horizontal position of 15 and a depth of 10.
# (Multiplying these together produces 150.)

# multiply your final horizontal position by your final depth


def read_input_as_list() -> list:
    """Reads input file where each line is a single int

    :return: each integer in file
    :rtype: list
    """
    return open('./input/input.txt').read().splitlines()


def horizontal_and_depth(instructions_list):
    hor = dep = 0
    for instruction in instructions_list:
        direction, distance = instruction.split(" ")
        if direction == "forward":
            hor += int(distance)
        if direction == "down":
            dep += int(distance)
        if direction == "up":
            dep -= int(distance)
    return hor, dep


instructions = read_input_as_list()
horizontal, depth = horizontal_and_depth(instructions)
print(horizontal * depth)  # ---> 1648020
