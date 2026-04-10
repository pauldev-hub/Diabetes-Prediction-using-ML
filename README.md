<div align="center">

# 🏥 Diabetes Prediction Application

**AI-Powered Diabetes Risk Assessment Platform**

[![React](https://img.shields.io/badge/React-19.1.1-%23087EA4?style=flat-square&logo=react)](https://react.dev/)
[![Vite](https://img.shields.io/badge/Vite-7.1.2-%23646CFF?style=flat-square&logo=vite)](https://vitejs.dev/)
[![Node.js](https://img.shields.io/badge/Node.js-18+-339933?style=flat-square&logo=node.js)](https://nodejs.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)]()
[![Deployed](https://img.shields.io/badge/Deployed-Vercel-000000?style=flat-square&logo=vercel)](https://vercel.com/)

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
- [Project Structure](#-project-structure)
- [Available Scripts](#-available-scripts)
- [Routes & Pages](#-routes--pages)
- [Usage Guide](#-usage-guide)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

The Diabetes Prediction Application is a web-based platform designed to help users assess their diabetes risk through an intelligent prediction model. The application provides a seamless, secure, and user-friendly interface for health risk assessment with optional API integration and local ONNX runtime inference.

**Key Highlights:**
- ⚡ Lightning-fast predictions with Vite + React
- 🔒 Secure client-side authentication with localStorage
- 🧠 ONNX runtime support for edge-based ML inference
- 📱 Fully responsive design for all devices
- 🎨 Clean and intuitive user interface
- 🚀 Deployed on Vercel with automatic deployments

---

## ✨ Features

| Feature | Description | Status |
|---------|-------------|--------|
| **User Authentication** | Secure login and session management | ✅ Implemented |
| **Health Risk Prediction** | AI-powered diabetes risk assessment | ✅ Implemented |
| **ONNX Runtime Support** | Local machine learning inference | ✅ Available |
| **API Integration** | Remote prediction via REST API | ✅ Configured |
| **Protected Routes** | Secure navigation with auth guards | ✅ Implemented |
| **Responsive Design** | Mobile, tablet, and desktop support | ✅ Implemented |
| **Real-time Feedback** | Instant prediction results | ✅ Implemented |
| **Professional UI** | Modern and intuitive interface | ✅ Implemented |

---

## 🛠️ Tech Stack

| Category | Technology | Version | Purpose |
|----------|------------|---------|---------|
| **Frontend Framework** | React | 19.1.1 | UI library |
| **Build Tool** | Vite | 7.1.2 | Fast bundler & dev server |
| **Routing** | React Router DOM | 7.8.2 | Client-side routing |
| **ML Runtime** | ONNX Runtime Web | 1.14.0 | ML inference engine |
| **Styling** | CSS3 | Latest | Responsive design |
| **Linting** | ESLint | 9.33.0 | Code quality |
| **Node.js** | Node | 18+ | Runtime environment |
| **Deployment** | Vercel | - | Production hosting |

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed on your system:

| Tool | Version | Download |
|------|---------|----------|
| **Node.js** | 18.0.0 or higher | [nodejs.org](https://nodejs.org/) |
| **npm** | 9.0.0 or higher | Included with Node.js |
| **Git** | Latest | [git-scm.com](https://git-scm.com/) |
| **Modern Browser** | Chrome/Firefox/Safari/Edge | Any modern browser |

---

## 🚀 Installation

Follow these steps to set up the project locally:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/diabetes-frontend.git
cd Diabetes_Frontend-main
```

### 2️⃣ Install Dependencies

```bash
npm install
```

This will install all required packages:
- React and React DOM
- React Router for navigation
- ONNX Runtime for ML inference
- ESLint for code quality
- Vite as the build tool

### 3️⃣ Environment Setup (Optional)

If you need to configure API endpoints, create a `.env` file:

```env
VITE_API_URL=https://diabetes-k80q.onrender.com
VITE_PORT=5173
```

### 4️⃣ Start Development Server

```bash
npm run dev
```

The application will start at `http://localhost:5173`

---

## 📁 Project Structure

```
Diabetes_Frontend-main/
│
├── public/                          # Static assets
│   ├── diabetes_model.onnx         # ONNX ML model
│   └── ort/                        # ONNX Runtime files
│
├── src/                            # Source code
│   ├── components/                 # Reusable components
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
│   ├── main.jsx                    # Entry point
│   └── index.css                   # Global styles
│
├── eslint.config.js               # ESLint configuration
├── vite.config.js                 # Vite configuration
├── vercel.json                    # Vercel deployment config
├── package.json                   # Dependencies & scripts
└── index.html                     # HTML template
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

### Deploy to Vercel

This project is configured for Vercel deployment:

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
```

### Vercel Configuration

The `vercel.json` file is already configured with:
- SPA routing (all routes redirect to index.html)
- Proper caching headers
- Environment variables support

**Production URL**: Your deployed app URL (configured in Vercel dashboard)

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

| Issue | Solution |
|-------|----------|
| **Port 5173 already in use** | Change port: `npm run dev -- --port 3000` |
| **Dependencies not installing** | Clear cache: `npm cache clean --force && npm install` |
| **CORS errors** | Ensure API endpoint is configured correctly |
| **localStorage not working** | Clear browser cache and cookies |
| **ONNX model not loading** | Check `public/diabetes_model.onnx` exists |

---

## 📚 Additional Resources

- [React Documentation](https://react.dev/)
- [Vite Documentation](https://vitejs.dev/)
- [React Router Guide](https://reactrouter.com/)
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-web/)
- [MDN Web Docs](https://developer.mozilla.org/)

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
