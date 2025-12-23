# 🏃 Human Pose Estimator App

A full-stack AI application that detects human pose landmarks in real-time using **FastAPI**, **Streamlit**, and **MediaPipe**. The application is containerized with **Docker** for easy deployment.

## 🚀 Features

* **Lightweight Model:** Uses Google's MediaPipe Pose model (optimized for CPU).
* **Dual Input Support:** Accepts both uploaded images and real-time webcam capture.
* **Microservices Architecture:**
    * **Backend:** FastAPI server handling image processing and inference.
    * **Frontend:** Streamlit UI for easy user interaction.
* **Dockerized:** Fully containerized setup with Docker Compose.

## 🛠️ Tech Stack

* **Language:** Python 3.9
* **Frontend:** Streamlit
* **Backend:** FastAPI, Uvicorn
* **Computer Vision:** MediaPipe, OpenCV, NumPy
* **DevOps:** Docker, Docker Compose

---

## 📂 Project Structure

```text
Human_Pose_Estimator_app/
├── docker-compose.yml       # Orchestration file
├── backend/                 # API Service
│   ├── Dockerfile
│   ├── main.py              # FastAPI application
│   └── requirements.txt     # Backend dependencies
└── frontend/                # UI Service
    ├── Dockerfile
    ├── app.py               # Streamlit application
    └── requirements.txt     # Frontend dependencies

```

---

## 🏁 Getting Started

### Prerequisites

* [Docker](https://www.docker.com/) and Docker Compose installed on your machine.

### Installation & Running

1. **Clone the repository:**
```bash
git clone https://github.com/Ankit-Navrang-Meshram/Human_Pose_Estimator_app.git
cd Human_Pose_Estimator_app

```


2. **Build and run the containers:**
```bash
docker compose up --build

```


3. **Access the Application:**
* **Frontend (Streamlit):** Open [http://localhost:8501](https://www.google.com/search?q=http://localhost:8501) in your browser.
* **Backend Docs (Swagger UI):** Open [http://localhost:8000/docs](https://www.google.com/search?q=http://localhost:8000/docs) to test the API directly.


4. **Stop the application:**
Press `Ctrl+C` in the terminal or run:
```bash
docker compose down

```



---

## ⚙️ Local Development (Without Docker)

If you wish to run the services locally without Docker, you must install the specific versions of dependencies to avoid protocol buffer conflicts.

**1. Backend Setup:**

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

```

*Note: We use `mediapipe==0.9.0.1` and `protobuf==3.20.3` to ensure compatibility.*

**2. Frontend Setup:**

```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py

```

---

## 🖼️ How It Works

1. **Upload:** The user uploads an image or uses the camera via the Streamlit interface.
2. **Request:** The image is converted to bytes and sent to the FastAPI backend via a POST request.
3. **Processing:** * FastAPI receives the image.
* MediaPipe processes the image to find 33 pose landmarks.
* OpenCV draws the skeleton connections on the image.


4. **Response:** The processed image is sent back to the frontend and displayed to the user.
