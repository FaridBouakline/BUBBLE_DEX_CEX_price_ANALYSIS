
## Project Description:
This project focuses on **fetching, merging, and analyzing BUBBLE data** from both  HUOBI and UNISWAP to conduct a comparative analysis of their price and trading behavior. The key steps include:

1. **Data Fetching**:
   - Collect historical price and volume data from a CEX (e.g., Binance, Coinbase) and Uniswap.
   - Ensure the data includes OHLCV (Open, High, Low, Close, Volume) metrics for both exchanges.

2. **Data Merging**:
   - Align the datasets from the CEX and Uniswap based on timestamps to create a unified dataset.
   - Handle discrepancies such as missing data or differing time resolutions.

3. **Comparative Analysis**:
   - Analyze price differences, spreads, and volatility between the CEX and Uniswap.
   - Investigate the impact of factors such as liquidity, gas fees, and market structure on price discrepancies.
   - Explore trading volume patterns and their influence on price discovery across the two exchanges.

4. **Insights and Conclusions**:
   - Identify key drivers of price differences, such as low liquidity on Uniswap or inefficiencies in arbitrage.
   - Propose potential improvements, such as enhancing liquidity or leveraging Layer 2 solutions, to reduce discrepancies.
   - Highlight the implications for traders, liquidity providers, and the broader DeFi ecosystem.

---

### Key Objectives:
- Understand the dynamics of price formation and trading behavior across centralized and decentralized exchanges.
- Identify inefficiencies and opportunities for arbitrage or improved market design.
- Provide actionable insights for market participants and protocol developers.

- ### How to run: given the constrain of fetching the data from ETHEREUM network, data saves as csv file have been added and then only need to run the playing_with_ccxt_example notebook

This should be straightforward
