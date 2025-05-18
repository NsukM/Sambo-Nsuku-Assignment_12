Here is your complete and final README.md:

⸻


# Assignment 12, 13 & 14 – Fitness Tracker: API, CI/CD & Open-Source Collaboration

This repository contains the complete implementation of the Fitness Tracker system:

- Assignment 12: Service Layer & RESTful API using FastAPI  
- Assignment 13: CI/CD pipeline with GitHub Actions & branch protection  
- Assignment 14: Open-source collaboration readiness, peer review, and onboarding support

---

## ✅ Architecture Overview

- `services/` – Business logic services interacting with repositories  
- `api/` – RESTful API layer using FastAPI  
- `main.py` – FastAPI entry point  
- `tests/` – Unit and integration tests using `pytest`  
- `docs/` – Swagger UI notes, OpenAPI placeholder, screenshots  
- `.github/workflows/` – GitHub Actions CI/CD pipeline  
- `CONTRIBUTING.md` – How new developers can contribute  
- `ROADMAP.md` – Future features and direction  
- `PROTECTION.md` – Branch protection policy  
- `LICENSE` – MIT license for open collaboration  

---

## ✅ How to Run the API

```bash
pip install fastapi uvicorn
uvicorn main:app --reload

Visit Swagger UI:
http://localhost:8000/docs

⸻

✅ Endpoints Summary

User Endpoints
	•	GET /api/users
	•	POST /api/users
	•	GET /api/users/{user_id}
	•	PUT /api/users/{user_id}
	•	DELETE /api/users/{user_id}

Fitness Profile Endpoints
	•	GET /api/profiles
	•	POST /api/profiles
	•	GET /api/profiles/{age}
	•	DELETE /api/profiles/{age}

Analytics
	•	GET /api/reports/summary

⸻

✅ Running Tests Locally

pip install pytest
pytest tests/


⸻

✅ Swagger Documentation

Due to GitHub’s browser-based environment (without a Python runtime),
FastAPI’s Swagger UI (http://localhost:8000/docs) could not be launched here.

However, the main.py file includes all routers from:
	•	/api/user_api.py
	•	/api/fitness_profile_api.py
	•	/api/analytics_api.py

Swagger will auto-generate documentation if the app is run locally.

⸻

✅ CI/CD Pipeline – Assignment 13

Continuous Integration (CI)
	•	Triggered on every push and pull request to main
	•	Runs all tests using pytest
	•	Blocks PR if any test fails

Continuous Delivery (CD)
	•	On successful merge to main, GitHub:
	•	Compresses the project into fitness-tracker.zip
	•	Uploads it as an artifact in the Actions tab

Branch Protection Rules
	•	Pull request reviews required
	•	Status checks (CI tests) must pass
	•	Direct pushes to main are blocked
	•	See PROTECTION.md for full policy

⸻

✅ Features Available for Contribution

Feature	Status	Label
BMI calculator	To Do	good-first-issue
Export reports to CSV	To Do	feature-request
Nutrition API integration	To Do	feature-request
Add Swagger examples	To Do	good-first-issue
Improve test coverage	In Progress	good-first-issue


⸻

✅ Getting Started

git clone https://github.com/NsukM/Sambo-Nsuku-Assignment_12.git
cd Sambo-Nsuku-Assignment_12
pip install -r requirements.txt
uvicorn main:app --reload


⸻

✅ Author
	•	Name: Nsuku Sambo
	•	Student Number: 221358986
	•	Module: Software Engineering
