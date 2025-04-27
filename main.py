import random

LANGS = {
    'en': {
        'welcome': "Welcome to Guess the Number!",
        'prompt': "Guess a number between 1 and 100:",
        'too_low': "Too low! Try again.",
        'too_high': "Too high! Try again.",
        'correct': "🎉 Correct! You guessed the number in {tries} tries.",
        'again': "Play again? (y/n): ",
        'bye': "Goodbye!"
    },
    'ar': {
        'welcome': "مرحباً بك في لعبة التخمين!",
        'prompt': "خمن رقماً بين 1 و 100:",
        'too_low': "قليل جداً! حاول مرة أخرى.",
        'too_high': "كبير جداً! حاول مرة أخرى.",
        'correct': "🎉 أحسنت! خمّنت الرقم بعد {tries} محاولة.",
        'again': "تلعب مرة أخرى؟ (ن/ع): ",
        'bye': "إلى اللقاء!"
    }
}

def choose_lang():
    lang = input("Choose language | اختر اللغة (en/ar): ").strip().lower()
    return 'ar' if lang == 'ar' else 'en'

def play(lang):
    secret = random.randint(1, 100)
    tries = 0
    print(LANGS[lang]['welcome'])
    while True:
        try:
            guess = int(input(LANGS[lang]['prompt'] + ' '))
            tries += 1
            if guess < secret:
                print(LANGS[lang]['too_low'])
            elif guess > secret:
                print(LANGS[lang]['too_high'])
            else:
                print(LANGS[lang]['correct'].format(tries=tries))
                break
        except ValueError:
            print("Invalid input! | إدخال غير صالح!")

def main():
    lang = choose_lang()
    while True:
        play(lang)
        again = input(LANGS[lang]['again']).strip().lower()
        if (lang == 'ar' and again != 'ع') or (lang == 'en' and again != 'y'):
            print(LANGS[lang]['bye'])
            break

if __name__ == "__main__":
    main()
