from InternetSpeedTwitterBot import InternetSpeedTwitterBot, PROMISED_UP, PROMISED_DOWN

bot = InternetSpeedTwitterBot()

bot.get_internet_speed()

if bot.up < PROMISED_UP or bot.down < PROMISED_DOWN:
    bot.tweet_at_provider()
else:
    print(f'Speeds within the promised range')
