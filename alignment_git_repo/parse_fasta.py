def parse_fasta(searchfield, filename, fileout):
    filehandle = open(filename, 'r')
    outfile = open(fileout, 'w')
    fasta_dict = {}
    seq = ''
    for line in filehandle:
        if line.startswith('>') and seq =='': #get the first fasta record as a key
            header = line

        elif line[0] != '>':
            seq = seq + line

        elif line.startswith('>') and seq != '':
            if searchfield in header:
                outfile.write(header+seq)
                fasta_dict[header] = seq
            seq = ''
            header = line

    filehandle.close()
    outfile.close()
    return fasta_dict

fasta_dict = parse_fasta('heavy chain', 'igSeqProt.fasta', 'igSeqProt_filtered.fasta')
print len(fasta_dict)
