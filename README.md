# Agri-Tech: A Predictive IoT Platform for Sustainable Farming

This repository contains the B.Tech Mini Project for our "Eco-Smart Agriculture" platform, developed at Pillai College of Engineering (2023-24).


---

### 1. 💡 Project Vision

Traditional irrigation is reactive and wasteful. Our solution transforms this model by creating a **proactive and predictive agri-tech platform**.

Instead of just automating sprinklers, this project uses a **full-stack IoT pipeline** to collect real-time sensor data, send it to the cloud for analysis, and run **predictive algorithms** to determine *future* watering needs. The system is designed as a **Climate-Tech** solution to enhance drought resilience and promote sustainable farming by optimizing water usage.

---

### 2. ⚙️ System Architecture & Functionality

Our platform operates as a complete "edge-to-app" system:

1.  **Edge Data Collection:** An **Arduino** microcontroller, acting as an edge device, collects continuous real-time data from **soil moisture and temperature sensors** in the field.
2.  **Cloud IoT Pipeline:** The Arduino transmits this data to a **cloud-native IoT platform** (e.g., Firebase, AWS IoT) for aggregation, processing, and storage.
3.  **Predictive Analytics:** Advanced algorithms on the cloud analyze historical trends and real-time data to **forecast optimal irrigation schedules** and identify patterns that suggest **nutrient deficiencies**.
4.  **Real-Time Dashboard:** A mobile application serves as the central dashboard. It provides farmers with **actionable intelligence** and data visualizations, allowing them to monitor crop health and manage the system from anywhere.

---

### 3. 🎯 Key Features

* **Predictive Irrigation:** Leverages ML models to move from *reacting* to dry soil to *predicting* irrigation needs 24-48 hours in advance.
* **Data-Driven Insights:** The app provides alerts for potential nutrient deficiencies based on patterns in the data, not just simple sensor thresholds.
* **Full-Stack IoT Solution:** A complete, integrated system from the physical hardware (sensors, Arduino) to the cloud backend (data processing) and the front-end (mobile app).
* **Water & Cost Optimization:** Directly addresses sustainability and budget management by cutting water waste, a critical component of modern **Climate-Tech**.

---

### 4. 🛠️ Technology Stack

* **Edge Device:** Arduino
* **Sensors:** Soil Moisture, Temperature
* **Cloud & Backend:** Google Firebase / AWS IoT (for data ingestion & analysis), Python (for analytics scripts)
* **Database:** Cloud-based (e.g., Firestore, Oracle 9)
* **Frontend:** Kotlin / Java (for Mobile App)
