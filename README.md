# Stock-market-prediction

Work flows:
- Data gathering
- Data preparation

Indicators:
- EMA
- MACD

Technical Analysis:
- Support/Resistance
- Volume
- News events

Model checklist:
- LSTM
- ESN
- ARIMA


Special Sectors to be considered:
- Biotech and pharamaseuticals (patents and funding)



Ideas from RL:
- Let the agent figure out the rules (DQN)
- Multi-armed bandit


Agents strategy 1:
- Getting Float, Demand, Supply, Volatity and Volume
- Correcting the threshold
- Checking the news stream
- Pass the series of tests:
    - News time
    - Is the symbol known?
    - Float
    - News headline (Sentiment analysis, number of positive words, how positive is it?)
    - Volume (is it incremental?)
 
Agents startegy 2:
- Check earning reports
- Probability of being positive or negative
- Price prediction

Agents strategy 3:
- Check the previous max gain in the stocks
- Find out the positive/negative/investments on these stocks.
- Why it got boosted?
    - Did it reported positive earnings?
    - Did it get an investment from a big company?
    - Do they have a new product?
- Should I trade this?

Agents Strategy 4:
- Check the pre-market earning reports of positive earning rate companies
- keep an eye on them before half an hour of US opening (for volatility)
- If there are enough moementum in the stock, buy on a dip just before the US opening (BTW this includes high risk)
