import os
import requests

TOKEN = os.getenv("RUBIKA_TOKEN")

GROUP_ID = "g0HPPEx0aac2e8fc5843b27493f80919"

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
""


def main():
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
    print("پاسخ روبیکا:", response.json())
    print("درخواست ارسال پیام انجام شد.")


if __name__ == "__main__":
    main()
