from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = 'YOUR_TOKEN'

def start(update, context):
    update.message.reply_text("Hi! I'm your bot.")

def echo(update, context):
    update.message.reply_text(f"You said: {update.message.text}")

# Exercise 1: Get the repositores of a user in github via api calls to github api
def get_repos(update, context, username):
    # TODO: Get the repositores of a user in github via api calls to github api
    pass


#2. Add a command to get the top 10 repositores in github via api calls to github api
def get_top_10_repos(update, context):
    # TODO: Get the top 10 repositores in github via api calls to github api
    pass

#3. Add a commad to get how many branches a repo has via api calls to github api
def get_branches(update, context, repo_name):
    # TODO: Get how many branches a repo has via api calls to github api
    pass

#4. Check if a GitHub repo has open issues and how many.
def get_open_issues(update, context, repo_name):
    # TODO: Get how many open issues a repo has via api calls to github api
    pass

#5. Check if a GitHub repo has open pull requests and how many.
def get_open_pull_requests(update, context, repo_name):
    # TODO: Get how many open pull requests a repo has via api calls to github api
    pass    

#6. Add a /weather <city> command→ Use OpenWeatherMap API to return current weather.
def get_weather(update, context, city):
    # TODO: Get the weather of a city via api calls to OpenWeatherMap API
    pass

#7. Add a /joke command → Use https://official-joke-api.appspot.com/random_joke API to return a random joke.
def get_joke(update, context):
    # TODO: Get a random joke via api calls to https://official-joke-api.appspot.com/random_joke API
    pass


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
