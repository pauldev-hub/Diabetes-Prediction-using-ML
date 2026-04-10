# Quick Start - Full Stack Development

## Run In 2 Terminal Windows

### Terminal 1: Backend (Python Flask API)
```bash
cd backend
python app.py
```
✅ **Backend running on:** `http://localhost:5000`

### Terminal 2: Frontend (React + Vite)
```bash
npm run dev:local
```
✅ **Frontend running on:** `http://localhost:5173`

## Test the Application

1. Open http://localhost:5173 in browser
2. Click "Get Started" → Login with credentials:
   - Username: `test`
   - Password: `test`
3. Fill in health metrics and click "Predict Probability"
4. See prediction results powered by local ML backend

## Architecture

```
Frontend (React)          Backend (Flask)
│                         │
├─ Login.jsx             ├─ app.py (ML API)
├─ Prediction.jsx        ├─ diabetes_model.pkl
├─ Navbar.jsx            └─ requirements.txt
└─ pages/


Workflow:
User Input → React Form → POST to http://localhost:5000/predict → 
ML Model Prediction → JSON Response → Display Result
```

## Backend API Reference

**POST /predict**
```json
// Request
{
  "pregnancies": 1,
  "glucose": 150,
  "bloodPressure": 80,
  "skinThickness": 30,
  "insulin": 100,
  "bmi": 25.5,
  "dpf": 0.5,
  "age": 40
}

// Response  
{
  "prediction": 1,           // 0 = No Diabetes, 1 = Diabetes
  "probability": 85.42       // Confidence percentage
}
```

## Deploy

**Frontend:** `npm run build` then deploy `dist/` to Vercel/Netlify
**Backend:** Already deployed at https://diabetes-k80q.onrender.com (production uses this)
