def compute_posterior(x, centroids, var):
    return np.sum(np.exp(-.5 * np.sum((x - centroids) ** 2, 1) / var) / np.sqrt(2 * np.pi * var))

def bayes(X, m0, m1, var):
    estimate = np.zeros(len(X))
    for i in range(len(X)):
        estimate[i] = int(compute_posterior(X[i, :], m1, var) > compute_posterior(X[i, :], m0, var))
    return estimate

y_hat = bayes(X_test, class0_centroids, class1_centroids, 1./5)
print("error on test set: %g" % np.mean(y_test != y_hat))