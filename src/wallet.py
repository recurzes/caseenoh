import models
import db
class Deposit:
    def process_deposit(self, user: models.User, amount: float):
        if amount <= 0:
            print("❌ Deposit amount must be positive.")
            return False

        try:
            connection = db.get_connections()
            cursor = connection.cursor()

            query = """
                    UPDATE users
                    SET balance = balance + ?
                    WHERE username = ?
                    """
            cursor.execute(query, (amount, user.get_username()))
            connection.commit()

            user.update_balance(amount)


            print(f"\n💰 Deposit of ${amount:.2f} successful!")
            print(f"New Balance: ${user.get_balance():.2f}")
            return True

        except Exception as e:
            print("❌ Deposit failed:", e)
            return False

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()