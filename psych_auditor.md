# 🧠 Behavioral Health (BH) Pre-Processing Filter v5.1
### *Excel-Integrated AI Pipeline for ICD-10 'F-Series' Claims*

## 📌 Clinical Use Case
Psychiatric and Behavioral Health claims (ICD-10 codes starting with **'F'**) often require specialized clinical review. If these claims bypass the "Pend" status and auto-process, it leads to high recovery costs and compliance risks.

## 🚀 The Solution: AI-Driven Batch Processing
This tool allows an analyst to key claim data into **Excel** and use a **Random Forest Classifier** to automatically highlight which claims must be routed to the BH Team.

### Key Features:
* **Excel Data Pipeline:** Direct integration with `.xlsx` files using `pandas` and `openpyxl`.
* **Automated Data Cleaning:** Built-in logic to strip currency symbols ($) and commas from billed/allowed amounts.
* **Diagnosis Code Intelligence:** Automatically detects 'F-Series' codes and cross-references with Provider Types.
* **Batch Actioning:** High-speed processing of large claim sets to prevent incorrect auto-adjudication.

## 🛠️ Tech Stack
* **Language:** Python 3.13
* **Libraries:** `Pandas`, `Scikit-Learn`, `Openpyxl`
* **Workflow:** Healthcare Utilization Management (UM) / Pre-Processing Audit

---
*Developed by T Bharath - Healthcare IT Analyst & AI Developer*