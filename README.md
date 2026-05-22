# 🚦 VisionGuard AI

**Real-time Smart Traffic Enforcement Platform**

> Detects vehicles, illegal window tint, licence plates, and verifies vehicle registration — all on a standard laptop with no dedicated GPU.

---

## 📋 Project Overview

VisionGuard AI is a modular, production-style Python/Flask web application that performs real-time AI-powered traffic enforcement using a connected camera feed.

| Feature | Technology |
|---|---|
| Object detection | YOLOv8 Nano (lightest model) |
| Licence plate OCR | PaddleOCR |
| Tint analysis | OpenCV brightness analysis |
| Web dashboard | Flask + Chart.js |
| Database | SQLite |
| Hardware target | Ryzen 3 CPU / 8 GB RAM / no GPU |

---

## 🗂 Project Structure

```
VisionGuardAI/
│
├── app.py                      # Flask application entry point
│
├── config/
│   └── settings.py             # All configuration (reads .env)
│
├── backend/
│   ├── detection/
│   │   ├── vehicle_detector.py # YOLOv8 vehicle detection (Phase 2)
│   │   ├── tint_detector.py    # Window tint analysis (Phase 2)
│   │   └── plate_reader.py     # PaddleOCR plate reading (Phase 3)
│   │
│   ├── database/
│   │   └── db.py               # SQLite init + query helpers
│   │
│   ├── routes/
│   │   ├── dashboard.py        # HTML page routes
│   │   ├── detection.py        # Camera + detection routes
│   │   └── api.py              # JSON REST API endpoints
│   │
│   └── utils/
│       ├── logger.py           # Coloured + rotating file logger
│       └── helpers.py          # Shared utility functions
│
├── frontend/
│   ├── templates/
│   │   ├── base.html           # Master template (navbar, footer)
│   │   ├── dashboard.html      # Live monitoring dashboard
│   │   ├── detections.html     # Detection history page
│   │   ├── alerts.html         # Alerts management page
│   │   └── settings.html       # System settings page
│   │
│   └── static/
│       ├── css/main.css        # Dark futuristic AI theme
│       ├── js/main.js          # Global utilities (clock, polling)
│       ├── js/dashboard.js     # Dashboard charts + data refresh
│       ├── img/                # Images
│       └── icons/              # Icons
│
├── data/
│   ├── db/                     # SQLite database files
│   ├── logs/                   # Rotating application logs
│   ├── screenshots/            # Captured violation frames
│   └── models/                 # YOLO .pt model files
│
├── tests/                      # Unit and integration tests
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## 🚀 How to Run (Phase 1)

### Step 1 — Clone the repository

```bash
git clone https://github.com/your-username/VisionGuardAI.git
cd VisionGuardAI
```

### Step 2 — Create a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Configure environment

```bash
cp .env.example .env
# Edit .env if needed (defaults work out of the box)
```

### Step 5 — Run the server

```bash
python app.py
```

### Step 6 — Open the dashboard

Open your browser and go to:
```
http://127.0.0.1:5000
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Main dashboard |
| GET | `/detections` | Detection history page |
| GET | `/alerts` | Alerts page |
| GET | `/settings` | Settings page |
| GET | `/api/stats` | JSON: summary statistics |
| GET | `/api/detections` | JSON: paginated detections |
| GET | `/api/alerts` | JSON: active alerts |
| POST | `/api/alerts/<id>/resolve` | Resolve an alert |
| GET | `/api/status` | JSON: system component status |
| GET | `/api/health` | JSON: server health check |
| POST | `/detections/start` | Start detection engine |
| POST | `/detections/stop` | Stop detection engine |
| GET | `/detections/stream` | MJPEG camera stream |

---

## 🗺 Development Phases

| Phase | Focus | Status |
|---|---|---|
| **1** | Project structure + architecture | ✅ Complete |
| **2** | OpenCV camera + YOLOv8 vehicle detection | 🔜 Next |
| **3** | Tint analysis + PaddleOCR plate reading | 🔜 Planned |
| **4** | Registration verification + alerts | 🔜 Planned |
| **5** | Performance optimisation + deployment | 🔜 Planned |

---

## ⚙ Hardware Requirements

- **CPU**: AMD Ryzen 3 or equivalent (Intel i3+)
- **RAM**: 8 GB minimum
- **GPU**: Not required (CPU inference only)
- **Camera**: USB webcam or built-in camera
- **OS**: Windows 10/11, Ubuntu 20.04+, macOS

---

## 📄 Licence

MIT Licence — see `LICENSE` for details.
