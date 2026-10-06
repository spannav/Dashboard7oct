# Business Requirements Document (BRD) - Revised

## Project: Global Video Game Sales & Market Analytics Dashboard

## 1. Project Overview & Objectives

### 1.1 Executive Summary
โครงการพัฒนา Interactive Dashboard สำหรับวิเคราะห์ภาพรวมตลาดเกมทั่วโลก (Global Video Game Market) แนวโน้มการเติบโต พฤติกรรมการซื้อของผู้บริโภคในแต่ละภูมิภาค ความสัมพันธ์ระหว่างประเภทเกม แพลตฟอร์ม และค่ายผู้พัฒนา ตลอดจนการวิเคราะห์ความสัมพันธ์ระหว่างคะแนนรีวิวกับยอดขายในรูปแบบที่เข้าใจง่าย

### 1.2 Core Business Questions

1. **Tab 1 (Executive Overview):** ตลาดเกมทั่วโลกมีมูลค่าเท่าไร แนวโน้มการเติบโตเป็นอย่างไร และพฤติกรรมการซื้อเกมในแต่ละภูมิภาคแตกต่างกันอย่างไร?
2. **Tab 2 (Genre & Platform Dynamics):** แพลตฟอร์มใดเหมาะกับเกมแนวไหน ค่ายผู้พัฒนาใดครองส่วนแบ่งตลาด ยอดขายรวมและยอดขายเฉลี่ยในแต่ละหมวดหมู่เป็นอย่างไร?
3. **Tab 3 (Critical Acclaim vs Commercial Success):** คะแนนรีวิวจากนักวิจารณ์และผู้เล่นสัมพันธ์กับยอดขายจริงอย่างไรในรูปแบบที่ดูง่ายและชัดเจน?

## 2. Technical Stack & Interactivity Guidelines

* **Backend Engine:** Python (e.g., Python 3.10+, FastAPI / Flask / Dash / Streamlit Backend)
* **Visualization Engine:** Plotly / Plotly Dash (หรือ Streamlit + Plotly Chart Objects)
* **Interactivity & State Management:**
  * ทุกแผนภูมิ (Charts) ในแท็บเดียวกันต้องรองรับ **Cross-Filtering / Synchronized Interaction** (ยกเว้น KPI การ์ดบางตัวที่ระบุเป็น Static)
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

### Tab 1: Executive Overview & Regional Market Share

**วัตถุประสงค์:** ตอบคำถามภาพรวมระดับผู้บริหารเกี่ยวกับมูลค่าตลาดเกมทั่วโลก แนวโน้มการเติบโต และพฤติกรรมการซื้อในแต่ละภูมิภาค (NA, EU, JP, Other)

#### 1. Key Performance Indicators (KPI Cards)
* **Global Total Sales (\$):** ยอดขายรวมทั่วโลก (ล้านดอลลาร์)
* **Total Game Titles:** จำนวนเกมทั้งหมดในระบบ
* **Top-Selling Genre:** หมวดหมู่เกมที่ทำรายได้สูงสุด
* **Top Console/Platform:** แพลตฟอร์มที่ครองยอดขายสูงสุด

#### 2. Visuals & Charts Specification
1. **Line Chart (Yearly Sales Trend):**
   * *แกน X:* ปีที่วางจำหน่าย (Release Year)
   * *แกน Y:* ยอดขายรวมทั่วโลก (\$ Global Sales)
   * *รายละเอียด:* แสดงแนวโน้มการเติบโตย้อนหลังตามปีเพื่อดูยุคทองของวงการเกม

2. **Stacked Bar / Donut Chart (Regional Breakdown):**
   * *แกน/มิติ:* สัดส่วนยอดขายจำแนกตามภูมิภาคหลัก (NA, EU, JP, Other) ซ้อนทับตามหมวดหมู่เกม (Genre)
   * *รายละเอียด:* วิเคราะห์ความชอบของแต่ละตลาด (เช่น JP ชอบ RPG vs NA ชอบ Shooter/Action)

3. **Horizontal Bar Chart (Top 10 Best-Selling Games):**
   * *แกน Y:* **ชื่อเกม (Clean Game Title Only)** 
     * **[ข้อกำหนดสำคัญ]:** ต้อง Clean Data โดยนำ Prefix/ID เช่น `Game___` หรือรหัสเกมออกทั้งหมด ให้แสดงผลเฉพาะชื่อเกมเพียวๆ เท่านั้น (เช่น "Wii Sports", "Grand Theft Auto V")
   * *แกน X:* ยอดขายรวม (\$ Global Sales)
   * *รายละเอียด:* แถบสีแยกยอดขายตามภูมิภาค (NA, EU, JP, Other) ของ 10 อันดับเกมที่ขายดีที่สุด

#### 3. Filters / Slicers (Tab 1)
* ช่วงปีที่วางจำหน่าย (Release Year Range Slider)
* ภูมิภาค (Region Selection)
* ตระกูลแพลตฟอร์มหลัก (Console Generation / Platform)

---

### Tab 2: Genre & Platform Dynamics

**วัตถุประสงค์:** วิเคราะห์ความสัมพันธ์ระหว่าง "เครื่องเกม (Platform)" "ประเภทเกม (Genre)" และ "ค่ายผู้พัฒนา (Publisher)"

#### 1. Key Performance Indicators (KPI Cards)
* **Most Published Genre (Static KPI Card):** 
  * **[ข้อกำหนดสำคัญ]:** แสดงหมวดหมู่เกมที่มีจำนวนเกมวางขายมากที่สุดแบบคงที่ (Show overall top published genre only) **ไม่ต้องเชื่อมต่อ Interactivity หรือ Callback กับกราฟอื่น**
* **Leading Publisher:** ค่ายเกมที่มีส่วนแบ่งการตลาดสูงสุด
* **Global Market Volume:** ปริมาณยอดขายรวมในหมวดหมู่ที่เลือก

#### 2. Visuals & Charts Specification
1. **Heatmap Matrix (Genre vs Platform Matrix):**
   * *แกน X:* แพลตฟอร์ม (Platform เช่น PS4, XOne, Switch, PC)
   * *แกน Y:* หมวดหมู่เกม (Genre)
   * *ค่าความร้อน (Color Intensity):* ยอดขายรวม (\$ Global Sales)

2. **Treemap Chart (Publisher Market Share):**
   * *โครงสร้าง:* สัดส่วนยอดขายรวมแยกตามค่ายเกมยักษ์ใหญ่ (เช่น Nintendo, EA, Ubisoft, Sony)

3. **Bar Chart 1: Total Sales by Genre (ยอดขายรวมตามหมวดหมู่):**
   * *แกน X:* หมวดหมู่เกม (Genre)
   * *แกน Y:* ยอดขายรวม (\$ Total Sales)
   * *รายละเอียด:* กราฟแท่งเดี่ยว เรียงลำดับจากยอดขายรวมสูงสุดไปต่ำสุด เพื่อความชัดเจนและอ่านง่าย

4. **Bar Chart 2: Average Sales per Game by Genre (ยอดขายเฉลี่ยต่อเกมตามหมวดหมู่):**
   * *แกน X:* หมวดหมู่เกม (Genre)
   * *แกน Y:* ยอดขายเฉลี่ย (\$ Average Sales per Title)
   * *รายละเอียด:* กราฟแท่งเดี่ยวแยกเฉพาะ แสดงประสิทธิภาพรายเกมว่าหมวดหมู่ไหนมี Yield สูงสุด

#### 3. Filters / Slicers (Tab 2)
* หมวดหมู่เกม (Genre Dropdown)
* ตระกูลแพลตฟอร์ม (PlayStation / Xbox / Nintendo / PC)
* ค่ายเกม (Publisher Multi-select)

---

### Tab 3: Critical Acclaim vs Commercial Success (Revised Easy-to-Read Edition)

**วัตถุประสงค์:** ปรับรูปแบบกราฟทั้งหมดให้เน้นความ **"อ่านง่าย-เข้าใจทันที"** เพื่อดูว่าคะแนนรีวิวส่งผลต่อยอดขายจริงมากน้อยเพียงใด

#### 1. Key Performance Indicators (KPI Cards)
* **Avg Critic Score:** คะแนนวิจารณ์เฉลี่ยรวม
* **Avg User Score:** คะแนนผู้เล่นเฉลี่ยรวม
* **Hit Games Count:** จำนวนเกมระดับ Hit (ยอดขายเกิน 1 ล้านชุด)

#### 2. Visuals & Charts Specification (New Simplified Layout)
1. **Bar Chart: Average Sales by Review Score Tiers (ยอดขายเฉลี่ยตามช่วงคะแนนรีวิว):**
   * *แกน X:* ช่วงคะแนนนักวิจารณ์ (Score Bins: `90-100 (Masterpiece)`, `80-89 (Great)`, `70-79 (Good)`, `Under 70 (Average/Poor)`)
   * *แกน Y:* ยอดขายเฉลี่ยต่อเกม (\$ Average Sales)
   * *ประโยชน์:* อ่านง่ายที่สุดเพื่อพิสูจน์ทันทีว่า "ยิ่งคะแนนสูง ยอดขายเฉลี่ยยิ่งสูงจริงหรือไม่"

2. **Side-by-Side Bar Charts: Top 10 Best Rated vs Top 10 Best Selling (เปรียบเทียบเกมคะแนนสูงสุด vs ขายดีที่สุด):**
   * *กราฟฝั่งซ้าย:* 10 อันดับเกมที่ได้คะแนน Critic Score สูงสุด
   * *กราฟฝั่งขวา:* 10 อันดับเกมที่มียอดขาย Global Sales สูงสุด
   * *ประโยชน์:* เปรียบเทียบได้อย่างชัดเจนโดยไม่ต้องดู Scatter plot ที่ซับซ้อน

3. **Grouped Bar Chart: Critic Score vs User Score by Genre (เปรียบเทียบคะแนนวิจารณ์ vs คะแนนผู้เล่น แยกตามหมวดหมู่):**
   * *แกน X:* หมวดหมู่เกม (Genre)
   * *แกน Y:* คะแนนเต็ม 100 (ทำการ Scale User Score จาก 10 เป็น 100 ให้เท่ากัน)
   * *รายละเอียด:* กราฟแท่งคู่เปรียบเทียบระหว่างคะแนน Critic และ User เพื่อดูว่าแนวเกมไหนที่มุมมองนักวิจารณ์กับผู้เล่นตรงกันหรือขัดแย้งกัน

#### 3. Filters / Slicers (Tab 3)
* ช่วงคะแนนรีวิว (Review Score Range Slider)
* หมวดหมู่เกม (Genre Dropdown)
* ช่วงปีวางจำหน่าย (Release Year Range)

---

## 4. Data Schema & Requirements for Antigravity Team

### Primary Table Structure (`video_game_sales`)

* `game_id` (VARCHAR / INT): รหัสเกม
* `title` (VARCHAR): ชื่อเกม *(ต้องดึงเฉพาะ Text ชื่อเกมเมื่อแสดงผลใน Tab 1)*
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