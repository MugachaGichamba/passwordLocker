class Credentials:
    credentials = []

    def __init__(self, username, credential_name, password):
        """
        constructor for credential class
        :param username:
        :param credential_name:
        :param password:
        """
        self.username = username
        self.credential_name = credential_name
        self.password = password

    def save_credential(self):
        """
        save a newly created user
        """
        Credentials.credentials.append(self);

