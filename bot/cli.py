import argparse

from bot.orders import (
    place_market_order,
    place_limit_order,
)


def run_cli():
    """
    Read command-line arguments
    and execute the correct order.
    """

    parser = argparse.ArgumentParser(
    description="Binance Futures Testnet Trading Bot",
    epilog="""
Examples:

Market Order:
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

Limit Order:
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 90000
""",
    formatter_class=argparse.RawDescriptionHelpFormatter
)

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading pair (e.g. BTCUSDT, ETHUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        choices=["BUY", "SELL"],
        help="Order side (BUY or SELL)"
    )

    parser.add_argument(
        "--type",
        required=True,
        choices=["MARKET", "LIMIT"],
        help="Order type (MARKET or LIMIT)"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float,
        help="Order Quantity"
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Limit Price"
    )

    

    args = parser.parse_args()

    print("\n" + "=" * 40)
    print("ORDER SUMMARY")
    print("=" * 40)
    print(f"Symbol     : {args.symbol}")
    print(f"Side       : {args.side}")
    print(f"Order Type : {args.type}")
    print(f"Quantity   : {args.quantity}")

    if args.type == "LIMIT":
      print(f"Price      : {args.price}")

    print("=" * 40)

    if args.type == "MARKET" and args.price is not None:
      parser.error("--price should not be provided for MARKET orders.")

    if args.type == "MARKET":

        result = place_market_order(
            args.symbol,
            args.side,
            args.quantity,
        )

    else:

        if args.price is None:

            parser.error(
                "--price is required for LIMIT orders."
            )

        result = place_limit_order(
            args.symbol,
            args.side,
            args.quantity,
            args.price,
        )

    # print(result)
    print("\n" + "=" * 40)

    if result.get("success"):
      print("ORDER PLACED SUCCESSFULLY")
      print("=" * 40)

      print(f"Order ID         : {result.get('order_id')}")
      print(f"Symbol           : {result.get('symbol')}")
      print(f"Side             : {result.get('side')}")
      print(f"Order Type       : {result.get('type')}")
      print(f"Status           : {result.get('status')}")
      print(f"Quantity         : {result.get('quantity')}")

      if result.get("executed_quantity") is not None:
        print(f"Executed Qty     : {result.get('executed_quantity')}")

      if result.get("price"):
        print(f"Price            : {result.get('price')}")

    else:
      print("ORDER FAILED")
      print("=" * 40)
      print(result.get("error"))

    print("=" * 40)