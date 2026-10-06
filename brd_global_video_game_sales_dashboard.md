# Business Requirements Document (BRD)

## Project: Global Video Game Sales & Market Analytics Dashboard

---

## 1. Project Overview & Objectives

### 1.1 Executive Summary
โครงการพัฒนา Interactive Dashboard สำหรับวิเคราะห์ภาพรวมตลาดเกมทั่วโลก (Global Video Game Market) แนวโน้มการเติบโต พฤติกรรมการซื้อของผู้บริโภคในแต่ละภูมิภาค ความสัมพันธ์ระหว่างประเภทเกม แพลตฟอร์ม และค่ายผู้พัฒนา ตลอดจนการวิเคราะห์ความสัมพันธ์ระหว่างคุณภาพของเกม (คะแนนรีวิว) กับยอดขายจริง เพื่อช่วยในการตัดสินใจเชิงกลยุทธ์สำหรับการลงทุนและการพัฒนาเกม

### 1.2 Core Business Questions
1. **Tab 1 (Executive Overview):** ตลาดเกมทั่วโลกมีมูลค่าเท่าไร แนวโน้มการเติบโตเป็นอย่างไร และพฤติกรรมการซื้อเกมในแต่ละภูมิภาคแตกต่างกันอย่างไร?
2. **Tab 2 (Genre & Platform Dynamics):** แพลตฟอร์มใดเหมาะกับเกมแนวไหน ค่ายผู้พัฒนาใดครองส่วนแบ่งตลาด และหมวดหมู่ใดสร้างยอดขายเฉลี่ยต่อเกมสูงสุด?
3. **Tab 3 (Critical Acclaim vs Commercial Success):** คะแนนรีวิวจากนักวิจารณ์และผู้เล่นส่งผลต่อยอดขายจริงหรือไม่ และสามารถระบุเกมกลุ่ม Blockbuster หรือ Hidden Gemsได้อย่างไร?

---

## 2. Technical Stack & Interactivity Guidelines

* **Backend Engine:** Python (e.g., Python 3.10+, FastAPI / Flask / Dash / Streamlit Backend)
* **Visualization Engine:** Plotly / Plotly Dash (หรือ Streamlit + Plotly Chart Objects)
* **Interactivity & State Management (Mandatory):**
  * ทุกแผนภูมิ (Charts) ในแท็บเดียวกันต้องรองรับ **Cross-Filtering / Synchronized Interaction** (เมื่อผู้ใช้คลิกข้อมูลในกราฟหนึ่ง กราฟและตัวชี้วัดอื่นๆ ในแท็บเดียวกันจะต้องกรองและอัปเดตข้อมูลตามทันที)
  * ใช้ Event Handling เช่น Plotly `clickData` / `selectedData` เพื่อส่ง State ไปยัง Component อื่นๆ

---

## 3. Dashboard Structure & Functional Specifications

```
+------------------------------------------------------------------------------------+
|                    Global Video Game Sales Analytics Dashboard                     |
+------------------------------------------------------------------------------------+
| [ Tab 1: Executive Overview ] | [ Tab 2: Genre & Platform ] | [ Tab 3: Reviews vs Sales ] |
+------------------------------------------------------------------------------------+
```

---

### Tab 1: Executive Overview & Regional Market Share
**วัตถุประสงค์:** ตอบคำถามภาพรวมระดับผู้บริหารเกี่ยวกับมูลค่าตลาดเกมทั่วโลก แนวโน้มการเติบโต และพฤติกรรมการซื้อในแต่ละภูมิภาค (NA, EU, JP, Other)

#### 1. Key Performance Indicators (KPI Cards)
* **Global Total Sales ($):** ยอดขายรวมทั่วโลก (ล้านดอลลาร์)
* **Total Game Titles:** จำนวนเกมทั้งหมดในระบบ
* **Top-Selling Genre:** หมวดหมู่เกมที่ทำรายได้สูงสุด
* **Top Console/Platform:** แพลตฟอร์มที่ครองยอดขายสูงสุด

#### 2. Visuals & Charts Specification
1. **Line Chart (Yearly Sales Trend):**
   * *แกน X:* ปีที่วางจำหน่าย (Release Year)
   * *แกน Y:* ยอดขายรวมทั่วโลก ($ Global Sales)
   * *คำอธิบาย:* แสดงแนวโน้มการเติบโตย้อนหลังตามปีเพื่อดูยุคทองของวงการเกม
2. **Stacked Bar / Donut Chart (Regional Breakdown):**
   * *แกน/มิติ:* สัดส่วนยอดขายจำแนกตามภูมิภาคหลัก (North America: NA, Europe: EU, Japan: JP, Other Regions) ซ้อนทับตามหมวดหมู่เกม (Genre)
   * *คำอธิบาย:* วิเคราะห์ความชอบของแต่ละตลาด (เช่น JP ชอบ RPG vs NA ชอบ Shooter/Action)
3. **Horizontal Bar Chart (Top 10 Best-Selling Games):**
   * *แกน Y:* ชื่อเกม (Game Titles)
   * *แกน X:* ยอดขายรวม ($ Global Sales)
   * *รายละเอียด:* แถบสีแยกยอดขายตามภูมิภาค (NA, EU, JP, Other) ของ 10 อันดับเกมที่ขายดีที่สุดตลอดกาล

#### 3. Filters / Slicers (Tab 1)
* ช่วงปีที่วางจำหน่าย (Release Year Range Slider)
* ภูมิภาค (Region Selection)
* ตระกูลแพลตฟอร์มหลัก (Console Generation / Platform)

---

### Tab 2: Genre & Platform Dynamics
**วัตถุประสงค์:** วิเคราะห์ความสัมพันธ์ระหว่าง "เครื่องเกม (Platform)" "ประเภทเกม (Genre)" และ "ค่ายผู้พัฒนา (Publisher)" เพื่อหาโอกาสในการผลิตและจำหน่ายเกม

#### 1. Key Performance Indicators (KPI Cards)
* **Most Published Genre:** หมวดหมู่ที่มีจำนวนเกมวางขายมากที่สุด
* **Average Sales per Game:** ยอดขายเฉลี่ยต่อเกมจำแนกตามหมวดหมู่
* **Leading Publisher:** ค่ายเกมที่มีส่วนแบ่งการตลาดสูงสุด

#### 2. Visuals & Charts Specification
1. **Heatmap Matrix (Genre vs Platform Matrix):**
   * *แกน X:* แพลตฟอร์ม (Platform เช่น PS4, XOne, Switch, PC)
   * *แกน Y:* หมวดหมู่เกม (Genre)
   * *ค่าความร้อน (Color Intensity):* ยอดขายรวม ($ Global Sales)
   * *คำอธิบาย:* แสดงว่าแพลตฟอร์มใดเด่นในเกมประเภทใด
2. **Treemap Chart (Publisher Market Share):**
   * *โครงสร้าง:* สัดส่วนยอดขายรวมแยกตามค่ายเกมยักษ์ใหญ่ (เช่น Nintendo, EA, Ubisoft, Sony, Square Enix)
   * *คำอธิบาย:* เปรียบเทียบส่วนแบ่งการตลาดของผู้พัฒนาแต่ละราย
3. **Combo Chart (Total Sales vs Avg Sales by Genre):**
   * *แกน X:* หมวดหมู่เกม (Genre)
   * *แกน Y1 (Bar):* ยอดขายรวม ($ Total Sales)
   * *แกน Y2 (Line):* ยอดขายเฉลี่ยต่อเกม ($ Avg Sales per Game)
   * *คำอธิบาย:* แยกแยะระหว่างหมวดหมู่ที่มีเกมเยอะจนยอดขายรวมสูง (High Volume) กับหมวดหมู่ที่ผลิตน้อยแต่ฮิตทุกเกม (High Yield)

#### 3. Filters / Slicers (Tab 2)
* หมวดหมู่เกม (Genre Dropdown)
* ตระกูลแพลตฟอร์ม (PlayStation / Xbox / Nintendo / PC)
* ค่ายเกม (Publisher Multi-select)

---

### Tab 3: Critical Acclaim vs Commercial Success
**วัตถุประสงค์:** วิเคราะห์ความสัมพันธ์ระหว่าง "คะแนนจากนักวิจารณ์ (Critic Score)" และ "คะแนนจากผู้เล่น (User Score)" ต่อ "ยอดขายจริง" พร้อมระบุกลุ่มเกมประเภท Blockbuster, Overhyped และ Hidden Gems

#### 1. Key Performance Indicators (KPI Cards)
* **Avg Critic Score of Top 100 Games:** คะแนนวิจารณ์เฉลี่ยของเกมติด Top 100
* **Hit Games Ratio (%):** สัดส่วนเกมระดับ Hit (ยอดขายเกิน 1 ล้านชุด %)
* **Correlation Score:** ค่าความสัมพันธ์ระหว่างคะแนนรีวิวกับยอดขาย

#### 2. Visuals & Charts Specification
1. **Scatter Plot (Critic Score vs Global Sales):**
   * *แกน X:* คะแนนนักวิจารณ์ (Critic Score: 0-100)
   * *แกน Y:* ยอดขายรวม ($ Global Sales)
   * *ขนาด/สีวงกลม:* แทนชื่อเกม และแถบสีตามหมวดหมู่เกม (Genre)
   * *การแบ่งกลุ่ม (Quadrants):*
     * **Blockbusters:** คะแนนสูง + ยอดขายสูง
     * **Overhyped:** คะแนนต่ำ + ยอดขายสูง
     * **Hidden Gems:** คะแนนสูง + ยอดขายต่ำ
2. **Box Plot / Violin Plot (Rating Distribution by Publisher/Genre):**
   * *แกน X:* ค่ายเกม (Publisher) หรือ หมวดหมู่เกม (Genre)
   * *แกน Y:* การกระจายตัวของคะแนนรีวิว (Critic / User Score)
   * *คำอธิบาย:* ประเมินเสถียรภาพและมาตรฐานคุณภาพงานของแต่ละค่าย
3. **Comparison Table (Top Rated vs Top Selling Matrix):**
   * *รายละเอียด:* ตารางเปรียบเทียบ 20 อันดับเกมที่ได้คะแนนรีวิวสูงสุด เทียบกับ 20 อันดับเกมที่ขายดีที่สุด เพื่อประเมินความสอดคล้องระหว่างคำวิจารณ์กับยอดขายจริง

#### 3. Filters / Slicers (Tab 3)
* ช่วงคะแนนรีวิว (Review Score Range Slider: e.g., 90+, 80-89)
* เรตติ้งความเหมาะสม (ESRB Rating: E, T, M)
* ช่วงปีวางจำหน่าย (Release Year Range)

---

## 4. Summary User Flow

1. **Tab 1 (Executive Overview):** ผู้บริหารเริ่มต้นดูภาพรวมยอดขายการเติบโตระดับโลก และเข้าใจพฤติกรรมแยกตามภูมิภาค
2. **Tab 2 (Genre & Platform Dynamics):** ทีมกลยุทธ์เจาะลึกการเลือกประเภทเกม แพลตฟอร์มที่จะลง และคู่แข่งในตลาด
3. **Tab 3 (Critical Acclaim vs Commercial Success):** ทีมพัฒนาผลิตภัณฑ์ประเมินผลกระทบของรีวิวและคุณภาพเกมต่อยอดขายเชิงพาณิชย์

---

## 5. Data Schema & Requirements for Antigravity Team

### Primary Table Structure (`video_game_sales`)
* `game_id` (VARCHAR / INT): รหัสเกม
* `title` (VARCHAR): ชื่อเกม
* `platform` (VARCHAR): แพลตฟอร์ม (PS4, XOne, Switch, PC ฯลฯ)
* `release_year` (INT): ปีที่วางจำหน่าย
* `genre` (VARCHAR): หมวดหมู่เกม
* `publisher` (VARCHAR): ค่ายผู้พัฒนา/จัดจำหน่าย
* `na_sales` (FLOAT): ยอดขายในอเมริกาเหนือ (Millions)
* `eu_sales` (FLOAT): ยอดขายในยุโรป (Millions)
* `jp_sales` (FLOAT): ยอดขายในญี่ปุ่น (Millions)
* `other_sales` (FLOAT): ยอดขายในภูมิภาคอื่น (Millions)
* `global_sales` (FLOAT): ยอดขายรวมทั่วโลก (Millions)
* `critic_score` (FLOAT): คะแนนรีวิวจากนักวิจารณ์ (0-100)
* `user_score` (FLOAT): คะแนนรีวิวจากผู้เล่น (0-10)
* `esrb_rating` (VARCHAR): เรตติ้งความเหมาะสม (E, T, M, ฯลฯ)