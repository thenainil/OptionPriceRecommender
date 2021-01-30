PROJECT NAME: Option Price Recommender

DESCRIPTION: A Python script where the trader receives the highest-probability option trade of the week. Best used at the start of the week to close out on Friday. 

INSTALLATION: 
Just download both files.
Ensure python is installed in your computer.
-pip install any required libraries which the terminal asks at runtime.
*Special note for matplotlib, install version 3.2.2. The latest version is not yet supported by all the libraries used*

USAGE:
Run Predictor.py, it will run the program.

1. The program will ask you to input the week of. Put in the Sunday or Monday of this week.
2. The program will output the best trade you can run for that Friday. It will give the direction (call/put), strike price, the target price, and the stop price.
3. By default, it looks at Friday, but, if you are willing to get dirty with the code, you can change the "5" in line 9 and line 10 of Predictor.py to the days from the entered date to get your answer. Note that sometimes, the TP & SL will equal to 0, this means there is no high probability trade for that timeframe and you're better off just sitting out the market.
4. You can also change the ticker you want to trade. By default it is "SPY". Again, if you're willing to get dirty with the code, you can change "SPY" in line 11 of Model.py to another ticker. I recommend a stable company or an index.
5. After the tweaks, you run Predictor.py and it will work just like before, but with the new parameters. It is possible the text "TRADE OF THE WEEK" could be moot.

CREDIT:
Nainil Patel
