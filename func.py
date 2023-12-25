# Exercise 2.2.2. 
# Define the program dollar->euro, which consumes a number of dollars and 
# produces the euro equivalent. Use the currency table in the newspaper to look up the current 
# exchange rate. 


EURO_RATE = 0.78

def money_conversion():
    while True:
        dollar_input = input("Input amount in dollar that you want to convert :$")

        if dollar_input.isdigit():
          
            dollar_input = int(dollar_input)
            # I had to convert to int

            euro_amount = dollar_input * EURO_RATE
            return int(euro_amount)
        
        else:
            print("Pls enter a valid digit")
         



dollar_euro_covert = money_conversion()
print(f"you converted into {dollar_euro_covert}euros")