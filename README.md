# Hotel Booking Clone

A hotel booking web app built with Python, Django and MySQL, with separate customer and admin areas.

**Customers** can search available rooms by city, room type and amenities, see availability and book a room,
with payment through Razorpay (test mode).

**Admins** get a dashboard to add hotels and rooms, manage room inventory, view bookings and manage customers.

## Tech stack

Python · Django · MySQL · Django ORM / QuerySets · HTML · CSS · Razorpay

## Project structure

```
hotelbooking/
├── hotelbooking/   # project settings and URLs
├── customerapp/    # search, booking and payment flow
├── adminapp/       # admin dashboard: hotels, rooms, bookings, customers
└── media/          # sample hotel images
```

## Run locally

1. Create and activate a virtual environment, then install dependencies:
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows (macOS/Linux: source venv/bin/activate)
   pip install -r requirements.txt mysqlclient
   ```
2. Create a MySQL database (default name `hotelbooking`) and set the connection details as environment variables:
   `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`.
3. Optional: `RAZOR_KEY_ID` / `RAZOR_KEY_SECRET` (Razorpay test keys), `EMAIL_HOST_USER` / `EMAIL_HOST_PASSWORD`,
   and `DJANGO_SECRET_KEY`.
4. Apply migrations and start the server:
   ```bash
   cd hotelbooking
   python manage.py migrate
   python manage.py runserver
   ```

Built during my Python full-stack apprenticeship at Ypsilon IT Solutions (2024).
