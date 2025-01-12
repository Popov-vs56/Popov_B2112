#https://t.me/Popov_B2112_bot
from telegram import  Update
from telegram.ext import  ApplicationBuilder, CommandHandler, ContextTypes
import requests
from bs4 import  BeautifulSoup


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
async def virsh1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Зоре моя вечірняя,...'
                                    f' Зійди над горою,...'
                                    f' Поговорим тихесенько...'
                                    f' В неволі з тобою....'
                                    f' Розкажи, як за горою...'
                                    f' Сонечко сідає,...'
                                    f' Як у Дніпра веселочка Воду позичає....'
                                    f' Як широка сокорина Віти розпустила…...'
                                    f' А над самою водою Верба похилилась;...'
                                    f' Аж по воді розіслала Зеленії віти,...'
                                    f' А на вітах гойдаються Нехрещені діти. {update.effective_user.first_name}')
async def virsh2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"""Садок вишневий коло хати,
Хрущі над вишнями гудуть,
Плугатарі з плугами йдуть,
Співають ідучи дівчата,
А матері вечерять ждуть.
Сім’я вечеря коло хати,
Вечірня зіронька встає.
Дочка вечерять подає,
А мати хоче научати,
Так соловейко не дає.
Поклала мати коло хати
Маленьких діточок своїх;
Сама заснула коло їх.
Затихло все, тілько дівчата
Та соловейко не затих. {update.effective_user.first_name}""")
async def virsh3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"""Як не любити зими сніжно-синьої
На Україні моїй,
Саду старого в пухнастому інеї,
Сивих, веселих завій?

Як не любити весни многошумної
Меду пахучих суцвіть,
Як не любити роботи розумної,
Праці, що дух веселить?

Як не любити утоми цілющої
Після гарячої гри,
Поклику птаха над темною пущею,
Рідних пісень з-за гори?

Як не любити любов’ю наснажених,
Мудрістю сповнених книг,
Троп невідомих, дерзань ще не зважених
І небосхилів нових?

Як не любити людини, що з атому
Креше добра блискавки,
Як не любить по змаганні завзятому
Дружнього стиску руки?

Як не любити пори, коли ночами
В щасті тремтить соловей,
Як не любить під бровами дівочими
Синього сяйва очей? {update.effective_user.first_name}""")
async def virsh4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"""За сонцем хмаронька пливе,
Червоні поли розстилає
І сонце спатоньки зове
У синє море: покриває
Рожевою пеленою,
Мов мати дитину.
Очам любо. Годиночку,
Малую годину
Ніби серце одпочине,
З Богом заговорить…
А туман, неначе ворог,
Закриває море
І хмароньку рожевую,
І тьму за собою
Розстилає туман сивий,
І тьмою німою
Оповиє тобі душу,
Й не знаєш, де дітись,
І ждеш його, того світу,
Мов матері діти. {update.effective_user.first_name}""")
async  def virsh5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"""Реве та стогне Дніпр широкий
Сердитий вітер завива,
Додолу верби гне високі,
Горами хвилю підійма.

І блідий місяць на ту пору
Із хмари де-де виглядав, −
Неначе човен в синім морю,
То виринав, то потопав.

Ще треті півні не співали,
Ніхто ніде не гомонів,
Сичі в гаю перекликались,
Та ясень раз-у-раз скрипів. {update.effective_user.first_name}""")
async def virsh6(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"""І досі сниться: під горою
Меж вербами та над водою
Біленька хаточка. Сидить
Неначе й досі сивий дід
Коло хатиночки і бавить
Хорошеє та кучеряве
Своє маленькеє внуча.
І досі сниться, вийшла з хати
Веселая, сміючись, мати,
Цілує діда і дитя
Аж тричі весело цілує,
Прийма на руки, і годує,
І спать несе. А дід сидить
І усміхається, і стиха
Промовить нишком: – Де ж те лихо?
Печалі тії, вороги?
І нищечком старий читає,
Перехрестившись, Отче наш.
Крізь верби сонечко сіяє
І тихо гасне. День погас
І все почило. Сивий в хату
Й собі пішов опочивати. {update.effective_user.first_name}""")
app = ApplicationBuilder().token("7741194068:AAEZbzGuMWTxBWAI-mvLaQ5m2NGkcxwOF6Q").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("virsh1", virsh1))
app.add_handler(CommandHandler("virsh2", virsh2))
app.add_handler(CommandHandler("virsh3", virsh3))
app.add_handler(CommandHandler("virsh4", virsh4))
app.add_handler(CommandHandler("virsh5", virsh5))
app.add_handler(CommandHandler("virsh6", virsh6))

app.run_polling()

