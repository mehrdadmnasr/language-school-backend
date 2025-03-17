# domain/users/value_objects.py

"""
Value Objects مربوط به اپلیکیشن users
"""

class FullName:
    """
    Value Object برای نام کامل کاربر
    """
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._validate() # فراخوانی متد اعتبارسنجی در سازنده

    def _validate(self):
        """
        متد داخلی برای اعتبارسنجی نام کامل
        قوانین اعتبارسنجی ساده به عنوان نمونه
        در پروژه‌های واقعی، اعتبارسنجی‌های دقیق‌تر و جامع‌تر مورد نیاز است.
        """
        if not self.first_name:
            raise ValueError("نام کوچک نمی‌تواند خالی باشد.")
        if not self.last_name:
            raise ValueError("نام خانوادگی نمی‌تواند خالی باشد.")
        if not isinstance(self.first_name, str) or not isinstance(self.last_name, str):
            raise TypeError("نام و نام خانوادگی باید رشته باشند.")
        if len(self.first_name) > 150 or len(self.last_name) > 150:
            raise ValueError("نام و نام خانوادگی نمی‌توانند بیشتر از 150 کاراکتر باشند.")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __eq__(self, other):
        """
        بررسی برابری دو Value Object FullName
        Value Object ها بر اساس مقدارشان مقایسه می‌شوند، نه هویت‌شان.
        """
        if isinstance(other, FullName):
            return (self.first_name == other.first_name and
                    self.last_name == other.last_name)
        return False

    def __hash__(self):
        """
        متد hash برای استفاده در ساختارهای داده‌ای Hashable (مانند set و dictionary)
        برای Value Object ها پیاده‌سازی متد __hash__ و __eq__ ضروری است.
        """
        return hash((self.first_name, self.last_name))
