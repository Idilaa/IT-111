def generate_customer_receipt(
        customer_name: str, 
        subtotal: float, 
        tax: float):
    
    # Calculate
    total = subtotal + tax

    # print
    customer_receipt = f"Hello {customer_name}, here is your sales receipt:\n"
    customer_receipt += f"Subtotal = $ {subtotal:.2f}\n"
    customer_receipt += f"     Tax = $ {tax:.2f}\n"
    customer_receipt += f"             --------\n"
    customer_receipt += f"   Total = $ {total:.2f}"

    return customer_receipt

# function
receipt = generate_customer_receipt("John", 1234.56, 123.46)
print(receipt)