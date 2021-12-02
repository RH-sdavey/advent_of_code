def read_input_as_list() -> list:
    """Reads input file where each line is a single int

    :return: each integer in file
    :rtype: list
    """
    with open('./input/input.txt', 'r') as f:
        return [int(line.strip()) for line in f.readlines()]


def chunk_content(content, chunk_size=3) -> [[]]:
    """Chunk content into a list of lists of chunk_size length, iterated over 1x1 (not 1x3)
    Will stop if it cant fill a new list with enough items == chunk_size

    Example: [1,2,3,4,5,6,7,8,9] -> [[1,2,3],[2,3,4],[3,4,5],[4,5,6],[5,6,7],[6,7,8]]

    :param int chunk_size: size of chunked lists
    :param list content: content to chunk into chunk size
    :return: chunked data
    :rtype: list
    """
    chunk_list = []
    start_pos = 0

    while start_pos < len(content)-(chunk_size - 1):
        chunk_list.append((content[start_pos], content[start_pos + 1], content[start_pos + 2]))
        start_pos += 1
    return chunk_list


def get_increase_count(content, do_sum=False):
    """Calculates increase count from list(int) (or list(tuple)

    Example:
        [1,2,3] --> 2
        [1,5,2] --> 1

    Example(do_sum):
        [(2,4,6), (1,2,3), (10,5,6)] --> [12,6,21] ---> 1
        [(10,4,6), (12,2,22), (22,12,12)] --> [20,36,46] ---> 3

    :param list content: to iterate over
    :param bool do_sum: if True, do sum() for item in content
    :return: number of increases for item to item+1 in content
    :rtype: int
    """
    increase_count = 0
    holder = content[0]
    for item in content[1:]:
        if do_sum:
            if sum(item) > sum(holder):
                increase_count += 1
        else:
            if item > holder:
                increase_count += 1
        holder = item
    return increase_count
