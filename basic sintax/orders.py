orders = int(input())
total = 0
order_price = 0
for _ in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if 0.01 <= price_per_capsule <= 100 and 1<= days <= 31 and 1 <= capsules_per_day <= 2000:
        order_price = price_per_capsule * days * capsules_per_day
        print(f"The price for the coffee is: ${order_price:.2f}")
        total += order_price
print(f"Total: ${total:.2f}")