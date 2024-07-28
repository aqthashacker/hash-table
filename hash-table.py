class UserManagerList:
    def __init__(self):
        self.users = []

    def add_user(self, user_id, user_data):
        self.users.append((user_id, user_data))

    def get_user(self, user_id):
        for uid, udata in self.users:
            if uid == user_id:
                return udata
        return None


class UserManagerDict:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, user_data):
        self.users[user_id] = user_data

    def get_user(self, user_id):
        return self.users.get(user_id, None)


# Example usage for UserManagerList
print("Using List-based UserManager:")
user_manager_list = UserManagerList()
user_manager_list.add_user(1, "Alice")
user_manager_list.add_user(2, "Bob")

print(user_manager_list.get_user(1))  # Output: Alice
print(user_manager_list.get_user(3))  # Output: None

# Example usage for UserManagerDict
print("\nUsing Dictionary-based UserManager:")
user_manager_dict = UserManagerDict()
user_manager_dict.add_user(1, "Alice")
user_manager_dict.add_user(2, "Bob")

print(user_manager_dict.get_user(1))  # Output: Alice
print(user_manager_dict.get_user(3))  # Output: None
