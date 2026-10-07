# 🎮 Global Video Game Sales & Market Analytics Dashboard

**GitHub Repository:** [https://github.com/spannav/Dashboard7oct](https://github.com/spannav/Dashboard7oct)

**🌐 Live Dashboard:** [https://dashboard7oct.onrender.com](https://dashboard7oct.onrender.com) *(Deploy on Render)*

## **สมาชิก กลุ่ม "ธนพล"**
| ลำดับ | รหัสนักศึกษา | ชื่อ-นามสกุล |
| :---: | :---: | :--- |
| 1 | 673020253-2 | ธนพล ท้าวนอ |
| 2 | 673020271-0 | อุดมศักดิ์ พระเสนา |
| 3 | 673020627-7 | ศุภณัฏฐ์ ปุณมา |
| 4 | 673020638-7 | พิชญธิดา ขัตติยะ |
| 5 | 673020639-5 | ศศิภัทชา เจียรเจริญกิจ |

---

## Project Overview
This project is an interactive dashboard for analyzing the global video game market, including growth trends, regional consumer behaviors, the relationship between game genres, platforms, and publishers, as well as the correlation between game quality (review scores) and commercial success.

## Technical Stack
| Technology | Detail |
|---|---|
| **Language** | Python 3.12 |
| **Framework** | Plotly Dash |
| **UI Components** | dash-bootstrap-components (Bootstrap theme) |
| **Data** | pandas, numpy |
| **Visualization** | plotly.express, plotly.graph_objects |
| **Deployment** | Render (Gunicorn) |

## Dashboard Structure
1. **Tab 1: Executive Overview & Regional Market Share** — Global sales trends, regional breakdown, and top games.
2. **Tab 2: Genre & Platform Dynamics** — Genre vs. platform performance, publisher market share, and average sales.
3. **Tab 3: Critical Acclaim & ESRB Strategy** — Impact of review scores on sales, ESRB rating analysis.

## Setup Instructions (Local Development)
```bash
# 1. Clone the repo
git clone https://github.com/spannav/Dashboard7oct.git
cd Dashboard7oct

# 2. Create virtual environment
python -m venv .venv

# 3. Activate (Windows PowerShell)
.venv\Scripts\Activate.ps1

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the dashboard
python app.py

# 6. Open browser → http://localhost:8050/
```

## Deployment (Render)
1. Push to GitHub
2. Go to [Render Dashboard](https://dashboard.render.com/)
3. **New → Web Service** → Connect GitHub repo `spannav/Dashboard7oct`
4. Settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:server`
   - **Python Version:** `3.12` (auto-detected from `runtime.txt`)
5. Deploy!

## Features
- 📊 Interactive cross-filtering across charts within the same tab
- 📋 Detailed KPI cards for quick insights
- 🔍 Slicers and filters for deep-dive analysis
- 🔄 Reset Filters button on every tab
- 🎨 Modern Soft Minimal design with sidebar navigation
