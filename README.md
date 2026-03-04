# Tracker

## What It Does
Reduces the hassle of filtering job-related emails from your inbox.
Connects to Gmail, pulls your job emails, classifies them using ML,
and gives you a unified platform to track every application —
interviews, rejections, offers, and confirmations — in one place.

## The Problem It Solves
The previous version (Apply-Log) used keyword rules to classify emails.
Words like "congratulations" or "opportunity" appeared in both real job
emails and spam — so the system constantly misclassified them.

This version replaces keyword rules with a TF-IDF + Logistic Regression
classifier that reads full email context, not just word presence.

## Tech Stack
- **Backend** — Python, FastAPI, PostgreSQL (async SQLAlchemy)
- **ML** — TF-IDF + Logistic Regression (scikit-learn)
- **Testing** — pytest, httpx, NullPool isolation
- **Planned** — Gmail API, OAuth 2.0, Docker, AWS EC2

## Status
- [x] FastAPI backend initialized
- [x] PostgreSQL connected — async engine, Base, session management
- [x] Database models and schemas defined
- [x] Full CRUD — POST, GET, PUT, DELETE /applications
- [x] Email ingestion endpoint — POST /emails/process
- [x] Analytics endpoint — GET /analytics/summary
- [x] ML classifier — TF-IDF + Logistic Regression trained and wired in
- [x] 8/8 tests passing with isolated test database
 ## WIP
- [ ] HTML preprocessing — strip tags before classification
- [ ] NER — extract company and role from email body
- [ ] Pagination and status filtering on GET /applications/
- [ ] Gmail API + OAuth integration
- [ ] Docker setup
- [ ] AWS deployment

## Current Trade-offs
The ML model is trained on 44 samples - a mix of real and synthetic
labeled job emails. This is enough to demonstrate the pipeline but
not production-ready. Known limitations:

- Emails contain HTML tags, reply chains, signatures, and boilerplate
  footers that add noise to the classifier
- No confidence score stored yet
- company and role fields are extracted as "pending" — NER planned
- Metrics (89% accuracy) are based on 9 test samples and are not
  statistically reliable

## How It Will Improve
Every email synced via Gmail (wip) - becomes new training data.
As labeled emails accumulate the model will be retrained automatically.
Target upgrade path: TF-IDF → fine-tuned DistilBERT at 500+ samples.

## Setup
```bash
git clone https://github.com/Krishna-721/tracker.git
cd tracker/backend
pip install -r requirements.txt
cp .env.example .env   # fill in your PostgreSQL URL
python ml/train.py     # train the model
uvicorn app.main:app --reload
```

Visit `http://localhost:8000/docs` for the full API.

---

> Gmail integration and full automation coming soon!
> Currently accepting manual email input via POST /emails/process.
