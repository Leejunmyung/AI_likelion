import seaborn as sns
import matplotlib.pyplot as plt

crash = sns.load_dataset("car_crashes")


plt.figure(figsize=(16,9))
sns.stripplot(x="abbrev", y="total", data=crash)
plt.title("car_crash")
plt.show()