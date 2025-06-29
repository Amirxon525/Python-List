### 🟢 **1. List yaratish bo‘yicha – 5 ta task**

**Task 01:** 3 ta meva nomidan iborat oddiy list yarating.

**Task 02:** 5 ta sonli ro‘yxat yarating va uni ekranga chiqaring.

**Task 03:** 3 ta ism va 3 ta yoshdan iborat 2 ta ro‘yxat yarating va ichma-ich list hosil qiling.

**Task 04:** `input()` yordamida foydalanuvchidan 3 ta ism olib ro‘yxat yarating.

**Task 05:** Ichida 2 ta ichma-ich ro‘yxat mavjud bo‘lgan (2x2 shaklda) ro‘yxat yarating va ularni chiroyli chiqaruvchi dastur yozing.

---

### 🟡 **2. List indexing bo‘yicha – 5 ta task**

**Task 06:** 5 ta shahar nomli ro‘yxatdan 3-chi elementni chop eting.

**Task 07:** Ro‘yxatdagi oxirgi elementni chop eting (manfiy indeksdan foydalaning).

**Task 08:** Ro‘yxatdagi 2-chi elementni yangi qiymatga almashtiring.

**Task 09:** Ichma-ich listdagi elementni indeks orqali o‘zgartiring (`students = [["Ali", 18], ["Vali", 20]] → Ali yoshini 19 ga almashtiring`).

**Task 10:** Foydalanuvchi kiritgan indeksga qarab ro‘yxatdagi qiymatni yangilang.

---

### 🔵 **3. List slicing bo‘yicha – 5 ta task**

**Task 11:** 10 ta sondan iborat ro‘yxatning 3-dan 6-gacha bo‘lgan qismini chiqaring.

**Task 12:** Ro‘yxatdagi barcha elementlardan faqat juft indeksdagilarni chiqaring (`0, 2, 4...`).

**Task 13:** Ro‘yxatni `[::-1]` bilan teskari qilib chiqaring.

**Task 14:** Oxirgi 3 ta elementni slicing orqali chiqaruvchi dastur yozing.

**Task 15:** Foydalanuvchidan `start` va `end` indekslarini olib, o‘sha oralig‘dagi bo‘limni chiqaring.

---

### 🟠 **4. List `len()` bo‘yicha mantiqiy 3 ta task**

**Task 16:** Ro‘yxat uzunligini aniqlang va agar u 5 dan katta bo‘lsa `"Ko‘p element"` deb chiqaring.

**Task 17:** Foydalanuvchi istalgancha ism kiritadi (`append` bilan), oxirida uzunligini `len()` bilan chiqaring.

**Task 18:** Ro‘yxat uzunligi toq bo‘lsa `True`, aks holda `False` deb chiqaruvchi dastur yozing.

---

### 🔴 **5. List metodlari bo‘yicha – 10 ta task**

**Task 19:** `append()` yordamida ro‘yxatga yangi ism qo‘shing.

**Task 20:** `insert()` yordamida ro‘yxat boshiga son qo‘shing.

**Task 21:** `remove()` yordamida ro‘yxatdan ism o‘chiring.

**Task 22:** `pop()` bilan oxirgi elementni olib tashlang.

**Task 23:** `index()` yordamida ismning indeksini aniqlang.

**Task 24:** `count()` yordamida "Ali" ismi necha marta qatnashganini aniqlang.

**Task 25:** `sort()` bilan ro‘yxatni alfavit tartibida saralang.

**Task 26:** `reverse()` yordamida ro‘yxatni teskari aylantiring.

**Task 27:** `clear()` yordamida barcha elementlarni o‘chiring.
`
**Task 28:** `copy()` yordamida ro‘yxat nusxasini oling va ikkalasini chiqarib solishtiring.
`
---

### 🧠 **Aralash va Mantiqiy 5 ta Qiyinroq Task**

---

**🔷 Task 29: Noyob elementlar ro‘yxati**

Foydalanuvchi 10 ta son kiritadi. Shu sonlardan takrorlanmaydigan (faqat bir marta uchragan) sonlardan iborat yangi ro‘yxat yarating.
*Misol:* `input: [1, 2, 2, 3, 4, 1, 5, 6, 3, 7]` → `output: [4, 5, 6, 7]`

---

**🔷 Task 30: Palindrom so‘zlar**

Foydalanuvchi kiritgan 5 ta so‘zdan iborat ro‘yxatdan **palindrom** (masalan: "alla", "kok") so‘zlarni ajratib, yangi ro‘yxatga oling.
*Shart:* So‘z o‘zi bilan teskari yozilganda bir xil bo‘lishi kerak.

---

**🔷 Task 31: Eng ko‘p takrorlangan element**

Ro‘yxatda eng ko‘p takrorlangan elementni toping (bir nechta bo‘lsa, birinchisini chiqaring).
*Misol:* `input: [3, 5, 3, 2, 5, 5, 1]` → `output: 5`

---

**🔷 Task 32: So‘z uzunligi bo‘yicha filter**

Foydalanuvchi so‘zlar ro‘yxatini kiritadi. Shu ro‘yxatdan faqat uzunligi 5 dan katta bo‘lgan so‘zlarni yangi ro‘yxatga yozing.
*Misol:* `["kitob", "dastur", "AI", "hello", "python"]` → `["dastur", "python"]`

---

**🔷 Task 33: To‘plamlar kesishmasi (intersection)**

2 ta ro‘yxat berilgan. Ularda umumiy bo‘lgan elementlarni alohida ro‘yxatga ajrating (takrorlarsiz).
*Misol:*
`list1 = [1, 2, 3, 4, 5]`
`list2 = [4, 5, 6, 7]`
→ `output: [4, 5]`

---

**🔷 Task 34: Raqamlar yig‘indisi 10 ga teng bo‘lgan juftliklar**

Foydalanuvchi 6 ta son kiritadi. Shu sonlar orasidan yig‘indisi **10** ga teng bo‘lgan barcha **juftliklarni (pair)** chiqaring.
*Misol:* `input: [1, 2, 3, 7, 8, 9]` → `output: [(1, 9), (2, 8), (3, 7)]`

---

**🔷 Task 35: Elementlarni guruhlash (group by length)**

Foydalanuvchi so‘zlardan iborat ro‘yxat kiritadi. So‘zlarni uzunligiga qarab 3 guruhga ajrating:

* `<=3 harfli`
* `4-6 harfli`
* `>6 harfli`
  Har bir guruh alohida ro‘yxatda bo‘lsin.

---

**🔷 Task 36: Eng uzun so‘zni topish**

Foydalanuvchi kiritgan so‘zlar ro‘yxatidan eng uzun so‘zni toping.
*Shart:* Agar bir nechta bo‘lsa, birinchi uchraganini qaytaring.

---

**🔷 Task 37: 2 ta ro‘yxatni almashtirish**

Foydalanuvchidan 2 ta teng uzunlikdagi ro‘yxat oling. Har bir ro‘yxatdagi mos indekslardagi qiymatlarni bir-biri bilan almashtiring.
*Misol:*
`list1 = [1, 2, 3]`
`list2 = [4, 5, 6]`
→ `list1 = [4, 5, 6]`, `list2 = [1, 2, 3]`

---
