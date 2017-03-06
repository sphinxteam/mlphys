d = []
for p in combinations(range(20), 10):
    p_tilde = set(range(20)).difference(p)
    A = samples[list(p)]
    B = samples[list(p_tilde)]
    d.append(np.mean(A) - np.mean(B))
    
d0 = df["A"].mean() - df["B"].mean()
print(np.mean(np.abs(d) > np.abs(d0)))