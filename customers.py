
# Reflection 1:
# I would use .get() when a field might be missing, so my program does not crash.
# I would use brackets when I know the key exists and need its value.

# Reflection 2:
# This reminds me of an Excel PivotTable because it groups and totals data.
# Python can be more useful for large datasets because it can automate the process.

# Exercise 1 - One customer
customer = {
    "name": "Alice",
    "email": "alice@gmail.com",
    "tier": "gold",
    "ytd_spend": 1500
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# Exercise 2 - Update and add
customer["phone"] = "555-1234"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

# Exercise 3 - Safe lookup
print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")

# Exercise 4 - Iterate
for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only gives the keys.
for key in customer:
    print(key)

# Exercise 5 - Lookup table
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)
final_price = 200 * (1 - discount)

print("Tier:", tier)
print("Discount:", f"{discount:.0%}")
print("Final price:", f"${final_price:.2f}")

# Exercise 6 - List of dictionaries
customers = [
    customer,
    {"name": "Bob", "tier": "silver"},
    {"name": "Charlie", "tier": "bronze"}
]

for person in customers:
    tier = person["tier"]
    rate = tier_discounts.get(tier, 0)
    amount = 300 * rate
    print(f"{person['name']}: {tier}, discount ${amount:.2f}")

# Exercise 7 - Nested catalog
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product}")

# Exercise 8 - Sales by region
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]
    sales[region] = sales.get(region, 0) + amount

for region in sorted(sales):
    print(f"{region}: {sales[region]}")
