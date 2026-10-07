# Business Requirements Document (BRD)
## ระบบ Global Video Game Sales Analytics Dashboard (v6.0)

**วันที่ปรับปรุงล่าสุด:** 7 ตุลาคม 2026  
**ผู้จัดทำ:** Strategy & Business Intelligence Team  
**ผู้รับมอบหมายพัฒนา (Developer):** Antigravity Team  

---

## 1. วัตถุประสงค์โครงการ (Project Purpose)
เอกสารนี้จัดทำขึ้นเพื่อระบุข้อกำหนดในการพัฒนา **Global Video Game Sales Analytics Dashboard** สำหรับใช้งานโดยทีมบริหารและนักวางแผนกลยุทธ์ค่ายเกม (Publisher & Strategy Analyst) โดยมีจุดประสงค์หลักดังนี้:
1. วิเคราะห์ภาพรวมตลาดเกมทั่วโลก แนวโน้มการเติบโต และความพฤติกรรมการบริโภคตามภูมิภาค
2. เจาะลึกความสัมพันธ์ระหว่างหมวดหมู่เกม (Genre), แพลตฟอร์ม (Platform) และค่ายเกม (Publisher)
3. ประเมินความพึงพอใจของนักวิจารณ์ (Critic Score) เทียบกับผู้เล่นจริง (User Score) พร้อมวิเคราะห์กลยุทธ์เรตติ้งความเหมาะสมเนื้อหา (ESRB Rating) ต่อผลตอบแทนด้านยอดขายทั่วโลก

---

## 2. ข้อกำหนดทางเทคนิคหลัก (Core Technical Requirements)
* **Backend Framework:** Python (FastAPI / Dash / Streamlit)
* **Data Visualization Library:** Plotly / Plotly Express (โหมด Interactive เต็มรูปแบบ)
* **Interactivity & Inter-chart Linking (Cross-filtering):**
  * กราฟทุกรูปภายในแท็บเดียวกันต้องเชื่อมต่อกันผ่าน Callbacks (เมื่อคลิกเลือก Filter หรือคลิก Element บนกราฟ กราฟอื่นในแท็บเดียวกันต้องกรองข้อมูลและอัปเดตตามทันที)
  * ยกเว้น KPI Card "Most Published Genre" ใน Tab 2 ที่กำหนดให้เป็นค่า Static (Unlinked)
* **Global Reset Filters Button Requirement (ใหม่ใน v6.0):**
  * ทุกแท็บต้องมีปุ่ม **"Reset Filters" (คืนค่าตัวกรองทั้งหมด)**
  * เมื่อผู้ใช้คลิกปุ่มนี้ ระบบต้องล้างค่า State ของ Filter ทั้งหมดในแท็บนั้นให้กลับเป็นค่า Default ทันทีโดย **ห้ามมีการโหลดหน้าเว็บใหม่ (No Full Page Refresh / Browser Reload)**
* **การระบุหน่วยข้อมูล (Data Units Standardize):**
  * ยอดขายทั้งหมดใช้หน่วย **ล้านดอลลาร์สหรัฐ ($M USD)**
  * คะแนนวิจารณ์ (Critic Score) ใช้หน่วย **คะแนน (Points 0–100)**
  * คะแนนผู้เล่น (User Score) ให้แปลงเป็นสเกล **คะแนน (Points 0–100)** โดยการคูณ 10 หากชุดข้อมูลเดิมเป็น 0–10
  * จำนวนเกมใช้หน่วย **จำนวนเกม (Titles)**

---

## 3. รายละเอียดข้อกำหนดรายแท็บ (Detailed Tab Specifications)

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
  * **Reset Filters Button:** ปุ่มสำหรับคืนค่า Filter ใน Tab 1 ทั้งหมดกลับเป็น Default

* **Visuals & Charts (กราฟและแผนภูมิ):**
  1. **Line Chart: Yearly Sales Trend**
     * *Sub-header Description:* "แสดงแนวโน้มยอดขายเกมรวมทั่วโลกย้อนหลังตามปีที่วางจำหน่าย ($M USD) เพื่อดูการเติบโตและยุคทองของวงการเกม"
     * *Axes:* X = Year, Y = Global Sales ($M USD)
  2. **Stacked Bar Charts (Vertical & Horizontal): Regional Breakdown**
     * *Sub-header Description:* "แสดงสัดส่วนยอดขายจำแนกตามภูมิภาคหลัก (NA, EU, JP, Other) ซ้อนทับตามหมวดหมู่เกม ($M USD)"
     * *Developer Note:* บังคับเชื่อมต่อ Callback เข้ากับ Filter ทุกตัว เมื่อผู้ใช้ปรับเปลี่ยน Filter กราฟ Stacked Bar ทั้งสองต้องเปลี่ยนตามเสมอ
  3. **Horizontal Bar Chart: Top 10 Best-Selling Games**
     * *Sub-header Description:* "จัดอันดับ 10 เกมที่มียอดขายรวมสูงสุด ($M USD)"
     * *Developer Note (Clean Label Requirement):* แกน Y ต้องแสดงเฉพาะ **Game Title บริสุทธิ์** เท่านั้น ตัดรหัสเกม Prefix เช่น `Game___` ออกทั้งหมด

---

### Tab 2: Genre & Platform Dynamics
**วัตถุประสงค์:** เจาะลึกโครงสร้างตลาด การกระจายตัวของค่ายเกม แพลตฟอร์ม และแนวเกมทำเงิน

* **KPI Cards:**
  1. **Hero KPI Card (ขนาดใหญ่พิเศษเด่นกว่ากล่องอื่น):** `Most Published Genre` (หมวดหมู่ที่มีจำนวนเกมวางขายมากที่สุด)
     * *Special Rule:* ให้เป็นค่า Static ปลดการเชื่อมต่อ Callback จากกราฟอื่น เพื่อให้แสดงค่าภาพรวมคงที่เสมอ
  2. **Standard KPI Card:** `Leading Publisher` (ค่ายเกมที่มีส่วนแบ่งตลาดสูงสุด)
  3. **Standard KPI Card:** `Global Sales` (ยอดขายรวม $M USD)

* **Filters & Slicers:**
  * Genre Selector (หมวดหมู่เกม)
  * Platform Family Selector (PlayStation / Xbox / Nintendo / PC)
  * Publisher Selector (ค่ายผู้พัฒนา)
  * **Reset Filters Button:** ปุ่มสำหรับคืนค่า Filter ใน Tab 2 ทั้งหมดกลับเป็น Default

* **Visuals & Charts:**
  1. **Heatmap Matrix: Genre vs Platform Matrix**
     * *Sub-header Description:* "แสดงความเข้มข้นของยอดขายรวม ($M USD) ระหว่างหมวดหมู่เกมเทียบกับแพลตฟอร์ม เพื่อดูความเข้ากันได้ของเครื่องเกมและแนวเกม"
  2. **Treemap Chart: Publisher Market Share**
     * *Sub-header Description:* "แสดงสัดส่วนส่วนแบ่งตลาดของค่ายเกมยักษ์ใหญ่ ยิ่งพื้นที่มากหมายถึงยอดขายรวมสะสม ($M USD) สูง"
  3. **Bar Chart: Total Sales by Genre**
     * *Sub-header Description:* "เปรียบเทียบยอดขายรวม ($M USD) แยกตามหมวดหมู่เกม เพื่อดูหมวดหมู่หลักที่สร้างรายได้มหาศาล"
     * *Developer Note:* ให้เหลือเพียงกราฟยอดขายรวมเพียงอย่างเดียว (ตัดกราฟ Average Sales ออกเพื่อความเรียบง่าย)

---

### Tab 3: Critical Acclaim & ESRB Content Rating Strategy
**วัตถุประสงค์:** ประเมินคุณภาพเกม (คะแนนวิจารณ์ vs คะแนนผู้เล่น) และวิเคราะห์กลยุทธ์เรตติ้งความเหมาะสมของเนื้อหา (ESRB Rating) เพื่อวางแผนกลุ่มเป้าหมายผู้เล่นและประเมินผลตอบแทนทางธุรกิจ

* **KPI Cards:**
  1. Avg Critic Score of Top 100 Games (คะแนนวิจารณ์เฉลี่ย 0–100 Points)
  2. Hit Games Percentage (% เกมที่มียอดขายเกิน 1 ล้านชุด)
  3. Correlation Score (ค่าความสัมพันธ์ระหว่างคะแนนวิจารณ์กับยอดขาย)

* **Filters & UI Controls (วางเรียงตัวกรองในแนวตั้ง Vertical Orientation):**
  1. **Release Year Range Slider (Vertical):** 
     * *Note / Explanatory Text:* "📌 หมายเหตุ: ตัวกรองช่วงปีวางจำหน่าย เพื่อวิเคราะห์วิวัฒนาการของคะแนนวิจารณ์และพฤติกรรมผู้เล่นตามยุคสมัย"
  2. **Critic Score Range Selector (Vertical):** 
     * *Note / Explanatory Text:* "📌 หมายเหตุ: ตัวกรองช่วงคะแนนวิจารณ์ เพื่อเจาะลึกเฉพาะกลุ่มเกมเกรด A (90+), B (80-89) หรือกลุ่มทั่วไป"
  3. **ESRB Rating Selector (Vertical):**
     * *Note / Explanatory Text:* "📌 หมายเหตุ: ตัวกรองเรตติ้งความเหมาะสมเนื้อหา (E, E10+, T, M) เพื่อดูการกระจายตัวตามกลุ่มอายุเป้าหมาย"
  4. **Reset Filters Button:** ปุ่มสำหรับคืนค่า Filter ใน Tab 3 ทั้งหมดกลับเป็น Default ทันทีโดยไม่ต้องกด Refresh เบราว์เซอร์

* **Visuals & Charts (รวม 4 กราฟหลัก):**

  1. **Horizontal Bar Chart: Top 10 Best Rated Games**
     * *Sub-header Description:* "แสดง 10 อันดับเกมที่ได้คะแนนนักวิจารณ์สูงสุด เทียบกับคะแนนวิจารณ์ (Points 0–100)"
     * *Developer Bug Fix Notes:*
       - รวมข้อมูลเกมเดี่ยวข้ามแพลตฟอร์มด้วย `mean()` บน `critic_score` ล็อคสเกลแกน X ไว้ที่ 0–100 เสมอ
       - ยุบรวมชื่อเกมก่อนพล็อต เพื่อป้องกันปัญหา Stacked Bar ซ้อนในอันดับที่ 1

  2. **Multi-Line Chart: Critic vs. User Score Comparison by Genre**
     * *Sub-header Description:* "เปรียบเทียบแนวโน้มคะแนนเฉลี่ยระหว่างนักวิจารณ์และผู้เล่นในแต่ละหมวดหมู่เกม (Points 0–100)"
     * *Visual Styling:*
       - 🔵 **เส้นสีน้ำเงิน:** คะแนนจากนักวิจารณ์ (`critic_score`)
       - 🔴 **เส้นสีแดง:** คะแนนจากผู้เล่น (`user_score` ที่ปรับสเกลเป็น 0–100)
     * *Axes:* X = Genre, Y = Average Score (Points 0–100)

  3. **100% Stacked Bar Chart: Regional Market Preference by ESRB Rating**
     * *Sub-header Description:* "แสดงสัดส่วนเปอร์เซ็นต์ยอดขายรายภูมิภาค (NA, EU, JP, Other) จำแนกตามเรตติ้งความเหมาะสมเนื้อหา (ESRB Rating)"
     * *Axes:* X = ESRB Rating (E, E10+, T, M), Y = Percentage Share (100%)
     * *Business Value:* ช่วยวิเคราะห์ความพฤติกรรมการซื้อเกมตามภูมิภาค เพื่อวางกลยุทธ์ทำตลาดและการแปลภาษา (Localization)

  4. **Heatmap Matrix: Genre x ESRB Sales Matrix**
     * *Sub-header Description:* "แสดงความเข้มข้นของยอดขายรวม ($M USD) ระหว่างแนวเกม (Genre) เทียบกับเรตติ้งเนื้อหา (ESRB Rating)"
     * *Axes:* X = ESRB Rating, Y = Genre, Color Intensity = Global Sales ($M USD)
     * *Business Value:* ชี้ช่องว่างตลาด (White Space) และแนวทางพัฒนาเกม เช่น หาแนวเกมที่เรต E หรือ T ทำรายได้ดีโดยไม่ต้องทำเรต M ที่มีความเสี่ยงสูง

  *(หมายเหตุ: ถอดกราฟ Top 10 Best Selling และ ESRB Line Chart ออกตามข้อสั่งการเรียบร้อยแล้ว)*

---

## 4. สรุปรายการแก้ไขสำหรับทีม Antigravity (Developer Checklist)

| Component / Tab | Action Required |
|---|---|
| **Global UI** | เพิ่มปุ่ม **"Reset Filters"** ในทุกแท็บ และเขียน State Management (Callback) ให้ล้างค่า Filter ทั้งหมด โดยห้ามสั่ง `location.reload()` |
| **Tab 1** | เขียน Clean Label Function ตัด Prefix `Game___` ออกจาก Y-axis ของ Top 10 Best Selling Chart |
| **Tab 1** | บังคับผูก Callbacks ของ Stacked Bars ทั้งหมดเข้ากับ Filters ในแท็บ |
| **Tab 2** | ปรับ `Most Published Genre` เป็น Hero KPI Card และถอด Callback ออก (Static Card) |
| **Tab 2** | ตัดซีรีส์ Average Sales ออกจาก Bar Chart เหลือเพียง Total Sales ($M USD) |
| **Tab 3** | **ถอดกราฟ Top 10 Best Selling ออก** จาก Tab 3 |
| **Tab 3** | **ถอดกราฟ ESRB Content Rating Sales Dynamics (Line Chart) ออก** จาก Tab 3 |
| **Tab 3** | จัดวาง Filters ในแนวตั้ง (Vertical Layout) พร้อมใส่ Helper Labels |
| **Tab 3** | แสดง Top 10 Best Rated Games โดยใช้ `mean()` บนคะแนนวิจารณ์ และล็อค Range แกน X ที่ `[0, 100]` |
| **Tab 3** | แสดง Dual Line Chart สำหรับ Critic vs User Score (สเกล 0–100, เส้นสีน้ำเงิน/แดง) |
| **Tab 3** | แสดง 100% Stacked Bar Chart สำหรับสัดส่วนยอดขายภูมิภาคตาม ESRB Rating |
| **Tab 3** | แสดง Heatmap Matrix สำหรับ Genre x ESRB Rating |