from datetime import datetime
import locale

def get_date() -> str:
    user_locale = locale.getlocale()
    print(user_locale)
    try:
        locale.setlocale(locale.LC_TIME, user_locale)
    except locale.Error:
        print(f"Locale {user_locale} not found. Using default locale.")
        locale.setlocale(locale.LC_TIME, 'C')
    today = datetime.now()
    return f'{today:%c}'


if __name__ == "__main__":
    print(get_date())