# 🕊️ Operation Navjeevan

## 📖 Overview

**Operation Navjeevan** is a humanitarian data analysis and simulation project developed as part of a major assignment for the *Python for Computer Science and Data Science 1 (CSE 3651)* course at SOA University.

This project simulates real-world, data-driven decision-making for humanitarian relief during the Russia-Ukraine conflict. It uses core Python concepts—including mutable and immutable objects, sets, tuples, lists, and dictionaries—to support the Indian Taskforce for Emergency Relief in managing aid distribution to affected Ukrainian cities.

You take on the role of an advanced intelligence agent, tasked with analyzing mission-critical data to determine high-alert zones and deliver life-saving supplies efficiently.

---

## ⚙️ Features

- ✅ **Clean and Sort Aid Requests**  
  Remove duplicates and alphabetize lists of cities needing aid.

- 🚨 **Identify High-Alert Zones**  
  Perform set operations to determine urgent cities based on multiple intelligence sources.

- 🧠 **City-Level Intelligence Mapping**  
  Construct a dictionary with population and aid data for high-alert cities. Compute total aid needs and affected population.

- 📦 **Track Supply Distribution**  
  Use nested dictionaries to track types and quantities of aid sent to Ukrainian and Russian cities.

---

## 🧪 Tech Stack

- Python 3.x
- Core Python Data Structures:
  - `list`
  - `set`
  - `tuple`
  - `dict`
- No external libraries required

---

## 🎯 Target Audience

- Python beginners and intermediate learners  
- Students applying data structures to real-world contexts  
- Educators using humanitarian case studies for programming assignments

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/operation-navjeevan.git
cd operation-navjeevan
```

### 2. Run the Scripts

Make sure Python 3 is installed on your machine.

```bash
python mission1_clear_field.py
```

> Replace the filename above with any mission-specific script you want to run.

---

## 🗂️ Project Structure

```
operation-navjeevan/
├── mission1_clear_field.py         # Remove duplicates and sort cities
├── mission2_high_alert.py          # Identify high-alert cities
├── mission3_city_intel.py          # Build dictionary of detailed city intel
├── mission4_supply_tracking.py     # Track distribution of supplies
├── README.md                       # This file
```

---

## 📊 Sample Input & Output

### Mission 1: Clearing the Field

**Input:**
```python
cities = ["Kyiv", "Kharkiv", "Odessa", "Kyiv", "Lviv", "Kharkiv", "Dnipro"]
```

**Output:**
```python
["Dnipro", "Kharkiv", "Kyiv", "Lviv", "Odessa"]
```

---

## 🔮 Future Enhancements

- 🌍 Integrate real-world data using APIs from humanitarian organizations  
- 📊 Add a simple web dashboard or CLI interface for visualizing the aid data  
- 🧭 Expand logic to factor in geographical proximity and logistics for smarter resource planning  
- 📦 Add tracking of supply expiry, restock alerts, and historical distribution logs

---

## 🙌 Acknowledgements

This project was developed as part of a course assignment under the guidance of the **Centre for Data Science**,  
*Institute of Technical Education & Research, SOA (Deemed to be University)*.

Gratitude to the mentors and educators who inspire students to solve real-world problems through code.

> *"Heroes are not born in the mother’s womb, they are born on the battlefield."*

---

## 📄 License

This project is intended for educational purposes. For any other use, please contact the author or institution.
