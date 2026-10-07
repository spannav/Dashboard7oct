# 📋 Handoff Document: Global Video Game Sales Analytics Dashboard

**วันที่ส่งต่อ:** 7 ตุลาคม 2026  
**โปรเจกต์:** Global Video Game Sales Analytics Dashboard  
**GitHub Repository:** https://github.com/spannav/Dashboard7oct  
**Branch:** `main`

---

## 1. ภาพรวมโปรเจกต์ (Project Overview)

Dashboard วิเคราะห์ข้อมูลยอดขายวิดีโอเกมทั่วโลก สร้างด้วย Python Plotly Dash มี 3 แท็บหลัก:
- **Tab 1:** ภาพรวมตลาดและยอดขายรายภูมิภาค
- **Tab 2:** เจาะลึกแนวเกม แพลตฟอร์ม และค่ายเกม
- **Tab 3:** วิเคราะห์คะแนนรีวิวและกลยุทธ์เรตติ้ง ESRB

---

## 2. โครงสร้างไฟล์ (File Structure)

```
Dashboard7oct/
├── app.py                              # ⭐ ไฟล์หลัก - Dash application (465 บรรทัด)
├── video_game_sales.csv                # ข้อมูลยอดขายเกม (mock data)
├── requirements.txt                    # Dependencies (dash, dash-bootstrap-components, pandas, plotly)
├── README.md                           # README พร้อมลิงก์ GitHub
├── .gitignore                          # Git ignore rules
├── assets/
│   └── style.css                       # ⭐ Custom CSS สไตล์ Modern Soft Minimal
├── generate_mock_data.py               # สคริปต์สร้างข้อมูลจำลอง
├── test_script.py                      # สคริปต์ทดสอบ
├── test_script2.py                     # สคริปต์ทดสอบ
├── brd_global_video_game_sales_dashboard.md  # BRD ฉบับแรก
├── fix_apppy.md                        # BRD แก้ไข round 1
├── fix_apppy_round2.md                 # BRD แก้ไข round 2
├── fix_apppy_round3.md                 # BRD แก้ไข round 3
├── fix_apppy_round4.md                 # BRD แก้ไข round 4 (Dual-Line Chart)
├── fix_apppy_round5.md                 # BRD แก้ไข round 5
├── fix_apppy_round6.md                 # BRD แก้ไข round 6 (ESRB Charts)
├── fix_apppy_round7.md                 # BRD แก้ไข round 7 (Reset Buttons, ถอดกราฟ)
├── dashboard_style.md                  # BRD สไตล์ v7.0 (Sidebar + Modern Theme)
├── project_status.md                   # สถานะโปรเจกต์เดิม
└── .venv/                              # Python virtual environment (ไม่ได้ push ขึ้น Git)
```

---

## 3. Tech Stack และ Dependencies

| เทคโนโลยี | รายละเอียด |
|---|---|
| **ภาษา** | Python 3.12 |
| **Framework** | Plotly Dash |
| **UI Components** | dash-bootstrap-components (ใช้ theme `BOOTSTRAP`) |
| **Data** | pandas, numpy |
| **Visualization** | plotly.express, plotly.graph_objects |
| **CSS** | Custom CSS ที่ `assets/style.css` (Dash auto-load) |

**ติดตั้ง:**
```bash
pip install -r requirements.txt
```

**รัน:**
```bash
python app.py
# Dashboard จะเปิดที่ http://localhost:8050/
# debug=True จะ auto-reload เมื่อแก้ไขไฟล์
```

---

## 4. สถาปัตยกรรม app.py (Architecture)

### 4.1 โครงสร้างโค้ด (บรรทัดโดยประมาณ)

| ส่วน | บรรทัด | รายละเอียด |
|---|---|---|
| Imports & Data Loading | 1-15 | โหลด CSV, rename column `coritic_scre` → `critic_score`, สร้าง `clean_title` |
| App Init & Layout | 17-47 | สร้าง Dash app, sidebar navigation, main layout |
| `render_tab_1()` | 50-92 | Layout ของ Tab 1 (Filters, KPIs, Graphs) |
| `render_tab_2()` | 94-131 | Layout ของ Tab 2 |
| `render_tab_3()` | 133-209 | Layout ของ Tab 3 (Vertical filters, ESRB checklist) |
| Navigation Callback | 211-229 | ฟังก์ชันสลับแท็บผ่าน Sidebar NavLinks |
| `update_tab_1()` | 231-299 | Callback อัปเดตกราฟ Tab 1 |
| `update_tab_2()` | 301-360 | Callback อัปเดตกราฟ Tab 2 |
| `update_tab_3()` | 362-435 | Callback อัปเดตกราฟ Tab 3 |
| Reset Callbacks | 437-459 | ปุ่ม Reset Filters ทั้ง 3 แท็บ |
| Main Entry | 461-465 | `app.run(debug=True)` |

### 4.2 การนำทาง (Navigation)

ใช้ **Sidebar Navigation** แทน `dcc.Tabs` เดิม:
- Sidebar อยู่ซ้าย (`position: fixed`, กว้าง 250px, สี `#343A40`)
- เนื้อหาหลักอยู่ขวา (`margin-left: 250px`)
- สลับแท็บด้วย `dbc.NavLink` → callback `render_content()` ที่ใช้ `dash.callback_context`

### 4.3 Cross-Filtering (การเชื่อมต่อกราฟ)

| Tab | กราฟที่ Click ได้ | ผลกระทบ |
|---|---|---|
| Tab 1 | `t1-yearly-sales` (selectedData) | กรองข้อมูลตามปีที่เลือก → อัปเดต Regional Breakdown + Top Games |
| Tab 2 | `t2-heatmap` (clickData) | กรองตาม Genre+Platform ที่คลิก → อัปเดต Treemap + Bar Chart |
| Tab 3 | `t3-score-tiers-bar` (clickData) | กรองตาม Score Tier ที่คลิก → อัปเดตกราฟทั้งหมดใน Tab 3 |

### 4.4 Reset Buttons

ทุกแท็บมีปุ่ม **"Reset Filters"** สีแดง ทรง Pill:
- รีเซ็ตทั้ง Filter (Dropdown, Slider, Checklist) **และ** Graph State (clickData, selectedData)
- ใช้ `prevent_initial_call=True` เพื่อไม่ให้ทำงานตอนโหลดหน้าแรก
- **ห้ามใช้ `location.reload()`** ต้องใช้ Callback เท่านั้น

---

## 5. รายละเอียดชุดข้อมูล (Dataset: video_game_sales.csv)

| Column | ประเภท | หมายเหตุ |
|---|---|---|
| `title` | string | ชื่อเกมดิบ (อาจมี prefix เช่น `Game___`) |
| `clean_title` | string | ชื่อที่ล้าง prefix แล้ว (สร้างตอน runtime) |
| `platform` | string | เครื่องเล่นเกม |
| `release_year` | int | ปีวางจำหน่าย |
| `genre` | string | หมวดหมู่เกม (~12 หมวด) |
| `publisher` | string | ค่ายเกม |
| `na_sales` | float | ยอดขายอเมริกาเหนือ ($M USD) |
| `eu_sales` | float | ยอดขายยุโรป ($M USD) |
| `jp_sales` | float | ยอดขายญี่ปุ่น ($M USD) |
| `other_sales` | float | ยอดขายภูมิภาคอื่น ($M USD) |
| `global_sales` | float | ยอดขายรวมทั่วโลก ($M USD) |
| `critic_score` | float | คะแนนนักวิจารณ์ (0-100) |
| `user_score` | float | คะแนนผู้เล่น (0-10, ต้อง *10 เพื่อปรับสเกล) |
| `esrb_rating` | string | เรตติ้งอายุ (E, E10+, T, M) — มีค่า NaN |

---

## 6. Design System & สไตล์ (assets/style.css)

| องค์ประกอบ | ค่า |
|---|---|
| **Sidebar BG** | `#343A40` (Dark Slate) |
| **Main Canvas BG** | `#F4F5F7` (Soft Light Gray) |
| **Card** | `border-radius: 20px`, `box-shadow: 0 10px 25px -5px rgba(0,0,0,0.04)`, ไม่มี border |
| **Hero Card** | `background-color: #6EB897` (Sage Green), ตัวอักษรสีขาว |
| **Nav Active** | `#4A4EA4` (Royal Indigo) |
| **Reset Button** | `border-radius: 50rem` (Pill shape), ใช้ `btn-danger` |
| **Plotly Charts** | `border-radius: 20px`, `overflow: hidden` |

**ชุดสีกราฟ Plotly:**
- หลัก: `#6EB897` (Sage Green), `#4A4EA4` (Indigo), `#FF6B6B` (Coral), `#FECB2E` (Amber)
- ขยาย (สำหรับกราฟที่มีหลายหมวด): เพิ่ม `#36C9C6`, `#9B5DE5`, `#F15BB5`, `#00BBF9`, `#00F5D4`, `#F4A261`, `#E76F51`, `#2A9D8F`

---

## 7. กราฟทั้งหมดในระบบ (All Charts)

### Tab 1: Executive Overview
| กราฟ | Component ID | ประเภท | ข้อมูลหลัก |
|---|---|---|---|
| Yearly Sales Trend | `t1-yearly-sales` | Line Chart | ยอดขายรวมรายปี |
| Regional Breakdown | `t1-regional-breakdown` | Stacked Bar | ยอดขายแยกภูมิภาค x แนวเกม |
| Top 10 Best-Selling | `t1-top-games` | Horizontal Stacked Bar | 10 เกมยอดขายสูงสุด |

### Tab 2: Genre & Platform
| กราฟ | Component ID | ประเภท | ข้อมูลหลัก |
|---|---|---|---|
| Genre vs Platform | `t2-heatmap` | Heatmap (imshow) | ยอดขายตาม Genre x Platform |
| Publisher Share | `t2-treemap` | Treemap | ส่วนแบ่งตลาดค่ายเกม |
| Sales by Genre | `t2-total-sales` | Bar Chart | ยอดขายรวมแยกตาม Genre |

### Tab 3: Reviews & ESRB
| กราฟ | Component ID | ประเภท | ข้อมูลหลัก |
|---|---|---|---|
| Sales by Score Tier | `t3-score-tiers-bar` | Bar Chart | ยอดขายเฉลี่ยตามเกรดคะแนน |
| Top 10 Best Rated | `t3-top-rated-bar` | Horizontal Bar | 10 เกมที่ได้คะแนนสูงสุด |
| Critic vs User Score | `t3-score-compare-bar` | Multi-Line Chart | เปรียบเทียบคะแนนนักวิจารณ์ vs ผู้เล่น |
| ESRB Regional | `t3-esrb-regional-bar` | 100% Stacked Bar | สัดส่วนยอดขายภูมิภาคตาม ESRB |
| ESRB Heatmap | `t3-esrb-heatmap` | Heatmap (imshow) | Genre x ESRB Rating |

---

## 8. ปัญหาที่ทราบ (Known Issues)

| # | ปัญหา | รายละเอียด | ความสำคัญ |
|---|---|---|---|
| 1 | `app.run()` ซ้ำ 2 ครั้ง | บรรทัด 462 และ 464 มี `app.run(debug=True)` ซ้ำ (ไม่กระทบเพราะถึงบรรทัดที่ 2 ไม่มีทาง) | ต่ำ |
| 2 | Dashboard เปิดได้เฉพาะ localhost | ยังไม่ได้ Deploy ขึ้น Cloud ทำให้คนอื่นเปิดจากเครื่องตัวเองไม่ได้ | สูง |
| 3 | Tab 2 Hero KPI ยังไม่ Static 100% | `Most Published Genre` ถูกตั้งค่าเป็น Static แต่อาจยังมี edge case | ปานกลาง |

---

## 9. สิ่งที่ยังไม่ได้ทำ / ทำต่อได้ (Pending / Future Work)

| # | งาน | รายละเอียด |
|---|---|---|
| 1 | **Deploy ขึ้น Cloud** | Deploy dashboard ให้เปิดได้จากเครื่องอื่นผ่าน URL สาธารณะ เช่น Render, Railway, Heroku หรือ PythonAnywhere — ต้องเพิ่ม `server = app.server` ใน app.py และสร้าง Procfile/runtime config |
| 2 | **เพิ่ม .gitignore** | ควร ignore `__pycache__/`, `.venv/`, `*.pyc` (อาจมีอยู่แล้วบางส่วน) |
| 3 | **ลบไฟล์ที่ไม่จำเป็น** | `test_script.py`, `test_script2.py`, `generate_mock_data.py` อาจไม่จำเป็นใน production |
| 4 | **แก้ app.run() ซ้ำ** | ลบ `app.run(debug=True)` บรรทัดที่ 464 ออก |
| 5 | **อัปเดต README** | เพิ่มลิงก์ Dashboard ที่ deploy แล้ว (แทน localhost) |

---

## 10. Git History (ล่าสุด)

```
36ecfde Fix duplicate colors in Tab 1 stacked bar and add GitHub link to README
5c4b44c final and gitignore
a0ac93a Update dashboard to version 7.0 with new styling, layout changes, and README updates
3b71e44 fix round 7
bb96ab6 not fix round3
7828cb0 Initial commit with README and Project Status
```

**Remote:** `origin → https://github.com/spannav/Dashboard7oct.git`  
**Branch ปัจจุบัน:** `main` (up-to-date กับ remote)

---

## 11. วิธีรันโปรเจกต์ (Quick Start for Next Developer)

```bash
# 1. Clone repo
git clone https://github.com/spannav/Dashboard7oct.git
cd Dashboard7oct

# 2. สร้าง virtual environment
python -m venv .venv

# 3. Activate (Windows PowerShell)
.venv\Scripts\Activate.ps1

# 4. ติดตั้ง dependencies
pip install -r requirements.txt

# 5. รัน dashboard
python app.py

# 6. เปิด browser ไปที่ http://localhost:8050/
```

---

## 12. BRD References

ไฟล์ BRD เรียงตามลำดับ (อ่านเพื่อเข้าใจ context ย้อนหลัง):
1. `brd_global_video_game_sales_dashboard.md` — ข้อกำหนดฉบับแรก
2. `fix_apppy.md` → `fix_apppy_round7.md` — การแก้ไขเรื่อยมา
3. `dashboard_style.md` — ข้อกำหนดสไตล์ v7.0 (ฉบับล่าสุด ใช้อ้างอิงหลัก)
