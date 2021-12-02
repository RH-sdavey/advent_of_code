# consider sums of a three-measurement sliding window. Again considering the above example:
# 199  A
# 200  A B
# 208  A B C
# 210    B C D
# 200  E   C D
# 207  E F   D
# 240  E F G
# 269    F G H
# 260      G H
# 263        H
# Start by comparing the first and second three-measurement windows.
# The measurements in the first window are marked A (199, 200, 208);
# their sum is 199 + 200 + 208 = 607.
# The second window is marked B (200, 208, 210);
# its sum is 618.
# The sum of measurements in the second window is larger than the sum of the first,
# so this first comparison increased.
#
# Your goal now is to count the number of times the sum of measurements in this sliding window
# increases from the previous sum.
# So, compare A with B, then compare B with C, then C with D, and so on.
# Stop when there aren't enough measurements left to create a new three-measurement sum.
#
# Use the same input file as part 1

from day_1.lib.functions import read_input_as_list, chunk_content, get_increase_count

input_list = read_input_as_list()
chunked_content = chunk_content(input_list)
print(get_increase_count(chunked_content, do_sum=True))  # ---> 1471
