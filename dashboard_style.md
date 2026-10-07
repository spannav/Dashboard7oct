# Business Requirements Document (BRD)

## ระบบ Global Video Game Sales Analytics Dashboard (v7.0)

**วันที่ปรับปรุงล่าสุด:** 7 ตุลาคม 2026  
**ผู้จัดทำ:** Strategy & Business Intelligence Team  
**ผู้รับมอบหมายพัฒนา (Developer):** Antigravity Team  

---

## 1. วัตถุประสงค์โครงการ (Project Purpose)
เอกสารนี้จัดทำขึ้นเพื่อระบุข้อกำหนดในการพัฒนา **Global Video Game Sales Analytics Dashboard** สำหรับใช้งานโดยทีมบริหารและนักวางแผนกลยุทธ์ค่ายเกม (Publisher & Strategy Analyst) โดยมีจุดประสงค์หลักดังนี้:
1. วิเคราะห์ภาพรวมตลาดเกมทั่วโลก แนวโน้มการเติบโต และพฤติกรรมการบริโภคตามภูมิภาค
2. เจาะลึกความสัมพันธ์ระหว่างหมวดหมู่เกม (Genre), แพลตฟอร์ม (Platform) และค่ายเกม (Publisher)
3. ประเมินความพึงพอใจของนักวิจารณ์ (Critic Score) เทียบกับผู้เล่นจริง (User Score) พร้อมวิเคราะห์กลยุทธ์เรตติ้งความเหมาะสมเนื้อหา (ESRB Rating) ต่อผลตอบแทนด้านยอดขายทั่วโลก
4. **มุ่งเน้นประสบการณ์ผู้ใช้ (UX/UI):** นำสไตล์ดีไซน์ Modern Dashboard (Soft Minimalist & Dark Slate Sidebar) มาปรับใช้เพื่อความสวยงาม อ่านง่าย และเป็นมืออาชีพระดับ Executive

---

## 2. ข้อกำหนดด้านสไตล์และการออกแบบ UI/UX (Design System & Aesthetics Specification)

ทีม Antigravity ต้องปรับแต่งสไตล์อินเทอร์เฟซ (UI/UX) ของ Dashboard ทั้งหมดให้อิงตามแนวทาง **Modern Soft Minimal Dashboard Visual Style** ดังนี้:

### 2.1 โทนสีและจานสี (Color Palette)
* **Sidebar Layout (แถบเมนูด้านซ้าย):**
  * Background Color: Dark Slate Blue / Dark Charcoal (`#343A40` / `#2B303A`)
  * Text & Icon Color: Soft Off-White (`#E2E8F0`) และ Muted Gray (`#94A3B8`)
  * Active Menu State: Highlight ด้วยพื้นหลังโทนสว่างเบาๆ หรือ Pill Badge
* **Main Canvas (พื้นที่แสดงผลหลัก):**
  * Background Color: Soft Light Gray (`#F4F5F7` / `#F8FAFC`)
* **Card Containers (กล่องกราฟและกล่อง KPI):**
  * Card Background: Pure White (`#FFFFFF`)
  * Corner Radius: **Extra Large Rounded (`border-radius: 20px - 24px`)**
  * Elevation / Shadow: Soft Drop Shadow (`box-shadow: 0 10px 25px -5px rgba(0,0,0,0.04)`)
* **Theme & Chart Colors Accent (สีประจำกราฟและตัวชี้วัด):**
  * **Sage Green (เขียวพาสเทลสดใส):** `#6EB897` หรือ `#7BA88B` (ใช้กับ KPI Hero / Accent 1)
  * **Royal Indigo / Purple (น้ำเงินม่วงเข้ม):** `#4A4EA4` หรือ `#5352ED` (ใช้กับ KPI / เส้น Critic Score)
  * **Coral / Red (แดงส้มสดใส):** `#FF6B6B` หรือ `#EE5253` (ใช้กับ Alert Badge / เส้น User Score)
  * **Soft Amber / Gold (เหลืองอุ่น):** `#FECB2E` หรือ `#FF9F43` (ใช้กับ Highlight Point)

### 2.2 โครงสร้างหน้าจอและเลย์เอาต์ (Layout Structure)
1. **Left Sidebar Navigation (แถบควบคุมฝั่งซ้าย):**
   * แสดง Logo / แบรนด์ด้านบนสุด
   * แสดง User Profile Card เล็กๆ (ชื่อนักวิเคราะห์/ผู้ใช้งาน)
   * เมนูการสลับแท็บ (Tab 1, Tab 2, Tab 3) พร้อมไอคอนแบบ Clean Vector
   * **Reset Filters Button** ดีไซน์เป็นกล่องการ์ดหรือปุ่มสไตล์ Pill Button ที่ด้านล่างซ้าย
2. **Top Header Bar (ส่วนหัวของพื้นที่หลัก):**
   * แสดงชื่อ Tab Header (เช่น Overview, Genre Dynamics, ESRB Strategy)
   * แสดง Pill Badges สรุปสถานะข้อมูล (เช่น `16.8k Titles Analyzed`)
   * ช่อง Search Bar ทรงโค้งมน (Pill Shape Search input)
3. **KPI Card Visual Style:**
   * **Hero Cards:** ทำมุมโค้งมนขนาดใหญ่ ใช้สีพื้นหลังเดี่ยวแบบดึงดูดสายตา (เช่น กล่องสีเขียว Sage หรือสีม่วง Indigo พร้อมตัวเลขสีขาวเด่น) ตามตัวอย่างดีไซน์อ้างอิง

---

## 3. ข้อกำหนดทางเทคนิคหลัก (Core Technical Requirements)

* **Backend Framework:** Python (FastAPI / Dash / Streamlit)
* **Data Visualization Library:** Plotly / Plotly Express (กำหนด Custom Plotly Template สีและ Font ให้ตรงกับ Theme)
* **Interactivity & Cross-filtering:**
  * กราฟทุกรูปภายในแท็บเดียวกันต้องเชื่อมต่อกันผ่าน Callbacks (เมื่อคลิกเลือก Filter หรือ Element บนกราฟ กราฟอื่นในแท็บเดียวกันต้องกรองข้อมูลและอัปเดตตามทันที)
  * ยกเว้น KPI Card "Most Published Genre" ใน Tab 2 ที่กำหนดให้เป็นค่า Static (Unlinked)
* **Global Reset Filters Button Requirement:**
  * ทุกแท็บต้องมีปุ่ม **"Reset Filters" (คืนค่าตัวกรองทั้งหมด)** สไตล์ Pill-shape
  * เมื่อคลิก ระบบต้องล้างค่า State ของ Filter ทั้งหมดในแท็บนั้นให้กลับเป็น Default ทันทีโดย **ห้ามสั่ง Reload/Refresh เบราว์เซอร์ (No Page Reload)**
* **การระบุหน่วยข้อมูล (Data Units Standardize):**
  * ยอดขายทั้งหมดใช้หน่วย **ล้านดอลลาร์สหรัฐ ($M USD)**
  * คะแนนวิจารณ์ (Critic Score) ใช้หน่วย **คะแนน (Points 0–100)**
  * คะแนนผู้เล่น (User Score) ให้แปลงเป็นสเกล **คะแนน (Points 0–100)**
  * จำนวนเกมใช้หน่วย **จำนวนเกม (Titles)**

---

## 4. รายละเอียดข้อกำหนดรายแท็บ (Detailed Tab Specifications)

### Tab 1: Executive Overview & Regional Market Share
**วัตถุประสงค์:** ภาพรวมระดับบริหาร ยอดขายรวม ตลาดแต่ละภูมิภาค และการจัดอันดับเกมฮิต

* **KPI Cards (ตัวชี้วัดหลัก):**
  1. Global Total Sales ($M USD)
  2. Total Game Titles (จำนวนเกมทั้งหมด)
  3. Top-Selling Genre (หมวดหมู่ทำรายได้สูงสุด)
  4. Top Console/Platform (แพลตฟอร์มครองยอดขายสูงสุด)

* **Filters & Slicers (ตัวกรองข้อมูล):**
  * Release Year Range Slider (ช่วงปีวางจำหน่าย)
  * Region Selector (ภูมิภาค)
  * Console Generation / Platform Selector (แพลตฟอร์ม)
  * **Reset Filters Button** (ปุ่มรีเซ็ตใน UI ซ้ายมือ)

* **Visuals & Charts (กราฟและแผนภูมิ):**
  1. **Line Chart: Yearly Sales Trend**
     * *Sub-header Description:* "แสดงแนวโน้มยอดขายเกมรวมทั่วโลกย้อนหลังตามปีที่วางจำหน่าย ($M USD) เพื่อดูการเติบโตและยุคทองของวงการเกม"
     * *Axes:* X = Year, Y = Global Sales ($M USD)
  2. **Stacked Bar Charts (Vertical & Horizontal): Regional Breakdown**
     * *Sub-header Description:* "แสดงสัดส่วนยอดขายจำแนกตามภูมิภาคหลัก (NA, EU, JP, Other) ซ้อนทับตามหมวดหมู่เกม ($M USD)"
  3. **Horizontal Bar Chart: Top 10 Best-Selling Games**
     * *Sub-header Description:* "จัดอันดับ 10 เกมที่มียอดขายรวมสูงสุด ($M USD)"
     * *Developer Note (Clean Label Requirement):* ตัดรหัส Prefix เช่น `Game___` ออกให้เหลือเฉพาะ Game Title บริสุทธิ์

---

### Tab 2: Genre & Platform Dynamics
**วัตถุประสงค์:** เจาะลึกโครงสร้างตลาด การกระจายตัวของค่ายเกม แพลตฟอร์ม และแนวเกมทำเงิน

* **KPI Cards:**
  1. **Hero KPI Card (สไตล์การ์ดสีสันโค้งมนเด่นพิเศษ):** `Most Published Genre` (หมวดหมู่ที่มีจำนวนเกมวางขายมากที่สุด) - *Static Card*
  2. **Standard KPI Card:** `Leading Publisher` (ค่ายเกมที่มีส่วนแบ่งตลาดสูงสุด)
  3. **Standard KPI Card:** `Global Sales` (ยอดขายรวม $M USD)

* **Filters & Slicers:**
  * Genre Selector (หมวดหมู่เกม)
  * Platform Family Selector (PlayStation / Xbox / Nintendo / PC)
  * Publisher Selector (ค่ายผู้พัฒนา)
  * **Reset Filters Button**

* **Visuals & Charts:**
  1. **Heatmap Matrix: Genre vs Platform Matrix**
     * *Sub-header Description:* "แสดงความเข้มข้นของยอดขายรวม ($M USD) ระหว่างหมวดหมู่เกมเทียบกับแพลตฟอร์ม"
  2. **Treemap Chart: Publisher Market Share**
     * *Sub-header Description:* "แสดงสัดส่วนส่วนแบ่งตลาดของค่ายเกมยักษ์ใหญ่ ($M USD)"
  3. **Bar Chart: Total Sales by Genre**
     * *Sub-header Description:* "เปรียบเทียบยอดขายรวม ($M USD) แยกตามหมวดหมู่เกม"

---

### Tab 3: Critical Acclaim & ESRB Content Rating Strategy
**วัตถุประสงค์:** ประเมินคุณภาพเกม (คะแนนวิจารณ์ vs คะแนนผู้เล่น) และวิเคราะห์กลยุทธ์เรตติ้งความเหมาะสมของเนื้อหา (ESRB Rating)

* **KPI Cards:**
  1. Avg Critic Score of Top 100 Games (Points 0–100)
  2. Hit Games Percentage (% เกมยอดขายเกิน 1 ล้านชุด)
  3. Correlation Score (ค่าความสัมพันธ์ระหว่างคะแนนกับยอดขาย)

* **Filters & UI Controls (วางใน Sidebar หรือ Panel ด้านซ้าย):**
  1. Release Year Range Slider
  2. Critic Score Range Selector
  3. ESRB Rating Selector
  4. **Reset Filters Button** (คลิกเพื่อล้างค่าโดยไม่ต้อง Refresh หน้าเว็บ)

* **Visuals & Charts (4 กราฟหลัก):**
  1. **Horizontal Bar Chart: Top 10 Best Rated Games**
     * *Sub-header Description:* "แสดง 10 อันดับเกมที่ได้คะแนนนักวิจารณ์สูงสุด เทียบกับคะแนนวิจารณ์ (Points 0–100)"
     * *Developer Note:* ใช้ `mean()` บน `critic_score` และล็อค Range แกน X ที่ `[0, 100]`
  2. **Multi-Line Chart: Critic vs. User Score Comparison by Genre**
     * *Sub-header Description:* "เปรียบเทียบแนวโน้มคะแนนเฉลี่ยระหว่างนักวิจารณ์และผู้เล่นในแต่ละหมวดหมู่เกม (Points 0–100)"
     * *Visual Styling:* 🔵 **เส้นสี Indigo Blue** = Critic Score / 🔴 **เส้นสี Coral Red** = User Score
  3. **100% Stacked Bar Chart: Regional Market Preference by ESRB Rating**
     * *Sub-header Description:* "แสดงสัดส่วนเปอร์เซ็นต์ยอดขายรายภูมิภาค (NA, EU, JP, Other) จำแนกตามเรตติ้งความเหมาะสมเนื้อหา (ESRB Rating)"
  4. **Heatmap Matrix: Genre x ESRB Sales Matrix**
     * *Sub-header Description:* "แสดงความเข้มข้นของยอดขายรวม ($M USD) ระหว่างแนวเกม (Genre) เทียบกับเรตติ้งเนื้อหา (ESRB Rating)"

---

## 5. สรุปรายการพัฒนาสำหรับทีม Antigravity (Developer Checklist)

| หมวดหมู่ | ข้อกำหนดการพัฒนา (Action Required) |
| --- | --- |
| **UI Design System** | ปรับ Theme หน้าจอทั้งหมดเป็น Modern Dark Slate Sidebar (`#343A40`) และ Main Canvas สีเทาอ่อน (`#F4F5F7`) |
| **Card Components** | กล่อง Card ทั้งหมดต้องมีความโค้งมนสูง (`border-radius: 20px`) พร้อมเงา Soft Drop Shadow |
| **Color Scheme** | กำหนดสีกราฟ Plotly ให้ใช้ชุดสี Sage Green, Royal Indigo, Coral Red, และ Amber Gold ตามภาพอ้างอิง |
| **Global UI** | เพิ่มปุ่ม **Reset Filters** ในสไตล์ Pill-button ทุกแท็บ และใช้ State Callback โดยไม่โหลด Refresh หน้าเว็บ |
| **Tab 1** | Clean Label Function ตัด Prefix `Game___` ออกจาก Y-axis ของ Top 10 Best Selling Chart |
| **Tab 2** | ทำ Hero KPI Card สีกราฟฟิคตัดสว่าง ( Sage Green/Indigo) สำหรับ `Most Published Genre` (Static Card) |
| **Tab 3** | ถอด Top 10 Best Selling และ ESRB Line Chart ออก ให้เหลือ 4 กราฟหลักตามข้อกำหนด |