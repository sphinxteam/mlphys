tval = (df["A"].mean() - df["B"].mean()) / np.sqrt(df["A"].sem() ** 2 + df["B"].sem() ** 2)
print(tval)