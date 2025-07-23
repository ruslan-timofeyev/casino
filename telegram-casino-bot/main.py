from aiogram import Bot, Dispatcher, executor, types
import os
from dotenv import load_dotenv
from balance import get_balance, update_balance
from wheel_logic import spin_wheel

load_dotenv()
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    user_id = str(message.from_user.id)
    update_balance(user_id, 0)  # init balance
    await message.answer("🎰 Добро пожаловать в Казино! Напиши /spin чтобы крутить колесо!")

@dp.message_handler(commands=["balance"])
async def check_balance(message: types.Message):
    user_id = str(message.from_user.id)
    balance = get_balance(user_id)
    await message.answer(f"💰 Ваш баланс: {balance} USDT")

@dp.message_handler(commands=["spin"])
async def spin(message: types.Message):
    user_id = str(message.from_user.id)
    result, win = spin_wheel()
    update_balance(user_id, win)
    await message.answer(f"🌀 {result}!
Выигрыш: {win} USDT")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
