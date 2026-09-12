result = []
name = 0

#Creating the load data function
def load_data():
    with open('C:\\Users\\jqngu\\OneDrive\\Desktop\\Stocks tracker\\stocks.txt', 'r') as file:

        reading_file = True
        while reading_file:
            entry = file.readline()
            cleaned = entry.rstrip("\n")
            print(cleaned)
            if (cleaned == ""):
                reading_file = False

            entries = cleaned.split(',')
            new_row = []
            new_row.append(entries)
            result.append(new_row)

    specific_row = int(input("Which of these columns would you like added up?: "))

    for row in result:
        name += int(row[specific_row-1])
    print(result)
    print(name)

#Creating the buy function
def buy_action():
    array = []
    share_type = input("What is the share name you are purchasing?: ")
    date = input("What is the date of purchase?: ")
    share_purchasing_amount = input("How many shares are you purchasing?: ")
    share_price = input("How much is each share worth right now?: ")
    with open('C:\\Users\\jqngu\\OneDrive\\Desktop\\Stocks tracker\\stocks.txt', 'a') as file:
            saved_stock_info = "BUY" + "," + share_type + "," + date + "," + share_purchasing_amount + "," + share_price
            file.write(f"{saved_stock_info}\n")

#Creating the sell function
def sell_action():

    share_type = input("What is the share name you are selling?: ")
    date = input("What is the date of selling?: ")
    share_selling_amount = input("How many shares are you selling?: ")
    share_price = input("How much is each share worth right now?: ")

    with open('C:\\Users\\jqngu\\OneDrive\\Desktop\\Stocks tracker\\stocks.txt', 'a') as file:
            stocks = file.write("SELL" + "," + share_type + "," + date + "," + share_selling_amount + "," + share_price + "\n")   

#Main loop that asks the user what they want to do
running = True
load_data()

while running is True:
    action = input("Would you like to (B)uy or (S)ell or (Q)uit?: ")  

    if action == "Q":
        running = False    

    if action == "B":
        buy_action()

    if action == "S":
        sell_action()