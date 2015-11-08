import csv
import math


totals = {
    'homicide': 0,
    'crim sexual assault': 0,
    'kidnapping': 0,
    'robbery': 0,
    'burglary': 0,
    'sex offense': 0,
    'other offense': 0,
    'battery': 0,
    'offense involving children': 0,
    'assault': 0,
    'stalking': 0,
    'arson': 0,
    'weapons violation': 0,
    'public peace violation': 0,
    'motor vehicle theft': 0,
    'criminal damage': 0,
    'deceptive practice': 0,
    'theft': 0,
    'intimidation': 0,
    'criminal trespass': 0,
    'interference with public officer': 0,
    'narcotics': 0,
    'liquor law violation': 0,
    'gambling': 0,
    'prostitution': 0,
    'other narcotic violation': 0,
    'concealed carry license violation': 0
}


# the array is non-domestic crimes, number of arrests and the danger for that crime
def gen_data(infile, outfile):
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
        'other narcotic violation': [0, 0, 1],
        'concealed carry license violation': [0, 0, 1]}

    with open(infile, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        nctr = 0
        for row in reader:
            if row[5].lower() == 'y':
                types_of_crime[row[2].lower()][1] += 1
            if row[6].lower() == 'n':
                types_of_crime[row[2].lower()][0] += 1

    for a in types_of_crime:
        totals[a] += types_of_crime[a][0]

    with open(outfile, 'w+') as f:
        writer = csv.writer(f, delimiter=',')
        for d in types_of_crime:
            if types_of_crime[d][0] > 0:
                writer.writerow([d, types_of_crime[d][0], types_of_crime[d][1],
                                 types_of_crime[d][0] * types_of_crime[d][2] * (
                                     1 / (math.pow(math.e, 2 * types_of_crime[d][1] / types_of_crime[d][0])))])
            else:
                writer.writerow([d, types_of_crime[d][0], types_of_crime[d][1],
                                 0])


gen_data('District1.csv', 'Data1.csv')
gen_data('District2.csv', 'Data2.csv')
gen_data('District3.csv', 'Data3.csv')
gen_data('District4.csv', 'Data4.csv')
gen_data('District5.csv', 'Data5.csv')
gen_data('District6.csv', 'Data6.csv')
gen_data('District7.csv', 'Data7.csv')
gen_data('District8.csv', 'Data8.csv')
gen_data('District9.csv', 'Data9.csv')
gen_data('District10.csv', 'Data10.csv')
gen_data('District11.csv', 'Data11.csv')
gen_data('District12.csv', 'Data12.csv')
gen_data('District14.csv', 'Data14.csv')
gen_data('District15.csv', 'Data15.csv')
gen_data('District16.csv', 'Data16.csv')
gen_data('District17.csv', 'Data17.csv')
gen_data('District18.csv', 'Data18.csv')
gen_data('District19.csv', 'Data19.csv')
gen_data('District20.csv', 'Data20.csv')
gen_data('District22.csv', 'Data22.csv')
gen_data('District24.csv', 'Data24.csv')
gen_data('District25.csv', 'Data25.csv')
print totals



