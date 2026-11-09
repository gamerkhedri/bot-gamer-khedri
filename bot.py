
import os
import time
import requests
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

TOKEN = os.getenv("RUBIKA_TOKEN")

GROUP_ID = "g0HPPEx0aac2e8fc5843b27493f80919"

TEHRAN = ZoneInfo("Asia/Tehran")

SEND_HOUR = 8
SEND_MINUTE = 0

MESSAGE = """لطفاً جهت ثبت شروع کار روزانه خود موارد زیر را ارسال کنید

با سلام همکاران عزیز

نام و نام خانوادگی -

اعلام شروع کار روزانه.

لطفا اطلاعات را کامل ارسال کنید

با تشکر از همکاری شما

مدیریت گروه گیمر خدری

ــــــــــــــــــــــــــــــــــــ

إِلَى الَّذِينَ يَنْتَظِرُونَ السُّقُوطَ
وَأَنَا لَا أَسْقُطُ إِلَّا بِأَمْرٍ مِنَ اللَّهِ

خطاب به کسانی که منتظر سقوط ما هستند:
ما به جز فرمان خدا سقوط نخواهیم کرد.
"""


def send_message():
    if not TOKEN:
        raise RuntimeError("توکن RUBIKA_TOKEN تنظیم نشده است.")

    url = f"https://botapi.rubika.ir/v3/{TOKEN}/sendMessage"

    response = requests.post(
        url,
        json={
            "chat_id": GROUP_ID,
            "text": MESSAGE
        },
        timeout=30
    )

    response.raise_for_status()

    print("پیام ارسال شد:", response.json())


def next_send_time():
    now = datetime.now(TEHRAN)

    target = now.replace(
        hour=SEND_HOUR,
        minute=SEND_MINUTE,
        second=0,
        microsecond=0
    )

    if target <= now:
        target += timedelta(days=1)

    return target


def main():
    print("ربات زمان‌بندی روبیکا فعال شد.")

    while True:
        target = next_send_time()
        now = datetime.now(TEHRAN)

        wait_seconds = (target - now).total_seconds()

        print("ارسال بعدی:", target.strftime("%Y-%m-%d %H:%M"))
        time.sleep(wait_seconds)

        try:
            send_message()
        except Exception as error:
            print("خطا در ارسال پیام:", error)


if __name__ == "__main__":
    main()
