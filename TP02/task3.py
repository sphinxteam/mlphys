def power_features(x, max_power):
    """
        Given a vector of data points, x, build a matrix of power
        features from 0 (constant) up to power p for use with
        polynomial fitting.
    """
    X = np.zeros((x.shape[0], max_power+1))
    
    for p in range(0,max_power+1):
        X[:,p] = np.power(x,p)    
    
    return X