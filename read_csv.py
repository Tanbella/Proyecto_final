import csv
import os


def read_csv(path):
    with open('data.csv','r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next( reader)
        print(header)
        data = []
        for row in reader:
            interable = zip( header, row)
            dic = {key: value for key, value in interable}
            data.append(dic)
        return data   




if __name__=='__main__':
    data= read_csv('archive\data.csv')
    print(data[1])

""" cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files)) """