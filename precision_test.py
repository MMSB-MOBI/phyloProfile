def df_intersect(df):
    print('intersecting')
    distance_matrix = df
    observed_adjency = pd.read_pickle('data/observed_adjency_matrix.pkl')

    d_ind = distance_matrix.index

    o_ind = observed_adjency.index

    ind = d_ind.intersection(o_ind)

    distance_matrix = distance_matrix.reindex(index=ind, columns=ind)

    #dico = distance_matrix.to_dict('split')
    print('intersected')
    return distance_matrix

def get_couples(index_list):
    for i in range(len(index_list)):
        for j in range(i+1,len(index_list)):
            yield((index_list[i],index_list[j]))

def couple_sorter(df):
    print('sorting')
    couple_dist={}
    dico = df.to_dict('split')
    for couple in get_couples(dico['index']):
        dist=df.loc[couple]
        couple_dist.setdefault(dist,[]).append(couple)
    couple_dist_ord = dict(sorted(couple_dist.items(),reverse=False))
    #print(couple_dist_ord)
    print('sorted')
    return couple_dist_ord

def courbe_rc(dico,shuffle):
    print('ploting')
    observed_adjency = pd.read_pickle('data/observed_adjency_matrix.pkl')
    P_list = []
    TP = 0
    FP = 0
    n = 1
    value_list = list(dico.values())
    if shuffle == True:
        random.shuffle(value_list)
    for value in value_list:
        for couple in value:
            if (observed_adjency.loc[couple[0],couple[1]]) == 1:
                TP = TP+1
            else:
                FP = FP+1
            n=n+1
            if n==1000:
                Precision = TP/(TP+FP)
                P_list.append(Precision)
                n = 1
    print('ploted')
    return P_list

def benchmark(list_path):
    dico_rc = {}
    for path in list_path:
        distance_matrix = pd.read_pickle(path)
        intersect_matrix = df_intersect(distance_matrix)
        couple_dist = couple_sorter(intersect_matrix)
        rc_ord = courbe_rc(couple_dist, False)
        dico_rc[path] = rc_ord
    rc_rand = courbe_rc(couple_dist, True)
    dico_rc['rand'] = rc_rand
    return dico_rc
