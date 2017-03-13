error_min = 1.0
for p in permutations(range(3)):
    # Permute labels following permutation p
    y_new = [p[yy] for yy in y_hat0]
    
    # Compute error; if smaller than min. so far, store permutation
    error = np.mean(y_train != y_new)
    if error < error_min:
        p_good = p
        error_min = error
        
    print("permutation: %s, error: %g" % (p, error))
    
# Permute labels following permutation that gives minimum error
y_hat = [p_good[yy] for yy in y_hat0]