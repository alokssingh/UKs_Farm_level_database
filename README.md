# 🌾 UK Farm-Level Database Builder

## 📌 Project Overview
This project builds a comprehensive **UK farm-level database** by integrating multiple datasets from various government and agricultural sources. The database provides insights into **ownership, crop types, environmental incentives, and agricultural production** using **Python-based data processing and analysis techniques**.

---

## 📂 Datasets Used

| Dataset | Year | Coverage | Insights & Limitations |
|---------|------|----------|------------------------|
| **Ordnance Survey MasterMap (OSMM)** | 2022 | All England’s agricultural fields | May underestimate total land coverage compared to DEFRA estimates |
| **CROME** | 2023 | Crop types in England | Does not differentiate between summer and winter crops; missing crop hexagonal data |
| **Land Registry (LR)** | 2023 | Ownership of agricultural fields | 46% of parcels lack ownership information |
| **Companies House (CH)** | 2023 | Registered agricultural companies | Includes duplicate entries; requires filtering by SIC codes |
| **Rural Payment Agency (RPA)** | 2023 | Land parcels receiving subsidies | Used only for validation purposes; no independent data for unregistered parcels |
| **Countryside Stewardship (CS)** | 2023 | Farmers receiving environmental incentives | Covers only 31% of agricultural land, forming a minimum threshold for farming entity assignments |
| **Organic Farms England** | 2022 | Organic farms in England & Wales | Lists the type of product grown at the farm |

---

## 🛠️ Key Processing Scripts & Notebooks

| File Name | Description |
|-----------|-------------|
| `cleaning_LR_using_ORD.ipynb` | Cleans and preprocesses Land Registry data, removing noise and inconsistencies. |
| `countryside_using_ord_remaining_mapping.ipynb` | Segments clusters within **Countryside Stewardship** data. |
| `add_nature_of_business.ipynb` | Categorizes businesses using SIC codes from **Companies House** data. |
| `crop_type.py` | Assigns **crop types** to land parcels using Ordnance Survey data. |
| `owner_assignment.ipynb` | Matches land ownership using **title numbers** from the Land Registry. |
| `final_voronoi.ipynb` | Applies **Voronoi-based unsupervised mapping** to unclassified Ordnance Survey fields. |
| `Merging_LR_CS.ipynb` | Merges cleaned **Land Registry** and **Countryside Stewardship** data **by owner and crop type**. |
| `production_no_cattle.ipynb` | Calculates production numbers for **cattle, livestock, sheep, and lamb**. |

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/alokssingh/UK_Farm_Database.git
cd UK_Farm_Database
```

### 2️⃣ Install Required Dependencies
```sh
pip install -r requirements.txt
```

---

## 🚀 Usage

To execute specific processing steps, run the appropriate scripts or notebooks:

### 📊 Run Data Cleaning & Preprocessing
```sh
jupyter notebook cleaning_LR_using_ORD.ipynb
```

### 🌱 Assign Crop Types to Parcels
```sh
python crop_type.py
```

### 🏡 Assign Ownership Data
```sh
jupyter notebook owner_assignment.ipynb
```

### 📌 Apply Voronoi Mapping
```sh
jupyter notebook final_voronoi.ipynb
```

### 🔗 Merge Cleaned Data
```sh
jupyter notebook Merging_LR_CS.ipynb
```

---

## 📊 Insights & Contributions
- **Land Ownership Mapping**: Links fragmented **ownership records** to known land parcels.
- **Crop Type Classification**: Assigns **crop types** to fields from OSMM and CROME datasets.
- **Agricultural Production Estimates**: Calculates **livestock and crop production numbers** at the farm level.
- **Geospatial Analysis**: Implements **Voronoi clustering** for unsupervised mapping.

---

## 🤝 Contributing
We welcome contributions! 🚜 If you'd like to contribute:
1. **Fork the repository**
2. **Create a new branch** (`git checkout -b feature-branch`)
3. **Commit your changes** (`git commit -m "Your Message"`)
4. **Push to the branch** (`git push origin feature-branch`)
5. **Open a Pull Request**

---

## 📜 License
This project is licensed under the **[MIT License](https://choosealicense.com/licenses/mit/)**.

🚀 **Happy Farming & Coding!** 🌾
