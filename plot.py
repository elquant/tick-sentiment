import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import settings


def find_keywords(row, **kwargs):
    found_keywords = []
    text = row["text"].lower()
    for keyword in kwargs.get("keywords"):
        if keyword.lower() in text:
            found_keywords.append(keyword)
    return ",".join(found_keywords)


tweets = pd.read_csv(settings.TWEETS_FILE_CSV)
tweets["symbols"] = tweets.apply(find_keywords, axis=1, keywords=settings.TICKER_SYMBOLS)
tweets["keywords"] = tweets.apply(find_keywords, axis=1, keywords=settings.TRACK_KEYWORDS)

symbol_counts = tweets["symbols"].value_counts()
keyword_counts = tweets["keywords"].value_counts()
grouped_by_symbol = tweets.groupby("symbols").agg([np.mean, np.std])
std = grouped_by_symbol["polarity"]["std"].iloc[1:]
mean = grouped_by_symbol["polarity"]["mean"].iloc[1:]

fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flat

ax0.pie(range(len(symbol_counts)), labels=symbol_counts.index)
ax0.set_title("Tweets mentioning ticker symbols")

ax1.bar(x=range(len(keyword_counts)), height=keyword_counts, color='b')
ax1.set_xticklabels(keyword_counts.index, rotation=90)
ax1.set_title("Keywords found on tweets")

ax2.bar(range(len(std)), std, color='r')
ax2.set_xticklabels(std.index, rotation=90)
ax2.set_title('Standard deviation of tweet sentiment')

ax3.bar(range(len(mean)), mean, color='r')
ax3.set_xticklabels(mean.index, rotation=90)
ax3.set_title('Mean tweet sentiment')

print(symbol_counts)
print(keyword_counts)

plt.legend()
plt.tight_layout()
plt.show()
