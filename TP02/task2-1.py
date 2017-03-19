def likelihood(x, y, m, d):
    """
        Define the likelihood for a given set of data and expanatory variable $m$,
            y = mx + noise (iid Gaussian)
    """
    r = y - m*x
    p = 1 / np.sqrt(2*np.pi*d) * exp(-1 / (2*d) * np.dot(r,r))
    return p

