print('smoketest')

"""
Pull in lines from dataset and put them into useable class
Eval class instance by key and add to dataline
"""
class DataLine(object):
    def __init__(self):
        self.key = ''
        self.label = ''
        self.year = ''
        self.month = ''
        self.total = ''
        self.data = {}
        super(DataLine, self).__init__()


class DataSet(DataLine):
    def __init__(self):
        self.ds_label = ''
        self.key = ''
        self.label = ''
        self.year = ''
        self.total = ''
        self.data = {}
        self.data_dict = {'label': self.ds_label, 'data': self.data}
        self.data_line = DataLine()


class OutputLine():
    def __init__(self):
        self.label = ''
        self.year = ''
        self.mo_data = {}
        self.data = {'year': self.year, 'mo_data': self.mo_data}


def create_data_obj(line):
    d = DataLine()
    sp_line = line.split(',')
    d.key = '{}{}'.format(sp_line[0], sp_line[1])
    d.label = sp_line[0]
    d.year = sp_line[1]
    d.month = sp_line[2]
    d.total = sp_line[3].replace('\n', '').replace(' ', '')
    return d

class CollectedData(DataLine):
    def __init__(self):
        self.Dataline()
        self.data = {}


local_dataset = []
with open('sample.txt', 'r') as f:
    for line in f:
        d = create_data_obj(line)
        local_dataset.append(d)

    copies = OutputLine()
    for obj in local_dataset:
        if obj.label == 'COPIES':
            if obj.year not in copies.data:
                copies.data['year'] = obj.year
                copies.mo_data[obj.month] = obj.total

    print(copies.data)
