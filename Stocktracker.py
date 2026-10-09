every_transactions = []
name = None

#Creating the load data function
def load_data():
    with open('C:\\Users\\jqngu\\OneDrive\\Desktop\\Stocks tracker\\stocks.txt', 'r') as file:

        reading_file = True
        while reading_file:
            entry = file.readline()
            cleaned = entry.rstrip("\n")
            
            if (cleaned == ""):
                reading_file = False
                break

            every_transactions.append(cleaned)
            print(cleaned)
#Creating the save data function that erases everything in the stocks.txt notepad and saves everything from the every_transactions global variable and saves it to the stocks.txt.
def save_data():
     with open('C:\\Users\\jqngu\\OneDrive\\Desktop\\Stocks tracker\\stocks.txt', 'w') as file:
          for transaction in every_transactions:
               file.write(str(transaction) + "\n")

#Creating the buy function
def buy_action():
    share_type = input("What is the share name you are purchasing?: ")
    date = input("What is the date of purchase?: ")
    share_amount = input("How many shares are you purchasing?: ")
    share_price = input("How much is each share worth right now?: ")
    
    saved_stock_info = "BUY" + "," + share_type + "," + date + "," + share_amount + "," + share_price

    every_transactions.append(saved_stock_info)            

#Creating the sell function
def sell_action():
    share_type = input("What is the share name you are selling?: ")
    date = input("What is the date of selling?: ")
    share_amount = input("How many shares are you selling?: ")
    share_price = input("How much is each share worth right now?: ")

    saved_stock_info = "SELL" + "," + share_type + "," + date + "," + share_amount + "," + share_price

    every_transactions.append(saved_stock_info)

#Creating the owned shares function that adds up how many shares you currently have
def owned_shares():
    account_question = input("\n" + "Would you like to know how many shares you own? (Y)es or (N)o: ")
    if account_question == "Y":
        every_stock = {}
        for trade in every_transactions:
            information = trade.split(",")

            if information[0] == "BUY":
                if information[1] in every_stock:
                    every_stock[information[1]] += float(information[3])
                elif information[1] is not every_stock:
                    every_stock[information[1]] = float(information[3])

            elif information[0] == "SELL":
                if information[1] in every_stock:
                    every_stock[information[1]] -= float(information[3])

        for stock in every_stock:
            print(f"{stock}: {every_stock[stock]} shares")

#Creating the gain loss function that tells the user the amount of money spent and profited on a company
def money_gain_loss():
    account_question = input("\n" + "Would you like to know your profit and loss for each? (Y)es or (N)o: ")
    if account_question == "Y":
        cost = {}
        revenue = {}
        for trade in every_transactions:
            information = trade.split(",")

            if information[0] == "BUY":
                if information[1] in cost:
                    cost[information[1]] += float(information[3]) * float(information[4])
                elif information[1] is not cost:
                    cost[information[1]] = float(information[3]) * float(information[4])

            elif information[0] == "SELL":
                if information[1] in revenue:
                    revenue[information[1]] += float(information[3]) * float(information[4])
                elif information[1] is not revenue:
                    revenue[information[1]] = float(information[3]) * float(information[4])
    
    for stock, cost in cost.items():
        if stock in revenue:
            revenue_amount = revenue[stock]
        else: 
            revenue_amount = 0
        print(f'''
{stock}: 
Cost: {cost:.2f} 
Revenue: {revenue_amount:.2f}''')

#Main loop that asks the user what they want to do
print("Action Company Date #ofshares $of1share")

load_data()

owned_shares()

money_gain_loss()

running = True

while running is True:
    action = input("\n" + "Would you like to (B)uy or (S)ell or (Q)uit?: ")  

    if action == "Q":
        running = False    

    if action == "B":
        buy_action()

    if action == "S":
        sell_action()


save_data()