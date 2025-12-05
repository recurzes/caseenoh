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
        print("-------------------- Profile ---------------------")
        print(f"{'Username:':<10} {self._username:<15} | {'Balance:':<10}${self._balance:>8.2f}")
        print(" ")

    def display_profile_info(self):
        print("Ugma na ni kay kapoy.")