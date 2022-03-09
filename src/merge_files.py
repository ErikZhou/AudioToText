import os, time, random
import sys
import glob


def merge_files(filenames, folder):
    #filenames = ['file1.txt', 'file2.txt', ...]
    for filename in filenames:
        print(filename)

    with open(folder + '/../merged.txt', 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                outfile.write('\n--------------\n')
                for line in infile:
                    outfile.write(line)
    pass
    

def run(folder):
    print('Parent process %s.' % os.getpid())
    path = folder #'./'
    extension = 'txt'
    result = [i for i in glob.glob((path + '/*.{}').format(extension))]
    length = len(result)
    print('files count is ', length)
    merge_files(result, folder)


def usage():
    print('python3 merge_files.py folder')
if __name__ == '__main__':
    usage()
    filepath = sys.argv[1]
    print('filepath',filepath)
    run(filepath)
