def phylo_to_distance_matrix(phylogenetic_matrix, p):
    '''
    Get:
        A dataframe of a phylogenetic matrix
        p the paramater of the minkowski formula
    Return:
        A dataframe of a distance matrix
    '''
    df = phylogenetic_matrix
    if p == 1:
        methode = 'manhatthan' 
    elif p == 2:
        methode = 'euclidean'
    else:
        methode = 'minkowski'
    distance_matrix = dm(df, df, p)
    distance_df = pd.DataFrame(
    distance_matrix,
    index = df.index,
    columns = df.index
    )
    #distance_df = distance_df.div(distance_df.values.max())
    return distance_df
