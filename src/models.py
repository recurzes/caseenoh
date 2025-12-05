
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

    def update_user(self, value,  type):
        if type == 1:
            self._username = value
        elif type == 2:
            self._password = value
        elif type == 3:
            self._email = value
        elif type == 4:
            self.name = value
        elif type == 5:
            self.last_name = value
        elif type == 6:
            self.month = int(value[0])
            self.day = int(value[1])
            self.year = int(value[2])
        elif type == 7:
            self.contact_no = value

    def over_display(self):
        balance = f"${self._balance:,.2f}"

        BOX_WIDTH = 60
        INNER_WIDTH = BOX_WIDTH - 2


        HALF = (INNER_WIDTH - 1) // 2

        LEFT_LABEL = "Username"
        RIGHT_LABEL = "Balance"

        left_text = f"{LEFT_LABEL}: {self._username}"
        right_text = f"{RIGHT_LABEL}: {balance}"

        left_text = left_text[:HALF].ljust(HALF)
        right_text = right_text[:HALF].ljust(HALF + 3)

        print("+" + "-" * BOX_WIDTH + "+")
        print(f"| {'PROFILE':^{BOX_WIDTH - 2}} |")
        print("+" + "-" * BOX_WIDTH + "+")
        print(f"|{left_text}│{right_text}|")
        print("+" + "-" * BOX_WIDTH + "+")

    def profile_info(self):
        password = self._password
        birth_date = f"{self.month:02d}/{self.day:02d}/{self.year}"
        contact_no = str(self.contact_no)
        balance = f"${self._balance:,.2f}"
        masked_password = "*" * (len(password) - 55)


        fields = ["Username", "Password", "Email", "First Name", "Last Name", "Birth Date", "Contact No.", "Balance"]
        values = [self._username, masked_password, self._email, self.name, self.last_name, birth_date, contact_no,
                  balance]
        max_length = max(len(f) + len(str(v)) + 5 for f, v in zip(fields, values))
        width = max(max_length, 50)

        print("+" + "-" * width + "+")
        print(f"| {'USER PROFILE':^{width - 2}} |")
        print("+" + "-" * width + "+")

        for field, value in zip(fields, values):
            print(f"| {field:<15}: {str(value):<{width - 19}} |")

        print("+" + "-" * width + "+")


