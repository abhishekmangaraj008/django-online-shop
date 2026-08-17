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
```

---

## 📸 Screenshots

### 🏠 Homepage

![Homepage](screenshots/homepage.png)

### 🛒 Shopping Cart

![Shopping Cart](screenshots/cart.png)

### 📦 My Orders

![My Orders](screenshots/orders.png)

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/abhishekmangaraj008/django-online-shop.git
cd django-online-shop
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```powershell
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create an admin user

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## 👨‍💻 Admin Panel

The Django Admin panel can be accessed at:

```text
http://127.0.0.1:8000/admin/
```

The admin panel can be used to manage:

- Products
- Categories
- Stock
- Orders
- Order status
- Payment status

---

## 🛒 Main User Flow

```text
Register / Login
       ↓
Browse Products
       ↓
Search / Filter Products
       ↓
View Product Details
       ↓
Add Product to Cart
       ↓
Manage Quantity
       ↓
Checkout
       ↓
Enter Customer Details
       ↓
Place Order
       ↓
Order Confirmation
       ↓
View My Orders
       ↓
Track Order Status
```

---

## 📌 Project Highlights

- Full-stack Django e-commerce application
- User authentication and authorization
- Product and category management
- Session-based shopping cart
- Inventory and stock management
- Checkout and order processing
- Order history and tracking
- Django Admin integration
- Responsive web interface

---

## 👨‍💻 Author

**Abhishek Mangaraj**

### GitHub

https://github.com/abhishekmangaraj008