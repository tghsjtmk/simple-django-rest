## 🧠 Rangkuman

| Konsep      | Implementasi                          |
| :---------- | :------------------------------------ |
| Custom User | `member.User` sebagai AUTH_USER_MODEL |
| Blog Model  | `Post` di `blog/models.py`            |
| API CRUD    | `generics.APIView` via DRF            |
| Auth        | JWT via `dj-rest-auth` + `simplejwt`  |
| Docs        | Swagger dengan `drf-spectacular`      |

---

## 💪 Tugas Akhir (Opsional)

Tambahkan fitur **Komentar**:

- Model `Comment` dengan relasi ke `Post`
- Endpoint CRUD `/api/blogs/comments/`
- Filter komentar berdasarkan `post_id`

---

## 🎯 Bonus

- Debug with `settings.DEBUG`
- Implementasi pagination
- Tambahkan field `category` di model Post
