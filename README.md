# SoilAI 🌱

**SoilAI** is a Python project that detects soil types from images and recommends suitable crops and fertilizers.

---

## 🚀 Features

✅ Detect soil types from images (dummy model for now).  
✅ Recommend crops and fertilizers.  
✅ Show soil locations on an interactive map.  
✅ Generate a PDF report with all results.

---

## 💻 How to Run

1. Clone this repo:

```
git clone https://github.com/NaveenReddy-28/SoilAI.git
```

2. Navigate into the folder:

```
cd SoilAI
```

3. Create virtual environment:

```
python -m venv soilai_env
```

4. Activate the environment (Windows):

```
soilai_env\Scripts\activate
```

5. Install requirements:

```
pip install -r requirements.txt
```

6. Run the tool:

```
python main.py --image "soil 1.jpg" --lat 18.6153 --lon 79.1633
```

---

## ✅ Example Output

When you run the command, you’ll see:

```
Detected soil type: Sandy
Recommended Crops: ['Watermelon', 'Peanuts']
Recommended Fertilizers: ['Compost', 'Sulphate of Potash']
Organic Amendments: ['Organic compost']
Map saved to soil_map.html
PDF report saved to Soil_Report.pdf
```

---

## 📸 Screenshots

*(Add screenshots here if you’d like.)*

---

## 📄 [View Example PDF Report](Soil_Report.pdf)

---

## ✨ Future Improvements

- Train a real CNN model for soil detection
- Build a web interface
- Add support for multiple soil samples at once

---

## 👨‍💻 Author

[Naveen Reddy](https://github.com/NaveenReddy-28/SoilAI)
