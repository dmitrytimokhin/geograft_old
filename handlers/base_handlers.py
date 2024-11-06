import logging

from aiogram import F, Router
from aiogram.filters import CommandStart, or_f
from aiogram.types import Message, CallbackQuery
from dotenv import load_dotenv
from keyboards import kb_go_home

base_router = Router()
logger = logging.getLogger('MAIN')
load_dotenv()


# --- Старт телеграм бота ---
@base_router.message(or_f(CommandStart(), F.text == '/start'))
async def cmd_start(message: Message):
    user_tg_id = message.from_user.id
    logger.debug(msg=f'The User {user_tg_id} pressed start')
    await message.answer(text='Добро пожаловать! В связи с ребрендингом компании, '
                              'Наш бот переехал на новый адрес: @GGMedBot \n\n',
                         reply_markup=kb_go_home)


@base_router.message()
async def un_know(message: Message):
    await message.answer(text='В связи с ребрендингом компании, '
                              'Наш бот переехал на новый адрес: @GGMedBot \n\n',
                         reply_markup=kb_go_home)


@base_router.callback_query()
async def un_know(callback: CallbackQuery):
    await callback.message.answer(text='В связи с ребрендингом компании, '
                                       'Наш бот переехал на новый адрес: @GGMedBot \n\n',
                                  reply_markup=kb_go_home)
    await callback.answer(text='Новый бот "@GGMedBot"',
                          show_alert=True)
