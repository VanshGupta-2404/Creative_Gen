# 🎨 CreativeGen Studio

AI-powered creative builder for retail media using FastAPI, React, and Generative AI.

## 🚀 Features
- AI background removal (Segment Anything)
- FastAPI backend
- React + Vite frontend
- Real-time image preview
- Modular AI pipeline (extensible)

## 🧠 Tech Stack
- FastAPI
- React (Vite)
- Segment Anything (SAM)
- OpenCV
- PyTorch

## 📂 Project Structure
creativegen-studio/
├── backend/
├── creativegen-frontend/


## ⚙️ Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

🎨 Frontend Setup
cd creativegen-frontend
npm install
npm run dev

📦 Model Download (Required)

Download SAM model manually:

sam_vit_h_4b8939.pth


Place it here:

backend/models/

🏆 Use Case

Designed for small & mid-sized advertisers to quickly generate retailer-compliant creatives.