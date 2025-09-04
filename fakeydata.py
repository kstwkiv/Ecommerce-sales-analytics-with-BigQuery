import csv
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# -----------------------
# CONFIG
# -----------------------
NUM_CUSTOMERS = 2000
NUM_PRODUCTS = 500
NUM_ORDERS = 50000

regions = ["North", "South", "East", "West"]
categories = ["Electronics", "Fitness", "Footwear", "Home", "Fashion"]
brands = ["TechBrand", "SoundMax", "FitLife", "CompEdge", "Speedster", "HomeEase", "StyleCo"]

# -----------------------
# GENERATE CUSTOMERS
# -----------------------
with open("customers.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["customer_id", "name", "email", "region", "signup_date"])
    
    for i in range(1, NUM_CUSTOMERS + 1):
        writer.writerow([
            f"C{i:04d}",
            fake.name(),
            fake.email(),
            random.choice(regions),
            fake.date_between(start_date="-3y", end_date="today")
        ])

# -----------------------
# GENERATE PRODUCTS
# -----------------------
with open("products.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["product_id", "product_name", "category", "brand", "price"])
    
    for i in range(1, NUM_PRODUCTS + 1):
        category = random.choice(categories)
        brand = random.choice(brands)
        price = round(random.uniform(50, 2000), 2)  # product prices between $50–$2000
        writer.writerow([
            f"P{i:04d}",
            f"{brand} {category} {i}",
            category,
            brand,
            price
        ])

# -----------------------
# GENERATE ORDERS
# -----------------------
with open("orders.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["order_id", "customer_id", "product_id", "order_date", "region", "quantity", "price", "total_amount"])
    
    for i in range(1, NUM_ORDERS + 1):
        customer_id = f"C{random.randint(1, NUM_CUSTOMERS):04d}"
        product_id = f"P{random.randint(1, NUM_PRODUCTS):04d}"
        order_date = fake.date_between(start_date="-2y", end_date="today")
        region = random.choice(regions)
        quantity = random.randint(1, 5)
        price = round(random.uniform(50, 2000), 2)
        total_amount = round(price * quantity, 2)
        
        writer.writerow([
            f"O{i:05d}",
            customer_id,
            product_id,
            order_date,
            region,
            quantity,
            price,
            total_amount
        ])
