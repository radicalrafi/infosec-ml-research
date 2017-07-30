import analyzer
import pedump as pe
from sklearn.externals import joblib

path = "/home/rafi/projects/research/malware-ml/smartav/testfiles/Win32.Turla/decrypted_rkctl_x64.dll"


def process_file(filepath):
    newfile = pe.PEFile(filepath)
    newfile_stats = newfile.Construct()

    return newfile_stats


def main():
    stats = process_file(path)
    print stats
    print stats.values()
    clf = joblib.load('classifier.pkl')
    if clf.predict(stats.values()) == 0:
        print 'Malicious'
    else:
        print 'Clean    '
if __name__ == '__main__':
    main()