# Part 1
def read_csv(filename):
    # Type your code below
    """
    reads CSV data stored in 'filename' and return two values, the header and the data
    the data is also converted to string and integer according to their data types
    """
    data = []
    with open (filename,'r') as f:
        header = f.readline().strip().split(',')
        #f.close is automatically called
        for line in f:
            info = f.readline().strip().split(',')
            info[0] = int(info[0])
            info[3] = int(info[3])
            data.append(info)
    return header, data
# Part 2
def filter_gender(enrolment_by_age, sex):
    # Type your code below
    """"
    filter the data based on the gender keyed in and returns a list of data for three columns excluding gender
    """
    new_data = []
    header, data = read_csv('pre-u-enrolment-by-age.csv')
    for line in data:
        if sex in line:
            line.pop(2)
            new_data.append(line)
    return new_data

# Part 3
def sum_by_year(enrolment):
    # Type your code below
    """
    returns a list of list consisting the total enrolment each year
    """
    total_enrol = []
    for i in range(35):
        total_enrol.append([1984+i,0])
        for line in enrolment:
            if line[0] == 1984+i:
                total_enrol[i][1] = total_enrol[i][1]+line[-1]
    return total_enrol

# Part 4
def write_csv(filename, header, data):
    # Type your code below
    """
    write a new file with header and fata in csv format
    at the same time the funcction will return the number of lines written
    """
    with open(filename, 'w') as f:
        out_header = ','.join(header)
        f.write(out_header)
        for line in data:
            out_line = str(','.join(str(e) for e in data))
            f.write(out_line)