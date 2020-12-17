class IUserService:
    def get_user_by_id(self, user_id): raise NotImplementedError
    def get_user_by_email(self, email): raise NotImplementedError
    def is_exists_user_by_username(self, username): raise NotImplementedError
    def is_exists_user_by_email(self, email): raise NotImplementedError
    def register_user(self, email, password): raise NotImplementedError
    def get_user_for_login(self, email, password): raise NotImplementedError
    def get_all_users(self): raise NotImplementedError
    def get_user_by_activate_code(self, activate_code): raise NotImplementedError
    def activate_user(self, user): raise NotImplementedError
    def is_exists_user_by_password(self, password): raise NotImplementedError
    def get_user_by_email_for_change_pass(self, email): raise NotImplementedError
    def send_reset_password(self, email): raise NotImplementedError
    def update_password(self, user , new_password): raise NotImplementedError
    def create_new_active_code(self, user): raise NotImplementedError
    def user_update_data(self, user_id, avatar, gender, website, phone, address, last_name, first_name, states, city): raise NotImplementedError
    def user_update_password(self, user_id, old_password, new_password): raise NotImplementedError
