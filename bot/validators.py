def validate_side(side):
    """
    Validate order side.
    """
    side = side.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL.")

    return side


def validate_order_type(order_type):
    """
    Validate order type.
    """
    order_type = order_type.upper()

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT.")

    return order_type


def validate_quantity(quantity):
    """
    Validate order quantity.
    """

    quantity = float(quantity)

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")

    return quantity


def validate_price(price):
    """
    Validate limit order price.
    """

    price = float(price)

    if price <= 0:
        raise ValueError("Price must be greater than 0.")

    return price


def validate_symbol(symbol):
    """
    Validate trading symbol.
    """

    symbol = symbol.upper()

    if len(symbol) < 6:
        raise ValueError("Invalid trading symbol.")

    return symbol