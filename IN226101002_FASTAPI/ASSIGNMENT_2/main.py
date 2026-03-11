from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

app = FastAPI()

# Initial products list
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 499, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 99, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "USB Hub", "price": 799, "category": "Electronics", "in_stock": False},
    {"id": 4, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": True},
]

# Storage lists
feedback_list = []
orders = []

# Q1 - Filter Products with Query Parameters
@app.get("/products/filter")
def filter_products(
    category: Optional[str] = None,
    max_price: Optional[int] = None,
    min_price: Optional[int] = None
):

    result = products

    if category:
        result = [
            p for p in result
            if p["category"].lower() == category.lower()
        ]

    if max_price:
        result = [
            p for p in result
            if p["price"] <= max_price
        ]

    if min_price:
        result = [
            p for p in result
            if p["price"] >= min_price
        ]

    return {
        "filtered_products": result,
        "count": len(result)
    }


# Q2 - Get Only Product Price
@app.get("/products/{product_id}/price")
def get_product_price(product_id: int):

    for p in products:
        if p["id"] == product_id:
            return {
                "name": p["name"],
                "price": p["price"]
            }

    return {"error": "Product not found"}


# Q3 - Customer Feedback Model
class CustomerFeedback(BaseModel):
    customer_name: str = Field(..., min_length=2)
    product_id: int = Field(..., gt=0)
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = Field(None, max_length=300)


# Q3 - Submit Feedback
@app.post("/feedback")
def submit_feedback(feedback: CustomerFeedback):

    feedback_list.append(feedback.dict())

    return {
        "message": "Feedback submitted successfully",
        "feedback": feedback,
        "total_feedback": len(feedback_list)
    }


# Q4 - Product Summary Dashboard
@app.get("/products/summary")
def product_summary():

    total_products = len(products)

    in_stock_count = len([
        p for p in products
        if p["in_stock"]
    ])

    out_of_stock_count = total_products - in_stock_count

    most_expensive = max(products, key=lambda p: p["price"])
    cheapest = min(products, key=lambda p: p["price"])

    categories = list(set([
        p["category"] for p in products
    ]))

    return {
        "total_products": total_products,
        "in_stock_count": in_stock_count,
        "out_of_stock_count": out_of_stock_count,
        "most_expensive": {
            "name": most_expensive["name"],
            "price": most_expensive["price"]
        },
        "cheapest": {
            "name": cheapest["name"],
            "price": cheapest["price"]
        },
        "categories": categories
    }


# Q5 - Order Item Model
class OrderItem(BaseModel):
    product_id: int = Field(..., gt=0)
    quantity: int = Field(..., ge=1, le=50)


# Q5 - Bulk Order Model
class BulkOrder(BaseModel):
    company_name: str = Field(..., min_length=2)
    contact_email: EmailStr
    items: List[OrderItem]


# Q5 - Bulk Order Endpoint
@app.post("/orders/bulk")
def place_bulk_order(order: BulkOrder):

    confirmed = []
    failed = []
    total = 0

    for item in order.items:

        product = next(
            (p for p in products if p["id"] == item.product_id),
            None
        )

        if not product:
            failed.append({
                "product_id": item.product_id,
                "reason": "Product not found"
            })
            continue

        if not product["in_stock"]:
            failed.append({
                "product_id": item.product_id,
                "reason": f"{product['name']} is out of stock"
            })
            continue

        subtotal = product["price"] * item.quantity
        total += subtotal

        confirmed.append({
            "product": product["name"],
            "qty": item.quantity,
            "subtotal": subtotal
        })

    return {
        "company": order.company_name,
        "confirmed": confirmed,
        "failed": failed,
        "grand_total": total
    }


# BONUS - Simple Order Model
class Order(BaseModel):
    product_id: int
    quantity: int


# BONUS - Create Order (Pending)
@app.post("/orders")
def create_order(order: Order):

    order_data = order.dict()
    order_data["id"] = len(orders) + 1
    order_data["status"] = "pending"

    orders.append(order_data)

    return order_data


# BONUS - Get Order by ID
@app.get("/orders/{order_id}")
def get_order(order_id: int):

    for order in orders:
        if order["id"] == order_id:
            return order

    return {"error": "Order not found"}


# BONUS - Confirm Order
@app.patch("/orders/{order_id}/confirm")
def confirm_order(order_id: int):

    for order in orders:
        if order["id"] == order_id:
            order["status"] = "confirmed"
            return order

    return {"error": "Order not found"}