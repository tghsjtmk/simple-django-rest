## 🕐 Sesi 1 - Pengenalan & Setup Project (40 menit)

### 🔍 Apa itu Django?

Django adalah framework web berbasis Python yang:

- Cepat dan aman.
- Menggunakan ORM (Object Relational Mapping) untuk mengelola database tanpa SQL manual.
- Cocok untuk membuat REST API modern.

---

### 📦 1. Buat Folder & Virtual Environment

```bash
mkdir simple-blog
cd simple-blog
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

---

### ⚙️ 2. Instalasi Dasar

```bash
pip install --upgrade pip
pip install django django-environ psycopg2-binary black
pip freeze
touch requirements.txt
```

Tambahkan versi ke `requirements.txt`:

```txt
Django==5.2.7
black==25.9.0
django-environ==0.12.0
psycopg2-binary==2.9.11
```

---

### 🧱 3. Membuat Project dan App `member`

```bash
django-admin startproject playground .
python manage.py startapp member
```

---
