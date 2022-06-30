def binary_matrix_builder(querry_orth,COG_dir):
    '''
    Get in input path of COG directory and build a Dataframe of phylogenetic profile.
    Index are protein identifiers
    Columns are strain identifiers
    Datas are presence or absence of homologue for the querry proteine
    '''
    querry_df = pd.read_csv(COG_list_file_path, delimiter=';')
    #iterate through the dataframe to fill a dictionnary of phylogenetic profile
    dico = {}
    for row in querry_df.itertuples():
        protein = row[6] #Locus tag
        gene_id = row[5] #PGD Gene ID
        file_path = f'{COG_directory_path}/COG_{gene_id}.csv'
        COG_df = pd.read_csv(file_path)
        strains = COG_df['Strain'].to_list()
        dico.setdefault(protein,[]).extend(strains)
    #inverse the dictionnary
    dicoinv={}
    for keys, values in dico.items(): 
        for value in values: 
            dicoinv.setdefault(value,[]).append(keys)
    #build a dataframe of binary phylogenetic profile, with protein id as index
    # and bacterian species as columns 
    phylo_df = pd.DataFrame(data=0,index=dico.keys(),columns=dicoinv.keys())
    for index in phylo_df.index:
        for column in phylo_df.columns:
            if column in dico[index]:
                phylo_df.loc[index,column] = 1
    save_dataframe('binary_phylogenetic_matrix.pkl')
