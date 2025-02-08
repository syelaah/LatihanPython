import seaborn as sns
df = sns.load_dataset("penguis")
sns.pairplot(df, hue="species")
