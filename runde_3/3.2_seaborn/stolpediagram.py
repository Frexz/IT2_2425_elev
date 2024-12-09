# seaborn-modulen er spesialtilpasset pandas-modulen
# og baserer seg på matplotlib, men gir flere tilpasningsmuligheter
# med mindre kode

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame([1, 2, 3], index=["En", "To", "Tre"], columns=["Antall"])

sns.barplot(x=df.index, y=df["Antall"])
plt.show()