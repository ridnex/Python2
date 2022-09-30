class Password_manager:
    def __init__(self, old_passwords :list):
        self.old_passwords = old_passwords
    def get_password(self):
        return self.old_passwords[-1]
    def set_password(self, new:str):
        if new not in self.old_passwords:
            self.old_passwords.append(new)
    def is_correct(self, attempt):
        if attempt == self.get_password():
            return True
        else:
            return False

passwords= ['123', '789', '156', '1894']
passt = Password_manager(passwords)
print(passt.get_password())
print(passt.is_correct('156'))
passt.set_password('178')
print(passt.get_password())
