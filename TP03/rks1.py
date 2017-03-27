from scipy.spatial.distance import pdist

# Compute distance matrix for both original and transformed sets of features
dists_orig = pdist(X_train)
dists_proj = pdist(generate_random_features(X_train, 2))

# Plot 2D histogram of distances between samples in original/transformed spaces
plt.hist2d(dists_orig, dists_proj, 100)