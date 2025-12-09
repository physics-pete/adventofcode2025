import sys

START_POSITION = 50

def convert_line(line_str):
    line_str_cleaned = line_str.strip()
    if len(line_str_cleaned) == 0:
        return ('N', 0)
    direction = line_str_cleaned[0]
    count = int(line_str_cleaned[1:])
    return (direction, count)

def count_zeros(movements):
    zeros = 0
    position = START_POSITION
    for direction, count in movements:
        if direction == 'R':
            position += count
        elif direction == 'L':
            position -= count
        position = position % 100
        if position == 0:
            zeros += 1
    return zeros

def count_everyzeros(movements):
    zeros = 0
    position = START_POSITION
    for direction, count in movements:
        if direction == 'N':
            continue

        old_position = position

        zeros += abs(count // 100)
        count = count % 100

        if direction == 'R':
            position += count
        elif direction == 'L':
            position -= count
        
        if position >= 100 or (position <= 0 and old_position != 0):
            zeros += 1

        print(f'{direction}{count} + {old_position} = {position} % 100 ({zeros})')

        position = position % 100
    return zeros

   

def main():
    with open(sys.argv[1], 'r') as fil:
        movements = [convert_line(line) for line in fil.readlines()]

    number_of_zero_positions = count_zeros(movements)
    number_of_everyzero_positions = count_everyzeros(movements)

    print(f'Zero End Positions: {number_of_zero_positions}')
    print(f'Every Zero Crossing: {number_of_everyzero_positions}')


if __name__ == "__main__":
    main()
