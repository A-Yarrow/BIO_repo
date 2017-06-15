import pandas as pd
import matplotlib as plt
import seaborn as sns
import pylab

def make_stacked_bar_chart(filename):

    data_frame = pd.read_csv(filename, sep='\t', header=2)
    del data_frame['GAP']
    data_frame['Position'] = data_frame['Position'].apply(lambda x: x-34)
    print data_frame.head()
    data_frame.plot.bar(stacked = True)






make_stacked_bar_chart('kappa_FR1_aa_freq.txt')