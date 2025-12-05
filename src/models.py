
import re
class User:

    def __init__(self, id, username, password, email, name, last_name, b_day, contact_no, balance=0.0):
        self.id = id
        self._username = username
        self._password = password
        self._email = email
        self.name = name
        self.last_name = last_name
        self.month = int(b_day[0])
        self.day = int(b_day[1])
        self.year = int(b_day[2])
        self.contact_no = int(contact_no)
        self._balance = balance

    def get_id(self):
        return self.id

    def get_username(self):
        return self._username

    def get_balance(self):
        return self._balance

    def get_user_info(self, value):
        if value == 0:
            return self._username
        elif value == 1:
            return self._password
        elif value == 2:
            return self._email
        elif value == 3:
            return self.name
        elif value == 4:
            return self.last_name
        elif value == 5:
            birth = self.month + self.day + self.year
            return birth
        elif value == 6:
            return self.contact_no
        return None

    def update_balance(self, amount):
        self._balance += amount

    def update_user(self, username):
        self._username = username

    def over_display(self):
        print("+" + "-" * 48 + "+")
        print(f"| {'PROFILE':^47}|")
        print("+" + "-" * 48 + "+")
        print(f"| {'Username':<15}: {self._username:<29} |")
        print(f"| {'Balance':<15}: ${self._balance:>10.2f}{'':<18} |")
        print("+" + "-" * 48 + "+")



    def profile_info(self):
        password = self._password
        birth_date = f"{self.month:02d}/{self.day:02d}/{self.year}"
        contact_no = str(self.contact_no)

        masked_password = "*" * (len(password) - 20)

        balance_str = f"${self._balance:,.2f}"
        if self._balance >= 0:
            balance_colored = f"\033[92m{balance_str}\033[0m"
        else:
            balance_colored = f"\033[91m{balance_str}\033[0m"

        fields = ["[1]Username", "[2]Password", "[3]Email", "[4]First Name", "[5]Last Name", "[6]Birth Date",
                  "[7]Contact No.", "Balance"]
        values = [self._username, masked_password, self._email, self.name, self.last_name, birth_date, contact_no,
                  balance_colored]


        def visible_len(s):
            return len(re.sub(r'\033\[[0-9;]*m', '', str(s)))


        max_length = max(visible_len(f) + visible_len(v) + 5 for f, v in zip(fields, values))
        width = max(max_length, 50)

        print("+" + "-" * width + "+")
        print(f"| {'PROFILE INFO':^{width}} |")
        print("+" + "-" * width + "+")

        for field, value in zip(fields, values):
            padding = width - 3 - len(field) - visible_len(value)
            print(f"| {field} : {value}{' ' * padding} |")

        print("+" + "-" * width + "+")

