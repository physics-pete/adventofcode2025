import sys

def extract_range(range_string):
    ends = range_string.split('-')
    return [int(ends[0]), int(ends[1])]

def find_invalid_ids(start, end):
    invalid_ids = []
    for number in [str(k) for k in range(start, end+1)]:
        if len(number) % 2 == 0:
            len_match = len(number) // 2
            if number[:len_match] == number[len_match:]:
                invalid_ids.append(int(number))
    return invalid_ids
                

def main():
    with open(sys.argv[1], 'r') as fil:
        ranges_strings = [line.strip().split(',') for line in fil.readlines()]

    all_ranges_strings = []

    for r in ranges_strings:
        all_ranges_strings += r

    all_ranges = [extract_range(r) for r in all_ranges_strings]

    sum_of_invalid_ids = 0
    for start, end in all_ranges:
        invalid_ids = find_invalid_ids(start, end)
        for invalid_id in invalid_ids:
            sum_of_invalid_ids += invalid_id

    print(sum_of_invalid_ids)


if __name__ == "__main__":
    main()
