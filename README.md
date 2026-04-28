# 🧹 Data Cleaning Project – Sales Orders Dataset

## 📌 Overview

This project demonstrates a complete data cleaning and preprocessing pipeline using Python (Pandas).
The dataset simulates real-world messy e-commerce sales data containing missing values, duplicates, inconsistent formats, and invalid entries.

The goal is to transform raw, unreliable data into a clean, structured, and analysis-ready dataset.

---

## 📂 Dataset Description

The raw dataset (`dirty_sales_orders.csv`) contains:

* Duplicate order IDs
* Missing customer names
* Inconsistent product and city naming
* Missing or invalid prices
* Invalid date formats

---

## 🛠️ Data Cleaning Process

The following steps were applied:

### 1. Remove Duplicates

* Eliminated full duplicate rows
* Removed duplicate `order_id` values

### 2. Handle Missing Values

* Filled missing customer names with `"Unknown"`
* Replaced missing prices with median value
* Fixed invalid dates using most frequent valid date

### 3. Standardize Text Data

* Converted product names to consistent format
* Standardized city names (case normalization + mapping)

### 4. Fix Data Types

* Converted `price` to numeric
* Converted `date` to datetime format

### 5. Data Sorting

* Sorted dataset by date for better structure

---

## 💻 Technologies Used

* Python 3.x
* Pandas
* NumPy

---

## 📜 How to Run the Project

### 1. Install dependencies

```bash
pip install pandas numpy
```

---

### 2. Run the cleaning script

```bash
python clean_sales.py
```

---

### 3. Output

After running the script, a cleaned dataset will be generated:

```
clean_sales_orders.csv
```

---

## 📊 Results

After cleaning, the dataset is:

* Free of duplicates
* Consistent in format
* Complete (no missing critical values)
* Ready for analysis or visualization

---

## 🚀 Key Skills Demonstrated

* Data Cleaning & Preprocessing
* Handling Missing Data
* Data Standardization
* Feature Formatting
* Real-world dataset simulation

---

## 📌 Project Structure

```
project/
│
├── dirty_sales_orders.csv
├── clean_sales.py
├── clean_sales_orders.csv
└── README.md
```

---

## 💡 Future Improvements

* Add data visualization dashboard (Streamlit / Power BI)
* Automate pipeline using ETL workflow
* Add logging system for data quality tracking

---


