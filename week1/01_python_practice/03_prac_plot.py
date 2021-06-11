import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips)

sns.countplot(x='sex', data=tips)
plt.show()