from telegram.ext import *
import keys

print('Starting up bot..')


def start_command(update,context):
    update.message.reply_text('Hello there! I am Miss Bytes. Nice to meet you!')

def help_command(update,context):
    update.message.reply_text('Try typing anything and I will respond!')

def custom_command(update,context):
    update.message.reply_text('This is a custom command!')




def handle_response(text: str) -> str:
    if 'hello' in text:
        return 'Hey there!'

    if 'how are you'in text:
        return 'I am good, thanks!' 


    return 'I dont know. Please, try something else'  

def handle_message(update, context):
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response=''   

    print(f'User ({update.message.chat.id}) says:"{text}" in {message_type}')


    if message_type=='group':
        if '@MissBytesBot' in text: 
            new_text = text.replace('@MisssBytesBot','').strp()
            response= handle_response(new_text)
    else:
        response = handle_response(text)

    update.message.reply_text(response)   
    
def error(update,context):
    print(f'Update{update} caused error: {context.error}')


if __name__=='__main__':
    updater = Updater(keys.token,use_context=True)
    dp = updater.dispatcher

    #Commands
    dp.add_handler(CommandHandler('start',start_command))
    dp.add_handler(CommandHandler('help',help_command))
    dp.add_handler(CommandHandler('custom',custom_command))

    #messages
    dp.add_handler(MessageHandler(Filters.text,handle_message))

    #Error
    dp.add_error_handler(error)

    #RubBot
    updater.start_polling(1.0)
    updater.idle()

