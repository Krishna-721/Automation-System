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
- **Planned** — Docker, AWS EC2

## Status
- [x] FastAPI backend initialized
- [x] PostgreSQL connected — async engine, Base, session management
- [x] Database models and schemas defined
- [x] Full CRUD — POST, GET, PUT, DELETE /applications
- [x] Email ingestion endpoint — POST /emails/process
- [x] Analytics endpoint — GET /analytics/summary
- [x] ML classifier — TF-IDF + Logistic Regression trained and wired in
- [x] Pagination and status filtering on GET /applications/
- [x] Confidence score on ML predictions
- [x] Gmail OAuth 2.0 — connect your inbox via /auth/gmail/login
- [x] Gmail sync — pull and classify emails via /gmail/sync
- [x] Spam filter — job alerts and newsletters filtered before classification
- [x] 8/8 tests passing with isolated test database

## WIP
- [ ] Expand training data — model currently at 44 samples, needs 150-200
- [ ] NER — extract company and role from email body
- [ ] Docker setup
- [ ] AWS deployment

## Current Trade-offs
The ML model is trained on 44 samples - a mix of real and synthetic
labeled job emails. This is enough to demonstrate the pipeline but
not production-ready. Known limitations:

- Emails contain HTML tags, reply chains, signatures, and boilerplate
  footers that add noise to the classifier
- company and role fields are not yet extracted — NER planned
- Metrics are based on a small test set and are not statistically reliable

## How It Will Improve
Every email synced via Gmail becomes new training data.
As labeled emails accumulate the model will be retrained automatically.
Target upgrade path: TF-IDF → fine-tuned DistilBERT at 500+ samples.

## Setup
```bash
git clone https://github.com/Krishna-721/tracker.git
cd tracker/backend
pip install -r requirements.txt
cp .env.example .env   # fill in your PostgreSQL URL and Google OAuth credentials
python ml/train.py     # train the model
uvicorn app.main:app --reload
```

Visit `http://localhost:8000/docs` for the full API.

### Connect Gmail
1. Visit `http://localhost:8000/auth/gmail/login`
2. Authenticate with your Google account
3. Sync your inbox via `GET /gmail/sync?user_id=your@email.com`

---

> Gmail OAuth is live. Connect via GET /auth/gmail/login then sync via GET /gmail/sync?user_id=your@email.com