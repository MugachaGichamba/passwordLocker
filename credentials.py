class Credentials:
    credentials = []

    def __init__(self, username, account, password):
        """
        constructor for credential class
        :param username:
        :param username:
        :param password:
        """
        self.username = username
        self.account = account
        self.password = password

    def save_credential(self):
        """
        save a newly created user
        """
        Credentials.credentials.append(self)

