def svd(df,threshold):
    '''
    Apply the svd method to a score profile matrix to reduce it noise according to a
    certain threshold
    '''
    df = df.fillna(0.0)
    df = df.divide(df.max(axis=1),axis='index')
    print("first normalisation")
    u, s, vh = np.linalg.svd(df, full_matrices=False)
    s[threshold:]=0.0
    P = np.dot(u * s, vh)
    print("svd")
    P_norm = np.linalg.norm(P,keepdims=True,axis=0)
    P_u = np.divide(P,P_norm)
    print("second normalisation")
    df = pd.DataFrame(P_u,index=df.index,columns=df.columns)
    print("done")
    return df
