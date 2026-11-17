
import asyncio
import random

highest_bid = 0
winner = None
auction_open = True
locked = False
last_bid_time = 0

lock = asyncio.Lock()
bid_event = asyncio.Event()


async def fake_user(user):
    global highest_bid, winner, auction_open, last_bid_time

    name = user["name"]

    while auction_open:
        await asyncio.sleep(random.uniform(1, 3))

        async with lock:
            if not auction_open or locked:
                break

            price = highest_bid + random.randint(1000, 10000)

            highest_bid = price
            winner = name
            last_bid_time = asyncio.get_running_loop().time()

            print(name, "offered:", price,"$")

            bid_event.set()


async def auction(users, product):
    global highest_bid, winner, auction_open
    global locked, last_bid_time

    highest_bid = int(product["price"])
    winner = None
    auction_open = True
    locked = False

    loop = asyncio.get_running_loop()
    start_time = loop.time()
    last_bid_time = start_time

    bid_event.clear()

    print("PRODUCT:", list(product.keys())[0])
    print("STARTING PRICE:", highest_bid)
    print("AUCTION STARTED!")

    tasks = [
        asyncio.create_task(fake_user(user))
        for user in users
    ]

    while True:
        async with lock:
            now = loop.time()

            remaining = 1200 - (now - start_time)
            idle_time = 10 - (now - last_bid_time)

            if remaining <= 0 or idle_time <= 0:
                locked = True
                auction_open = False
                break

            bid_event.clear()
            timeout = min(remaining, idle_time)

        try:
            await asyncio.wait_for(
                bid_event.wait(),
                timeout=timeout
            )
        except asyncio.TimeoutError:
            continue

    print("PRICE LOCKED!")

    for i in range(3, 0, -1):
        print(f"{i} seconds left...")
        await asyncio.sleep(1)

    await asyncio.gather(*tasks)

    print("AUCTION CLOSED!")

    if winner:
        print("Winner:", winner)
        print("Highest price:", highest_bid)
    else:
        print("No bids!")
