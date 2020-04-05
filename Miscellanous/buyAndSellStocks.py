def maxProfit(prices):
	# Create a variable which stores the profit gained during transacrions
	profit = 0

	for i in range(1, len(prices)):

		if prices[i] - prices [i - 1] > 0:
			profit += prices[i] - prices[i - 1]

	return profit


print(maxProfit([7,6,4,3,1]))
