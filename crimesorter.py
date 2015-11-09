import csv
import math


def read_file(filename):
    types_of_crime = {
        'homicide': [0, 0, 205],
        'crim sexual assault': [0, 0, 115],
        'kidnapping': [0, 0, 108],
        'robbery': [0, 0, 86.4],
        'burglary': [0, 0, 47.2],
        'sex offense': [0, 0, 58.2],
        'other offense': [0, 0, 49],
        'battery': [0, 0, 49.5],
        'offense involving children': [0, 0, 49.5],
        'assault': [0, 0, 52],
        'stalking': [0, 0, 45],
        'arson': [0, 0, 39.6],
        'weapons violation': [0, 0, 49.5],
        'public peace violation': [0, 0, 30],
        'motor vehicle theft': [0, 0, 33.3],
        'criminal damage': [0, 0, 35.2],
        'deceptive practice': [0, 0, 35.2],
        'theft': [0, 0, 29.4],
        'intimidation': [0, 0, 33],
        'criminal trespass': [0, 0, 22],
        'interference with public officer': [0, 0, 22],
        'narcotics': [0, 0, 17.1],
        'liquor law violation': [0, 0, 5.1],
        'gambling': [0, 0, 5],
        'prostitution': [0, 0, 15],
        'other narcotic violation': [0, 0, 17.1],
        'concealed carry license violation': [0, 0, 49.5]}

    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            print row[5].lower()
            if row[5].lower() == 'n':
                types_of_crime[row[1].lower()][0] += 1
                if row[4].lower() == 'y':
                    types_of_crime[row[1].lower()][1] += 1

    return types_of_crime


def process(types_of_crime):
    out_dict = {}
    for d in types_of_crime:
        if types_of_crime[d][0] > 0:
            out_dict[d] = [types_of_crime[d][0], types_of_crime[d][1], types_of_crime[d][0] * types_of_crime[d][2] * (
                                        1 / (math.pow(math.e, 2 * types_of_crime[d][1] / types_of_crime[d][0])))]
        else:
            out_dict[d] = [types_of_crime[d][0], types_of_crime[d][1], 0]

    return out_dict


def write_file(out_dict, filename):
    with open(filename, 'w+') as f:
        writer = csv.writer(f, delimiter=',')
        for d in out_dict:
            writer.writerow([d] + out_dict[d])


def gen_data(infile, outfile):
    types_of_crime = read_file(infile)
    reports = 0
    arrests = 0
    print types_of_crime
    for d in types_of_crime:
        reports += types_of_crime[d][0]
        arrests += types_of_crime[d][1]
    if reports > 0:
        print arrests / reports, reports
    out_dict = process(types_of_crime)
    write_file(out_dict, outfile)


def gen_for_all():
    for district in [t for t in range(1, 26) if t not in [13, 21, 23]]:
        gen_data('District' + str(district) + '.csv', 'Data' + str(district) + '.csv')


def gen_one(outfile):
    types_l = {}
    for district in [t for t in range(1, 26) if t not in [13, 21, 23]]:
        types_l[district] = (process(read_file('District' + str(district) + '.csv')))

    rows = []

    for d in types_l[1]:  # crimes
        row = [d]
        for district in [t for t in range(1, 26) if t not in [13, 21, 23]]:
            for i in range(len(types_l[district][d])):
                row.append(types_l[district][d][i])

        rows.append(row)

    with open(outfile, 'w+') as f:
        writer = csv.writer(f, delimiter=',')
        for r in rows:
            writer.writerow(r)


def split():
    with open('all_crimes.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        district = 1
        out = open('District1.csv', 'w+')
        writer = csv.writer(out, delimiter=',')
        for row in reader:
            jayz = int(str(row[6])[:-2])
            if jayz != district:
                out.close()
                district = int(str(row[6])[:-2])
                if district > 25:
                    return
                out = open('District' + str(district) + '.csv', 'w+')
                writer = csv.writer(out, delimiter=',')
            writer.writerow(row)


gen_one('data.csv')


