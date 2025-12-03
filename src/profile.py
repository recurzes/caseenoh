import db
import hashlib
import auth

class Profile:
    def update_profile(self, values, type):
        global query, params
        connection = db.get_connection()
        cursor = connection.cursor()

        try:
            if type == 1:
                query = """
                        UPDATE users
                        SET first_name = %s
                        WHERE id = %s \
                        """
                params = (values,
                          auth.Authentication.current_user.get_id())
            elif type == 2:
                query = """
                        UPDATE users
                        SET last_name = %s
                        WHERE id = %s \
                        """
                params = (values,
                          auth.Authentication.current_user.get_id().get_id(),)
            elif type == 3:
                query = """
                        UPDATE users
                        SET contact_number = %s
                        WHERE id = %s \
                        """
                params = (values,
                          auth.Authentication.current_user.get_id().get_id(),)
            elif type == 4:
                query = """
                        UPDATE users
                        SET birth_month = %s,
                            birth_day   = %s,
                            birth_year  = %s
                        WHERE id = %s \
                        """
                params = (values[0],
                          values[1],
                          values[2],
                          auth.Authentication.current_user.get_id().get_id())
            elif type == 5:
                query = """
                        UPDATE users
                        SET email = %s
                        WHERE id = %s \
                        """
                params = (values,
                          auth.Authentication.current_user.get_id().get_id(),)
            elif type == 6:
                query = """
                        UPDATE users
                        SET username = %s
                        WHERE id = %s \
                        """
                params = (values,
                          auth.Authentication.current_user.get_id().get_id())
            elif type == 7:
                hashed_password = hashlib.sha256(values.encode()).hexdigest()
                query = """
                        UPDATE users
                        SET password = %s
                        WHERE id = %s \
                        """
                params = (hashed_password,
                          auth.Authentication.current_user.get_id(),)

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
        connection = db.get_connection()
        cursor = connection.cursor()

        try:
            query = """DELETE 
                       FROM users
                       WHERE id = %s;"""

            values = (
                self.current_user.get_id(),
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

