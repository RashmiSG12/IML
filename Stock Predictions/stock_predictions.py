def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    first_line = data[0].split()
    m = float(first_line[0])
    k = int(first_line[1])
    d = int(first_line[2])
    
    stocks = []
    for i in range(1, k + 1):
        parts = data[i].split()
        name = parts[0]
        owned = int(parts[1])
        prices = list(map(float, parts[2:]))
        stocks.append((name, owned, prices))
    
    transactions = []

    for name, owned, prices in stocks:
        current_price = prices[-1]
        previous_prices = prices[:-1]
        average_price = sum(previous_prices) / 4
        
        if current_price < average_price:
            # Buy as much as we can with available money
            shares_to_buy = int(m // current_price)
            if shares_to_buy > 0:
                transactions.append(f"{name} BUY {shares_to_buy}")
                m -= shares_to_buy * current_price
        elif current_price > average_price and owned > 0:
            # Sell all owned shares
            transactions.append(f"{name} SELL {owned}")
            m += owned * current_price
    
    print(len(transactions))
    for transaction in transactions:
        print(transaction)

if __name__ == '__main__':
    main()
