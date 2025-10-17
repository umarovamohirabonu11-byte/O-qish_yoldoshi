from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

# 🔐 Bot tokeningiz
BOT_TOKEN = "7951188300:AAHglCoQpr9FpYTduwOTeVXUo8V2yVnBnaA"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# 🎯 Asosiy menyu (endilikda tugmalar havolalarga ulangan)
def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="📖 Badiiy", url="https://www.youtube.com/@BadiiyKitoblar"),
            InlineKeyboardButton(text="🔬 Ilmiy", url="https://www.youtube.com/@IlmiyBilimlar")
        ],
        [
            InlineKeyboardButton(text="💪 Motivatsion", url="https://t.me/motivatsion_kanal"),
            InlineKeyboardButton(text="🏛️ Tarixiy", url="https://t.me/bookuznavoiy_tarixiy")
        ],
        [
            InlineKeyboardButton(text="🧭 Sarguzasht", url="https://www.youtube.com/@Sarguzashtlar"),
            InlineKeyboardButton(text="ℹ️ Ma’lumot", url="https://t.me/oqish_malumot")
        ],
        [
            InlineKeyboardButton(text="⚙️ Sozlamalar", callback_data="sozlamalar")
        ]
    ])

# 🔙 Orqaga tugmasi (faqat sozlamalardan chiqish uchun)
def back_button():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back_to_menu")]
    ])

# 🚀 /start buyrug‘i
@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(
        "👋 Salom! Men **O‘qiy Yo‘ldoshi** botman.\n\n"
        "Quyidagi janrlardan birini tanlang va kanalga o‘ting 👇",
        reply_markup=main_menu()
    )

# ⚙️ Sozlamalar (callback orqali)
@dp.callback_query(lambda c: c.data == "sozlamalar")
async def sozlamalar(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "⚙️ **Sozlamalar**\n\n"
        "Bu yerda siz:\n"
        "• Tilni o‘zgartirishingiz 🌐\n"
        "• Tungi rejimni yoqishingiz 🌙\n"
        "• Bildirishnomalarni boshqarishingiz 🔔 mumkin.",
        reply_markup=back_button()
    )
    await callback.answer()

# 🔙 Asosiy menyuga qaytish
@dp.callback_query(lambda c: c.data == "back_to_menu")
async def back_to_menu(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "🏠 Asosiy menyu:\nQuyidagi **janrlardan** birini tanlang 👇",
        reply_markup=main_menu()
    )
    await callback.answer()

# 🏁 Botni ishga tushirish
async def main():
    print("✅ O‘qiy Yo‘ldoshi bot ishga tushdi!")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
