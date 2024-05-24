
def compound_annual_growth_rate(ending_value: int, beginning_value: int, number_of_years: float) -> float:
    return ((ending_value/beginning_value)**(1/number_of_years)) * 100

def sharpe_ratio(return_of_portfolio: int, risk_free_rate: float, std_of_portfolio_excess_return: float) -> float:
    return (return_of_portfolio - risk_free_rate)/std_of_portfolio_excess_return

def maximum_drawdown(stock_data: list) -> float:
    index, curr, peak = 0, 0, 0
    maximum_drawdown = 0
    duration = 0

    while index < len(stock_data):
        if curr < stock_data[index][0]:
            curr = stock_data[index][0]
        else:
            peak = curr
            start = stock_data[index][1]

            while curr <= peak:
                curr = stock_data[index][0]
                curr_drawdown = abs(peak - curr)/peak

                if (maximum_drawdown < curr_drawdown):
                    maximum_drawdown = curr_drawdown
                    duration = start - stock_data[index][1]
                index += 1

        index += 1

    return (maximum_drawdown, duration)

# def Calmar():
#     compound_annual_growth_rate()/maximum_drawdown()

def main():
    

if __name__ == "__main__":
    main()