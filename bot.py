#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""Simple inline keyboard bot with multiple CallbackQueryHandlers.
This Bot uses the Updater class to handle the bot.
First, a few callback functions are defined as callback query handler. Then, those functions are
passed to the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Example of a bot that uses inline keyboard that has multiple CallbackQueryHandlers arranged in a
ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line to stop the bot.
"""
from telegram import (
    Animation,
    Audio,
    BotCommand,
    BotCommandScope,
    Chat,
    ChatMember,
    ChatPermissions,
    ChatPhoto,
    Contact,
    Document,
    File,
    GameHighScore,
    Location,
    MaskPosition,
    Message,
    MessageId,
    PassportElementError,
    PhotoSize,
    Poll,
    ReplyMarkup,
    ShippingOption,
    Sticker,
    StickerSet,
    TelegramObject,
    Update,
    User,
    UserProfilePhotos,
    Venue,
    Video,
    VideoNote,
    Voice,
    WebhookInfo,
    InlineKeyboardMarkup,
    ChatInviteLink,
)

from typing import (
    TYPE_CHECKING,
    Callable,
    List,
    Optional,
    Tuple,
    TypeVar,
    Union,
    no_type_check,
    Dict,
    cast,
    Sequence,
)
import logging
from telegram import InlineKeyboardButton
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
)
import re
import requests
from telegram.files.inputmedia import InputMediaDocument
import telegram_send
import os
from telegram.ext import Updater, InlineQueryHandler, CommandHandler

PORT = int(os.environ.get('PORT', 5000))
TOKEN = os.environ["5072578561:AAH1k4MKGTHCmr6WX2WJJNrwsJlczOT96xY"]

name_bot="wearelegion"
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Stages
FIRST, SECOND = range(2)
# Callback data
ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT,NINE,TEN,ELEVEN, TWELVE, THIRTEEN, FOURTEEN, FIFTEEN, SIXTEEN, SEVENTEEN, EIGHTEEN, NINETEEN,TWENTY, TWENTYONE = range(21)


def start(update: Update, context: CallbackContext) -> int:
    """Send message on `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    # Build InlineKeyboard where each button has a displayed text
    # and a string as callback_data
    # The keyboard is a list of button rows, where each row is in turn
    # a list (hence `[[...]]`).
    keyboard = [
        [
            InlineKeyboardButton("Pentesting Tools", callback_data=str(ONE)),
            InlineKeyboardButton("Codings", callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now
    return FIRST


def start_over(update: Update, context: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Pentesting Tools", callback_data=str(ONE)),
            InlineKeyboardButton("Codings", callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Instead of sending a new message, edit the message that
    # originated the CallbackQuery. This gives the feeling of an
    # interactive menu.
    query.edit_message_text(text="What are you looking for ?", reply_markup=reply_markup)
    return FIRST


def one(update: Update, context: CallbackContext) -> int:
    """Your choise is Pentesing Tools"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Wireless Testing", callback_data=str(FOUR)),           
            InlineKeyboardButton("Malware Thearts", callback_data=str(FIVE)),
            InlineKeyboardButton("Denail Of Service", callback_data=str(SIX)),
            InlineKeyboardButton("Footprinting", callback_data=str(SEVEN)),
            InlineKeyboardButton("Session Hijacking", callback_data=str(EIGHT)),
            InlineKeyboardButton("Exit", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Your choise is Pentesing Tools", reply_markup=reply_markup
    )
    return FIRST


def two(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Python", callback_data=str(NINE)),
            InlineKeyboardButton("HTML", callback_data=str(TEN)),
            InlineKeyboardButton("PHP", callback_data=str(ELEVEN)),
            InlineKeyboardButton("DataBase + SQL", callback_data=str(TWELVE)),
            InlineKeyboardButton("Exit", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Your Choise Is Codings", reply_markup=reply_markup
    )
    return FIRST


def three(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("I want more, please !!!", callback_data=str(ONE)),
            InlineKeyboardButton("I've Got all the things I want", callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="You sure you want to exit ?", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return SECOND


def four(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Click_Me_For_Link", callback_data=str(THIRTEEN)),
            InlineKeyboardButton("Exit", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="You choose Wireless testing", reply_markup=reply_markup
    )
    return FIRST

def five(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Click_Me_For_Link", callback_data=str(FOURTEEN)),
            InlineKeyboardButton("Exit", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="You choose Malware thearts", reply_markup=reply_markup
    )
    return FIRST

def six(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Click_Me_For_Link", callback_data=str(FIFTEEN)),
            InlineKeyboardButton("Exit", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="You choose Denial of service", reply_markup=reply_markup
    )
    return FIRST

def seven(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Click_Me_For_Link", callback_data=str(SIXTEEN)),
            InlineKeyboardButton("Exit", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="You choose Footprinting", reply_markup=reply_markup
    )
    return FIRST

def eight(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Click_Me_For_Link", callback_data=str(SEVENTEEN)),
            InlineKeyboardButton("Exit", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="You choose Session Hijacking", reply_markup=reply_markup
    )
    return FIRST

def nine(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Click_Me_For_Link", callback_data=str(EIGHTEEN)),
            InlineKeyboardButton("Exit", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="You choose Python", reply_markup=reply_markup
    )
    return FIRST

def ten(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Click_Me_For_Link", callback_data=str(NINETEEN)),
            InlineKeyboardButton("Exit", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="You choose HTML", reply_markup=reply_markup
    )
    return FIRST

def eleven(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Click_Me_For_Link", callback_data=str(TWENTY)),
            InlineKeyboardButton("Exit", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="PHP", reply_markup=reply_markup
    )
    return FIRST

def twelve(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Click_Me_For_Link", callback_data=str(TWENTYONE)),
            InlineKeyboardButton("Exit", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="You choose Database + SQL", reply_markup=reply_markup
    )
    return FIRST

def thirteen(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            query.edit_message_text(text="https://mega.nz/file/o1hVzapI#cAKjAaC40OvJTQWXI3bYkJym9rEHoH1qcFXvafy3eio"),
            InlineKeyboardButton("Exit", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Here your link or file/folder", reply_markup=reply_markup
    )
    return FIRST

def fourteen(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
             query.edit_message_text(text="https://mega.nz/file/s8BhzSzY#Jft_7zdYdYijLixDVM42OSVrjx8iHGFQN47sdzZa0oM"),
            InlineKeyboardButton("Exit", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Here your link or file/folder", reply_markup=reply_markup
    )
    return FIRST

def fifteen(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            query.edit_message_text(text="https://mega.nz/file/IgZTESwI#9nmfunCuoY1XwlLzKzAxEh_wK9AFAQ5xeVCCT4mSUlM"),
            InlineKeyboardButton("Exit", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Here your link or file/folder", reply_markup=reply_markup
    )
    return FIRST

def sixteen(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            query.edit_message_text(text="https://mega.nz/file/l8ADUSaY#hVIIvlMSvDL4oNQiu8O2O-WnSiQ3EYSHWlC1Daxbfik"),
            InlineKeyboardButton("Exit", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Here your link or file/folder", reply_markup=reply_markup
    )
    return FIRST

def seventeen(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            query.edit_message_text(text="https://mega.nz/file/4wB3lCpQ#3aycdqbzhtnm3-qhOaw6DpHKz3i07Auf5_pedLIaKaE"),
            InlineKeyboardButton("Exit", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Here your link or file/folder", reply_markup=reply_markup
    )
    return FIRST

def eighteen(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            query.edit_message_text(text="https://mega.nz/file/MlhUlJ5Z#jRW4y6bEYdcyjvrmKWbXm0oIx0dl-VdJYAsILigjp0s"),
            InlineKeyboardButton("Exit", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Here your link or file/folder", reply_markup=reply_markup
    )
    return FIRST

def nineteen(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            query.edit_message_text(text="https://mega.nz/file/gwAzQK7a#cq6Xw3kx7RiHmYE02vhfMmcjZPTTFwwVc92pVZUtQG0"),
            InlineKeyboardButton("Exit", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Here your link or file/folder", reply_markup=reply_markup
    )
    return FIRST

def twenty(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            query.edit_message_text(text="https://mega.nz/file/h4BXyYKb#a892YK1iOtAiO5ieyP2r3qpk12yClQNq-gw8ENjQ_qY"),
            InlineKeyboardButton("Exit", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Here your link or file/folder", reply_markup=reply_markup
    )
    return FIRST

def twentyone(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            query.edit_message_text(text="https://mega.nz/folder/l1BTRAoD#6B2-ZVvCLfrVAVCCJT040g"),
            InlineKeyboardButton("Exit", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Here your link or file/folder", reply_markup=reply_markup
    )
    return FIRST


def end(update: Update, context: CallbackContext) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="See you next time!")
    return ConversationHandler.END


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop', bop))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [
                CallbackQueryHandler(one, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(two, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(three, pattern='^' + str(THREE) + '$'),
                CallbackQueryHandler(four, pattern='^' + str(FOUR) + '$'),
                CallbackQueryHandler(five, pattern='^' + str(FIVE) + '$'),
                CallbackQueryHandler(six, pattern='^' + str(SIX) + '$'),
                CallbackQueryHandler(seven, pattern='^' + str(SEVEN) + '$'),
                CallbackQueryHandler(eight, pattern='^' + str(EIGHT) + '$'),
                CallbackQueryHandler(nine, pattern='^' + str(NINE) + '$'),
                CallbackQueryHandler(ten, pattern='^' + str(TEN) + '$'),
                CallbackQueryHandler(eleven, pattern='^' + str(ELEVEN) + '$'),
                CallbackQueryHandler(twelve, pattern='^' + str(TWELVE) + '$'),
                CallbackQueryHandler(thirteen, pattern='^' + str(THIRTEEN) + '$'),
                CallbackQueryHandler(fourteen, pattern='^' + str(FOURTEEN) + '$'),
                CallbackQueryHandler(fifteen, pattern='^' + str(FIFTEEN) + '$'),
                CallbackQueryHandler(sixteen, pattern='^' + str(SIXTEEN) + '$'),
                CallbackQueryHandler(seventeen, pattern='^' + str(SEVENTEEN) + '$'),
                CallbackQueryHandler(eighteen, pattern='^' + str(EIGHTEEN) + '$'),
                CallbackQueryHandler(nineteen, pattern='^' + str(NINETEEN) + '$'),
                CallbackQueryHandler(twenty, pattern='^' + str(TWENTY) + '$'),
                CallbackQueryHandler(twentyone, pattern='^' + str(TWENTYONE) + '$'),
            ],
            SECOND: [
                CallbackQueryHandler(start_over, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(end, pattern='^' + str(TWO) + '$'),
            ],
        },
        fallbacks=[CommandHandler('start', start)],
    )
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://telebawabot.herokuapp.com/' + TOKEN)
    
    updater.idle()

if __name__ == '__main__':
    main()
