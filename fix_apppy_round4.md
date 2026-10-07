# Business Requirements Document (BRD) - Version 3.1

## Project: Global Video Game Sales & Market Analytics Dashboard

## 1. Executive Summary & Core Objectives

### 1.1 Project Overview

โครงการพัฒนา Interactive Dashboard สำหรับวิเคราะห์ภาพรวมตลาดเกมทั่วโลก (Global Video Game Market) แนวโน้มการเติบโต พฤติกรรมการซื้อของผู้บริโภคในแต่ละภูมิภาค ความสัมพันธ์ระหว่างประเภทเกม แพลตฟอร์ม และค่ายผู้พัฒนา ตลอดจนการวิเคราะห์เปรียบเทียบมุมมองคะแนนระหว่างนักวิจารณ์และผู้เล่นจริง โดยเน้นการแสดงผลที่ชัดเจน มีหน่วยกำกับ (Units) คำอธิบายกราฟที่เข้าใจง่าย และอ่านค่าได้ทันที

### 1.2 Core Business Questions

* **Tab 1:** ตลาดเกมทั่วโลกมีมูลค่ารวมเท่าไร เติบโตอย่างไร และแต่ละภูมิภาคมีความชอบที่แตกต่างกันอย่างไร?

* **Tab 2:** ประเภทเกมใดทำรายได้สูงสุด ค่ายเกมใดครองตลาด และแพลตฟอร์มใดเหมาะกับเกมแนวไหน?

* **Tab 3:** คะแนนวิจารณ์ส่งผลต่อยอดขายจริงหรือไม่ และรสนิยมระหว่างนักวิจารณ์กับผู้เล่นในแต่ละหมวดหมู่เกมมีความเหมือนหรือต่างกันอย่างไร?

## 2. Technical Stack & Interactivity Guidelines

* **Backend Engine:** Python 3.10+ (FastAPI / Dash / Streamlit Backend)

* **Visualization Engine:** Plotly / Plotly Dash

* **Interactivity Requirements:**

  * ทุกแผนภูมิในแท็บเดียวกันต้องเชื่อมต่อกับ Global Filters ผ่าน Reactive Callbacks เมื่อผู้ใช้เปลี่ยนตัวกรอง ข้อมูลและกราฟทั้งหมดในแท็บนั้นต้อง Re-render ทันที

  * กราฟทุกตัวต้องมี **หน่วย (Units)** กำกับชัดเจนที่แกน X/Y และ Tooltip

  * กราฟทุกตัวต้องมี **คำอธิบายใต้หัวข้อ (Sub-header Description)** ระบุชัดเจนว่าเปรียบเทียบอะไรกับอะไร

## 3. Dashboard Structure & Detailed Specifications

```
+------------------------------------------------------------------------------------+
|                    Global Video Game Sales Analytics Dashboard                     |
+------------------------------------------------------------------------------------+
| [ Tab 1: Executive Overview ] | [ Tab 2: Genre & Platform ] | [ Tab 3: Reviews vs Sales ] |
+------------------------------------------------------------------------------------+
```

### Tab 1: Executive Overview & Regional Market Share

#### 1. Key Performance Indicators (KPI Cards)

* **Global Total Sales:** ยอดขายรวมทั่วโลก `[หน่วย: ล้านดอลลาร์สหรัฐ ($M USD)]`

* **Total Game Titles:** จำนวนเกมทั้งหมดในระบบ `[หน่วย: เกม (Titles)]`

* **Top-Selling Genre:** หมวดหมู่เกมที่ทำรายได้สูงสุด `[หน่วย: ชื่อหมวดหมู่ และ ยอดขาย $M USD]`

* **Top Console/Platform:** แพลตฟอร์มที่มียอดขายรวมสูงสุด `[หน่วย: ชื่อแพลตฟอร์ม และ ยอดขาย $M USD]`

#### 2. Visuals & Charts Specification

1. **Line Chart: Yearly Global Sales Trend**

   * **คำอธิบายใต้หัวข้อ:** *"แสดงการเปรียบเทียบระหว่าง `ปีที่วางจำหน่าย` กับ `ยอดขายรวมทั่วโลก ($M USD)` เพื่อดูแนวโน้มการเติบโตและยุคทองของอุตสาหกรรมเกม"*

   * **แกน X:** ปีที่วางจำหน่าย (Release Year) `[หน่วย: ปี ค.ศ.]`

   * **แกน Y:** ยอดขายรวม (\$ Global Sales) `[หน่วย: ล้านดอลลาร์สหรัฐ ($M USD)]`

2. **Stacked Bar / Donut Chart: Regional Sales Breakdown**

   * **คำอธิบายใต้หัวข้อ:** *"แสดงการเปรียบเทียบระหว่าง `ภูมิภาคหลัก (NA, EU, JP, Other)` ซ้อนทับตาม `หมวดหมู่เกม (Genre)` เพื่อดูสัดส่วนยอดขายและความนิยมของเกมแต่ละแนวในแต่ละท้องถิ่น"*

   * **แกน X / Segment:** ภูมิภาค (North America, Europe, Japan, Other) `[หน่วย: ล้านดอลลาร์สหรัฐ ($M USD) และ ร้อยละ (% Share)]`

   * **แกน Y / Color:** หมวดหมู่เกม (Genre)

   * **ข้อกำหนดสำคัญ:** กราฟนี้ **ต้องผูก Callback กับ Global Filters** ใน Tab 1 เพื่อให้อัปเดตตามการเลือกของผู้ใช้

3. **Horizontal Bar Chart: Top 10 Best-Selling Games**

   * **คำอธิบายใต้หัวข้อ:** *"แสดงการเปรียบเทียบระหว่าง `10 อันดับเกมที่ขายดีที่สุด` กับ `ยอดขายจำแนกตามภูมิภาค` เพื่อดูความนิยมของเกมระดับ Blockbuster"*

   * **แกน Y:** ชื่อเกม (Game Title Only) `[ข้อกำหนด: ต้อง Clean Data ตัดรหัส เช่น Game___ ออก ให้เหลือเฉพาะชื่อเกม]`

   * **แกน X:** ยอดขายรวม (\$ Global Sales) `[หน่วย: ล้านดอลลาร์สหรัฐ ($M USD)]`

#### 3. Global Filters (Tab 1)

* ช่วงปีที่วางจำหน่าย (Release Year Range Slider)

* เลือกภูมิภาค (Region Selection)

* ตระกูลแพลตฟอร์ม (Console/Platform Generation)

---

### Tab 2: Genre & Platform Dynamics

#### 1. Key Performance Indicators (KPI Cards)

* **Most Published Genre (Featured Hero KPI Card):**

  * **การออกแบบ:** กล่องขนาดใหญ่เด่นพิเศษ (Hero Layout - Span 2 Columns)

  * **ข้อมูล:** หมวดหมู่ที่มีจำนวนเกมถูกผลิตมากที่สุด `[หน่วย: ชื่อหมวดหมู่ และ จำนวนเกม (Titles)]`

  * **การทำงาน:** Static Overview ไม่ถูกกรองตามการคลิกกราฟอื่น

* **Leading Publisher:** ค่ายเกมที่ครองส่วนแบ่งตลาดสูงสุด `[หน่วย: ชื่อค่าย และ ยอดขาย $M USD]`

* **Global Market Volume:** ยอดขายรวมของหมวดหมู่ที่กรอง `[หน่วย: ล้านดอลลาร์สหรัฐ ($M USD)]`

#### 2. Visuals & Charts Specification

1. **Heatmap Matrix: Genre vs. Platform Sales**

   * **คำอธิบายใต้หัวข้อ:** *"แสดงการเปรียบเทียบระหว่าง `หมวดหมู่เกม (Genre)` กับ `แพลตฟอร์มเครื่องเล่น (Platform)` โดยใช้ระดับสีวัด `ยอดขายรวม` เพื่อหาจุดจับคู่ที่ทำรายได้สูงสุด"*

   * **แกน X:** แพลตฟอร์ม (Platform) | **แกน Y:** หมวดหมู่เกม (Genre)

   * **ค่าสี (Z-Axis):** ยอดขายรวม (\$ Global Sales) `[หน่วย: ล้านดอลลาร์สหรัฐ ($M USD)]`

2. **Treemap Chart: Publisher Market Share**

   * **คำอธิบายใต้หัวข้อ:** *"แสดงการเปรียบเทียบสัดส่วน `ส่วนแบ่งการตลาดของค่ายผู้พัฒนา (Publishers)` กับ `ยอดขายรวม` เพื่อดูค่ายเกมที่เป็นผู้นำในตลาด"*

   * **ขนาดพื้นที่:** ยอดขายรวม (\$ Global Sales) `[หน่วย: ล้านดอลลาร์สหรัฐ ($M USD) และ % ส่วนแบ่ง]`

3. **Single Bar Chart: Total Sales by Genre**

   * **คำอธิบายใต้หัวข้อ:** *"แสดงการเปรียบเทียบระหว่าง `หมวดหมู่เกม (Genre)` กับ `ยอดขายรวม ($M USD)` เรียงลำดับจากมากไปน้อย เพื่อดูมูลค่าตลาดของแต่ละประเภทเกม"*

   * **แกน X:** หมวดหมู่เกม (Genre)

   * **แกน Y:** ยอดขายรวม (\$ Global Sales) `[หน่วย: ล้านดอลลาร์สหรัฐ ($M USD)]`

---

### Tab 3: Critical Acclaim vs Commercial Success

#### 1. Global Filters (Tab 3) - Vertical UI & Notes

* **Review Score Range Filter (Vertical Slider):**

  * **UI Layout:** วางแนวตั้ง (Vertical Orientation) Side-panel

  * **หมายเหตุติดบน Filter:** *"หมายเหตุ: ตัวกรองนี้ใช้สำหรับเลือกช่วงคะแนนวิจารณ์ (Critic Score 0-100 Points) เพื่อวิเคราะห์เฉพาะกลุ่มเกมที่มีระดับคุณภาพตามกำหนด"*

* **Release Year Range Filter (Vertical Slider):**

  * **UI Layout:** วางแนวตั้ง (Vertical Orientation) Side-panel

  * **หมายเหตุติดบน Filter:** *"หมายเหตุ: ตัวกรองนี้ใช้สำหรับเลือกช่วงปี ค.ศ. ที่วางจำหน่าย เพื่อวิเคราะห์แนวโน้มคะแนนและยอดขายตามช่วงเวลา"*

#### 2. Visuals & Charts Specification

1. **Bar Chart: Average Sales by Review Score Tiers**

   * **คำอธิบายใต้หัวข้อ:** *"แสดงการเปรียบเทียบระหว่าง `กลุ่มช่วงคะแนนรีวิว (Score Tiers)` กับ `ยอดขายเฉลี่ยต่อเกม ($M USD/Game)` เพื่อประเมินว่าเกมคะแนนสูงขายได้ดีกว่าจริงหรือไม่"*

   * **แกน X:** ช่วงคะแนน (`90-100`, `80-89`, `70-79`, `<70`) `[หน่วย: ช่วงคะแนน (Points)]`

   * **แกน Y:** ยอดขายเฉลี่ยต่อเกม (Avg Sales per Title) `[หน่วย: ล้านดอลลาร์สหรัฐต่อเกม ($M USD/Game)]`

2. **Side-by-Side Bar Charts: Top 10 Best Rated vs Top 10 Best Selling**

   * **กราฟซ้าย - Top 10 Best Rated Games:**

     * **คำอธิบายใต้หัวข้อ:** *"แสดง `10 อันดับเกมที่ได้คะแนนนักวิจารณ์สูงสุด` เทียบกับ `คะแนนรีวิว`"*

     * **แกน Y:** ชื่อเกม (Clean Title) | **แกน X:** คะแนนวิจารณ์เฉลี่ย `[หน่วย: คะแนน (Points 0-100)]`

     * **Data Fix:** ล็อคสเกลแกน X ไว้ที่ `range_x=[0, 100]` เสมอ และใช้การคำนวณแบบ `mean()` เพื่อป้องกันปัญหาสเกลทะลุ 100

   * **กราฟขวา - Top 10 Best Selling Games:**

     * **คำอธิบายใต้หัวข้อ:** *"แสดง `10 อันดับเกมที่มียอดขายสูงสุด` เทียบกับ `ยอดขายรวมทุกแพลตฟอร์ม`"*

     * **แกน Y:** ชื่อเกม (Clean Title) | **แกน X:** ยอดขายรวม `[หน่วย: ล้านดอลลาร์สหรัฐ ($M USD)]`

     * **Data Fix:** สั่ง Group Data บรรทัดเดียวตามชื่อเกม `groupby('title')` เพื่อป้องกันการเกิด Stacked Segment บนอันดับ 1

3. **Updated Line Chart: Critic vs. User Score Comparison Chart (Dual-Line Chart)**

   * **การปรับเปลี่ยน:** เปลี่ยนจาก Diverging Bar มาเป็น **Multi-Line Chart** สองเส้นเปรียบเทียบ เพื่อให้อ่านและเปรียบเทียบเทรนด์ง่ายยิ่งขึ้น

   * **ชื่อกราฟ:** Critic vs. User Score Comparison Chart by Genre

   * **คำอธิบายใต้หัวข้อ:** *"แสดงการเปรียบเทียบระหว่าง `คะแนนเฉลี่ยจากนักวิจารณ์ (Critic Score)` และ `คะแนนเฉลี่ยจากผู้เล่น (User Score)` ในแต่ละหมวดหมู่เกม (Genre) เพื่อดูความสอดคล้องของรสนิยม"*

   * **แกน X:** หมวดหมู่เกม (Genre - Action, Misc, Shooter, Simulation, Platform, Racing, Role-Playing, Sports, ฯลฯ)

   * **แกน Y:** คะแนนเฉลี่ย (Average Score) `[หน่วย: คะแนน (Points 0-100 scale)]` `[ล็อคช่วงแกน Y: 0 ถึง 100]`

   * **เส้นกราฟและโทนสี (Color Legend):**

     * 🔴 **เส้นสีแดง (Red Line with Markers):** `User Score` (คะแนนจากผู้เล่น)

     * 🔵 **เส้นสีน้ำเงิน (Blue Line with Markers):** `Critic Score` (คะแนนจากนักวิจารณ์)

   * **ความง่ายในการใช้งาน:** ผู้ใช้สามารถมองเห็นจุดตัด (Intersections) และระยะห่างของเส้นกราฟทั้งสองสีในแต่ละ Genre ได้อย่างชัดเจนทันที

## 4. Developer Action Items Summary for Antigravity

1. **Tab 3 Critic vs User Redesign (Line Chart):**
   * แปลงข้อมูล `User Score` ให้อยู่ในสเกลเดียวกัน (หาก raw data เป็น 0-10 ให้คูณ 10 เพื่อให้เป็น 0-100 เท่ากับ `Critic Score`)
   * พล็อตกราฟเส้นคู่ (`px.line` หรือ `go.Scatter` mode='lines+markers')
   * ตั้งค่าสีเส้นให้ตรงสเปก: `User Score` = สีแดง (`#FF0000` / `red`), `Critic Score` = สีน้ำเงิน (`#0000FF` / `blue`)
   * กำหนดแกน Y ล็อคช่วงที่ `[0, 100]`

2. **Units & Sub-headers:** ตรวจสอบว่า KPI, Label แกน X/Y และ Sub-titles ระบุหน่วยและคำอธิบายครบถ้วนตาม BRD

3. **Tab 1 Stacked Bar Callbacks:** เชื่อมต่อ Reactive Callbacks ของ Stacked Bar เข้ากับ Filter ช่วงปี, ภูมิภาค และแพลตฟอร์ม

4. **Tab 3 Vertical Filters:** กำหนด Orientation ของ Review Score Slider และ Release Year Slider ให้เป็น `vertical` พร้อมแสดง Note ติดบน UI