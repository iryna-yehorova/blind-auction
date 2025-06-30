auction = {}

start_auction = True

while start_auction:
    user_name = input("Write client name\n")
    user_bid = int(input("Write client bid in $\n"))

    auction[user_name] = user_bid
    is_again = input("Do you want to add more bids? y/n \n").lower()
    print("\n" * 20)

    if is_again == 'n':
        start_auction = False
        max_bid_user = ""
        max_bid = 0

        for user in auction:
            if auction[user] > max_bid:
                max_bid = auction[user]
                max_bid_user = user

        print(f"The person with the name {max_bid_user} with {max_bid}$ bid.")