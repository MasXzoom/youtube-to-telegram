import logging
import re
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from config import TELEGRAM_TOKEN  # Pastikan Anda memiliki file config.py dengan token bot Anda
import yt_dlp as youtube_dl

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome! Send me a YouTube link and choose the video resolution.')

def validate_youtube_url(url):
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
    )
    match = re.match(youtube_regex, url)
    if match:
        return True, match.group(6)
    else:
        return False, None

def handle_message(update: Update, context: CallbackContext) -> None:
    url = update.message.text
    is_valid, video_id = validate_youtube_url(url)
    if is_valid:
        keyboard = [
            [InlineKeyboardButton("MP4 360p", callback_data=f"360_{video_id}"),
             InlineKeyboardButton("MP4 720p", callback_data=f"720_{video_id}"),
             InlineKeyboardButton("MP4 1080p", callback_data=f"1080_{video_id}")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Choose the video resolution:', reply_markup=reply_markup)
    else:
        update.message.reply_text('Invalid URL. Please make sure you are sending a correct YouTube link.')

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    resolution, video_id = query.data.split('_')
    format_opt = f"bestvideo[height<={resolution}]+bestaudio/best"
    download_and_send_video(query, context, video_id, format_opt)

def download_and_send_video(query, context, video_id, format_opt):
    ydl_opts = {
        'format': format_opt,
        'outtmpl': f'{video_id}.%(ext)s',
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(f'http://www.youtube.com/watch?v={video_id}', download=True)
            filename = ydl.prepare_filename(info_dict)

        chat_id = query.message.chat_id
        logger.info(f"File {filename} successfully downloaded. Now sending...")
        context.bot.send_video(chat_id=chat_id, video=open(filename, 'rb'))

    except Exception as e:
        context.bot.send_message(chat_id=query.message.chat_id, text='Failed to download or send the file. Please try again later.')
        logger.error(f"Error downloading or sending video: {e}")
    finally:
        if os.path.exists(filename):
            os.remove(filename)

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()