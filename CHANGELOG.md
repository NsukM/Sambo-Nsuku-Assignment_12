

# CHANGELOG – Assignment 12, 13 & 14

## [v4.0.0] – Assignment 14: Open-Source Collaboration and Peer Review

### Added
- CONTRIBUTING.md with setup, coding standards, and contribution guidelines
- ROADMAP.md outlining future enhancements
- LICENSE (MIT) for open collaboration
- VOTING_RESULTS.md summarizing GitHub engagement and peer feedback
- REFLECTION.md with personal reflection on open-source collaboration
- GitHub issues labeled as good-first-issue and feature-request
- New section in README.md: Features Available for Contribution

---

## [v3.0.0] – Assignment 13: CI/CD and Branch Protection

### Added
- .github/workflows/ci.yml for CI/CD pipeline
- Automated pytest test execution on push and pull requests
- Artifact generation (fitness-tracker.zip) on successful merge to main
- Branch protection policy documented in PROTECTION.md
- README.md updated with CI/CD process and protection details

---

## [v2.0.0] – Assignment 12: Full Service Layer & REST API

### Added
- services/ layer for user, profile, and analytics logic
- api/ endpoints implemented with FastAPI
- main.py application entry point connecting all routers
- Unit and integration tests in tests/services/ and tests/api/
- Swagger UI auto-generated at /docs
- README.md with API usage and instructions

### Future Enhancements
- Token-based authentication
- Deployment on AWS (Lambda, API Gateway)
