def hamming(phylogenetic_matrix_path):
    '''
    Get:
        A dataframe of a binary phylogenetic matrix
    Return:
        A dataframe of a distance matrix
    '''
    df = pd.read_pickle(f'{phylogenetic_matrix_path}')
    hamming = pdist(df, metric='hamming')
    distance_matrix = squareform(hamming)
    distance_df = pd.DataFrame(
    distance_matrix,
    index = df.index,
    columns = df.index
    )
    return distance_df
