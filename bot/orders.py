from bot.client import get_client
from bot.validators import (
    validate_side,
    validate_symbol,
    validate_quantity,
    validate_price
)
from bot.logging_config import setup_logger


logger = setup_logger()


def place_market_order(symbol, side, quantity):
    """
    Place a Market Order.
    """

    try:

        client = get_client()

        symbol = validate_symbol(symbol)
        side = validate_side(side)
        quantity = validate_quantity(quantity)

        logger.info(
            f"Sending MARKET order | "
             f"Symbol={symbol} "
             f"Side={side} "
             f"Quantity={quantity}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity,
        )

        logger.info(
        f"Order Success | "
        f"Order ID={order['orderId']} | "
        f"Status={order['status']} | "
        f"Executed Qty={order['executedQty']}"
)

        return {
            "success": True,
            "order_id": order["orderId"],
            "symbol": order["symbol"],
            "side": order["side"],
            "type": order["type"],
            "status": order["status"],
            "quantity": order["origQty"],
            "executed_quantity": order["executedQty"],
            "price": order["price"]
        }

    except Exception as e:

        logger.error(f"Order Failed | {e}")

        return {
            "success": False,
            "error": str(e)
        }
    
def place_limit_order(symbol, side, quantity, price):
    """
    Place a LIMIT Order.
    """

    try:

        client = get_client()

        symbol = validate_symbol(symbol)
        side = validate_side(side)
        quantity = validate_quantity(quantity)
        price = validate_price(price)

        logger.info(
            f"Sending LIMIT order | "
            f"Symbol={symbol} "
            f"Side={side} "
            f"Quantity={quantity} "
            f"Price={price}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(
            f"Limit Order Success | "
            f"Order ID={order['orderId']} | "
            f"Status={order['status']}"
        )

        return {
            "success": True,
            "order_id": order["orderId"],
            "symbol": order["symbol"],
            "side": order["side"],
            "type": order["type"],
            "status": order["status"],
            "quantity": order["origQty"],
            "price": order["price"]
        }

    except Exception as e:

        logger.error(f"Limit Order Failed | {e}")

        return {
            "success": False,
            "error": str(e)
        }

def cancel_order(symbol, order_id):
    """
    Cancel an existing order.
    """

    try:

        client = get_client()

        symbol = validate_symbol(symbol)

        logger.info(
            f"Cancelling Order | Symbol={symbol} | Order ID={order_id}"
        )

        order = client.futures_cancel_order(
            symbol=symbol,
            orderId=order_id
        )

        logger.info(
            f"Order Cancelled | "
            f"Order ID={order['orderId']} | "
            f"Status={order['status']}"
        )

        return {
            "success": True,
            "order_id": order["orderId"],
            "symbol": order["symbol"],
            "status": order["status"]
        }

    except Exception as e:

        logger.error(f"Cancel Order Failed | {e}")

        return {
            "success": False,
            "error": str(e)
        }