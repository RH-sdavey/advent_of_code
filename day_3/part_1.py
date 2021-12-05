# --- Day 3: Binary Diagnostic ---
# Given the following diagnostic report:
# 00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010

# 10101 = 10
# 01010 = 5

# Considering only the first bit of each number,
# there are five 0 bits and seven 1 bits. Since the most common bit is 1,
# the first bit of the gamma rate is 1.
# The most common second bit of the numbers in the diagnostic report is 0,
# so the second bit of the gamma rate is 0.

# The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively,
# and so the final three bits of the gamma rate are 110.

# So, the gamma rate is the binary number 10110, or 22 in decimal.
# The epsilon rate is calculated in a similar way; rather than use the most common bit,
# the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal.
# Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.
# Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate,
# then multiply them together.
# What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary)

result_str = "".join(
    "10" if bits.count("1") > len(bits) / 2 else "01"
    for bits in zip(*open('./input/input.txt').read().splitlines())
)
print(int(result_str[::2], 2) * int(result_str[1::2], 2))  # -> 3374136
