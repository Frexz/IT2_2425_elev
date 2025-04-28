import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.precision", 2)

df = pd.read_csv("credit_card.csv")
spanske = df[["Surname", "Age", "Balance", "Tenure", "Geography"]]
spanske = spanske[spanske["Geography"]=="Spain"]
spanske = spanske[spanske["Age"] < 30]
spanske = spanske.sort_values(by="Balance", ascending=False).head(5)
spanske = spanske.drop(columns=["Geography"])

#print(spanske)

gruppert = df[["Geography", "EstimatedSalary"]]
gruppert = gruppert.groupby(gruppert["Geography"]).mean()


plt.ylim(90000, 105000)
sns.barplot(data=gruppert, x="Geography", y="EstimatedSalary")
plt.show()
