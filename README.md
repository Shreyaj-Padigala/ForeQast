# ForeQast
This repository will include any ForeQast implementations and resources.



Introductory to the project:

1) Ethereum is a growing asset for many retail investors and large firms due to crypto being able to let asset holders have more possesion over their money (removing the need for third party bank institutions)
   and its increasing use cases in NFT collection (another digital crypto asset) and online transactions.
   
3) Over the past decade up until now, Ethereum has been an asset which has gained more and more attention due to increasing value against DXY (U.S. Dollar), making it a common investment asset among traders due its
   high return rates.
   
5) Although Ethereum for a great amount of time has been a major risk asset, the federal adoption of crypto currency like $BTC (Bitcoin) and $ETH (Ethereum) in the past couple of years has made crypto a safer and
   more reliable asset. For example, traders gained access to ethereum ETFs (ETF being an exchange-traded investment product that must register with the Security and Exchange Commission as an open-end investment
   company), making a big step foreward towards crypto currency adoption.

6) However, with the greater adoption of the asset along with increasing use cases of this asset, it begs the question of what are effective strategies for holding ethereum and making the most returns as possible.

7) This reserach propses this: We will implement Recurrent Neural Networks (RNNs, RNN-LSTM Hybrids, HM-RNNs) to analyze years of ETH/USD trading pair data and to make reasonable price predictions based on previous
   historical price trends.

8) For learning purposes/participant onboarding we will use the ETHUSD.csv dataset from kaggle (file will be found under main branch of repo). Later on for our real implementation we will try to get a Yahoo
   Finance Dataset which contains more information regarding price like volume, market cap, RSI, MACD, and more if possible. The kaggle data set will only include OHLC (open high low close) and price for that day.

9) The specific structure of ETHUSD.csv
   #how it would be formatted on file
   [Date], [Open], [High], [Low], [Close], [Adj Close], [Volume]
   ...
   [Date], [Open], [High], [Low], [Close], [Adj Close], [Volume]

   being able to work with this data set and making a solid model will allow for smooth and straightforeward process for real implementation. This is because the real implementation is essentially the same thing
   but takes into account of more parameters and note just these 7.
   



Implementations:

1) You will write your implementation on jupyter notebooks (google colab for simplicity and no need to run locally on computer)
   
2) Your models need to give the following statistics (ideally, try to return these statistics in the final cells of jupyter notebook):
    a) Mean Error (ME)
    b) Mean Absolute Error (MAE)
    c) Mean Percentage Error (MPE)
    d) Mean Absolute Percentage Error (MAPE)

   Make sure you understand what these statistics mean because you WILL be asked why they are significant and what they show about the performance of the model. Furthermore, it can help you identify if
   anything is wrong with your model. As a finance project, your statistics will be most heavily questioned as finance is a topic that is very prone to randomness.

   These will be the statistics that you all will use during your presentations (symposium night)

4) Libraries that are probably necessary will be found in my own implementations that will be under the main branch (feel free to do this however you want but this is just a good starting point)
   
5) I fine with delays with tasks like paper readings and implementations but they can't be prolonged or this will become an issue. Lets say I assigned a implementation today, then i would
   reasonably expect that finished by next week or sometimes 2 weeks the at same day of week.

6) Tasks like presentation slides/mock presentations (will go over in different section) MUST be on time since your teamates actively depend on your efforts.
   
7) Understanding implementation system design is far more importatant being able to understand the specific algorithm used. Feel free to get help on small tasks like that but please be able to understand the
   RNN, RNN-LSTM, and HM-RNN architecture. Dont worry you dont need to know this on the first day, just learn them as you finish each implementation.

8) Once you finish an implementation, please push it on to your branch and we will talk about it on build nights first thing

