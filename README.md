# 🚀 Livekadeh Tunnel - Official Releases & API Documentation

[![GitHub Release](https://img.shields.io/github/v/release/livekadeh/livekadeh-tunnel-releases?color=cyan&label=Latest%20Version)](https://github.com/livekadeh/livekadeh-tunnel-releases/releases/latest)
[![Platforms](https://img.shields.io/badge/Platforms-Android%20%7C%20Windows%20%7C%20Linux%20%7C%20macOS-blue)](#-client-downloads)
[![License](https://img.shields.io/badge/License-Proprietary-red)](#)

سامانه تانلینگ و وی‌پی‌ان اختصاصی لایوکده (Livekadeh Tunnel) با پروتکل رمزنگاری Zero-DPI و معماری چندمسیره (Multipath TCP & UDP) برای دور زدن فیلترینگ شدید، کاهش پینگ و پایدارسازی اینترنت.

---

## 📥 دانلود نسخه‌های کلاینت (Client Downloads - v1.9.2)

| سیستم‌عامل (Platform) | معماری (Architecture) | لینک دانلود مستقیم (Direct Download) | توضیحات |
| :--- | :--- | :--- | :--- |
| **Android** | `Universal (arm64, v7a, x86_64)` | [📱 دانلود مستقیم APK (v1.9.2)](https://github.com/livekadeh/livekadeh-tunnel-releases/releases/download/v1.9.2/livekadeh-tunnel-v1.9.2.apk) | همراه با ویدجت صفحه اصلی، اسپیدتست و ریکانکت خودکار |
| **Windows** | `x86_64 (64-bit)` | [🪟 دانلود پکیج Zip کامل](https://github.com/livekadeh/livekadeh-tunnel-releases/releases/download/v1.9.2/livekadeh_tunnel-windows-x86_64.zip) | شامل برنامه گرافیکی GUI و درایور کرنل Wintun |
| **Windows** | `x86_64 (Single Exe)` | [⚙️ دانلود فایل اجرایی livekadeh_tunnel.exe](https://github.com/livekadeh/livekadeh-tunnel-releases/releases/download/v1.9.2/livekadeh_tunnel.exe) | نیازمند قرارگیری wintun.dll در کنار فایل |
| **Linux** | `x86_64` | [🐧 دانلود نسخه لینوکس CLI](https://github.com/livekadeh/livekadeh-tunnel-releases/releases/download/v1.9.2/livekadeh_tunnel-linux-x86_64.tar.gz) | دارای منوی ترمینالی تعاملی و مدیریت پروفایل‌ها |
| **macOS** | `Apple Silicon (M1/M2/M3/M4)` | [🍎 دانلود نسخه مک ARM64](https://github.com/livekadeh/livekadeh-tunnel-releases/releases/download/v1.9.2/livekadeh_tunnel-macos-arm64.tar.gz) | باینری نیتیو بدون نیاز به Rosetta |
| **iOS (iPhone/iPad)** | `arm64 (iOS 14.0+)` | [🍏 دانلود مستقیم فایل IPA (v1.9.2)](https://github.com/livekadeh/livekadeh-tunnel-releases/releases/download/v1.9.2/LivekadehTunnel.ipa) | مناسب ثبت و امضا در اناردونی، سیب‌اپ، Sideloadly و AltStore |
| **iOS Simulator** | `arm64 / x86_64` | [📦 دانلود پکیج شبیه‌ساز (App Bundle)](https://github.com/livekadeh/livekadeh-tunnel-releases/releases/download/v1.9.2/LivekadehTunnel.app.zip) | تست مجازی در Appetize.io یا شبیه‌ساز مک |

---

## 🍏 راهنمای استفاده از نسخه iOS (iPhone & iPad Quick Start)

1. **ثبت و امضا (Signing & Installation)**:
   - فایل `LivekadehTunnel.ipa` را دانلود نموده و جهت امضای شرکتی یا ادهاک در سامانه‌هایی نظیر **اناردونی (Anardoni)**، **سیب‌اپ** یا **آی‌اپس** ثبت نمایید.
   - همچنین برای استفاده رایگان با اپل‌آیدی شخصی می‌توانید از برنامه‌های **Sideloadly** یا **AltStore** بر روی ویندوز یا مک استفاده کنید.
2. **افزودن سریع کانفیگ با لینک**:
   - در پنل مدیریت ادمین روی دکمه **کپی لینک (livekadeh://)** کلیک کنید.
   - در اپلیکیشن، لینک کپی‌شده را در بخش پروفایل وارد نمایید تا کلیه مشخصات سرور، کلید و پورت آنی ست شوند.
3. **اسکن QR Code**:
   - اسکن مستقیم از طریق دوربین گوشی یا انتخاب عکس/اسکرین‌شات کیوآرکد از آلبوم تصاویر.
4. **مدیریت پروفایل‌ها (Multi-Profile)**:
   - تعریف چندین سرور مجزا و انتخاب سریع از صفحه اصلی بدون نیاز به ورود مجدد اطلاعات.


## 📱 راهنمای استفاده از نسخه اندروید (Android Quick Start)

1. فایل `livekadeh-tunnel-v1.9.2.apk` را دانلود و نصب کنید.
2. دسترسی‌های درخواستی (مجوز VPN Service و Notifications) را تأیید کنید.
3. **افزودن کانفیگ**:
   - کلیک بر روی آیکون **QR Code** در گوشه صفحه برای اسکن کد ارائه شده توسط ادمین، یا
   - کپی کردن لینک کانفیگ (`livekadeh://...`) و زدن گزینه Import from Clipboard، یا
   - ورود دستی آدرس سرور (IP:Port) و کلید رمزنگاری (Key).
4. **مدیریت چند کانفیگ (Multi-Profile)**:
   - با لمس آیکون پروفایل در نوار بالایی می‌توانید چندین سرور/کانفیگ مختلف را با نام دلخواه ذخیره کرده و به سادگی بین آنها سوئیچ کنید.
5. **ویدجت صفحه اصلی (Home Screen Widget)**:
   - روی صفحه اصلی گوشی دست خود را نگه دارید، بخش ابزارک‌ها (Widgets) را باز کنید و **Livekadeh Tunnel** را اضافه کنید تا با یک کلیک وصل/قطع شوید.
6. **ریکانکت خودکار و یکپارچه**:
   - در صورت تغییر شبکه (سوئیچ از Wi-Fi به همراه اول/ایرانسل یا بالعکس)، اپلیکیشن به صورت هوشمند و بدون خاموش شدن VPN، سشن را در شبکه جدید بازیابی می‌کند.

---

## 🪟 راهنمای استفاده از نسخه ویندوز (Windows Quick Start)

1. فایل فشرده `livekadeh_tunnel-windows-x86_64.zip` را دانلود کرده و آن را از حالت فشرده استخراج (Extract) نمایید.
2. روی فایل `livekadeh_tunnel.exe` راست‌کلیک کرده و گزینه **Run as administrator** را بزنید.
3. **مدیریت پروفایل‌ها (Config Profiles)**:
   - کلید **+ New**: ساخت یک کانفیگ جدید.
   - نام پروفایل را مستقیماً در کادر مربوطه تایپ کنید.
   - آدرس سرور و کلید رمزنگاری را وارد کنید (یا روی دکمه Import QR کلیک کنید).
   - کلید **Save**: ذخیره کانفیگ انتخاب‌شده.
   - کلید **Del**: حذف کانفیگ انتخاب‌شده.
4. دکمه بزرگ **CONNECT TUNNEL** را بزنید. درایور قدرتمند لایه ۳ Wintun فعال شده و ترافیک رمزنگاری می‌شود.

---

## 📡 مستندات جامع REST API پنل مدیریت (Admin Panel API Documentation)

پنل مدیریت لایوکده دارای یک وب‌سرویس RESTful مدرن بر پایه JSON است که امکان اتصال به ربات‌های تلگرام، پنل‌های فروش، سامانه‌های مانیتورینگ و اسکریپت‌های اتوماسیون را فراهم می‌کند.

**آدرس پایه (Base URL):**
```
http://<SERVER_IP>:8444
```

---

### ۱. احراز هویت (Authentication)

#### ورود مدیر (Login)
* **متد:** `POST`
* **مسیر:** `/api/auth/login`
* **بدنه درخواست (JSON):**
```json
{
  "username": "admin",
  "password": "YOUR_ADMIN_PASSWORD"
}
```
* **پاسخ موفق (200 OK):**
```json
{
  "status": "ok",
  "message": "Login successful"
}
```
*(کوکی سشن به صورت خودکار در مرورگر یا کلاینت HTTP ذخیره می‌شود)*

#### خروج مدیر (Logout)
* **متد:** `POST`
* **مسیر:** `/api/auth/logout`

---

### ۲. اطلاعات و آمار سیستم (System Info & Health)

* **متد:** `GET`
* **مسیر:** `/api/system`
* **توضیحات:** دریافت اطلاعات سخت‌افزاری سرور، مصرف رم و CPU، نسخه سیستم، کل حجم تبادل‌شده، و تعداد کاربران آنلاین.
* **نمونه پاسخ (200 OK):**
```json
{
  "status": "ok",
  "server": {
    "version": "1.9.1",
    "uptime": 86400,
    "total_rx": 5368709120,
    "total_tx": 10737418240,
    "active_sessions": 12
  },
  "system": {
    "loadAvg": [0.15, 0.22, 0.18],
    "memTotal": 4294967296,
    "memUsed": 1073741824,
    "memPercent": 25,
    "cpuCount": 4,
    "hostname": "livekadeh-core-1",
    "serverIp": "194.31.108.53",
    "serverPort": 8443,
    "version": "1.9.1"
  },
  "totalUsers": 25,
  "onlineUsers": 12
}
```

---

### ۳. مدیریت کاربران (Client Management)

#### ۳.۱. لیست تمامی کاربران
* **متد:** `GET`
* **مسیر:** `/api/users`
* **نمونه پاسخ:**
```json
{
  "status": "ok",
  "users": [
    {
      "assigned_ip": 10,
      "assigned_ip_str": "10.10.10.10",
      "name": "User-Ali",
      "enabled": 1,
      "online": 1,
      "type": "TCP",
      "num_conns": 8,
      "remote_ip": "5.120.35.42:54321",
      "country": "Iran",
      "country_code": "IR",
      "country_emoji": "🇮🇷",
      "isp": "Mobile Telecommunication Company of Iran (MCI)",
      "total_rx": 104857600,
      "total_tx": 524288000,
      "max_bytes": 53687091200,
      "expires_at": 1795000000,
      "speed_limit_kbps": 20480
    }
  ]
}
```

#### ۳.۲. ساخت کاربر جدید (Add User)
* **متد:** `POST`
* **مسیر:** `/api/users`
* **بدنه درخواست (JSON):**
```json
{
  "name": "Reza",
  "expireDays": 30,
  "maxGb": 50,
  "speedLimitMbps": 20
}
```
* **توضیحات پارامترها:**
  - `name`: نام نمایشی کاربر (الزامی)
  - `expireDays`: مدت اعتبار به روز (صفر یا خالی برای دائمی)
  - `maxGb`: محدودیت حجم مصرفی به گیگابایت (صفر یا خالی برای نامحدود)
  - `speedLimitMbps`: سقف سرعت دانلود/آپلود به مگابیت بر ثانیه (صفر برای نامحدود)
* **نمونه پاسخ:**
```json
{
  "status": "ok",
  "user": {
    "assigned_ip": 11,
    "name": "Reza",
    "key_hex": "e4f8a1...",
    "configUrl": "livekadeh://e4f8a1...@194.81.108.53:8443?name=Reza"
  }
}
```

#### ۳.۳. ویرایش اطلاعات کاربر (Update User)
* **متد:** `PUT`
* **مسیر:** `/api/users/:assignedIp`
* **بدنه درخواست (JSON):**
```json
{
  "enabled": 1,
  "expireDays": 60,
  "maxGb": 100,
  "speedLimitMbps": 50
}
```

#### ۳.۴. قطع اتصال فعال کاربر (Kick User)
* **متد:** `POST`
* **مسیر:** `/api/users/:assignedIp/kick`
* **توضیحات:** سشن فعال و تانل کلاینت را بدون حذف حساب کاربری او بلافاصله قطع می‌کند.

#### ۳.۵. ریست حجم مصرفی (Reset Traffic)
* **متد:** `POST`
* **مسیر:** `/api/users/:assignedIp/reset-traffic`
* **توضیحات:** میزان ترافیک مصرف شده (TX/RX) کاربر را صفر می‌کند.

#### ۳.۶. حذف دائمی کاربر (Delete User)
* **متد:** `DELETE`
* **مسیر:** `/api/users/:assignedIp`

#### ۳.۷. دریافت کانفیگ و QR Code کاربر
* **متد:** `GET`
* **مسیر:** `/api/users/:assignedIp/config`
* **نمونه پاسخ:**
```json
{
  "status": "ok",
  "configUrl": "livekadeh://e4f8a1...@194.81.108.53:8443?name=Reza",
  "serverIp": "194.81.108.53",
  "serverPort": 8443,
  "assignedInternalIp": "10.10.10.11",
  "keyHex": "e4f8a1b2c3d4..."
}
```

#### ۳.۸. تنظیمات سرور و پورت اتصال (Server Connection Settings)
* **متد:** `GET` / `POST`
* **مسیر:** `/api/settings`
* **توضیحات:** مشاهده و تنظیم آدرس عمومی سرور و پورت اتصال تانل جهت درج دقیق در بارکد QR و لینک‌های اتصال.

---

### ۴. پشتیبان‌گیری و بازیابی (Backup & Restore)

#### دریافت فایل بکاپ (Export Backup)
* **متد:** `GET`
* **مسیر:** `/api/backup`
* **توضیحات:** یک فایل کامل JSON از تمامی تنظیمات، اکانت‌ها، کلیدها و اعتبارات دانلود می‌کند.

#### بازگردانی بکاپ (Import Restore)
* **متد:** `POST`
* **مسیر:** `/api/restore`
* **بدنه درخواست:** محتوای JSON بکاپ قبلی.

---

## 🛠️ نمونه کدهای cURL برای توسعه‌دهندگان

```bash
# ۱. لاگین در پنل و ذخیره کوکی در فایل cookies.txt
curl -c cookies.txt -X POST http://YOUR_SERVER:8444/api/auth/login \
     -H "Content-Type: application/json" \
     -d '{"username":"admin","password":"YOUR_PASSWORD"}'

# ۲. ساخت کاربر جدید با ۵۰ گیگ حجم و اعتبار ۱ ماهه
curl -b cookies.txt -X POST http://YOUR_SERVER:8444/api/users \
     -H "Content-Type: application/json" \
     -d '{"name":"TestClient","expireDays":30,"maxGb":50,"speedLimitMbps":20}'

# ۳. دریافت وضعیت سرور و کاربران آنلاین
curl -b cookies.txt -X GET http://YOUR_SERVER:8444/api/system
```

---
*توسعه داده شده با ❤️ برای آزادی اینترنت و پایداری شبکه.*
