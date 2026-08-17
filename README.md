# 🛒 My Online Shop

A full-stack e-commerce web application built with **Django and Python**.  
The project provides a complete online shopping experience with product browsing, search, categories, cart management, checkout, inventory management, authentication, and order tracking.

---

## 🚀 Features

### 👤 User Authentication
- User registration
- User login
- User logout
- Authenticated user information
- User-specific order history

### 🛍️ Product Management
- Product listing
- Product detail pages
- Product images
- Product pricing
- Product descriptions
- Product categories
- Product search
- Category filtering

### 🛒 Shopping Cart
- Add products to cart
- Remove products from cart
- Increase product quantity
- Decrease product quantity
- Cart item total calculation
- Grand total calculation
- Stock availability checking
- Quantity limited according to available stock

### 📦 Inventory Management
- Product stock tracking
- Low-stock warning
- Out-of-stock handling
- Automatic stock reduction after order placement
- Prevent ordering more than available stock

### 💳 Checkout & Orders
- Checkout page
- Customer information
- Order summary
- Order placement
- Cash on Delivery
- Online payment status
- Order confirmation page

### 📍 Order Tracking
- Order history
- Order details
- Order date
- Customer details
- Ordered products
- Order total
- Payment method
- Payment status
- Order status tracking

Order statuses include:

- 🟡 Pending
- 🔵 Processing
- 🚚 Shipped
- 🟢 Delivered
- 🔴 Cancelled

### ⚙️ Admin Panel
- Django Admin panel
- Product management
- Category management
- Order management
- Inventory management
- Order status management

### 📱 User Interface
- Responsive layout
- Navigation bar
- Product cards
- Shopping cart interface
- Checkout interface
- Order tracking interface
- Clean and simple design

---

## 🛠️ Technologies

- **Python**
- **Django**
- **HTML5**
- **CSS3**
- **SQLite**
- **Django Templates**

---

## 📁 Project Structure

```text
online-shop/
├── cart/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── cart.py
│   ├── urls.py
│   └── views.py
│
├── myshop/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── orders/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── shop/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── base.html
│   └── registration/
│
├── media/
│   └── products/
│
├── screenshots/
│   ├── homepage.png
│   ├── cart.png
│   └── orders.png
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore