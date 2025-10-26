


# 🎥 YouTube Manager

A Python-based YouTube Manager that helps users organize, analyze, and manage their YouTube content using **MongoDB** as the database and **PyMongo** as the connector.  
This project provides CRUD operations for videos, channels, playlists, and analytics tracking — all from an intuitive command-line interface or integrated UI.

---

## 🚀 Features

- 📦 **Add / View / Update / Delete** YouTube videos  
- 📋 **Manage playlists** and their associated videos  
- 📊 **Track video stats** like views, likes, and comments  
- 🔍 **Search** videos or playlists by title, tags, or category  
- 🗃️ **MongoDB Integration** using PyMongo  
- 💾 Persistent storage for YouTube data  
- ⚙️ Easy configuration and modular Python structure  

---

## 🧠 Tech Stack

| Component | Technology Used |
|------------|----------------|
| **Language** | Python 3.x |
| **Database** | MongoDB |
| **Connector** | PyMongo |
| **Interface** | Command-line / Tkinter (optional) |

---

## 📁 Project Structure

```

YouTube-Manager/
│
├── main.py               # Entry point of the app
├── db_config.py          # MongoDB connection setup
├── video_manager.py      # CRUD operations for videos
├── playlist_manager.py   # Playlist management functions
├── analytics.py          # Stats & performance tracking
├── requirements.txt      # Required dependencies
└── README.md             # Project documentation

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/youtube-manager.git
cd youtube-manager
````

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate       # For Linux/Mac
venv\Scripts\activate          # For Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure MongoDB

* Make sure MongoDB is running locally or in the cloud (MongoDB Atlas).
* Update your connection string in **`db_config.py`**:

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["youtube_manager"]
```

---

## ▶️ How to Run

```bash
python main.py
```

You’ll be prompted with menu options to perform various YouTube management actions like adding videos, viewing playlists, or checking analytics.

---

## 🧩 Example Commands

```
1. Add New Video
2. Update Video Stats
3. View All Playlists
4. Delete a Video
5. Search by Tag
6. Exit
```

---

## 📊 Database Structure (Example)

**Database:** `youtube_manager`

**Collections:**

* `videos`
* `playlists`
* `analytics`

**Sample Document (videos):**

```json
{
  "_id": "abcd1234",
  "title": "Python Crash Course",
  "channel": "Code Alien",
  "views": 12000,
  "likes": 850,
  "tags": ["python", "tutorial", "beginner"],
  "upload_date": "2025-10-20"
}
```

---

## 🧰 Dependencies

```
pymongo==4.6.0
python-dotenv==1.0.1
```

---

## 🧑‍💻 Future Enhancements

* 🌐 Add a Flask/Django-based web interface
* 📅 Integrate YouTube API for real-time data sync
* 📈 Add visual analytics dashboard using Matplotlib or Plotly
* 🔐 Include authentication for different users

---

## 🤝 Contributing

Contributions are welcome!
If you’d like to improve the YouTube Manager, please **fork** the repo, create a new branch, and submit a **pull request**.

---

## 🧾 License

This project is licensed under the **MIT License**.

---

## ✨ Author

**Rakshit Bagait**
🔗 [GitHub](https://github.com/rakshitbagait) | [LinkedIn](https://linkedin.com/in/rakshitbagait)

---

<div align="center">
  <img src="image-1.png" alt="YouTube Manager Logo" width="200" style="border-radius:50%;">
  <p>📺 Manage. Analyze. Grow your channel with <b>YouTube Manager</b>.</p>
</div>
---


