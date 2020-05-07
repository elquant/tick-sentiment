import pandas as pd
import matplotlib.pyplot as plt
import settings


def get_symbols(row):
    symbols = []
    text = row["text"].upper()
    for symbol in settings.TICKER_SYMBOLS:
        if symbol in text:
            symbols.append(symbol)
    return ",".join(symbols)


tweets = pd.read_csv("data/tweets.csv")
tweets["symbols"] = tweets.apply(get_symbols, axis=1)

counts = tweets["symbols"].value_counts()
plt.bar(x=range(len(counts)), height=counts)
plt.title("Tweets mentioning ticker symbols")
plt.xlabel("Symbols")
plt.ylabel("# of tweets")
plt.show()

print(counts)
