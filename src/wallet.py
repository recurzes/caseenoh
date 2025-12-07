import models
import db
class Wallet:
    def __init__(self, user: models.User):
        self.user = user

    def process_deposit(self, amount: float):
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
            cursor.execute(query, (amount, self.user.get_username()))
            connection.commit()

            self.user.update_balance(amount)
            print(f"\n💰 Deposit of ${amount:.2f} successful!")
            print("")
            return True

        except Exception as e:
            print("❌ Deposit failed:", e)
            return False

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def process_withdrawal(self, amount: float):
        if amount <= 0:
            print("Deposit amount must be positive")

        try:
            connection = db.get_connections()
            cursor = connection.cursor()

            query = """
                    UPDATE users
                    SET balance = balance - ?
                    WHERE username = ?
                    """

            cursor.execute(query, (amount, self.user.get_username()))
            connection.commit()

            self.user.update_balance(amount)
            print(f"Withdrawal of ${amount:.2f} to GCash number {self.user.get_user_info(6)} successful!")
            print("")
            return True

        except Exception as e:
            print("Withdrawal failed")
            return False

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def process_deduction(self, amount: float):
        if amount <= 0:
            print("Deposit amount must be positive")

        try:
            connection = db.get_connections()
            cursor = connection.cursor()

        except Exception as e:
            print("Deduction failed")
            return False

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def process_win(self, amount: float):
        if amount <= 0:
            print("Winning amount must be positive")

        try:
            connection = db.get_connections()
            cursor = connection.cursor()

            query = """
                    UPDATE users
                    SET balance = balance + ?
                    WHERE username = ?
                    """

            cursor.execute(query, (amount, self.user.get_username()))
            connection.commit()

            self.user.update_balance(amount)
            print(f"You won a total of ${amount:.2f} and has been added to account!")
            print("")
            return True

        except Exception as e:
            print("Adding winnings failed")
            return False




