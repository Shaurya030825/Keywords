def calculate_change(paid,price):
    change= paid - price
    return change

ticket_price= 30
print("===PARKING TICKET PAYMENT HELPER===")
print(f"This parking ticket costs {ticket_price} units.")
print("Accepted Coins: 1,5,20,25\n")

total_Inserted= 0
coins_inserted= 0

while True:
    coin= int(input("Insert a coin(1, 5,20, 25):"))
    if coin != 1 and coin != 5 and coin != 20 and coin != 25:
        print("Invalid Coin, try again!\n")
        continue
    total_Inserted +=1
    coins_inserted+= 1
    print(f"Inserted {coin}. Total so far: {total_Inserted}\n")

    if total_Inserted >= ticket_price:
        print("Enough money inserted")
        break
change_due= calculate_change(total_Inserted, ticket_price)

print("Printing your paarking ticket.")

if change_due==0:
    pass
else:
    print("Here is your change: {change_due } units.")

print("===\n Payment Summary===")
print("Ticket price:", ticket_price)
print("Coins inserted:", coins_inserted)
print("Total paid:", total_Inserted)
print("Change given:", change_due)
print("=======================")
print("Parking Ticket Payment Complete!")