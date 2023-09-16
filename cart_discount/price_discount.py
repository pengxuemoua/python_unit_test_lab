def main():

    #print(discount([10, 4, 20]))  # Expect this to print 4
    # what other lists might this function be called with?
    display_total = discount([-8.25, -96.85, -101, -8578])
    print(f'You recieved a discount of: ${display_total}')

def discount(item_prices):
    """ Complete this function that returns the discount earned for a list of item prices
    If a customer has ordered more than three items, the cheapest item is free.
    Example: if this function is called with a list of [10, 4, 20] then return 4.
    """
    
    try:
        total_items = len(item_prices)
        if total_items >= 3:
            min_price = min(item_prices)
            if min_price < 0:
                raise ValueError('Sorry, please enter a value of 0 or greater.')
            return min_price
        elif total_items < 3: 
            return None
    except TypeError:
        return None

if __name__ == '__main__':
    main()