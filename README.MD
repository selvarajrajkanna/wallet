## Wallet Transaction System

This is a wallet transaction system developed using Django and Django Rest Framework. It allows users to create wallets, credit/debit money, and retrieve balances and transaction history.

### Setup Instructions

Follow these steps to set up and run the system in your local environment:
### 1. Clone the Repository

```commandline
git clone https://github.com/yourusername/wallet-transaction-system.git
cd wallet-transaction-system
```

2. Install Dependencies

```commandline
pip install -r requirements.txt
```

3. Run Migrations
```commandline
python manage.py migrate
```

4. Start the Development Server
```commandline
python manage.py runserver
```

The development server should now be running at http://localhost:8000/.

### Usage
#### API Endpoints

Create Wallet: POST /create_wallet/  
Credit Money: POST /credit_money/  
Debit Money: POST /debit_money/  
Get Balance: GET /get_balance/<user_id>/  
Get Transaction History: GET /get_transaction_history/<wallet_id>/<start_date>/<end_date>/  

### API Examples

Create Wallet

```commandline
curl -X POST http://localhost:8000/create_wallet/ -d "user=1&balance=100&minimum_balance=10"
```

Credit Money
```commandline
curl -X POST http://localhost:8000/credit_money/ -d "wallet=1&amount=50"
```

Debit Money
```commandline
curl -X POST http://localhost:8000/debit_money/ -d "wallet=1&amount=30"
```

Get Balance
```commandline
curl http://localhost:8000/get_balance/1/
```

Get Transaction History
```commandline
curl http://localhost:8000/get_transaction_history/1/2024-04-01/2024-04-30/
```

#### Notes

Ensure you have Python and pip installed on your system.
This system uses SQLite as the default database.
Make sure to customize settings, such as authentication and authorization, based on your requirements.
For production use, consider deploying on a production server and securing it properly.

#### Contributors

[@Selvaraj rajkanna S](https://github.com/selvarajrajkanna/)
