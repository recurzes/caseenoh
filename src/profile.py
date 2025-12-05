import db
import hashlib



class Profile:
    def __init__(self, authentication):
        self.authentication = authentication

    def update_profile(self, values, type):
        global query, params
        connection = db.get_connections()
        cursor = connection.cursor()

        try:
            if type == 1:
                query = """
                        UPDATE users
                        SET first_name = ?
                        WHERE id = ? \
                        """
                params = (values,
                          self.authentication.current_user.get_id())
            elif type == 2:
                query = """
                        UPDATE users
                        SET last_name = ?
                        WHERE id = ? \
                        """
                params = (values,
                          self.authentication.current_user.get_id())
            elif type == 3:
                query = """
                        UPDATE users
                        SET contact_number = ?
                        WHERE id = ?
                        """
                params = (values,
                          self.authentication.current_user.get_id())
            elif type == 4:
                query = """
                        UPDATE users
                        SET birth_month = ?,
                            birth_day   = ?,
                            birth_year  = ?
                        WHERE id = ?
                        """
                params = (values[0],
                          values[1],
                          values[2],
                          self.authentication.current_user.get_id())
            elif type == 5:
                query = """
                        UPDATE users
                        SET email = ?
                        WHERE id = ? 
                        """
                params = (values,
                          self.authentication.current_user.get_id())
            elif type == 6:
                query = """
                        UPDATE users
                        SET username = ?
                        WHERE id = ? 
                        """
                params = (values,
                          self.authentication.current_user.get_id())
                self.authentication.current_user.update_user(values)
            elif type == 7:
                hashed_password = hashlib.sha256(values.encode()).hexdigest()
                query = """
                        UPDATE users
                        SET password = ?
                        WHERE id = ?
                        """
                params = (hashed_password,
                          self.authentication.current_user.get_id())

            cursor.execute(query, params)
            connection.commit()

            print("\n✅ Account Updated!.")
            return True

        except Exception as e:
            print("\n❌ Error during registration:", e)
            return False

        finally:
            cursor.close()
            connection.close()

    def delete_account(self):
        connection = db.get_connections()
        cursor = connection.cursor()

        try:
            query = """DELETE
                       FROM users
                       WHERE id = ?;"""

            values = (
                self.authentication.current_user.get_id(),
            )
            cursor.execute(query, values)
            connection.commit()

            print("\n✅ Account Deleted.")
            return True

        except Exception as e:
            print("\n❌ Error during registration:", e)
            return False

        finally:
            cursor.close()
            connection.close()

