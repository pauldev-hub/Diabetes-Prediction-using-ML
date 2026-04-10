<div align="center">

# 🏥 Diabetes Prediction Application

**AI-Powered Diabetes Risk Assessment Platform with Full Stack Architecture**

[![React](https://img.shields.io/badge/React-19.1.1-%23087EA4?style=flat-square&logo=react)](https://react.dev/)
[![Vite](https://img.shields.io/badge/Vite-7.1.2-%23646CFF?style=flat-square&logo=vite)](https://vitejs.dev/)
[![Node.js](https://img.shields.io/badge/Node.js-18+-339933?style=flat-square&logo=node.js)](https://nodejs.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-%23000000?style=flat-square&logo=flask)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776ab?style=flat-square&logo=python)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0.0+-F7931E?style=flat-square&logo=scikit-learn)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)]()
[![Frontend Deployed](https://img.shields.io/badge/Frontend-Vercel-000000?style=flat-square&logo=vercel)](https://vercel.com/)
[![Backend Deployed](https://img.shields.io/badge/Backend-Render-46E3B7?style=flat-square&logo=render)](https://render.com/)

---

> A modern, responsive web application for predicting diabetes risk using machine learning. Built with React, Vite, and ONNX runtime for edge-based predictions.

[Live Demo](#-live-deployment) • [Features](#-features) • [Quick Start](#-quick-start) • [Documentation](#-documentation)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
  - [Frontend Setup](#frontend-setup)
  - [Backend Setup](#backend-setup)
- [Project Structure](#-project-structure)
- [Available Scripts](#-available-scripts)
- [Routes & Pages](#-routes--pages)
- [API Documentation](#-api-documentation)
- [Usage Guide](#-usage-guide)
- [Deployment](#-deployment)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

The Diabetes Prediction Application is a comprehensive full-stack web platform designed to help users assess their diabetes risk through intelligent machine learning models. It features a modern React frontend and a robust Flask backend API, providing a seamless, secure, and user-friendly interface for health risk assessment.

**Architecture:**
- **Frontend**: React + Vite SPA deployed on Vercel
- **Backend**: Flask API with scikit-learn ML model deployed on Render
- **Database**: Trained ML model (diabetes_model.pkl) with scikit-learn

**Key Highlights:**
- ⚡ Lightning-fast predictions with Vite + React frontend
- 🔒 Secure client-side authentication with localStorage
- 🧠 scikit-learn powered ML model for diabetes prediction
- 🌐 RESTful API with CORS support for cross-origin requests
- 📱 Fully responsive design for all devices
- 🎨 Clean and intuitive user interface
- 🚀 Full-stack deployment on Vercel (frontend) & Render (backend)
- 📊 Probability-based predictions with accuracy metrics

---

## ✨ Features

| Feature | Description | Status |
|---------|-------------|--------|
| **User Authentication** | Secure login and session management | ✅ Implemented |
| **ML-Based Prediction** | scikit-learn powered diabetes risk assessment | ✅ Implemented |
| **Probability Analysis** | Risk percentage calculation and insights | ✅ Implemented |
| **RESTful API** | Flask backend with comprehensive error handling | ✅ Implemented |
| **CORS Support** | Cross-origin requests for seamless integration | ✅ Implemented |
| **Protected Routes** | Secure navigation with authentication guards | ✅ Implemented |
| **Responsive Design** | Mobile, tablet, and desktop support | ✅ Implemented |
| **Real-time Feedback** | Instant prediction results with probability | ✅ Implemented |
| **Professional UI** | Modern and intuitive interface | ✅ Implemented |
| **Model Persistence** | Joblib serialized ML model with prediction | ✅ Implemented |

---

## 🛠️ Tech Stack

### Frontend

| Category | Technology | Version | Purpose |
|----------|------------|---------|---------|
| **Frontend Framework** | React | 19.1.1 | UI library |
| **Build Tool** | Vite | 7.1.2 | Fast bundler & dev server |
| **Routing** | React Router DOM | 7.8.2 | Client-side routing |
| **ML Runtime** | ONNX Runtime Web | 1.14.0 | Optional edge ML inference |
| **Styling** | CSS3 | Latest | Responsive design |
| **Linting** | ESLint | 9.33.0 | Code quality |
| **Node.js** | Node | 18+ | Runtime environment |
| **Deployment** | Vercel | Latest | Production hosting |

### Backend

| Category | Technology | Version | Purpose |
|----------|------------|---------|---------|
| **Framework** | Flask | 3.0.0+ | Web framework |
| **CORS** | flask-cors | 3.0.0+ | Cross-origin requests |
| **ML Library** | scikit-learn | 1.0.0+ | Machine learning model |
| **Data Processing** | pandas | 1.3.0+ | Data manipulation |
| **Numerical Computing** | numpy | 1.20.0+ | Array operations |
| **Model Serialization** | joblib | 1.0.0+ | Model persistence |
| **WSGI Server** | Gunicorn | 21.0.0+ | Production server |
| **Language** | Python | 3.9+ | Backend runtime |
| **Deployment** | Render | Latest | Production hosting |

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed on your system:

### Frontend Requirements

| Tool | Version | Download |
|------|---------|----------|
| **Node.js** | 18.0.0 or higher | [nodejs.org](https://nodejs.org/) |
| **npm** | 9.0.0 or higher | Included with Node.js |
| **Modern Browser** | Chrome/Firefox/Safari/Edge | Any modern browser |

### Backend Requirements

| Tool | Version | Download |
|------|---------|----------|
| **Python** | 3.9 or higher | [python.org](https://www.python.org/) |
| **pip** | 21.0 or higher | Included with Python |
| **Virtual Environment** | venv | Built-in with Python |

### Both

| Tool | Version | Download |
|------|---------|----------|
| **Git** | Latest | [git-scm.com](https://git-scm.com/) |

---

## 🚀 Installation

### Frontend Setup

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/diabetes-frontend.git
cd Diabetes_Frontend-main
```

#### 2️⃣ Install Frontend Dependencies

```bash
npm install
```

This will install all required packages:
- React and React DOM
- React Router for navigation
- ONNX Runtime for optional ML inference
- ESLint for code quality
- Vite as the build tool

#### 3️⃣ Setup Frontend Environment (Optional)

Create a `.env` file in the root directory:

```env
VITE_API_URL=https://your-backend-api.com
VITE_PORT=5173
```

#### 4️⃣ Start Frontend Development Server

```bash
npm run dev
```

The frontend will be available at `http://localhost:5173`

---

### Backend Setup

#### 1️⃣ Navigate to Backend Directory

```bash
cd backend
```

#### 2️⃣ Create Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3️⃣ Install Backend Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Flask web framework
- flask-cors for CORS support
- scikit-learn for ML model
- numpy and pandas for data processing
- joblib for model loading
- gunicorn for production server

#### 4️⃣ Verify Model File

Ensure `diabetes_model.pkl` exists in the `backend/` directory. This is the trained ML model.

#### 5️⃣ Start Backend Development Server

```bash
python app.py
```

The backend API will be available at `http://localhost:5000`

---

## 🛠️ Full Setup Script (Optional)

Run this to set up both frontend and backend at once:

**Windows:**
```bash
# Frontend setup
npm install

# Backend setup
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

**macOS/Linux:**
```bash
# Frontend setup
npm install

# Backend setup (in another terminal)
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

---

## 📁 Project Structure

```
Diabetes_Frontend-main/
│
├── public/                          # Static assets
│   ├── diabetes_model.onnx         # Optional ONNX ML model
│   └── ort/                        # ONNX Runtime files
│
├── src/                            # Frontend source code
│   ├── components/                 # Reusable React components
│   │   ├── Footer.jsx              # Footer component
│   │   ├── Navbar.jsx              # Navigation bar
│   │   └── PredictionForm.jsx      # Prediction form
│   │
│   ├── pages/                      # Page components
│   │   ├── Home.jsx                # Home page
│   │   └── Prediction.jsx          # Prediction page
│   │
│   ├── App.jsx                     # Main app component
│   ├── Login.jsx                   # Login page
│   ├── ProtectedRoute.jsx          # Route guard component
│   ├── main.jsx                    # Application entry point
│   └── index.css                   # Global styles
│
├── backend/                        # Backend source code
│   ├── app.py                      # Flask application (main server)
│   ├── diabetes_model.pkl          # Trained scikit-learn model
│   ├── requirements.txt            # Python dependencies
│   ├── Procfile                    # Deployment configuration
│   ├── runtime.txt                 # Python runtime version
│   └── venv/                       # Virtual environment (local development)
│
├── eslint.config.js               # ESLint configuration
├── vite.config.js                 # Vite configuration
├── vercel.json                    # Vercel deployment config (frontend)
├── package.json                   # Node.js dependencies & scripts
├── index.html                     # HTML template
└── README.md                      # Documentation (this file)
```

---

## 🎮 Available Scripts

Run these commands in the project directory:

| Command | Description | Purpose |
|---------|-------------|---------|
| `npm run dev` | Start development server | Local development with HMR |
| `npm run build` | Build for production | Create optimized bundle |
| `npm run lint` | Run ESLint | Check code quality |
| `npm run preview` | Preview production build | Test production build locally |

### Development Workflow

```bash
# Start development with hot reload
npm run dev

# In another terminal, check code quality
npm run lint

# Build for production
npm run build

# Preview the production build
npm run preview
```

---

## 🌐 API Documentation

The backend Flask API provides endpoints for prediction and health checks.

### Base URL

**Development:** `http://localhost:5000`  
**Production:** `https://your-backend-api.com`

### Endpoints

#### 1. Health Check

```http
GET /
```

**Response:**
```json
{
  "message": "Diabetes Prediction API is running!"
}
```

**Status Code:** `200 OK`

---

#### 2. Prediction Endpoint

```http
POST /predict
Content-Type: application/json
```

**Request Body:**
```json
{
  "pregnancies": 6,
  "glucose": 148,
  "bloodPressure": 72,
  "skinThickness": 35,
  "insulin": 0,
  "bmi": 33.6,
  "dpf": 0.627,
  "age": 50
}
```

| Field | Type | Description | Range |
|-------|------|-------------|-------|
| `pregnancies` | int | Number of pregnancies | 0-17 |
| `glucose` | int | Plasma glucose concentration | 0-199 |
| `bloodPressure` | int | Diastolic blood pressure | 0-122 |
| `skinThickness` | int | Triceps skin fold thickness | 0-99 |
| `insulin` | int | 2-hour serum insulin | 0-846 |
| `bmi` | float | Body Mass Index | 0-67.1 |
| `dpf` | float | Diabetes Pedigree Function | 0.078-2.42 |
| `age` | int | Age in years | 21-81 |

**Success Response (200):**
```json
{
  "prediction": 1,
  "probability": 78.45
}
```

| Field | Type | Description |
|-------|------|-------------|
| `prediction` | int | `0` = No Diabetes, `1` = Diabetes Positive |
| `probability` | float | Percentage confidence (0-100) |

**Error Response (400):**
```json
{
  "error": "Error message describing what went wrong"
}
```

---

### Example Usage (JavaScript/Fetch)

```javascript
async function predictDiabetes(features) {
  try {
    const response = await fetch('https://your-api-url/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(features)
    });

    const data = await response.json();
    
    if (response.ok) {
      console.log(`Prediction: ${data.prediction}`);
      console.log(`Probability: ${data.probability}%`);
    } else {
      console.error(`Error: ${data.error}`);
    }
  } catch (error) {
    console.error('Request failed:', error);
  }
}

// Usage
const features = {
  pregnancies: 6,
  glucose: 148,
  bloodPressure: 72,
  skinThickness: 35,
  insulin: 0,
  bmi: 33.6,
  dpf: 0.627,
  age: 50
};

predictDiabetes(features);
```

---

### CORS Configuration

The backend has CORS enabled for all origins in development. For production, configure allowed origins in `app.py`:

```python
CORS(app, resources={r"/predict": {"origins": ["https://your-frontend-url.com"]}})
```

---

## 🗺️ Routes & Pages

| Route | Component | Access | Purpose |
|-------|-----------|--------|---------|
| `/` | Home | Public | Landing page & app overview |
| `/login` | Login | Public | User authentication |
| `/predict` | Prediction | Protected | Diabetes risk prediction form |

### Route Protection

- **Home Page**: Accessible to all users
- **Login Page**: Accessible to all users (redirects if already logged in)
- **Prediction Page**: Protected by `ProtectedRoute` - requires authentication
- **Authentication**: Client-side via localStorage (`isLoggedIn`, `username`)

---

## 📖 Usage Guide

### 1. **Home Page**
- Overview of the application
- Information about diabetes prediction
- Call-to-action buttons for login/prediction

### 2. **Login Page**
- Simple authentication form
- Input: Username
- Stores credentials in localStorage
- Redirects to prediction page on success

### 3. **Prediction Page**
- Accessible only when authenticated
- Input health parameters (age, BMI, glucose, etc.)
- Real-time prediction results
- Display risk assessment

### 4. **Prediction Form**
The form collects the following health metrics:

```javascript
{
  age: number,
  gender: string,
  bmi: number,
  bloodPressure: number,
  glucose: number,
  insulinLevel: number,
  pregnancies: number,
  skinThickness: number
}
```

### 5. **API Integration**

**Default Behavior**: The app calls the remote API endpoint:

```
POST https://diabetes-k80q.onrender.com/predict
Content-Type: application/json

{
  "feature1": value,
  "feature2": value,
  ...
}
```

**Optional**: Use local ONNX Runtime by enabling the `diabetes_model.onnx` inference in your code.

---

## 🔐 Authentication Flow

```
Login Form → Validate Input → Store in localStorage 
  → Set isLoggedIn=true → Redirect to /predict
```

### Stored Data
```javascript
localStorage.setItem('isLoggedIn', 'true');
localStorage.setItem('username', 'username');
```

### Logout
```javascript
localStorage.removeItem('isLoggedIn');
localStorage.removeItem('username');
```

---

## 🌐 Deployment

### Frontend Deployment (Vercel)

This project is configured for Vercel deployment:

#### 1. Deploy with Vercel CLI

```bash
# Install Vercel CLI (if not already installed)
npm i -g vercel

# Deploy from root directory
vercel
```

#### 2. Deploy via GitHub

1. Push to GitHub: `git push origin main`
2. Connect GitHub repo to Vercel dashboard
3. Vercel will auto-deploy on every push

#### Vercel Configuration

The `vercel.json` file is already configured with:
- SPA routing (all routes redirect to index.html)
- Proper caching headers
- Environment variables support

**Production URL**: `https://your-app.vercel.app` (configured in Vercel dashboard)

---

### Backend Deployment (Render/Heroku)

Deploy the Flask backend to production using Render or Heroku.

#### Render Deployment

1. **Create Render Account**: Visit [render.com](https://render.com/)

2. **Push Backend to GitHub** (if not already):
   ```bash
   git add backend/
   git commit -m "Add backend code"
   git push origin main
   ```

3. **Connect Repository**:
   - Create new Web Service
   - Connect your GitHub repo
   - Select root directory: `backend/`

4. **Configure Environment**:
   - Runtime: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

5. **Deploy**: Click "Create Web Service"

**Production URL**: `https://your-backend-api.onrender.com`

#### Heroku Deployment (Alternative)

```bash
# Install Heroku CLI
# Visit: https://devcenter.heroku.com/articles/heroku-cli

# Login to Heroku
heroku login

# Create new Heroku app
heroku create your-app-name

# Set buildpack
heroku buildpacks:set heroku/python

# Deploy
git push heroku main
```

---

### Environment Variables

#### Frontend (.env)
```env
VITE_API_URL=https://your-backend-api.onrender.com
VITE_PORT=5173
```

#### Backend (Render/Heroku)
Set in deployment dashboard:
```
FLASK_ENV=production
```

---

## 🔧 Configuration

### Vite Configuration (`vite.config.js`)

Default Vite setup with React Fast Refresh enabled.

### ESLint Configuration (`eslint.config.js`)

Code quality rules enforce:
- React best practices
- Proper hook usage
- Code consistency

### Environment Variables

Create `.env` file for custom configuration:

```env
VITE_API_URL=https://your-api-endpoint.com
VITE_MODEL_PATH=/diabetes_model.onnx
```

---

## 🤝 Contributing

We welcome contributions! Here's how to help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines

- Follow ESLint rules: `npm run lint`
- Keep components small and focused
- Use meaningful commit messages
- Add comments for complex logic
- Test your changes locally

---

## 📝 Code Quality

Run linting to ensure code quality:

```bash
npm run lint
```

Fix linting issues automatically:

```bash
npm run lint -- --fix
```

---

## 🐛 Troubleshooting

### Frontend Issues

| Issue | Solution |
|-------|----------|
| **Port 5173 already in use** | Change port: `npm run dev -- --port 3000` |
| **Dependencies not installing** | Clear cache: `npm cache clean --force && npm install` |
| **CORS errors** | Ensure backend API URL is configured in `.env` |
| **localStorage not working** | Clear browser cache and cookies |
| **ONNX model not loading** | Check `public/diabetes_model.onnx` exists |
| **Blank page after login** | Check browser console for JS errors |
| **API calls failing** | Verify backend is running: `http://localhost:5000` |

### Backend Issues

| Issue | Solution |
|-------|----------|
| **Port 5000 already in use** | Kill process: `lsof -ti:5000 \| xargs kill -9` (Linux/Mac) or use different port |
| **Virtual environment not activating** | Ensure correct path and use full activation command |
| **Module not found errors** | Reinstall dependencies: `pip install -r requirements.txt` |
| **Model file not found** | Ensure `diabetes_model.pkl` exists in `backend/` directory |
| **CORS errors** | Flask-CORS is installed: `pip install flask-cors` |
| **Prediction returns error** | Check input data format matches API specification |
| **Gunicorn not found** | Install: `pip install gunicorn` |
| **Python version conflict** | Use Python 3.9+: `python --version` |

### Full Stack Issues

| Issue | Solution |
|-------|----------|
| **Frontend can't reach backend** | Check backend URL in `.env`, ensure backend is running |
| **Authentication not working** | Check localStorage in browser DevTools Application tab |
| **Deployment failing** | Review deployment logs in Vercel/Render dashboard |
| **Prediction always returns 0** | Verify model file is correctly trained and loaded |

---

## 📚 Additional Resources

### Documentation

- [React Documentation](https://react.dev/)
- [Vite Documentation](https://vitejs.dev/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [scikit-learn Documentation](https://scikit-learn.org/)
- [React Router Guide](https://reactrouter.com/)

### ML & Data Science

- [scikit-learn Diabetes Example](https://scikit-learn.org/stable/datasets/toy_dataset.html#diabetes-dataset)
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-web/)
- [Machine Learning Basics](https://developers.google.com/machine-learning/guides)

### Deployment

- [Vercel Documentation](https://vercel.com/docs)
- [Render Documentation](https://render.com/docs)
- [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python)

### General

- [MDN Web Docs](https://developer.mozilla.org/)
- [GitHub Documentation](https://docs.github.com/)

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👥 Support & Contact

For questions, issues, or suggestions:
- Open an [Issue](https://github.com/yourusername/diabetes-frontend/issues)
- Start a [Discussion](https://github.com/yourusername/diabetes-frontend/discussions)
- Email: your-email@example.com

---

<div align="center">

### ⭐ If you found this helpful, please star the repository!

Made with ❤️ for better healthcare through AI

**[↑ Back to top](#-diabetes-prediction-application)**

</div>
