# Diabetes Prediction - Full Stack Setup

This project contains both frontend (React + Vite) and backend (Flask ML API).

## Project Structure
```
Diabetes_Frontend-main/
├── src/                  # React frontend
├── backend/             # Flask backend with ML model
├── public/              # Static assets
└── package.json         # Frontend dependencies
```

## Prerequisites
- Node.js 18+ (for frontend)
- Python 3.8+ (for backend)
- pip (Python package manager)

## Installation

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
```

### Frontend Setup
```bash
npm install
```

## Running the Application

### Option 1: Full Stack (Recommended for Development)
Run backend and frontend together in separate terminals:

**Terminal 1 - Backend:**
```bash
cd backend
python app.py
```
Backend will run on `http://localhost:5000`

**Terminal 2 - Frontend:**
```bash
npm run dev
```
Frontend will run on `http://localhost:5173`

### Option 2: Frontend Only (Uses Remote API)
```bash
npm run dev
```
Frontend connects to `https://diabetes-k80q.onrender.com` (hosted backend)

## API Endpoints

### Backend (Flask)
- `GET /` - Health check
- `POST /predict` - Make diabetes prediction

**Request Body:**
```json
{
  "pregnancies": 0,
  "glucose": 120,
  "bloodPressure": 80,
  "skinThickness": 20,
  "insulin": 100,
  "bmi": 25.5,
  "dpf": 0.5,
  "age": 30
}
```

**Response:**
```json
{
  "prediction": 1,
  "probability": 85.5
}
```

## Login Credentials (for testing)
- Username: `test` / Password: `test`
- Username: `admin` / Password: `admin123`
- Username: `john` / Password: `john123`

## Environment Variables

### Frontend
- `VITE_API_URL` - Backend API URL (`.env.local` for dev, `.env.production` for prod)

### Backend
- Set in `app.py` - uses default `localhost:5000` for development

## Tech Stack

**Frontend:**
- React 19
- Vite 7
- React Router 7
- CSS (custom styling)

**Backend:**
- Flask 3.1
- scikit-learn 1.6 (ML model)
- joblib (model persistence)
- CORS (cross-origin requests)
- Gunicorn (production server)

## Deployment

### Frontend
Deploy to Vercel/Netlify - uses remote backend by default

### Backend
The backend is deployed on Render.com at `https://diabetes-k80q.onrender.com`

## Notes
- The ML model (`diabetes_model.pkl`) is pretrained and loaded on backend startup
- Frontend uses localStorage for authentication (client-side only)
- Disable CORS restriction when deploying to different domains
- For production, use environment variables for API URL configuration
