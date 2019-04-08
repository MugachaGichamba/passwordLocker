class User:
    """
    blueprint for user accounts

    """
    users = []

    def __init__(self, names,  password ):
        """
        constructor for users
        :param names:
        :param password:
        """
        self.names = names
        self.password = password

    def saveUser(self):
        """
        save a newly created user
        """
        User.users.append(self);