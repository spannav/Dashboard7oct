# 🎮 Global Video Game Sales & Market Analytics Dashboard
เว็บแอปพลิเคชัน Interactive Analytics Dashboard สำหรับวิเคราะห์ข้อมูลและสถิติวิดีโอเกมทั่วโลก โดยมีวัตถุประสงค์หลักเพื่อช่วยเหลือทีมบริหาร นักวางแผนการตลาด และนักพัฒนาเกม ในการประเมินแนวโน้มตลาด พฤติกรรมผู้บริโภครายภูมิภาค การจับคู่แนวเกมกับแพลตฟอร์มเครื่องเล่น และวิเคราะห์กลยุทธ์คะแนนรีวิวร่วมกับเรตติ้งอายุ (ESRB) เพื่อนำไปใช้ตัดสินใจเชิงกลยุทธ์ทางธุรกิจและวางแผนพัฒนาเกมได้อย่างแม่นย

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

## 📌 ภาพรวมโปรเจกต์ (Project Overview)

แดชบอร์ดนี้ออกแบบขึ้นเพื่อเปลี่ยนข้อมูลเชิงปริมาณด้านยอดขายเกมให้เป็น **คำแนะนำเชิงกลยุทธ์ (Strategic Actionable Insights)** สำหรับทีมบริหาร นักวางแผนการตลาด และนักพัฒนาเกม โดยครอบคลุมมุมมองสำคัญ 3 ด้าน:

* **Regional Market Preference:** วิเคราะห์สัดส่วนยอดขายเกมและพฤติกรรมการบริโภคในทวีปอเมริกาเหนือ (NA), ยุโรป (EU), ญี่ปุ่น (JP) และภูมิภาคอื่นๆ (Other)
* **Genre & Platform Synergy:** วิเคราะห์ความสัมพันธ์และการเลือกจับคู่ระหว่างแนวเกมกับแพลตฟอร์มเครื่องเล่นหลักที่สร้างรายได้สูงสุด
* **Reviews & ESRB Rating Strategy:** ประเมินผลกระทบระหว่างคะแนนนักวิจารณ์ (Critic Score), คะแนนผู้เล่นจริง (User Score) และเรตติ้งจำกัดอายุเนื้อหาต่อผลตอบแทนทางธุรกิจ

---

## 📂 แหล่งที่มาและขอบเขตข้อมูล (Data Source & Scope)

| หัวข้อการเปรียบเทียบ | ชุดข้อมูลต้นทาง (Original Data Source) | ชุดข้อมูลที่ประมวลผลบน Dashboard (Filtered Scope) |
|---|---|---|
| **แหล่งที่มาข้อมูล** | [Kaggle - Video Game Sales Dataset](https://www.kaggle.com/datasets/gregorut/videogamesales) (ดึงจาก [vgchartz.com](https://www.vgchartz.com)) | ดึงข้อมูลย่อยจาก Kaggle มาประมวลผลบน Dashboard |
| **จำนวนรายการข้อมูล** | **16,500+ รายการ** (16,598 Rows) | **500 รายการ** (`500 Titles`) |
| **ช่วงปีข้อมูล** | ย้อนหลังตั้งแต่ปี 1980 เป็นต้นมา | เน้นเฉพาะเกมยุคร่วมสมัยปี **2013 – 2024** |
| **ขอบเขตการคัดเลือก** | รวมเกมทั้งหมดที่มียอดขายตั้งแต่ 100,000 ชุดขึ้นไป | คัดเลือกเฉพาะ **Top 500 Games (Hit / Blockbuster Games)** |
| **เหตุผลการคัดกรอง** | ข้อมูลดิบเน้นเก็บประวัติศาสตร์ยอดขายวงการเกมทั้งหมด | **1. Focus Modern Trends:** วิเคราะห์คอนโซล Gen 8–9 (PS4, PS5, Switch, XSX) และ PC ยุคปัจจุบัน<br>**2. Business Impact:** มุ่งเน้นกลุ่มเกมทำเงินหลักที่ขับเคลื่อนเศรษฐกิจตลาดเกม<br>**3. Dashboard UX & Speed:** เพิ่มความเร็ว Render บน Plotly Dash และป้องกันกราฟอัดแน่นเกินไป |

---

## 🎨 แหล่งอ้างอิงต้นแบบดีไซน์ (UI/UX Design Reference)

* **Design Inspiration:** [Halo Lab - Dashboard Design Examples](https://www.halo-lab.com/blog/dashboard-design-examples)

---

## 🔑 นิยามคำศัพท์และหมวดหมู่ข้อมูล (Key Terminology)

### 1. แพลตฟอร์มเครื่องเล่นเกม (Platforms)
* **PC:** Personal Computer (คอมพิวเตอร์ตั้งโต๊ะและโน้ตบุ๊ก)
* **PS4:** PlayStation 4 (คอนโซลยุคที่ 8 จาก Sony)
* **PS5:** PlayStation 5 (คอนโซลยุคปัจจุบัน/ยุคที่ 9 จาก Sony)
* **Switch:** Nintendo Switch (คอนโซลกึ่งพกพาจาก Nintendo)
* **XOne:** Xbox One (คอนโซลยุคที่ 8 จาก Microsoft)
* **XSX:** Xbox Series X (คอนโซลยุคปัจจุบัน/ยุคที่ 9 จาก Microsoft)

### 2. แนวเกมหลัก 8 ประเภท (Game Genres)
* **Misc (เกมปาร์ตี้ / ครอบครัว):** เกมเล่นสนุกในกลุ่มเพื่อนหรือครอบครัว เน้นความเพลิดเพลิน ไม่เน้นความรุนแรง (เช่น *Just Dance*, *Wii Sports*)
* **Sports (เกมกีฬา):** เกมจำลองการแข่งขันกีฬาจริง (เช่น *FIFA / EA Sports FC*, *NBA 2K*)
* **Simulation (เกมจำลองสถานการณ์):** เกมจำลองการใช้ชีวิต สร้างเมือง หรือวางแผนบริหาร (เช่น *The Sims*, *Animal Crossing*)
* **Platform (เกมกระโดดด่าน):** เกมบังคับตัวละครกระโดดข้ามสิ่งกีดขวางผ่านด่าน (เช่น *Super Mario*)
* **Shooter (เกมยิง):** เกมมุมมองบุคคลที่หนึ่ง/สาม เล็งยิงเป้าหมาย สู้กันในสมรภูมิ (เช่น *Call of Duty*, *PUBG*)
* **Role-Playing / RPG (เกมสวมบทบาท):** เกมเน้นเนื้อเรื่องเข้มข้น ปรับแต่งและพัฒนาความสามารถตัวละคร (เช่น *Pokémon*, *Final Fantasy*)
* **Racing (เกมแข่งรถ):** เกมขับรถประชันความเร็ว (เช่น *Mario Kart*, *Need for Speed*)
* **Action (เกมแอ็กชัน):** เกมต่อสู้เคลื่อนไหวรวดเร็ว เน้นจังหวะและฝีมือการควบคุม (เช่น *God of War*, *GTA*)

### 3. เรตติ้งความเหมาะสมเนื้อหา (ESRB Content Ratings)
* **E (Everyone):** เหมาะสำหรับทุกคน ทุกวัย ไม่มีเนื้อหารุนแรง
* **E10+ (Everyone 10+):** เหมาะสำหรับผู้เล่นอายุ 10 ขวบขึ้นไป อาจมีความรุนแรงแฟนตาซีเล็กน้อย
* **T (Teen):** เหมาะสำหรับวัยรุ่นอายุ 13 ปีขึ้นไป อาจมีภาษาหรือเนื้อหาชวนตื่นเต้น
* **M (Mature 17+):** เหมาะสำหรับผู้ใหญ่ อายุ 17 ปีขึ้นไป เนื้อหามีความรุนแรงหรือสมจริง

---

## 🖥️ รายละเอียดองค์ประกอบบนแดชบอร์ด (Dashboard Features)

### 📌 Tab 1: Executive Overview & Regional Market Share
* **KPI Summary Cards:** แสดงยอดขายรวม ($M USD), จำนวนเกม (Titles), แนวเกมขายดีที่สุด และแพลตฟอร์มอันดับ 1
* **Yearly Sales Trend (Line Chart):** วิเคราะห์แนวโน้มยอดขายเกมรวมทั่วโลกย้อนหลังตั้งแต่ปี 2013–2024 เพื่อดูทิศทางการเติบโตของอุตสาหกรรม
* **Regional Breakdown (Stacked Bar Chart):** เปรียบเทียบสัดส่วนยอดขายตามทวีปหลัก (NA, EU, JP, Other) ซ้อนทับตามแนวเกม
* **Top 10 Best-Selling Games (Horizontal Bar Chart):** จัดอันดับ 10 เกมที่ทำรายได้สูงสุดในโลก พร้อมทำ Clean Label ตัด Prefix รหัสเกมออก

### 📌 Tab 2: Genre & Platform Dynamics
* **Hero KPI Card:** แสดง `Most Published Genre` (แนวเกมที่มีการสร้างมากที่สุด) แบบ Static Card เพื่อคงค่าเปรียบเทียบมาตรฐาน
* **Genre vs Platform Heatmap:** ตารางความร้อนแสดงความเข้มข้นยอดขายรวมระหว่างแนวเกมคู่กับเครื่องเล่นเกม เพื่อหาความเข้ากันได้
* **Publisher Market Share (Treemap):** วิเคราะห์ส่วนแบ่งตลาดสะสมของค่ายเกมยักษ์ใหญ่
* **Total Sales by Genre (Bar Chart):** เปรียบเทียบเม็ดเงินยอดขายรวมแยกตามประเภทเกม

### 📌 Tab 3: Critical Acclaim & ESRB Strategy
* **Sales by Review Score Tiers (Bar Chart):** วิเคราะห์ผลตอบแทนยอดขายเฉลี่ยต่อเกมตามเกรดคะแนนรีวิว (90+, 80-89, 70-79, <70)
* **Top 10 Best Rated Games:** จัดอันดับ 10 เกมที่ได้คะแนนจากนักวิจารณ์สูงสุด (ล็อคสเกลแกน X ที่ 0–100 Points)
* **Critic vs User Score Comparison (Multi-Line Chart):** เปรียบเทียบคะแนนเฉลี่ยระหว่างสื่อมวลชน (เส้นสี Indigo Blue) กับผู้เล่นจริง (เส้นสี Coral Red)
* **Regional Preference by ESRB (100% Stacked Bar):** สัดส่วนยอดขายตามภูมิภาคจำแนกตามเรตติ้งอายุ
* **Genre x ESRB Sales Matrix (Heatmap):** วิเคราะห์ช่องว่างทางการตลาด (White Space) ในการเลือกทำแนวเกมคู่กับเรตติ้งอายุเพื่อลดความเสี่ยงทางธุรกิจ

---

## 📁 โครงสร้างไฟล์ในโปรเจกต์ (File Directory)

| ชื่อไฟล์ / โฟลเดอร์ | ประเภท | คำอธิบายหน้าที่ |
|---|---|---|
| **`app.py`** | Source Code | ⭐ ไฟล์หลัก Dash Application รวม Layout และ Callbacks |
| **`video_game_sales.csv`** | Dataset | ฐานข้อมูลยอดขายเกม (500 Titles Scope) |
| **`assets/style.css`** | Styling | Custom CSS สไตล์ Modern Soft Minimalist & Dark Sidebar |
| **`requirements.txt`** | Dependencies | รายการ Libraries ที่ใช้ในโปรเจกต์ |
| **`README.md`** | Docs | เอกสารอธิบายภาพรวมและการใช้งานโปรเจกต์ |
| **`HANDOFF.md`** | Docs | เอกสารสรุปสถาปัตยกรรมระบบและการส่งมอบงาน |
| **`project_status.md`** | Docs | เอกสารบันทึกสถานะโปรเจกต์ |
| **`dashboard_style.md`** | Docs | เอกสารข้อกำหนดสไตล์ UI/UX (BRD v7.0) |
| **`brd_global_video_game_sales_dashboard.md`** | Docs | ข้อกำหนดความต้องการทางธุรกิจ (BRD) ฉบับแรก |
| **`fix_apppy.md` - `fix_apppy_round7.md`** | Docs | เอกสารบันทึกการแก้ไขโค้ดตามรอบงาน (Round 1 - 7) |
| **`generate_mock_data.py`** | Script | สคริปต์สำหรับสร้าง/เตรียมข้อมูลทดสอบ |
| **`test_script.py` / `test_script2.py`** | Script | สคริปต์ทดสอบการทำงานภายในระบบ |
| **`.gitignore`** | Config | กฎการละเว้นไฟล์สำหรับ Git Version Control |
| **`.venv/`** | Environment | Python Virtual Environment |
| **`__pycache__/`** | Cache | ไฟล์แคชการประมวลผลของ Python |

---

## 🛠️ เทคโนโลยีที่ใช้ (Tech Stack & Dependencies)

| เทคโนโลยี / ไลบรารี | เวอร์ชัน / สเปก | รายละเอียดการใช้งาน |
|---|---|---|
| **Python** | 3.12+ | ภาษาหลักในการประมวลผลข้อมูลและ Web Server |
| **Plotly Dash** | Latest | Framework สำหรับสร้าง Web Interactive Analytics |
| **Dash Bootstrap Components** | `BOOTSTRAP` Theme | จัดสรร Responsive UI Layout และ Grid Components |
| **Pandas & NumPy** | Latest | บริหารจัดการ คัดกรอง และคำนวณสถิติชุดข้อมูล |
| **Plotly Express & Graph Objects** | Latest | สร้างและปรับแต่งแผนภูมิมิติปฏิสัมพันธ์ (Interactive Charts) |

---

## 🚀 วิธีการติดตั้งและเปิดใช้งาน (Quick Start)

### 1. Clone Repository
```bash
git clone https://github.com/spannav/Dashboard7oct.git
cd Dashboard7oct
```

### 2. สร้างและเปิดใช้งาน Virtual Environment
* **Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  ```
* **macOS / Linux:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 3. ติดตั้ง Dependencies
```bash
pip install -r requirements.txt
```

### 4. รันแอปพลิเคชัน
```bash
python app.py
```
