from InternetSpeedTwitterBot import InternetSpeedTwitterBot

PROMISED_DOWNLOAD = 50
PROMISED_UPLOAD = 15

Bot = InternetSpeedTwitterBot()

internet_speed = Bot.speedtest_results()
upload = float(internet_speed[1].text)
download = float(internet_speed[0].text)

if PROMISED_DOWNLOAD > download or PROMISED_UPLOAD > upload:
    twitter = Bot.x_post(upload, download)
