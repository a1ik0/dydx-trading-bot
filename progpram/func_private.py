from datetime import datetime, timedelta
import time
from pprint import pprint
from func_utils import format_number


# Place market order
def place_market_order(client, market, side, size, price, reduce_only):
    # Get Position Id
    account_response = client.private.get_account()
    position_id = account_response.data["account"]["positionId"]

    # Get expiration time
    server_time = client.public.get_time()
    expiration = datetime.fromisoformat(
        server_time.data["iso"].replace("Z", "")
    ) + timedelta(seconds=7000)

    # Place an order
    placed_order = client.private.create_order(
        position_id=position_id,  # required for creating the order signature
        market=market,
        side=side,
        order_type="MARKET",
        post_only=False,
        size=size,
        price=price,
        limit_fee="0.015",
        expiration_epoch_seconds=time.time() + 65,
        time_in_force="FOK",
        reduce_only=reduce_only,
    )

    # Return results
    return placed_order.data


# Abort all open positions
def abort_all_positions(client):
    # Cancel all orders
    client.private.cancel_all_orders()

    # Protect API
    time.sleep(0.5)

    # Get markets for reference of tick size
    markets = client.public.get_markets().data

    # Protect API
    time.sleep(0.5)

    # Get all positions
    positions = client.private.get_positions(status="OPEN")
    all_positions = positions.data["positions"]

    # Handle open positions
    close_orders = []
    if len(all_positions) > 0:
        # Loop through each position
        for position in all_positions:
            # Determine market
            market = position["market"]

            # Determine side
            side = "BUY"
            if position["side"] == "LONG":
                side = "SELL"

            # Get price
            price = float(position["entryPrice"])
            accept_price = price * 1.7 if side == "BUY" else price * 0.3
            tick_size = markets["markets"][market]["tickSize"]
            accept_price = format_number(accept_price, tick_size)

            # Place order to close
            order = place_market_order(
                client, market, side, position["sumOpen"], accept_price, True
            )

            # Append the result
            close_orders.append(order)

            # Protect API
            time.sleep(0.5)

        # Return closed orders
        return close_orders
