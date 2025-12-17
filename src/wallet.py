import models
import db

class Wallet:
    _instance = None
    _user = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Wallet, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # Don't reset user on repeated __init__ calls
        pass

    @classmethod
    def initialize(cls, user: models.User):
        """Initialize the wallet singleton with a user session."""
        instance = cls()
        cls._user = user
        return instance

    @classmethod
    def clear(cls):
        """Clear the wallet singleton (call on logout)."""
        cls._user = None

    @property
    def user(self):
        if Wallet._user is None:
            raise RuntimeError("Wallet not initialized. Call Wallet.initialize(user) first.")
        return Wallet._user

    def process_deposit(self, amount: float):
        if amount <= 0:
            print("❌ Deposit amount must be positive.")
            return False

        connection = None
        cursor = None
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
            print("❌ Withdrawal amount must be positive")
            return False

        connection = None
        cursor = None
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

            self.user.update_balance(-amount)
            print(f"💵 Withdrawal of ${amount:.2f} to GCash number {self.user.get_user_info(6)} successful!")
            print("")
            return True

        except Exception as e:
            print("❌ Withdrawal failed:", e)
            return False

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def process_deduction(self, amount: float):
        if amount <= 0:
            print("❌ Deduction amount must be positive")
            return False

        connection = None
        cursor = None
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

            self.user.update_balance(-amount)
            print(f"💸 ${amount:.2f} deducted from your account.")
            print("")
            return True

        except Exception as e:
            print("❌ Deduction failed:", e)
            return False

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def process_win(self, amount: float):
        if amount <= 0:
            print("❌ Winning amount must be positive")
            return False

        connection = None
        cursor = None
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
            print(f"🎉 You won a total of ${amount:.2f} and it has been added to your account!")
            print("")
            return True

        except Exception as e:
            print("❌ Adding winnings failed:", e)
            return False

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

