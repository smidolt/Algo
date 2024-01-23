# TrendFollow Strategy

This is a simple trend-following strategy implemented in Python using the Freqtrade framework. The strategy is designed to work on a 5-minute timeframe and aims to capture short-term price trends in the market.

## Installation

1. First, ensure you have [Freqtrade](https://www.freqtrade.io/) installed and set up.
2. Copy the `TrendFollowStr.py` file into the `user_data/strategies` directory of your Freqtrade installation.
3. Use prepared conf.file

## Strategy Overview

The TrendFollowStr strategy uses the following indicators:

- **On-Balance Volume (OBV):** OBV is a cumulative indicator that measures buying and selling pressure based on trading volume.
- **Exponential Moving Average (EMA):** A 20-period EMA is used as a trend indicator.

## Strategy Parameters

- **minimal_roi:** A dictionary representing the minimum return on investment required for the strategy to exit a position.
- **stoploss:** The stop-loss value for the strategy. If the position reaches this level, it will be closed to limit losses.
- **trailing_stop:** If set to `True`, a trailing stop will be used to protect profits and limit losses.
- **trailing_stop_positive:** The percentage at which the trailing stop will be triggered to protect profits.
- **trailing_stop_positive_offset:** An offset added to the trailing stop to reduce the risk of premature triggering.
- **trailing_only_offset_is_reached:** If set to `True`, the trailing stop will be used only after the positive offset is reached.

## Indicator Calculation

The strategy uses the `populate_indicators` method to calculate the following indicators:

1. **OBV (On-Balance Volume):** Calculated using the `ta.OBV` function from the `talib` library.
2. **EMA (Exponential Moving Average):** A 20-period EMA of the closing prices.

## Entry Rules

The strategy determines the entry points using the `populate_entry_trend` method with the following conditions:

- Enter Long:
  - The current closing price is above the EMA.
  - The previous closing price was below the previous EMA.
  - The current OBV is higher than the previous OBV.

- Enter Short:
  - The current closing price is below the EMA.
  - The previous closing price was above the previous EMA.
  - The current OBV is lower than the previous OBV.

## Exit Rules

The strategy determines the exit points using the `populate_exit_trend` method with the following conditions:

- Exit Long:
  - The current closing price is below the EMA.
  - The previous closing price was above the previous EMA.
  - The current OBV is higher than the previous OBV.

- Exit Short:
  - The current closing price is above the EMA.
  - The previous closing price was below the previous EMA.
  - The current OBV is lower than the previous OBV.

## Disclaimer

This strategy is provided for educational purposes only and should not be considered financial advice. Use it at your own risk and make sure to test it thoroughly before using it in a live trading environment.
