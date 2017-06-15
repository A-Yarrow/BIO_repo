#/bin/bash
blastp -db igSeqProt -query 1H3X.fasta -outfmt "10 pident sseq" > heavy_chain_aligned.txt

