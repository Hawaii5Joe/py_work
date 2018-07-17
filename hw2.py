##USER INPUT VARIABLES
# Using a single function, gather the following user input and store each item as a variable:
# Purchaser name
user_first_name = input("Please provide your first name ")
user_last_name = input("Please provide your last name ")
# Purchaser address
user_street = input("Please provide your street address ")
user_zip = input("Please provide your zip code ")
# Purchaser phone number (entered as 503-555-1211)
user_phone_num = input("Please provide your phone number ")
# Car Make and Model
user_model = input("Please provide your cars model ")
user_make = input("Please provide your cars make ")
# Purchase Price
user_purchase_price = float(input("Please provide sale price "))

#SINGLE FUNCTION
def user_bio(user_first_name, user_last_name, user_make, user_model, user_purchase_price):
    sales_tax = float(user_purchase_price) * float(.101)
    licensing_fee = float(50.45)
    dealer_prep_fee = float(560.55)
    transaction_id = (user_last_name[-4:]) + "_" + (user_phone_num.split("-")[0])
    total_cost = user_purchase_price + sales_tax + licensing_fee + dealer_prep_fee
    # Hello Christopher Robin!
    print("Hello " + user_first_name.capitalize() + " " + user_last_name.capitalize() + " !")
    # Thank you for your purchase of a Nissan Versa. Following is a break down of your total price:
    print(
        "Thank you for your purchase of a " + user_make + " " + user_model + "." + " Following is a break down of your total price:")
    # Sales Price: $2000.00
    print("Sales Price:" + " $" + str("%.2f" % user_purchase_price))
    # Tax: $50.00
    print("Tax:" + " $" + str("%.2f" % sales_tax))
    # Licensing Fee: $50.00
    print("Licensing Fee:" + " $" + str("%.2f" % licensing_fee))
    # Dealer Prep Fee: $50.00
    print("Dealer Prep Fee:" + " $" + str("%.2f" % dealer_prep_fee))
    # Total Price: $2150.00
    print("Total Price:" + " $" + str("%.2f" % total_cost))
    # Unique ID
    print(
        "You have been assigned an ID number of " + transaction_id.upper() + "." " Please refer to this ID number if you have any questions.")

#FUNCTION CALL
user_bio(user_first_name, user_last_name, user_make, user_model, user_purchase_price)
