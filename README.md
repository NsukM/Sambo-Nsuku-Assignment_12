# Assignment 12 – Service Layer & API for Fitness Tracker

This repository contains the implementation of a full *Service Layer* and *RESTful API* for the Fitness Tracker project using *FastAPI*. This includes business logic services, API endpoints, Swagger documentation, and test coverage.

---

## ✅ Architecture Overview

- services/: Business logic services interacting with repositories
- api/: RESTful API layer using FastAPI
- main.py: FastAPI entry point
- tests/: Unit and integration tests
- docs/: Swagger screenshot and OpenAPI file

---

## ✅ How to Run the API

bash
pip install fastapi uvicorn
uvicorn main:app --reload

Visit Swagger UI at:
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

✅ Running Tests

pip install pytest
pytest tests/



⸻

✅ Swagger Documentation
	•	Screenshot: docs/swagger_screenshot.png
	•	OpenAPI JSON (if exported): docs/openapi.json

⸻

✅ Author
	•	Name: Nsuku Sambo
	•	Student Number: 221358986
	•	Module: Software Engineering

---
