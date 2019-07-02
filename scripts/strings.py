# token for telegram bot
TOKEN = '<UseYourToken>'

# sequence of messages which will be sent to user
MESSAGE_QUEUE = (
    'Введи спочатку в якому роді до тебе звертатися',
    'Про що ти хочеш, щоб я тобі надокучав?',
    'Процес запущено. Постараюсь не забути 📿',
    'Радий був понадокучати! Звертайся ще якщо що 🎳🌬',
    ('За тобою числяться:', 'рід і завдання - "', '"\nБудемо змінювати? 🐶')
)

# species which user can choose
USER_SPECIES = ('👨 Чоловічий', '👩 Жіночий', '😸 Середній')

# reminder templates for specific user species
REMINDERS = {
    USER_SPECIES[0]: (
        (('Ну що не забув', '? 🐨'), 'CENTER'),
        ('📸 Угадай що ти ще досі не зробив?', 'LEFT'),
        (('Не забув', '?'), 'CENTER'),
        (('Ще треба', 'не забув? 🤔'), 'CENTER')
    ),
    USER_SPECIES[1]: (
        (('Ну що не забула', '? 🐨'), 'CENTER'),
        ('📸 Угадай що ти ще досі не зробила?', 'LEFT'),
        (('Не забула', '?'), 'CENTER'),
        (('Ще треба', 'не забула? 🤔'), 'CENTER')
    ),
    USER_SPECIES[2]: (
        (('Ну що не забуло', '? 🐨'), 'CENTER'),
        ('📸 Угадай що ти ще досі не зробило?', 'LEFT'),
        (('Не забуло', '?'), 'CENTER'),
        (('Ще треба', 'не забуло? 🤔'), 'CENTER')
    ),
    'Без роду': (
        (('Як ідуть справи з', '?'), 'CENTER'),
        (('Що там з', '? 🏕'), 'CENTER'),
        ('⚒ Нагадую, що тобі треба', 'LEFT'), ('Не забудь', 'LEFT'),
        ('- ось що тобі ще потрібно зробити 🦖', 'RIGHT'),
        (('Не знаєш чим зайнятись? А як же', '?'), 'CENTER'),
        (('Ну і як', '? 🤟'), 'CENTER'), ('Прийшла пора', 'LEFT'),
        ('. Зробиш по-братські? 👩‍🚀', 'RIGHT'),
        ('Щось мені підказує, що ти ще й досі не', 'LEFT')
    )
}

# message if user wants to stop job
STOP_MESSAGE = '🙌 Достатньо нагадувати, дякую'

# message if user wants to call /start
START_MESSAGE = '🙏 О Великий Бот! Взиваю до твоєї допомоги знову!'

# options when user call bot for second time
CHANGE_DATA_ANSWERS = ('🔁 Хочу змінити рід', '⏰ Хочу змінити нагадування',
                       '😎 Хочу змінити все', '🌠 Запускаємо так, як є')

# db info for manual filling out
USER = "<YourUserInfo>"
PASSWORD = "<YourPasswordInfo>"
HOST = "<YourHostInfo>"
DATABASE = "<YourDatabaseInfo>"
