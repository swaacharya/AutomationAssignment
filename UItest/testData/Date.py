from datetime import datetime, timedelta

now = datetime.now() 

today = now.strftime("%Y-%m-%d")
todayplus30 = (now + timedelta(days=30)).strftime("%Y-%m-%d")

Date ={
    "today": today,
    "todayplus30": todayplus30
}