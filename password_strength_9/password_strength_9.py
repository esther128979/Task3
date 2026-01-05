import string  # מודול שמכיל הגדרות של תווים מיוחדים (!@#$ וכו')


def has_sequential_chars(password: str, length: int = 3) -> bool:
    """
    בודקת האם הסיסמה מכילה רצף עוקב של תווים
   
    """
    # מעבר על הסיסמה בחלונות של 'length' תווים
    for i in range(len(password) - length + 1):
        chunk = password[i:i + length]  # תת-מחרוזת רציפה באורך length

        # בדיקה אם כל התווים הם אותיות
        if chunk.isalpha():
            # המרת האותיות לקודי ASCII קטנים לצורך בדיקת רצף
            codes = [ord(c.lower()) for c in chunk]

            # בדיקה אם הקודים עוקבים (למשל: 97,98,99)
            if codes == list(range(codes[0], codes[0] + length)):
                return True  # נמצא רצף עוקב של אותיות

        # בדיקה אם כל התווים הם ספרות
        if chunk.isdigit():
            # המרת התווים למספרים
            nums = [int(c) for c in chunk]

            # בדיקה אם הספרות עוקבות (למשל: 1,2,3)
            if nums == list(range(nums[0], nums[0] + length)):
                return True  # נמצא רצף עוקב של ספרות

    return False  # לא נמצא שום רצף עוקב


def is_strong_password(password: str) -> bool:
    """
    בודקת האם סיסמה עומדת בכללי חוזק:
    - אורך מינימלי
    - סוגי תווים שונים
    - ללא חזרות מרובות
    - ללא רצפים עוקבים
    """

    # כלל 1: אורך מינימלי של 8 תווים
    if len(password) < 8:
        return False

    # כלל 2: בדיקה שיש סוגי תווים שונים
    has_lowercase = any(c.islower() for c in password)     # אות קטנה
    has_uppercase = any(c.isupper() for c in password)     # אות גדולה
    has_digit = any(c.isdigit() for c in password)         # ספרה
    has_special = any(c in string.punctuation for c in password)  # תו מיוחד

    # אם אחד מסוגי התווים חסר – הסיסמה לא חזקה
    if not all([has_lowercase, has_uppercase, has_digit, has_special]):
        return False

    # כלל 3: אין תו שמופיע יותר מפעמיים
    for char in set(password):
        if password.count(char) > 2:
            return False

    # כלל 4: אין רצפים עוקבים של אותיות או ספרות
    if has_sequential_chars(password):
        return False

    return True  # הסיסמה עומדת בכל הכללים


if __name__ == "__main__":
    # רשימת סיסמאות לבדיקה
    test_passwords = [
        "Abc!1234",
        "Aa1!Aa1!",
        "Strong!9",
        "AAAaaa1!",
        "Ab!9xYz"
    ]

    # בדיקה והדפסה של תוצאות החוזק לכל סיסמה
    for pwd in test_passwords:
        print(pwd, "->", is_strong_password(pwd))
