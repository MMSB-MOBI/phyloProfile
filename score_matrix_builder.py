def score_matrix_builder(score_file_dir):
    path = score_file_dir
    dico_prot={}
    for file in os.listdir(path):
        dico_strain={}
        df = pd.read_csv(f'{path}{file}', header=None)
        protein = file.strip('_scores.txt')
        dico_prot[protein]=dico_strain
        for row in df.itertuples():
            strain = row[3]
            score = row[4]
            dico_strain[strain]=score
    df = pd.DataFrame(dico_prot)
    df.to_pickle('score_phylogenetic_matrix.pkl')
