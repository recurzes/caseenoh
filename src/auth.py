import hashlib
import mysql.connector
import db
from models import User
import ui

class Authentication:

    current_user = None

    def __init__(self):
        self.current_user = None

    def register(self, username, password, email, name, last_name, b_day, contact_no):
        connections = db.get_connections()
        cursor = connections.cursor()

        try:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            query = """
            INSERT INTO users (username, password, email, first_name, last_name, birth_month, birth_day, birth_year, contact_number)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            values = (username,
                hashed_password,
                email,
                name,
                last_name,
                b_day[0],
                b_day[1],
                b_day[2],
                contact_no)
            cursor.execute(query, values)
            connections.commit()
            print("\n✅ Registration successful.")
            return True

        except mysql.connector.errors.IntegrityError:
            print("\n❌ Username already exists.")
            return False

        except Exception as e:
            print("\n❌ Error during registration:", e)
            return False

        finally:
            cursor.close()
            connections.close()

    def login(self, username, password):
        connections = db.get_connections()
        cursor = connections.cursor()

        try:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            query = """
                    SELECT id,
                           username,
                           password,
                           email,
                           first_name,
                           last_name,
                           birth_month,
                           birth_day,
                           birth_year,
                           contact_number,
                           balance
                    FROM users
                    WHERE username = ? 
                    """

            cursor.execute(query, (username,))
            result = cursor.fetchone()

            if result and result[2] == hashed_password:
                self.current_user = User(
                    id=result[0],
                    username=result[1],
                    password=result[2],
                    email=result[3],
                    name=result[4],
                    last_name=result[5],
                    b_day=(result[6], result[7], result[8]),
                    contact_no=result[9],
                    balance=float(result[10])
                )

                print(f"\n👋 Welcome back, {username}!")
                return True
            else:
                print("\n❌ Invalid username or password.")
                return False

        except Exception as e:
            print("\n❌ Login error:", e)
            return False

        finally:
            cursor.close()
            connections.close()

    def logout(self):
        if self.current_user:
            print(f"\nLogged out: {self.current_user.get_username()}")
            self.current_user = None

    def profile(self):
        self.current_user.over_display()

    def get_user(self, value):
        self.current_user.get_user_info(value)

    def get_profile_info(self):
        self.current_user.display_profile_info()
        ui.pause()

    def get_ids(self):
        return self.current_user.get_id()
