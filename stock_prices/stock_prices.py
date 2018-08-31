#!/usr/bin/python

import argparse
import itertools

def find_max_profit(prices):
  # prices = iter(prices)
  # profit = 0
  # least = next(prices)
  # for price in prices:
  #   least = min(least, price)
  #   profit = max(profit, price - least)
  profit = max(sell - buy for buy, sell in itertools.combinations(prices, 2))
  return profit

if __name__ == '__main__':
  # You can test your implementation by running 
  # `python stock_prices.py [prices]` where prices is comprised of
  # space-separated integer values
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))