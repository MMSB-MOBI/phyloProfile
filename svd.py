def svd(array,threshold):
    '''
    Apply the svd method to a score profile matrix to reduce it noise according to a
    certain threshold
    '''
    P = np.nan_to_num(array)
    P_max = np.amax(P,axis=1,keepdims=True)
    P = np.divide(P,P_max)
    u, s, vh = np.linalg.svd(P, full_matrices=False)
    s[threshold:]=0.0
    P = np.dot(u * s, vh)
    P_norm = np.linalg.norm(P,keepdims=True,axis=0)
    P_u = np.divide(P,P_norm)
    return P_u
