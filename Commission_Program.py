#Name: Nicholas Boes (nboes)
#Final Problem: 1

def get_total_sales():
    #Obtains the sales information from the user and checks for proper input
    loop = True
    while loop:
        sales = input("Enter the total sales amount->")
        try:
            #Checks for a numbers
            sales = float(sales)
            #Checks for a positive number
            if sales < 0:
                print(f"Input ({sales}) is negative. Please enter a positive number.")
                continue
            else:
                break
        except ValueError:
            print(f"Input ({sales}) is not a number. Please enter a positive number.")
        except:
            print("Something went wrong!")
            exit(1)
    return sales

def calc_sales_commission(sales):
    #Figures the commission rate and bonus from the sales information
    if sales < 5000:
        com_rate = .08
        bonus = 0
    elif sales <= 10000:
        com_rate = .1
        bonus = 100
    else:
        com_rate = .12
        bonus = 500
    return com_rate, bonus

def output_results(sales, com_rate, bonus):
    #Calculates the commission and displays the results
    commission = com_rate * sales + bonus
    print(f"Total Sales: ${int(round(sales, 0))} | Commission Rate: {com_rate*100}% | Bonus: ${bonus} | Total Commission ${round(commission, 2)}")

def main():
    #Gets the sales information
    sales = get_total_sales()
    #Gets the commission rate and the bonus
    com_rate, bonus = calc_sales_commission(sales)
    #Outputs the results
    output_results(sales, com_rate, bonus)
main()