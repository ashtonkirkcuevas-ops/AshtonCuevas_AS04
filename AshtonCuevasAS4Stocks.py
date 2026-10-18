def get_prices():
    ticker = input("Enter stock ticker: ").upper()
    text = input("Enter daily prices separated by commas: ")
    return ticker, text.split(",")
 
 
def clean_data(raw_prices):
    prices = []
    for item in raw_prices:
        try:
            price = float(item.strip())
            if price > 0:
                prices.append(price)
        except ValueError:
            print("Skipping bad value:", item)
    return prices
 
 
def compute_indicators(prices):
    average = sum(prices) / len(prices)
    highest = max(prices)
    lowest = min(prices)
    last = prices[-1]
    return average, highest, lowest, last
 
 
def analyze(prices):
    if prices[-1] > prices[0]:
        return "Going UP"
    elif prices[-1] < prices[0]:
        return "Going DOWN"
    else:
        return "No change"
 
 
def generate_signals(last, average):
    if last > average:
        return "BUY"
    elif last < average:
        return "SELL"
    else:
        return "HOLD"
 
 
def create_report(ticker, average, highest, lowest, last, trend, signal):
    print("\n----- STOCK REPORT:", ticker, "-----")
    print("Last price:", last)
    print("Average:   ", round(average, 2))
    print("Highest:   ", highest)
    print("Lowest:    ", lowest)
    print("Trend:     ", trend)
    print("Signal:    ", signal)
    print("-----------------------------\n")
 
 
def main():
    ticker, raw = get_prices()
    prices = clean_data(raw)
    if len(prices) == 0:
        print("No valid prices entered.")
        return
    average, highest, lowest, last = compute_indicators(prices)
    trend = analyze(prices)
    signal = generate_signals(last, average)
    create_report(ticker, average, highest, lowest, last, trend, signal)
 
 
main()