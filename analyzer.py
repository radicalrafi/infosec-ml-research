"""
@file:analyzer.py
@desc:Construct Dataset from a directory of samples
@author:notarbart
@license:MIT or UAYSF
"""
import os
import pedump
import pandas as pd

# globals
malicious = '/PATH/TO/MALICIOUS/FILES'
clean = 'samples/cleanfiles'
directory = 'samples/malicious'
# samples = os.walk(directory)
# write PE Information


def pe2vec(direct):
    """
    dirty function (handling all exceptions) for each sample
    it construct a dictionary of dictionaries in the format:
        sample x : pe informations
    PEFile fails to parse some files gonna try to fix it
    """
    dataset = {}
    for subdir, dirs, files in os.walk(direct):
        for f in files:
            file_path = os.path.join(subdir, f)
            try:
                pe = pedump.PEFile(file_path)
                dataset[str(f)] = pe.Construct()
            except Exception as e:
                print e
    return dataset

# now that we have a dictionary let's put it in a clean csv file


def vec2csv(dataset):
    df = pd.DataFrame(dataset)
    infected = df.transpose()  # transpose to have the features as rows
    # utf-8 is prefered from what i've seen
    infected.to_csv('dataset30.csv',
                    sep=',', encoding='utf-8')


def main():
    malwareset = pe2vec(directory)
    vec2csv(malwareset)

if __name__ == "__main__":
    main()
