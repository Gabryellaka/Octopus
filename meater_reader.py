import argparse
import datetime

def main():
    args = parse_arguments()
    readings_list = parse_file(args.filename)


    for reading in readings_list:
        print(reading)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Read the contents of a file.")
    parser.add_argument("filename", help="the name of the file to read")
    args = parser.parse_args()
    return args

def parse_file(filename):
    readings_list = []
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    reading = parse_line(line, line_number)
                    if reading:
                        readings_list.append(reading)
                except ValueError as e:
                    print(f"Error on line {line_number}, data is likely in an unexpected format: {e}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return readings_list

def parse_line(line, line_number):
    sets = line.strip().split('|')
    if sets[0] == 'METER' and len(sets) == 3:
        global meter_id
        meter_id = int(sets[1])
    elif sets[0] == 'READING' and len(sets) == 6:
        date = datetime.datetime.strptime(sets[3], "%Y%m%d").date()
        return {
            'METER_ID': meter_id,
            'READING_ID': int(sets[1]),
            'VALUE': float(sets[2]),
            'DATE': date,
            'STATUS': sets[4] if sets[4] in {'V', 'F'} else 'Invalid'
        }
    elif sets[0] == 'HEADER' or sets[0] == 'FOOTER':
        return None
    else:
        print(f"Skipping line {line_number}: Unexpected format or missing fields.")
        return None


def count_meters(readings_list):
    return len(readings_list)

def sum_of_valid_meters(readings_list):
    sum = 0
    for reading in readings_list:
        if reading['STATUS'] == 'V':
            sum +=1 # assuming its a sum of how many readings there are and not of the value of each reading

    return sum

def sum_of_invalid_meters(readings_list):
    sum = 0
    for reading in readings_list:
        if reading['STATUS'] == 'F':
            sum +=1 # assuming its a sum of how many readings there are and not of the value of each reading
    return sum

def find_highest_and_lowest_valid_reading(readings):
    valid_readings = [reading['VALUE'] for reading in readings if reading['STATUS'] == 'V']
    if not valid_readings:
        return None, None
    highest = max(valid_readings)
    lowest = min(valid_readings)
    return highest, lowest

def find_most_recent_and_oldest_reading(readings):
    valid_dates = [reading['DATE'] for reading in readings if reading['STATUS'] == 'V']
    if not valid_dates:
        return None, None
    most_recent = max(valid_dates)
    oldest = min(valid_dates)
    return most_recent, oldest

if __name__ == "__main__":
    main()
