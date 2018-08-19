from datetime import datetime

print('smoketest')

"""
Pull in lines from dataset and put them into useable class
Eval class instance by key and add to dataline
"""
class DataLine(object):
    def __init__(self):
        self.label = ''
        self.year = ''
        self.month = ''
        self.total = ''
        super(DataLine, self).__init__()


class OutputLine():
    def __init__(self):
        self.label = ''
        self.year = ''
        self.mo_data = {}
        self.data = {'label': self.label, 'year': self.year, 'mo_data': self.mo_data}


class DataSet(OutputLine):
    def __init__(self):
        self.key = ''
        self.data_line = OutputLine()


def create_data_obj(line):
    d = DataLine()
    sp_line = line.split(',')
    d.key = '{}{}'.format(sp_line[0], sp_line[1])
    d.label = sp_line[0]

    try:
        d.year = int(sp_line[1].replace(' ', ''))
    except Exception:
        raise ValueError('Year should be numeric.')

    d.month = sp_line[2]
    d.total = sp_line[3].replace('\n', '').replace(' ', '')
    return d


def build_year(label, year, local_dataset):
    output = OutputLine()
    for obj in local_dataset:
        if obj.year != year:
            continue
        if obj.label == label:
            output.label = label
            if obj.year not in output.data:
                output.data['label'] = obj.label
                output.data['year'] = obj.year
                output.mo_data[obj.month] = obj.total

    return output


local_dataset = []
with open('sample.txt', 'r') as f:
    for line in f:
        d = create_data_obj(line)
        local_dataset.append(d)

    collected_list = []
    year = datetime.now().year
    year_ctr = 0
    while year_ctr <= 5:
        copies = build_year('COPIES', year, local_dataset)
        collected_list.append(copies)
        payment = build_year('PAYMENT', year, local_dataset)
        collected_list.append(payment)
        year_ctr += 1
        year = year - 1

    for item in collected_list:
        if item.label:
            print(item.label, item.data)
