# data_collector

This code is for collecting data from Turkish Stock Market. I designed the program because I did not find any API about Turkish Stock Market to train a model in order to do stock market predictions. The repository only includes the python code to get, parse and upload the data. The automation of the program is done by using Azure Cloud Functions and Crontab expression (special Azure Crontab expression): 

{second} {minute} {hour} {day} {month} {day of week} -> 0 */10 7-15 * * 1-5 -> Every ten minutes between 10am to 6pm (Server timezone is GMT0 but Turkish timezone is GMT+3) from monday to friday

The Azure Cloud Functions side of the app is not published on GitHub yet.
