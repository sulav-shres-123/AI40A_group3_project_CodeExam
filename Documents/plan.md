# CodeExam: Team Plan

> Status: **draft for team review** (22 Nov 2026). Items marked *(to confirm)* need a team decision.
> Sprint dates and story numbers come from our project backlog: the [Google Sheet `CodeExam_Project_Logs`](https://docs.google.com/spreadsheets/d/1tfZ5bA3O4vtW1Jed4QUYUkUNgUzSBHn_/edit?usp=sharing&ouid=114220969951788972793&rtpof=true&sd=true) (master list of user stories).
> **Day-to-day tasks, owners and status are tracked on Trello:** *(Trello board link to be added)*.
> **Roles and responsibilities are not fixed yet.** Section 4 lists the roles we need so the team can assign them.

## 1. Goal

By **13 Dec 2026** (planned final release in the logbook), ship one complete, working path through CodeExam:

> **A teacher creates an exam with tests → a student takes it, runs code and submits → Judge0 grades it with partial credit → the teacher sees the result.**

Everything else in our 67 user stories is planned, but comes after this path works.

## 2. Where we are now

| Item | Status |
| --- | --- |
| Design | Done. See [`docs/DESIGN.md`](docs/DESIGN.md) |
| Proposal | Done. See [`docs/proposal.pdf`](docs/proposal.pdf) |
| Apps to install | Listed in [`docs/requirements/required-apps.txt`](docs/requirements/required-apps.txt) |
| User stories and sprint backlogs | Done in the Google Sheet (67 stories, 143 points) |
| Task tracking | Trello |
| Code | **Not started.** Sprints 1–7 have no recorded progress. |
| Roles | **Not assigned yet** (see section 4) |
| Time left | **3 one-week sprints** (Sprints 8–10) |

Our planned pace is about 14 points per sprint, so about **42 points** fit in the time left. That's why the plan below is a reduced scope.

## 3. Repository structure

```
AI40A_group3_project_CodeExam/
├─ README.md            Start here: what the project is, folder guide, setup
├─ plan.md              This file: goal, roles, sprint plan, rules
├─ backlog/             Project management: links to Trello (tasks) and the Google Sheet (user stories)
├─ docs/                Everything people read
│  ├─ requirements/     required-apps.txt: apps every member must install
│  ├─ proposal.pdf      Final proposal
│  └─ DESIGN.md         Full design plan (the "why")
├─ app/                 Flask application: models, forms, views, api, services, templates, static (code from P04)
├─ worker/              Grading worker, a separate process (US33)
├─ tests/               pytest TDD + BDD tests (filled by task P07)
├─ infra/               docker compose, server and Judge0 setup (P03, P08)
├─ .github/             CI and the pull request template (section 7)
├─ wsgi.py              gunicorn entry point (P04)
├─ .env.example         Settings template: copy to .env
├─ .gitignore           Keeps secrets (.env), virtual envs and junk out of Git
└─ .gitattributes       Same line endings for Windows and Mac users
```

Each folder's `README.md` explains what belongs in it, and [`docs/STRUCTURE.md`](docs/STRUCTURE.md) maps the whole repo. Arriving later:
- `requirements.txt` at the root: the Python packages to install with `pip install -r requirements.txt` (task P04)
- `migrations/`: created by `flask db init` in P05 (it refuses to run if the folder already exists)

## 4. Roles (not assigned yet)

**Team:** Sulav Shrestha · Aashish Shrestha · Prashna Bhukhaju · Dilkash Shekh · Basant Nayak · Ellie Bohora (6 people).

The logbook currently lists Sulav as Scrum Master and the others as Developers 1–5, with work split by layer (backend, frontend design, TDD, frontend integration, BDD). **These are placeholders, not final assignments.** Use the table below to agree real roles, then update the logbook to match.

**"Description"** says whether a written role description already exists:
- ✅ **Available:** described in the named document. Read it before choosing the role.
- 📝 **Needed:** only a name exists so far. The team should write 3–5 lines (what the role owns and delivers) before assigning it.

| # | Role | Responsibilities | Description | Interested | Status |
| --- | --- | --- | --- | --- | --- |
| R1 | **Scrum Master / coordinator** | Runs check-ins and sprint reviews, keeps the Trello board up to date, tracks blockers, talks to the module leader | 📝 Needed (logbook names the role only) | — | Open (logbook placeholder: Sulav) |
| R2 | **Backend: Flask API** | App structure, auth and roles, exam/question/test-case routes, JSON API, security checks | ✅ `docs/DESIGN.md` §20 "Backend — exams" | **Aashish** | Open |
| R3 | **Backend: sessions and grading** | Exam sessions, server-side deadlines, auto-save, submissions, grading queue and worker | ✅ `docs/DESIGN.md` §20 "Backend — sessions" | **Aashish** (backend) | Open |
| R4 | **Database (MySQL)** | Schema, migrations, queries, test data, nightly backups | 📝 Needed (schema is in `DESIGN.md` §10, but no role description) | **Aashish** | Open |
| R5 | **DevOps and infrastructure** | VPS, Docker and `docker compose`, Judge0 install and limits, deployment, HTTPS, CI | ✅ `docs/DESIGN.md` §20 "Infrastructure and DevOps" | **Aashish** | Open |
| R6 | **Frontend: student UI** | Exam screen, Monaco editor setup, countdown, Run/Submit, question navigation | ✅ `docs/DESIGN.md` §20 "Frontend — student" | — | Open |
| R7 | **Frontend: teacher UI** | Shared layout, authoring forms, results table, monitoring pages | ✅ `docs/DESIGN.md` §20 "Frontend — teacher" | — | Open |
| R8 | **UI/UX design** | Wireframes, page layout, CSS, consistent look across pages | 📝 Needed (logbook: "Frontend development (Design)") | — | Open |
| R9 | **QA: TDD (unit and integration tests)** | Test setup, unit tests for grading/deadlines, authorisation tests, adversarial sandbox tests | 📝 Needed (logbook: "TDD Testing"; approach in `DESIGN.md` §18) | — | Open |
| R10 | **QA: BDD (scenario tests)** | Turns each story's Given/When/Then into tests, end-to-end checks, demo rehearsal | 📝 Needed (logbook: "BDD Testing") | — | Open |
| R11 | **Documentation and report** | Report, ERD, API docs, decision log, demo video, presentation | ✅ `docs/DESIGN.md` §20 "QA and documentation" (combined with testing there; may need its own description) | — | Open |
| R12 | **AI features owner** *(later, only if Sprint 10 finishes early)* | AI hint assistant and AI integrity flags (US63–67) | ✅ `docs/DESIGN.md` §14 and §20 | — | Deferred |

**Notes for assigning roles:**
- **Aashish's preference:** backend (Flask API), database (MySQL) and DevOps (Docker, deployment). **Not** frontend. For documentation, Aashish will **help** with technical input and by reviewing for accuracy, but **not write** it.
- **R2–R5 are too much for one person in 3 weeks.** If Aashish takes them, pair him with at least one other person (for example, a second backend developer on R3, or a backup on R5 who can also redeploy).
- One person can hold several small roles (for example, R1 with R11, or R8 with R7), but every role needs **one named owner and one backup**.
- Fill in the "Interested" column with each member's preference before assigning.

## 5. What we build, sprint by sprint

The **Main role** column shows which role leads each item. Each story still needs backend, frontend and testing work, as in the logbook. Names are added once section 4 is agreed.

**Acceptance criteria and Given/When/Then scenarios** for each story are in the Google Sheet. **Owners and status** are tracked on Trello, with one card per story or task.

### Setup (start Mon 23 Nov, needed before stories can be tested)

| ID | Task | Main role | Folder / file |
| --- | --- | --- | --- |
| P01 | Repo structure and this plan (this branch) | R1 + R2 | whole repo |
| P02 | Check all 5 collaborators accepted their invites; protect `main` | Repo owner (Sulav) | GitHub settings |
| P03 | Buy the VPS and get Judge0 running and reachable | R5 DevOps | `infra/` |
| P04 | Flask skeleton: `create_app`, config, `requirements.txt`, `.env.example` | R2 Backend API | `app/` |
| P05 | MySQL 8 schema and first migration | R4 Database | `app/models/`, `migrations/` |
| P06 | Shared page layout (`base.html`) and CSS | R8 UI/UX + R7 | `app/templates/`, `app/static/` |
| P07 | Test setup: pytest + pytest-bdd *(to confirm)* | R9 + R10 QA | `tests/` |
| P08 | `docker compose` for local web + MySQL | R5 DevOps | `infra/` |
| P09 | CI: run tests on every pull request | R5 DevOps | `.github/workflows/` |

### Sprint 8: 23–29 Nov · Teacher can build an exam (12 pts)

| Story | Title | Pts | Main role |
| --- | --- | --- | --- |
| US1 | Teacher registration and login | 2 | R2 Backend API |
| US21 | Student login | 2 | R2 Backend API |
| US2 | Create exam | 2 | R7 Teacher UI |
| US5 | Add question | 2 | R7 Teacher UI |
| US9 | Add visible sample tests | 2 | R2 Backend API |
| US10 | Add hidden tests (never sent to students) | 2 | R2 Backend API |

### Sprint 9: 30 Nov – 6 Dec · Student can take an exam and run code (15 pts)

| Story | Title | Pts | Main role |
| --- | --- | --- | --- |
| US15 | Publish exam (simplified: visible to all students, no class assignment) | 3 | R2 Backend API |
| US22 | View available exams | 1 | R6 Student UI |
| US24 | Start exam, with the deadline set by the server | 3 | R3 Sessions and grading |
| US26 | Locked-down code editor (Monaco) | 3 | R6 Student UI |
| US27 | Run code against sample tests in Judge0 | 5 | R3 + R5 |

### Sprint 10: 7–13 Dec · Submit, grade, see results (16 pts)

| Story | Title | Pts | Main role |
| --- | --- | --- | --- |
| US30 | Submit a question | 2 | R3 Sessions and grading |
| US33 | Queue submissions for grading | 5 | R3 Sessions and grading |
| US34 | Run every hidden test in isolation (Judge0) | 5 | R3 + R5 |
| US35 | Partial credit score | 2 | R3 Sessions and grading |
| US48 | Results table for the teacher | 2 | R7 Teacher UI |
| R01 | Deploy to the server, rehearse, record the demo | – | R5 DevOps + R10 + everyone |

**Feature freeze: Thu 10 Dec.** After that, only bug fixes, deployment and the demo.

**Stretch (only if ahead):** US32 countdown and auto-submit (3), US28 console output (2), US11 question points (1).

**Deferred:** the other 48 stories (94 points) stay in the Sheet and are reported as future work.

## 6. How we work

| Topic | Rule |
| --- | --- |
| Branches | Never push to `main`. Branch from `main`: `feat/us27-run-sample-tests`, `fix/...`, `chore/...`, `docs/...` |
| Commits | `type(scope): what changed`, e.g. `feat(exams): add create exam form`. Types: feat, fix, test, docs, chore |
| Pull requests | 1 approval from someone else, then squash merge and delete the branch |
| Reviewers (by role) | Backend and database → QA: TDD (R9) · DevOps → Backend (R2/R3) · Student UI ↔ Teacher UI (R6 ↔ R7) · Tests → Backend · Docs → the role whose work is described |
| Trello | Move your card when you start, open a PR and finish. Put the story ID (e.g. US1) in the card, branch and PR titles so they're easy to match. |
| Daily | Pull `main` before starting work. Keep branches short (≤ 3 days). |

## 7. Files still to add (planned, not in this branch)

| File | Purpose | When | Role |
| --- | --- | --- | --- |
| `CONTRIBUTING.md` | Section 6 in full, step by step | Sprint 8 | R1 |
| `.github/PULL_REQUEST_TEMPLATE.md` | Checklist on every PR | Sprint 8 | R1 |
| `.github/CODEOWNERS` | Auto-requests the right reviewer | After roles and usernames are confirmed | R1 + repo owner |
| `.github/workflows/ci.yml` | Runs tests on every PR | P09, once tests exist | R5 |
| `.env.example` | Settings template, with no real secrets | P04 | R2 |
| ERD (redrawn) | Database diagram that matches the real database, for the report | After P05 | R4 (draws), R11 (formats for the report) |
| `docs/API.md` | List of API routes | Sprint 8 onward | R2/R3 (technical content), R11 (writing) |
| `docs/ROLES.md` | Full descriptions for the 📝 roles in section 4 | Before assigning roles | Whole team |

On GitHub (in the browser): protect `main` and confirm all collaborators have accepted. Task tracking (cards, owners, status) happens on **Trello**, not GitHub issues.

## 8. Open questions

1. **Assign roles (section 4):** collect everyone's preferences, write the 📝 descriptions, and choose an owner and a backup for each role.
2. GitHub usernames for Prashna, Dilkash, Basant and Ellie.
3. Has anyone written any code outside this repo?
4. Is 13 Dec the real deadline? When are the report, demo and presentation due?
5. Is the logbook graded? If yes, its roles must be updated to match section 4.
6. Python version (3.12 or 3.13 suggested; everyone must match) and BDD tool (pytest-bdd suggested).
7. Who pays for the VPS?
8. **Which database design do we build?** The ERD in the proposal and `docs/DESIGN.md` §10 are different: the ERD has no session deadline or auto-save tables (needed by US24 and US29) and includes multiple-choice questions, which are out of scope. Suggestion: build from `DESIGN.md` §10 and redraw the ERD afterwards. Decide before P05.
