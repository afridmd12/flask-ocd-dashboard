# 📊 Stock Market Dashboard

An interactive **Stock Market Analysis Dashboard** built with **Flask** and **Plotly**, deployed on **Render**, and version-controlled with **GitHub**.  
This project allows users to upload CSV files, select stock tickers, and visualize stock price trends.

🔗 **Live Demo:** [https://stock-marketing.onrender.com](https://stock-marketing.onrender.com)

---

## 🚀 Complete Process (From Start to Finish)

### 1. Create Project Folder
D:\stock_marketing_work

### 2. Create & Activate Virtual Environment
- Windows:
  - `python -m venv venv`
  - `venv\Scripts\activate`
- macOS/Linux:
  - `python3 -m venv venv`
  - `source venv/bin/activate`

### 3. Install Dependencies
- Install required libraries:
  - `pip install flask plotly pandas gunicorn`
- Export dependencies:
  - `pip freeze > requirements.txt`

### 4. Build Flask Application
- Created `app.py` with routes:
  - `/` → Main dashboard (CSV upload + ticker selection + charts)
  - `/report` → Report page for extended analysis
- Used:
  - Flask → backend server
  - Plotly → interactive charts
  - Pandas → CSV data handling

### 5. Add Project Files
- `app.py` → Main Flask application  
- `templates/` → HTML templates (dashboard, report)  
- `static/` → CSS/JS assets  
- `requirements.txt` → Installed dependencies  
- `Procfile` → For Render deployment (`web: gunicorn app:app`)  

### 6. Initialize Git & Push to GitHub
- `git init`  
- `git remote add origin https://github.com/afridmd12/stock_marketing.git`  
- `git add .`  
- `git commit -m "Initial commit"`  
- `git push -u origin main`

### 7. Deploy on Render
1. Go to [Render](https://render.com)  
2. Create a new **Web Service**  
3. Connect GitHub repository  
4. Add:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Deploy 🚀  

---

## ✅ Features
- Upload CSV with stock data  
- Select tickers and visualize interactive charts  
- `/report` page for extended analysis  
- Hosted live on Render  

---

---

## 💻 Run Locally
1. Clone repo:  
   `git clone https://github.com/afridmd12/stock_marketing.git`
2. Navigate:  
   `cd stock_marketing`
3. Create virtual environment & activate  
4. Install dependencies:  
   `pip install -r requirements.txt`
5. Run app:  
   `python app.py`
6. Open in browser:  
   `http://127.0.0.1:3001`

---

## 🌐 Deployment
- Hosted on **Render**
- Live URL: [https://stock-marketing.onrender.com](https://stock-marketing.onrender.com)

---

## 📝 Author
👤 Mohammed Afrid  
📌 GitHub: [afridmd12](https://github.com/afridmd12)  
