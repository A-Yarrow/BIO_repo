#usr/bin/python
import pandas as pd
def filter_alignment(filename, file_out):
	file_out_handle = open(file_out, 'w')
	df = pd.read_csv(filename, header = None, names = ['pct identity', 'sequence'] )
	#print df.head()
	df_filtered = df[df['pct identity'].apply(lambda x: float(x)) >= 50]
	print df_filtered.head()
	print 'df_filtered:', df_filtered.shape
	print 'df:', df.shape
	#df_filtered_seq = df_filtered[df_filtered['sequence']]
	sequence = df_filtered['sequence']
	n = 0
	for i in sequence.values:
		n=n+1
		file_out_handle.write('>'+str(n)+'\n'+i+'\n')
	#for a in df_filtered.iteritems():
	#	print a.values()
filter_alignment('heavy_chain_aligned.txt', 'heavy_chain_aligned_filtered.txt')