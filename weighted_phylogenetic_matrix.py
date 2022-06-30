def weighted_phylogenetic_matrix(phylogenetic_matrix):
    '''
    Get:
        A dataframe of a binary phylogentic matrix
    Return:
        A dataframe of a weighted phylogenetic matrix
    '''
    g_size = len(df.index)
    for column in df.columns:
        homologue = df[column].to_numpy()
        h_number = np.sum(homologue)
        score = h_number/g_size
        df[column].replace(1, score, inplace=True)
        df.to_pickle('nonbinary_phylogenetic_matrix.pkl')
    return df