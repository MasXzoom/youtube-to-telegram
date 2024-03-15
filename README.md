# YouTube Downloader Telegram Bot

## Overview
**YouTube Downloader Telegram Bot** adalah bot Telegram yang memungkinkan pengguna untuk mengunduh video dari YouTube langsung melalui chat Telegram. Dengan menyediakan link video YouTube, pengguna dapat memilih resolusi video yang diinginkan, dan bot akan mengirimkan video tersebut sebagai file video langsung ke chat Telegram mereka.

Fitur utama:
- Mendukung berbagai resolusi video (360p, 720p, 1080p)
- Pengunduhan cepat dan pengiriman langsung ke chat Telegram
- Mudah digunakan dengan antarmuka berbasis InlineKeyboard

## Teknologi
Proyek ini dibangun menggunakan:
- Python 3
- `python-telegram-bot` library untuk integrasi Telegram Bot API
- `yt-dlp` untuk pengunduhan video dari YouTube


### Prasyarat
Pastikan Anda memiliki Python 3 dan pip terinstal pada sistem Anda. Bot ini telah diuji dengan Python 3.8+.

### Instalasi

1. **Clone Repository**
   
   Pertama, clone repository ini ke sistem lokal Anda menggunakan git:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name


## Persiapan

Pastikan Anda telah menginstal Python 3 dan pip pada sistem Anda. Bot ini telah diuji dengan Python 3.8 atau lebih baru.

## Cara Menggunakan

1. **Buat Virtual Environment (Opsional)**

    Disarankan menggunakan virtual environment untuk menjaga dependensi terisolasi:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Untuk Unix atau MacOS
    venv\Scripts\activate  # Untuk Windows
    ```

2. **Instal Dependensi**

    Instal semua dependensi yang diperlukan menggunakan pip:
    ```bash
    pip install -r requirements.txt
    ```

3. **Konfigurasi Token Bot**

    Buat file `config.py` dan tambahkan token bot Telegram Anda:
    ```python
    TELEGRAM_TOKEN = 'your_bot_token_here'
    ```
    Anda dapat mendapatkan token bot dari [@BotFather](https://t.me/BotFather) di Telegram.

4. **Menjalankan Bot**

    Setelah konfigurasi selesai, jalankan bot dengan perintah:
    ```bash
    python bot.py
    ```
    Bot sekarang harus aktif dan merespons permintaan di Telegram.

## Penggunaan

- Kirim link video YouTube ke bot.
- Pilih resolusi video yang diinginkan dari opsi yang disediakan.
- Bot akan mengunduh video dan mengirimkannya ke chat Anda.

## Kontribusi

Kontribusi selalu diterima! Silakan fork repo, buat perubahan, dan kirimkan Pull Request. Untuk masalah besar, harap buka issue terlebih dahulu untuk mendiskusikan apa yang ingin Anda ubah.

## Lisensi

Distributed under the MIT License. Lihat file `LICENSE` untuk informasi lebih lanjut.
