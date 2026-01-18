# Churn Prediction AI Dashboard

## 🎯 Project Overview

This is an **end-to-end Machine Learning web application** designed to predict customer churn using a trained model. The project includes both backend (Python/Flask) and frontend (HTML/CSS/JS) components.

**Current Status**: Ready for GitHub Pages deployment ✅

---

## 📁 Project Structure

### For GitHub Pages Hosting (Static Site)

```
docs/
├── index.html                    # Main page
├── _config.yml                   # Jekyll config
└── assets/
    ├── css/style.css            # Styling
    ├── js/main.js               # Interactivity
    └── images/                  # Dashboard images
```

### For Backend Deployment (Python/Flask)

```
Backend files (for reference - deploy separately):
├── app.py                        # Flask application
├── prediction_db.py              # Database handling
├── train_new_model.py            # Model training
├── requirements.txt              # Python dependencies
└── models/
    ├── churn_model.pkl           # Trained model
    ├── scaler.pkl                # Feature scaler
    └── features.pkl              # Feature list
```

---

## 🚀 Quick Start: GitHub Pages Deployment

### Prerequisites

- GitHub account
- Git installed locally
- Images ready (`dashboard.png`, `churn.png`)

### Step 1: Prepare Images

Copy your images to: `docs/assets/images/`

### Step 2: Commit and Push

```bash
cd c:\Users\K.Raj Kumar\Documents\project
git add .
git commit -m "Deploy to GitHub Pages"
git push origin Readytogo
```

### Step 3: Enable GitHub Pages

1. Go to GitHub → Your Repository → **Settings**
2. Navigate to **Pages**
3. Under "Build and deployment":
   - Source: **GitHub Actions**
4. Wait 1-2 minutes

### Step 4: Access Your Site

Your site will be live at:

```
https://yourusername.github.io/Churn_Prediction
```

---

## 📊 Features

✅ **Responsive Design** - Works on all devices  
✅ **Interactive Charts** - Real-time data visualization  
✅ **Dark Theme** - Professional dark blue aesthetic  
✅ **Smooth Navigation** - Fixed navbar with smooth scrolling  
✅ **Demo Predictions** - Frontend-only demo functionality

---

## 🔧 Integration with Backend API

For **full ML prediction functionality**, integrate with your Flask backend:

### 1. Deploy Flask App

Deploy `app.py` to a backend service:

- **Heroku** (free tier ending)
- **Railway** ⭐ Recommended
- **Render.com**
- **PythonAnywhere**

Example with Railway:

```bash
railway up
```

### 2. Update API Endpoint

In `docs/index.html`, update the form handler:

```javascript
// Replace the demo prediction with API call
const response = await fetch("https://your-api.herokuapp.com/predict", {
  method: "POST",
  body: JSON.stringify(formData),
});
const result = await response.json();
```

### 3. Enable CORS

In `app.py`, ensure CORS is enabled:

```python
from flask_cors import CORS
CORS(app)
```

---

## 📦 Installation & Local Setup

### Backend (Optional - for local testing)

**1. Create Virtual Environment**

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

**2. Install Dependencies**

```bash
pip install -r requirements.txt
```

**3. Run Flask App**

```bash
python app.py
```

Access at: `http://localhost:5000`

### Frontend (GitHub Pages)

No installation needed! Just push to GitHub and it works.

---

## 📋 Files Explanation

### `docs/index.html`

- Main page with all sections
- Form for prediction input
- Chart.js for visualization
- Demo JavaScript logic

### `docs/assets/css/style.css`

- Dark blue professional theme
- Animations and glowing effects
- Responsive design (mobile-friendly)
- CSS variables for easy customization

### `docs/assets/js/main.js`

- Form input focus styling
- Basic interactivity

### `.nojekyll`

- Tells GitHub Pages to serve files as-is
- Prevents Jekyll from processing

### `.github/workflows/deploy.yml`

- Automated deployment workflow
- Runs on every push to main/Readytogo

---

## 🎨 Customization

### Change Colors

Edit CSS variables in `docs/assets/css/style.css`:

```css
:root {
  --primary: #38bdf8; /* Blue */
  --bg-main: #0b1120; /* Dark background */
  --text-main: #f1f5f9; /* Light text */
}
```

### Update Content

Edit text and images in `docs/index.html`

### Add Custom Domain

1. Create `CNAME` file with your domain
2. Update DNS settings in your domain provider

---

## 🔗 Backend Requirements

### Python Packages

```
Flask==2.3.2
scikit-learn==1.3.2
pandas==2.1.2
numpy==1.26.4
joblib==1.3.2
SQLAlchemy==2.0.20
flask_sqlalchemy==3.0.3
matplotlib==3.8.2
gunicorn==21.2.0
```

### Model Files

- `models/churn_model.pkl` - Trained model
- `models/scaler.pkl` - Feature scaler
- `models/features.pkl` - Feature names

---

## 🐛 Troubleshooting

### Site Not Loading

- ✅ Check `.nojekyll` file exists in root
- ✅ Verify GitHub Pages enabled in Settings
- ✅ Clear browser cache

### Images Not Showing

- ✅ Copy images to `docs/assets/images/`
- ✅ Verify filenames: `dashboard.png`, `churn.png`
- ✅ Check file permissions

### CSS/JS Not Applying

- ✅ Check file paths use `./assets/` prefix
- ✅ Hard refresh: `Ctrl+Shift+R`
- ✅ Verify files in docs folder

### API Not Connecting

- ✅ Ensure backend deployed and running
- ✅ Check CORS enabled on backend
- ✅ Verify API URL in JavaScript

---

## 📊 Dataset Information

The project trains on customer banking data:

- **Features**: Credit Score, Age, Tenure, Balance, Salary, etc.
- **Target**: Customer Churn (Yes/No)
- **Model**: Trained classification model (Random Forest / XGBoost)

---

## 👥 Team

| Name               | ID         |
| ------------------ | ---------- |
| K Rajkumar         | 229X1A32B8 |
| A Eswar Prasad     | 239X5A32C9 |
| A Harikishan Reddy | 239X5A32D1 |

**Guided By**: Sri. Y. Shiva Kumar, Assistant Professor  
**Institution**: G Pulla Reddy Engineering College

---

## 📝 License

This project is developed for educational purposes.

---

## 🔗 Useful Links

- [GitHub Pages Docs](https://docs.github.com/en/pages)
- [Railway Deployment](https://railway.app/)
- [ML Model Training](./train_new_model.py)
- [API Endpoints](./app.py)

---

## ✅ Deployment Checklist

- [ ] Copy images to `docs/assets/images/`
- [ ] Test locally (visit `docs/index.html`)
- [ ] Commit all files: `git add .`
- [ ] Push to GitHub: `git push origin Readytogo`
- [ ] Enable GitHub Pages in Settings
- [ ] Wait 1-2 minutes for deployment
- [ ] Visit: `https://yourusername.github.io/Churn_Prediction`
- [ ] (Optional) Deploy backend to Railway/Heroku
- [ ] (Optional) Update API endpoint in frontend

---

**Last Updated**: January 2026  
**Status**: ✅ Ready for GitHub Pages
