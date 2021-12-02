# To do this, count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.) In the example above, the changes are as follows:
#
# 199 (N/A - no previous measurement)
# 200 (increased)
# 208 (increased)
# 210 (increased)
# 200 (decreased)
# 207 (increased)
# 240 (increased)
# 269 (increased)
# 260 (decreased)
# 263 (increased)
# In this example, there are 7 measurements that are larger than the previous measurement.
# Find the number of increases for "..\input\input.txt"
from day_1.lib.functions import read_input_as_list, get_increase_count

input_list = read_input_as_list()
print(get_increase_count(input_list))  # ---> 1448

