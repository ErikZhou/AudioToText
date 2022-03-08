from multiprocessing import Pool
import os, time, random
import sys
import glob


def long_time_task(index, filename):
    print('Run task %s (%s)...' % (index, os.getpid()))
    start = time.time()
    # time.sleep(random.random() * 3)
    #peg.get_peg_from_csv(filename, index)
    #get_peg_one_year.get_peg_from_csv(filename, index)
    # python audio_to_text.py ~/data/split/202p01.mp3 -o 0.txt
    txt = filename + '.txt'
    #os.chdir('./')
    os.system('python audio_to_text.py ' + filename + ' -o ' + txt)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (index, (end - start)))


def run(filepath):
    print('Parent process %s.' % os.getpid())
    path = filepath #'./'
    extension = 'mp3'
    #os.chdir(path)

    #result = [i for i in glob.glob('*.{}'.format(extension))]
    result = [i for i in glob.glob((path + '/*.{}').format(extension))]
    length = len(result)
    print('files count is ', length)
    #os.chdir('./')

    p = Pool(length)
    index = 0
    for filename in result:
        print(filename)
        p.apply_async(long_time_task, args=(index, filename,))
        index += 1
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


if __name__ == '__main__':
    filepath = sys.argv[1]
    print('filepath',filepath)
    run(filepath)
