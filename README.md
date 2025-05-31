
# 🔥 Algerian Forest Fire Prediction

This project focuses on predicting the **Fire Weather Index (FWI)** using real-world environmental data from Algeria. Multiple regression models were trained and evaluated to determine the most accurate predictor for fire risk.

---

## 📁 Project Structure

```
algerian_forest_fire/
│
├── Algerian_forest_fires_dataset.csv              # Raw dataset
├── Algerian_forest_fires_cleaned_dataset.csv      # Cleaned dataset after preprocessing
├── algerian_cleaning.ipynb                        # Data cleaning + EDA + feature engineering
├── algerian_training.ipynb                        # Model training and evaluation
├── Algerian_Forest_Fire_Prediction/               # Folder with any additional project files
└── README.md                                      # Project documentation
```

---

## 🧹 Data Cleaning & 🔧 Feature Engineering

📍 Performed in `algerian_cleaning.ipynb`:

- Removed unnecessary columns like `'day'`, `'month'` (text format).
- Handled missing values.
- Converted categorical values to numerical.
- Combined region-wise data into one cohesive dataset.
- Applied transformations to create relevant features for prediction.
- Removed outliers using boxplots.

Cleaned data was saved as `Algerian_forest_fires_cleaned_dataset.csv`.

---

## 📊 Model Building & Evaluation

📍 Done in `algerian_training.ipynb`.

Several regression models were trained and compared:

| Model             | MAE (Mean Absolute Error) | R² Score   |
|------------------|----------------------------|------------|
| **Linear Regression** | **0.5468**             | **0.9847** |
| Lasso             | 1.1331                     | 0.9492     |
| Ridge             | 0.5642                     | 0.9843     |
| ElasticNet        | 1.8822                     | 0.8753     |
| RidgeCV           | 0.5642                     | 0.9843     |
| ElasticNetCV      | 0.6575                     | 0.9814     |

✅ **Best Performing Model:** `Linear Regression`

---

## 🚫 No Web App *(Yet)*

This version focuses solely on **data preprocessing, feature engineering**, and **model building**.  
A **web app/dashboard** may be added later for real-time predictions and user interaction.

---

## 🔍 Dataset Info

The dataset includes environmental factors like:

- Temperature
- Relative Humidity (RH)
- Wind Speed
- Rain
- FFMC, DMC, DC, ISI (Fire weather indexes)
- Fire occurrence status

---

## 🚀 Future Improvements

- [ ] Add a **Streamlit or Flask web app** for live predictions.
- [ ] Integrate **real-time weather API** to auto-fetch current data.
- [ ] Enhance data visualization with heatmaps, line charts, etc.
- [ ] Improve model accuracy using hyperparameter tuning or ensemble methods.

---

## 🧠 Skills Used

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn (Linear, Lasso, Ridge, ElasticNet)
- MAE & R² metrics

---
