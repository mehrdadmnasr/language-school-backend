# domain/users/entities.py

import uuid
from datetime import datetime
from domain.users.value_objects import FullName # وارد کردن Value Object FullName

class User:
    """
    موجودیت User (کاربر)
    """
    def __init__(
            self,
            user_id=None,
            username=None,
            password_hash=None,
            email=None,
            full_name=None, # جایگزینی first_name و last_name با FullName
            is_active=True,
            date_joined=None,
            last_login=None
    ):
        """
        سازنده کلاس User

        :param user_id: شناسه یکتای کاربر (UUID)
        :param username: نام کاربری
        :param password_hash: رمز عبور کاربر (هش شده)
        :param email: آدرس ایمیل کاربر
        :param full_name: Value Object FullName برای نام کامل کاربر
        :param is_active: وضعیت فعال بودن کاربر (پیش‌فرض: True)
        :param date_joined: تاریخ عضویت کاربر
        :param last_login: آخرین تاریخ ورود کاربر
        """
        self.user_id = user_id if user_id is not None else uuid.uuid4()
        self.username = username
        self.password_hash = password_hash
        self.email = email
        self.full_name = full_name # استفاده از Value Object FullName
        self.is_active = is_active
        self.date_joined = date_joined if date_joined is not None else datetime.now()
        self.last_login = last_login

    def __str__(self):
        return f"User(id={self.user_id}, username={self.username}, full_name={self.full_name})" # به‌روزرسانی __str__

    def activate(self):
        if not self.is_active:
            self.is_active = True

    def deactivate(self):
        if self.is_active:
            self.is_active = False

    def check_password(self, password):
        return self.password_hash == password

    def set_password(self, new_password):
        self.password_hash = new_password

    @property
    def first_name(self): # property برای دسترسی به نام کوچک از Value Object FullName
        return self.full_name.first_name if self.full_name else None

    @property
    def last_name(self): # property برای دسترسی به نام خانوادگی از Value Object FullName
        return self.full_name.last_name if self.full_name else None
