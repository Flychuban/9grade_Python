class Contact():
    def __init__(self, name, phone_number, sec_number, email, instagram_profile, facebook_profile) -> None:
        self._name = name
        self._phone_number = phone_number
        self._email = email
        self._instagram_profile = instagram_profile
        self._sec_number = sec_number
        self._facebook_profile = facebook_profile
        
        def get_name(self):
            return self._name
        
        def get_phone_number(self):
            return self._phone_number
        
        def get_email(self):
            return self._email
        
        def get_instagram_profile(self):
            return self._instagram_profile
        
        def get_sec_number(self):
            return self._sec_number
        
        def get_facebook_profile(self):
            return self._facebook_profile
        
        def set_name(self, new_name):
            self._name = new_name
        
        def set_phone_number(self, new_phone_number):
            self._phone_number = new_phone_number
        
        def set_email(self, new_email):
            self._email = new_email
            
        def set_instagram_profile(self, new_instagram_profile):
            self._instagram_profile = new_instagram_profile
        
        def set_sec_number(self, new_sec_number):
            self._sec_number = new_sec_number
        
        def set_facebook_profile(self, new_facebook_profile):
            self._facebook_profile = new_facebook_profile