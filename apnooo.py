menu = {
    'Churma': 80,
    'Bati': 60,
    'Dal': 70,
    'Roti': 15,
    'Aachar': 25,
    'Lahesun Chatni': 20,
    'Chhach': 40,
    'Papad': 10,
    'Gulab Jamun': 50,
}

def display_menu():
    print("\n" + "="*40)
    print("          APPNOO RESTAURANT MENU")
    print("="*40)
    for item, price in menu.items():
        print(f"{item:12} - ₹{price}")
    print("="*40)

def get_quantity(item_name):
    while True:
        try:
            quantity = int(input(f"How many {item_name}s would you like? "))
            if quantity > 0:
                return quantity
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

def calculate_discount(total):
    if total > 500:
        discount = total * 0.10
        print(f"🎉 You got a 10% discount! Saved: ₹{discount:.2f}")
        return total - discount
    return total

def main():
    print("Welcome to Appnoo Restaurant! 🍽️")
    
    order_total = 0
    ordered_items = {}
    continue_ordering = True

    while continue_ordering:
        display_menu()
        
        item = input("\nEnter the item name you want to order : ").strip().title()
        
        if item.lower() == 'done':
            break
        
        if item in menu:
            quantity = get_quantity(item)
            item_total = menu[item] * quantity
            order_total += item_total
            
            if item in ordered_items:
                ordered_items[item] += quantity
            else:
                ordered_items[item] = quantity
            
            print(f"✅ Added {quantity} {item}(s) - ₹{item_total}")
        else:
            print(f"❌ '{item}' is not available. Please choose from the menu.")
            continue
        
        another = input("Add another item? (yes/no): ").lower()
        continue_ordering = another in ['yes', 'y']

    if ordered_items:
        print("\n" + "="*40)
        print("           ORDER SUMMARY")
        print("="*40)
        for item, quantity in ordered_items.items():
            print(f"{item:12} x{quantity:2} - ₹{menu[item] * quantity}")
        print("="*40)
        
        final_total = calculate_discount(order_total)
        print(f"TOTAL AMOUNT: ₹{final_total:.2f}")
        print("="*40)
        print("Thank you for your order! 🎉")
    else:
        print("No items were ordered. Goodbye!")

if __name__ == "__main__":
    main()
