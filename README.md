# share-of-search
Calculating Share of Search from Google Trends. 

This small script will help quickly calculate your monthly Share of Search for brands and competitors. This follows the article published on WARC by [James Hankins](https://twitter.com/JCPHankins). 

This script will query Google Trends using the supplied keywords, process the data, and output a DataFrame for visualisation. There's also an optional section to plot the data using Seaborn.

Libraries required:

- pandas
- pyTrends
- matplotlib
- seaborn

On backlog:
- Fixing bug that happens when date ranges are closer than 5 years apart
- Make analysis available for more than 5 keywords

