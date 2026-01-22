import configparser
config = configparser.RawConfigParser()
config.read('.\\configurations\\config.ini')

class Read_Config:
    @staticmethod
    def admin_page_url():
        url= config.get('user login info', 'admin_page_url')
        return url

    @staticmethod
    def username():
        url = config.get('user login info', 'username')
        return url

    @staticmethod
    def password():
        url = config.get('user login info', 'password')
        return url

    @staticmethod
    def invalid_username():
        url = config.get('user login info', 'invalid_username')
        return url