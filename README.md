# Online Payment and Billing Management System (OPBMS)

OPBMS is a Django-based web application that simulates online billing, subscription renewals, and payment tracking. It replaces payment gateways with in-app simulations, making it ideal for academic demonstrations and internal billing workflows.

## Key Features

### Admin
- Sign in through the Django admin site or dedicated admin workspace
- Create customer accounts (username, email, password, profile details)
- Assign one-time bills with title, amount, due date, and bill type
- Configure recurring monthly subscriptions (OTT plans, memberships, donations, etc.)
- Pause/resume subscriptions; the system auto-generates monthly bills until cancelled
- View a realtime dashboard with outstanding amounts and recent payments
- Inspect a user’s profile, bills, subscriptions, and transactions in one place

### Customer
- Secure login using credentials issued by admins
- Dashboard summarising pending bills, recent payments, and active subscriptions
- Simulate bill payments (status instantly changes to “Paid” and creates a transaction)
- Create and manage personal monthly subscriptions; bills generate automatically each cycle
- Review payment history and spending analytics via Chart.js bar and pie charts
- Update profile details (full name, phone, address)

### System Behaviour
- Uses Django’s built-in `auth.User` model with an extended `Profile`
- `Bill`, `Subscription`, and `Transaction` models capture the core billing domain
- Automatic subscription bill generation occurs whenever dashboards are loaded
- All payments are simulated and recorded as “Simulated” transactions—no gateway integration required
- Supports SQLite out of the box; can be configured for PostgreSQL

## Technology Stack

- **Backend:** Django 5.2.7, Python 3.8+
- **Database:** SQLite (default) or PostgreSQL
- **Frontend:** Django templates, HTML5, CSS, Chart.js
- **Authentication:** Django’s built-in authentication and sessions

## Getting Started

1. **Clone & enter the project folder**
   ```bash
   cd opbms
   ```

2. **Create & activate a virtual environment** (recommended)
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Apply database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** for Django admin access
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Visit the app**
   - Customer portal: http://127.0.0.1:8000/
   - Admin workspace: http://127.0.0.1:8000/admin/
   - Django admin site: http://127.0.0.1:8000/django-admin/

## Usage Flow

### Admin Workflow
1. Sign in via `/admin/dashboard/` (or `/django-admin/` for full admin site)
2. Create customer accounts (`Customers → Create Customer`)
3. Assign one-time bills or create recurring subscriptions for any user
4. Monitor outstanding balances and recent payments from the dashboard

### Customer Workflow
1. Log in at `/login/` with provided credentials
2. Review upcoming bills and active subscriptions from the dashboard (`/portal/`)
3. Simulate payment to mark a bill as paid
4. Create personal subscriptions with monthly renewals
5. Analyse spending history through charts or view detailed transaction logs
6. Keep profile information up to date in the profile section

## Core Models

| Model         | Purpose |
|---------------|---------|
| `Profile`     | Extends `auth.User` with full name, phone, address |
| `Bill`        | Represents a single bill with status (Paid/Unpaid) |
| `Subscription`| Defines recurring monthly charges with next renewal date |
| `Transaction` | Records simulated payment events |

Recurring subscriptions automatically generate a new `Bill` for each cycle until the subscription is paused.

## Project Structure

```
opbms/
├── billingapp/        # Core models, forms, utilities (bills, subscriptions, transactions)
├── billingplatform/   # Global Django settings, URLs, root views
├── adminportal/       # Admin-facing workspace (dashboards, customer management)
├── customerportal/    # Customer-facing portal (dashboard, analytics, payments)
├── templates/         # Shared templates for landing/staff/customer UI
├── static/            # CSS, JS, and assets
└── manage.py          # Django management script
```

## Configuration Notes

- **Database:** Update `DATABASES` in `billingplatform/settings.py` if you prefer PostgreSQL.
- **Authentication:** `LOGIN_URL`, `LOGIN_REDIRECT_URL`, and `LOGOUT_REDIRECT_URL` are preconfigured.
- **Recurring engine:** `billingapp.utils.ensure_subscription_bills` is invoked whenever dashboards load; adjust scheduling if you integrate Celery or CRON.
- **Styling:** Base styles live in `static/css/style.css`; Chart.js assets are loaded from a CDN.

## Development Tips

- Use Django admin (`/django-admin/`) for inspecting raw models during development.
- When running migrations after structural changes, delete `db.sqlite3` if you need a clean schema.
- Extend forms or templates as needed—each app keeps presentation logic separated.

## License

This project is intended for educational and demonstration purposes. Adapt it freely for learning or internal tooling.
