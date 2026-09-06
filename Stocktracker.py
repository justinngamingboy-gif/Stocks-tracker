#Creating the buy function
def buy_action():
    shares_type = input("What is the share name you are purchasing?: ")
    date = input("What is the date of purchase?: ")
    share_purchasing_amount = input("How many shares are you purchasing?: ")
    shares_price = input("How much is each share worth right now?: ")
    with open('C:\\Users\\jqngu\\OneDrive\\Desktop\\Stocks tracker\\stocks.txt', 'a') as file:
            stocks = file.write("BUY" + "," + shares_type + "," + date + "," + share_purchasing_amount + "," + shares_price + "\n")

#Creating the sell function
def sell_action():
    share_type = input("What is the share name you are selling?: ")
    date = input("What is the date of selling?: ")
    share_selling_amount = input("How many shares are you selling?: ")
    share_price = input("How much is each share worth right now?: ")
    with open('C:\\Users\\jqngu\\OneDrive\\Desktop\\Stocks tracker\\stocks.txt', 'a') as file:
            stocks = file.write("SELL" + "," + share_type + "," + date + "," + share_selling_amount + "," + share_price + "\n")   

#Creating the read function which reads what is in the file for every action made and saved
def read_action():
    with open('C:\\Users\\jqngu\\OneDrive\\Desktop\\Stocks tracker\\stocks.txt', 'r') as file:
        stocks = file.read()
        print(stocks)

#Main loop that asks the user what they want to do
running = True

while running is True:
    action = input("Would you like to (B)uy or (S)ell or (R)ead or (Q)uit?: ")  

    if action == "Q":
        running = False    

    if action == "B":
        buy_action()

    if action == "S":
        sell_action()

    if action == "R":
        read_action()