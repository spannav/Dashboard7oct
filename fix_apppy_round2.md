# Business Requirements Document (BRD) - Updated & Fixed

## Project: Global Video Game Sales & Market Analytics Dashboard

## 1. Project Overview & Objectives

### 1.1 Executive Summary

โครงการพัฒนา Interactive Dashboard สำหรับวิเคราะห์ภาพรวมตลาดเกมทั่วโลก (Global Video Game Market) แนวโน้มการเติบโต พฤติกรรมการซื้อของผู้บริโภคในแต่ละภูมิภาค ความสัมพันธ์ระหว่างประเภทเกม แพลตฟอร์ม และค่ายผู้พัฒนา ตลอดจนการวิเคราะห์ความสัมพันธ์ระหว่างคะแนนรีวิวกับยอดขายในรูปแบบที่เข้าใจง่ายและถูกต้องตามหลักสถิติ

### 1.2 Core Business Questions

1. **Tab 1 (Executive Overview):** ตลาดเกมทั่วโลกมีมูลค่าเท่าไร แนวโน้มการเติบโตเป็นอย่างไร และพฤติกรรมการซื้อเกมในแต่ละภูมิภาคแตกต่างกันอย่างไร?

2. **Tab 2 (Genre & Platform Dynamics):** แพลตฟอร์มใดเหมาะกับเกมแนวไหน ค่ายผู้พัฒนาใดครองส่วนแบ่งตลาด และยอดขายรวมในแต่ละหมวดหมู่เป็นอย่างไร?

3. **Tab 3 (Critical Acclaim vs Commercial Success):** คะแนนรีวิวจากนักวิจารณ์และผู้เล่นสัมพันธ์กับยอดขายจริงอย่างไร โดยไม่มีข้อผิดพลาดในการแสดงผลคะแนนและยอดขายซ้อนทับ?

## 2. Technical Stack & Interactivity Guidelines

* **Backend Engine:** Python (e.g., Python 3.10+, FastAPI / Flask / Dash / Streamlit Backend)

* **Visualization Engine:** Plotly / Plotly Dash (หรือ Streamlit + Plotly Chart Objects)

* **Interactivity & State Management:**

  * ทุกแผนภูมิ (Charts) ในแท็บเดียวกันต้องรองรับ **Dynamic Reactive Callbacks** เมื่อมีการเลือก Filter ใดๆ ข้อมูลใน Dataframe จะต้องถูกกรองใหม่ และ Re-render กราฟทั้งหมดในแท็บทันที

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

   * *แกน X:* ปีที่วางจำหน่าย (Release Year) | *แกน Y:* ยอดขายรวมทั่วโลก (\$ Global Sales)

2. **Stacked Bar / Donut Chart (Regional Breakdown - Vertical/Horizontal Stacked Bar):**

   * *รายละเอียด:* แสดงสัดส่วนยอดขายจำแนกตามภูมิภาคหลัก (NA, EU, JP, Other) ซ้อนทับตามหมวดหมู่เกม (Genre)

   * **\[ข้อกำหนดการแก้ไขสำคัญ\]:** กราฟ Stacked Bar ทั้งแนวตั้งและแนวนอน **ต้องเชื่อมต่อ Callback กับ Global Filters** (Release Year, Region, Console) ทุกครั้งที่มีการปรับ Filter กราฟ Stacked Bar นี้ต้องอัปเดตกรองข้อมูลตามทันที (แก้ปัญหาเดิมที่เลือก Filter แล้วกราฟไม่เปลี่ยน)

3. **Horizontal Bar Chart (Top 10 Best-Selling Games):**

   * *แกน Y:* **ชื่อเกม (Clean Game Title Only)** - ต้อง Clean Data นำ Prefix/ID เช่น `Game___` ออกทั้งหมด ให้แสดงผลเฉพาะชื่อเกมเพียวๆ

   * *แกน X:* ยอดขายรวม (\$ Global Sales)

   * *รายละเอียด:* แถบสีแยกยอดขายตามภูมิภาคของ 10 อันดับเกมที่ขายดีที่สุด และต้องตอบสนองต่อ Filter ใน Tab 1 เช่นกัน

#### 3. Filters / Slicers (Tab 1)

* ช่วงปีที่วางจำหน่าย (Release Year Range Slider)

* ภูมิภาค (Region Selection)

* ตระกูลแพลตฟอร์มหลัก (Console Generation / Platform)

---

### Tab 2: Genre & Platform Dynamics

**วัตถุประสงค์:** วิเคราะห์ความสัมพันธ์ระหว่าง "เครื่องเกม (Platform)" "ประเภทเกม (Genre)" และ "ค่ายผู้พัฒนา (Publisher)"

#### 1. Key Performance Indicators (KPI Cards) - UI Redesign

* **Most Published Genre (Featured Hero KPI Card):**

  * **\[ข้อกำหนดดีไซน์ใหม่\]:** ปรับขนาดกล่องให้อยู่ในรูปแบบ **Featured/Hero Card** โดยมีขนาดใหญ่กว่า (เช่น Span 2 Columns หรือ Font Size ใหญ่ขึ้น 1.5x) และเน้นสีพื้นหลัง/ขอบให้โดดเด่นกว่ากล่อง `Leading Publisher` และ `Global Market Volume` ชัดเจน

  * *ลักษณะการทำงาน:* ค่า Static แสดงหมวดหมู่ที่มีจำนวนเกมวางขายมากที่สุดในภาพรวม

* **Leading Publisher (Standard KPI Card):** ค่ายเกมที่มีส่วนแบ่งการตลาดสูงสุด (ขนาดปกติ)

* **Global Market Volume (Standard KPI Card):** ปริมาณยอดขายรวมในหมวดหมู่ที่เลือก (ขนาดปกติ)

#### 2. Visuals & Charts Specification

1. **Heatmap Matrix (Genre vs Platform Matrix):**

   * *แกน X:* แพลตฟอร์ม | *แกน Y:* หมวดหมู่เกม | *ค่าความร้อน:* ยอดขายรวม (\$ Global Sales)

2. **Treemap Chart (Publisher Market Share):**

   * *โครงสร้าง:* สัดส่วนยอดขายรวมแยกตามค่ายเกมยักษ์ใหญ่

3. **Bar Chart: Total Sales by Genre (ยอดขายรวมตามหมวดหมู่ - Single Chart):**

   * **\[ข้อกำหนดสำคัญ\]:** **ตัดกราฟยอดขายเฉลี่ยออก** ให้เหลือเฉพาะกราฟแท่งยอดขายรวม (`Total Global Sales`) กราฟเดียวเท่านั้น

   * *แกน X:* หมวดหมู่เกม (Genre) | *แกน Y:* ยอดขายรวม (\$ Total Sales) เรียงลำดับจากสูงไปต่ำเพื่อความสบายตาและอ่านง่าย

#### 3. Filters / Slicers (Tab 2)

* หมวดหมู่เกม (Genre Dropdown) / ตระกูลแพลตฟอร์ม / ค่ายเกม (Publisher Multi-select)

---

### Tab 3: Critical Acclaim vs Commercial Success (Bug Fixes & UX Enhancements)

**วัตถุประสงค์:** แสดงความสัมพันธ์ระหว่างคะแนนรีวิวกับยอดขายด้วยรูปแบบที่อ่านง่ายและถูกต้องตามหลักข้อมูล

#### 1. Filters / Slicers (Tab 3) - UX Enhancements

* **Review Score Range Filter (Vertical Slider with Descriptive Note):**

  * **\[ข้อกำหนด UI ใหม่ 1\]:** ปรับทิศทางการแสดงผลของ Filter Range Slider ให้เป็น **แนวตั้ง (Vertical Orientation)** เพื่อประหยัดพื้นที่แนวนอน

  * **\[ข้อกำหนด UI ใหม่ 2\]:** เพิ่มหมายเหตุ/คำอธิบายชัดเจนไว้ที่ตัว Filter ว่า:  
    `"หมายเหตุ: Filter นี้ใช้สำหรับเลือกช่วงคะแนนรีวิว (Critic Score Range 0-100) เพื่อกรองและวิเคราะห์เฉพาะกลุ่มเกมที่มีระดับคุณภาพตามช่วงคะแนนที่กำหนด"`

#### 2. Visuals & Charts Specification & Bug Fixes

1. **Bar Chart: Average Sales by Review Score Tiers (ยอดขายเฉลี่ยตามช่วงคะแนน):**

   * *แกน X:* ช่วงคะแนนนักวิจารณ์ (Bins: `90-100`, `80-89`, `70-79`, `<70`) | *แกน Y:* ยอดขายเฉลี่ยต่อเกม (\$ Average Sales)

2. **Side-by-Side Bar Charts: Top 10 Best Rated vs Top 10 Best Selling (พร้อมการแก้ไขบั๊ก):**

   * **กราฟที่ 1: Top 10 Best Rated (10 อันดับเกมคะแนนสูงสุด):**

     * **\[การแก้ไขบั๊ก 1 - แกน X ทะลุเกิน 100\]:**  
       * *สาเหตุของบั๊ก:* เกิดจากการนำคะแนน (`critic_score`) ของเกมเดียวกันที่ลงหลายแพลตฟอร์มมาบวกซ้ำกัน (`sum()`) ทำให้คะแนนรวมทะลุเป็น 150-200  
       * *วิธีแก้ไขสำหรับ Developer:* ต้องใช้ค่าเฉลี่ย `mean()` หรือ `max()` ของคะแนนเกมนั้นๆ และสั่งตั้งค่าสเกลแกน X ของ Plotly ให้ล็อคขอบเขตไว้ที่ **`range_x=[0, 100]`** เสมอ

     * **\[การแก้ไขบั๊ก 2 - แถบสแต็กซ้อนกันในอันดับแรก (Stacked Bar Artifact)\]:**  
       * *สาเหตุของบั๊ก:* เกมอันดับ 1 (เช่น GTA V หรือ Wii Sports) มีข้อมูลแยกหลายบรรทัดตามแพลตฟอร์ม Plotly จึงนำยอดขายแต่ละแพลตฟอร์มมาสแต็กซ้อนกันในแท่งเดียว  
       * *วิธีแก้ไขสำหรับ Developer:* ให้ทำการ Group Data ใน Pandas ก่อนพล็อตด้วย `df.groupby('title')` เพื่อรวมยอดขายของทุกแพลตฟอร์มให้กลายเป็น 1 Single Value ต่อ 1 Title ก่อนส่งเข้า Plotly Bar Chart หรือตั้งค่า `barmode='group'` เพื่อป้องกันการเกิด Stacked Segment

   * **กราฟที่ 2: Top 10 Best Selling (10 อันดับเกมยอดขายสูงสุด):**

     * ประยุกต์ใช้การ Group Data แบบเดียวกันเพื่อป้องกันไม่ให้เกิดแถบ Stack ซ้อนกันในรายชื่ออันดับ 1

3. **Grouped Bar Chart: Critic Score vs User Score by Genre:**

   * *แกน X:* หมวดหมู่เกม (Genre) | *แกน Y:* คะแนนเปรียบเทียบ (Scale 0-100) เปรียบเทียบระหว่าง Critic Score และ User Score

## 4. Summary of Developer Action Items for Antigravity

1. **Tab 1 Callbacks:** Bind filter events to updated figures for all horizontal and vertical Stacked Bar charts.
2. **Tab 2 Hero KPI & Cleanup:** Apply CSS/Styling to make `Most Published Genre` KPI prominent (larger card). Remove the Average Sales Bar Chart.
3. **Tab 3 UI & Math Fixes:**
   * Set Review Score Slider orientation to vertical with descriptive helper text.
   * Hard-cap Critic Score X-Axis limit to 100 (`range_x=[0, 100]`) and fix score aggregation logic (use `mean` instead of `sum`).
   * Perform Pandas `groupby('title')` aggregation prior to plotting Top 10 charts to fix the multi-platform stacking artifact on Rank #1.