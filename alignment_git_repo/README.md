This is a collection of scripts to produce a stacked bar plot 
showing the varriation in amino acid sequence for the
Fc constance region (CH2_CH3 domain)



1. First query local blast installation with the following command:
blastp -db igSeqProt -query 1H3X.fasta -outfmt "10" > igSeqProt.fasta
produces alignement in multiple fasta output.

2. 2. parse_fasta.py:
python script to filter the multiple fasta generated above.
It takes three arguments; searchfield, filename, and fileout.
Filters the fasta with the search field in the header. Filename is the  
multiple fasta input to parse and fileout is the name of the output fasta.
Here, searchfield = 'heavy chain', input fasta = igSeqProt.fasta, and  
outfile = igSeqProt_filtered.fasta.

3. blastp.sh:
A one line bash script that uses a local installation of the blast
software to query the multiple fasta generated above.
It aligns to to 1H3X.fasta (PDB code)
aind produces a multiple fasta alignment in tabular format with only 
sequence identity and aligned sequence.

4. filter_alignement.py:
Takes alignment above and filters for percent identity > 50%
Outputs filtered multiple fasta file.

5. This file is read into bioedit annd a table detailing percentage 
amino acid at each position is generated.

6. They python notebook, stacked_bar.ipynb, plots a stacked bar chart of variable amino acids at specific positions.  
