# In addition to horizontal position and depth, you'll also need to track a third value,
# aim, which also starts at 0.

# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
#    It increases your horizontal position by X units.
#    It increases your depth by your aim multiplied by X.

# Now,
# forward 5 adds 5 to your horizontal position, a total of 5.
#       Because your aim is 0, your depth does not change.
# down 5 adds 5 to your aim, resulting in a value of 5.
# forward 8 adds 8 to your horizontal position, a total of 13.
#       Because your aim is 5, your depth increases by 8*5=40.
# up 3 decreases your aim by 3, resulting in a value of 2.
# down 8 adds 8 to your aim, resulting in a value of 10.
# forward 2 adds 2 to your horizontal position, a total of 15.
#       Because your aim is 10, your depth increases by 2*10=20 to a total of 60.
# After following these new instructions, you would have a horizontal position of 15 and a depth of 60.
#       (Multiplying these produces 900.)
#
# What do you get if you multiply your final horizontal position by your final depth?


class Submarine:

    def __init__(self):
        self.instructions_file = './input/input.txt'
        self.instructions = open(self.instructions_file)
        self.aim = 0
        self.horizontal = 0
        self.depth = 0

    @staticmethod
    def read_instructions():
        return open('./input/input.txt').read().splitlines()

    def process_instructions(self):
        for instruction in self.read_instructions():
            self.move(instruction)

    def move(self, instruction: str):
        direction, distance = instruction.split(" ")
        if direction == "forward":
            self.horizontal += int(distance)
            self.depth += (self.aim * int(distance))
        if direction == "down":
            self.aim += int(distance)
        if direction == "up":
            self.aim -= int(distance)

    def calculate_final_position(self):
        return self.horizontal * self.depth


part_2 = Submarine()
part_2.process_instructions()
print(part_2.calculate_final_position())  # ---> 1759818555
