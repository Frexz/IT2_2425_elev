import pandas as pd

df = pd.read_csv("../tips.csv")

# a)
print("\n", "( a )".center(40, "-"))
print(f"Antall rader: {len(df.index)}\nAntall kolonner: {len(df.columns)}")

# b)
print("\n", "( b )".center(40, "-"))
print(*df.columns, sep=" | ")

# c)
print("\n", "( c )".center(40, "-"))
print(df.head(3))

# d)
print("\n", "( d )".center(40, "-"))
print(df[["total_bill", "tip"]])

# e)
print("\n", "( e )".center(40, "-"))
print(df[df.index == 99])

# f)  - Alternativt bruke følgende for betingelsen: df.index.isin([10, 11])
print("\n", "( f )".center(40, "-"))
print(df[(df.index == 9) | (df.index == 10)][["sex", "size"]]) # Symbolet | i dette tilfellet betyr or'

# g)
print("\n", "( g )".center(40, "-"))
print(df[df["total_bill"] < 8])