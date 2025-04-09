STOCK = {
    "mango":10,
    "apple":10,
    "banana":10
}

def in_stock(fruit):
    required = fruit.lower()
    if(required in STOCK):
        return f"Stock contains {STOCK[required]} {required}s"        
    else : return "Not found "

def main():    
    user_input = input("Enter fruit ")  
    print(in_stock(user_input))

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()