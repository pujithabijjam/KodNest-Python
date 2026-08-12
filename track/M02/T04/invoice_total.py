def display_invoice_total(price, quantity):
    display_invoice = price * quantity
    print("Total:", display_invoice)
price = int(input())
quantity = int(input())
display_invoice_total(price, quantity)