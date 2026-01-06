import re
from urllib.parse import urlparse
from flask import Flask, render_template, request 

web = Flask(__name__)

# ===== LOGIC =====
def check_phone(phone):
    if not phone.isdigit():
        return "❌ Có ký tự không phải số"
    if len(phone) != 10:
        return "❌ Độ dài bất thường"
    if phone == phone[0] * len(phone):
        return "❌ Số lặp bất thường"
    return "✅ Số điện thoại hợp lệ"

def check_email(email):
    if not email:
        return "❌ Email trống"
    if " " in email:
        return "❌ Email có khoảng trắng"
    if "@" not in email:
        return "❌ Email thiếu ký tự @"
    if "." not in email:
        return "❌ Email thiếu dấu ."
    return "✅ Email hợp lệ (cơ bản)"

def check_url(url):
    if not url:
        return "❌ URL trống"
    if " " in url:
        return "❌ URL có khoảng trắng"
    if not (url.startswith("http://") or url.startswith("https://")):
        return "❌ URL thiếu http:// hoặc https://"
    return "✅ URL hợp lệ (cơ bản)"

# ===== ROUTE HOME =====
@web.route("/")
def home():
    return render_template("index.html")

# ===== ROUTE CHECK =====
@web.route("/check", methods=["POST"])
def check():
    phone = request.form.get("phone", "").strip()
    email = request.form.get("email", "").strip()
    url = request.form.get("url", "").strip()

    if phone:
        message = check_phone(phone)
    elif email:
        message = check_email(email)
    elif url:
        message = check_url(url)
    else:
        message = "❌ Vui lòng nhập dữ liệu"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    web.run(debug=True)
