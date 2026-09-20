# CodeExam — Project Plan

A browser-based coding exam **and learning platform**, built on the same editor and execution pipeline. Students write and run real code during the exam; the system grades it against hidden test cases automatically, and teachers review, override and export instead of reading handwritten code on paper. Outside of exams, the same platform gives students an untimed practice mode, teacher-assigned homework, student-authored practice questions, class discussion boards, and an AI assistant that hints rather than answers — with a matching AI-assisted monitoring layer inside the exam itself, every detection of which is flagged for a teacher to review before anything happens to a student.

> Project plan for the Integrated Project · six-person team · about 21 weeks
>
> **Stack:** Python · Flask · Jinja2 · MySQL 8 · Monaco · self-hosted Judge0 · an LLM API for the practice assistant · Docker

---

## Contents

1. [What we are building](#1-what-we-are-building)
2. [The problem, and who has it](#2-the-problem-and-who-has-it)
3. [Why this project suits us](#3-why-this-project-suits-us)
4. [Three changes to the original spec](#4-three-changes-to-the-original-spec)
5. [Scope — what we build, and in what order](#5-scope--what-we-build-and-in-what-order)
6. [The 67 functional requirements](#6-the-67-functional-requirements)
7. [System architecture](#7-system-architecture)
8. [The exam state machine](#8-the-exam-state-machine)
9. [Code execution — the most important decision](#9-code-execution--the-most-important-decision)
10. [Database — 18 tables](#10-database--18-tables)
11. [Routes — pages and about 40 endpoints](#11-routes--pages-and-api)
12. [Frontend — 14 pages and the editor](#12-frontend--14-jinja-pages-and-the-editor)
13. [Plagiarism detection (stretch)](#13-plagiarism-detection-stretch)
14. [Learning platform and AI features](#14-learning-platform-and-ai-features)
15. [Integrity features — and what we will admit](#15-integrity-features--and-what-we-will-admit)
16. [Infrastructure and cost](#16-infrastructure-and-cost)
17. [Security — our own threat model](#17-security--our-own-threat-model)
18. [Testing strategy](#18-testing-strategy)
19. [Repository and Git conventions](#19-repository-and-git-conventions)
20. [Who does what](#20-who-does-what)
21. [The 21-week plan](#21-the-21-week-plan)
22. [Risk register](#22-risk-register)
23. [Definition of done](#23-definition-of-done)
24. [Settle this week](#24-settle-this-week)
25. [How we pitch it](#25-how-we-pitch-it)

---

## 1. What we are building

Today a coding exam in most colleges is written on paper. Students hand-write Python they cannot run. Teachers read it by eye, guess whether it would have worked, and mark it. It is slow, it is inconsistent, and it tests handwriting as much as programming.

CodeExam replaces that. A teacher writes an exam as a set of problems, each with sample test cases the student can see and hidden test cases they cannot. A student opens the exam in a browser, writes code in a deliberately stripped-down editor, runs it against the sample tests, and submits. The moment they submit, the code is executed in an isolated sandbox against every hidden test, and a score comes back based on how many passed.

The teacher gets a results table instead of a pile of paper, can open any student's code alongside its test output, can override the automatic score where the machine was unfair, and can export everything as CSV.

That is the exam half. The same editor, sandbox and grading pipeline also run a second, equally core half: a learning platform students use every week rather than once a semester — an untimed practice mode, teacher-assigned homework, student-authored practice questions, a class discussion board, and an AI assistant that answers with hints and questions instead of solutions (section 14). The exam half is summative and locked down; the learning half is formative and deliberately open. Building both from one codebase is the point — a second, unrelated product would be twice the work for no shared benefit.

The student-facing exam screen looks roughly like this:

```
┌────────────────────────────────────────────────────────────────┐
│ Q2 of 4 · Reverse a linked list · 10 marks    08:41 remaining  │
├──────────────────────────────────┬─────────────────────────────┤
│ 1  def reverse(head):            │ SAMPLE TESTS                │
│ 2      prev = None               │                             │
│ 3      cur = head                │ test_empty          PASS    │
│ 4      while cur:                │ test_single         PASS    │
│ 5          nxt = cur.next        │ test_three          PASS    │
│ 6          cur.next = prev       │ test_long           FAIL    │
│ 7          prev = cur            │                             │
│ 8          cur = nxt             │ 4 hidden tests     hidden   │
│ 9      return prev               │                             │
└──────────────────────────────────┴─────────────────────────────┘
```

That screen is the exam half of the product; the practice, homework, and discussion screens in section 14 are the learning half, built from the same components. Everything else in this document exists to create both, grade what comes out of the exam side, and prove it was fair.

> **One sentence for the viva:** we are not building a better code editor. We are building the pipeline that takes untrusted student code, runs it safely under strict resource limits, scores it fairly with partial credit, and gives a teacher enough evidence to trust or correct that score — and the same pipeline, outside exam conditions, is what lets a student practise and a teacher assign homework without either of us building it twice.

---

## 2. The problem, and who has it

### The teacher's problem

Marking 50 handwritten programs takes hours and is unreliable. Two teachers give the same answer different marks. A missing colon might cost a student marks, or might not, depending on who is reading. There is no way to check whether the code would actually have run. Re-marking after a complaint means reading everything again.

### The student's problem

They are assessed on something they never do in real life: writing code without running it. A good programmer with weak handwriting is penalised. A student who would have found their bug in ten seconds with an interpreter loses the marks anyway.

### Why now, and why us

- **The users are in our building.** We can interview our own lecturers this week and find out what they actually need, rather than guessing. Almost no student project can say that.
- **The pain is measurable.** Hours spent marking, inconsistency between markers, time between exam and results. All of these are numbers we can ask for and put in the report.
- **A pilot is realistic.** Running one real class quiz on our platform in week 15 is achievable, and it would make the project dramatically stronger than a demo with invented data.

> **Honest about novelty:** HackerRank, Codility, DOMjudge, Moodle CodeRunner and Judge0 already exist. We are not inventing the category. What we are building is a system tuned for a specific context — a college exam hall, one language, teachers who are not programmers, and no budget. We should say this plainly rather than pretend otherwise. Nobody marks a capstone down for building in an established category; they mark it down for pretending the category is empty.

---

## 3. Why this project suits us

| Module requirement | How we meet it |
| --- | --- |
| Working end-to-end web application | Three roles, full exam lifecycle, deployed on our own server |
| Backend REST API | Flask, about 40 JSON endpoints alongside the page routes |
| HTML, CSS, JavaScript frontend | 14 Jinja-rendered pages, plain JS where the page needs to be live, plus the Monaco editor. No React |
| MySQL relational database | 18 tables with real relationships, managed with Alembic migrations |
| Git and GitHub with meaningful history | Branch protection, pull request review, one issue per task |
| At least 35 functional requirements | 67, listed in section 6 |

### What each of us gets out of it

- **Backend depth.** This is a genuinely stateful system. Sessions, timers, queues, retries. Far past CRUD.
- **Infrastructure and DevOps.** Containers, resource limits, queueing under burst load, a real deployment on a real server. This is the most valuable part of the project and the rarest in a student portfolio.
- **Systems thinking.** The exam state machine, and what happens when a network drops at minute 47 of a 60-minute exam, is the kind of problem that separates a developer from someone who has only followed tutorials.
- **Security awareness.** We are running untrusted code. Thinking about that seriously, and documenting the decisions, is worth a section of the report on its own.

---

## 4. Three changes to the original spec

The first draft of this idea specified some things that do not fit our brief or our budget. These are settled now, before any code is written.

| Draft said | We are doing | Why |
| --- | --- | --- |
| PostgreSQL | **MySQL 8** | Our brief requires MySQL. No technical downside for this workload |
| Node.js or Python | **Python + Flask** | Settled. We are taught Flask in depth, so we have a lecturer who can debug our code with us |
| React frontend | **Jinja templates + plain JS + Monaco** | React costs the team 25–40 hours and the brief does not ask for it. Jinja renders on the server, so most pages need no JavaScript at all. Those hours go into the grading pipeline instead |
| Build our own Docker sandbox | **Self-host Judge0** | See section 9. This is the most important decision in the project |
| Webcam snapshots | **Cut entirely** | See section 15 |

### What Jinja changes, and what it does not

Jinja renders HTML on the server. Flask builds the page, fills in the data, and sends finished HTML to the browser. Most of our pages — exam lists, authoring forms, results tables, admin — need no JavaScript beyond a little form handling.

Three places still need JSON and JavaScript, because the page has to change without reloading:

- **The exam screen.** The Monaco editor, the countdown, auto-save, Run and Submit all talk to JSON endpoints. Reloading the page mid-exam is not acceptable.
- **The live monitoring dashboard.** Polls a JSON endpoint every few seconds.
- **Grading progress.** Polls while submissions are being graded.

So the architecture is deliberately **hybrid**: Jinja page routes for everything a human reads, JSON endpoints for everything that has to update live. This still satisfies the module's REST API requirement — around 40 JSON endpoints — and it means ten of our 14 pages are far simpler to build than they would be in a single-page app.

Say this explicitly in the report. "We chose server-side rendering for the pages that do not change and a JSON API only for the parts that must update live" is a design decision, not a shortcut.

---

## 5. Scope — what we build, and in what order

67 functional requirements is the documentation target. It is not the build order. Building everything in parallel produces 67 half-finished features in week 18 — and this list now spans two pillars, not one, which makes sequencing matter even more than it did before.

### Must ship — weeks 1 to 12

- Python only, one language
- Teacher: create an exam, add questions with visible and hidden test cases, publish
- Student: locked-down editor, run against visible tests, console output, auto-save
- Server-authoritative countdown, warnings, auto-submit at expiry
- Submission executed through self-hosted Judge0 against all hidden tests
- Automated grading with partial credit and distinct failure statuses
- Teacher: results table, per-student code and test output, manual override, CSV export
- Tab-switch and paste-attempt logging
- Roster upload, class assignment, user and role management

### Add if time allows — weeks 13 to 16

- Live monitoring dashboard. **Start with polling every few seconds, not WebSockets.** Polling is trivial, works, and is honest. Add WebSockets only if polling demonstrably fails under load, and say so in the report
- Plagiarism similarity detection (section 13)
- Question bank with tags, reuse across exams
- Per-question analytics: pass rate, average score, time spent
- Weighted test cases

### Second pillar — the learning platform, weeks 13 onward (section 14)

Equal in importance to the must-ship exam list, but deliberately sequenced after it, because none of it can be tested properly until the exam platform it shares infrastructure with is stable.

- Practice mode: untimed, unlimited runs, same editor and sandbox
- Teacher-assigned homework, ungraded or lightly-graded
- Student-authored questions, teacher-moderated before publishing
- Class discussion board
- AI assistant (hints, not answers) in practice mode and homework only — never in the exam screen
- AI-assisted combination of exam-integrity signals into a single reviewable flag, always subject to teacher sign-off before any consequence

### Cut permanently

- **Webcam snapshots.** Section 15 explains why at length
- **Multi-language support.** Python only. Each extra language is another execution image, another set of resource limits, another set of edge cases. It adds no marks and multiplies the work
- **Lockdown browser mode.** Cannot be done properly from a web page. Claiming it would be dishonest
- **Autonomous action from any AI signal.** No AI output — similarity, behavioural, or otherwise — is ever allowed to change a grade or lock out a student without a teacher's decision. This is not being weakened later for convenience

---

## 6. The 67 functional requirements

### Teacher — exam authoring (12)

1. Register and log in as a teacher
2. Create an exam with title, duration and open/close window
3. Edit exam details
4. Archive or delete an exam
5. Add a question with statement and starter code
6. Edit a question
7. Delete a question
8. Reorder questions within an exam
9. Add visible sample test cases to a question
10. Add hidden test cases to a question
11. Set the point value of each question
12. Preview the exam exactly as a student would see it

### Teacher — delivery (8)

13. Upload a class roster from CSV
14. Assign an exam to a class or section
15. Publish and schedule an exam to open automatically
16. Unpublish or cancel a scheduled exam
17. Grant a per-student time extension for accessibility
18. Duplicate an exam for reuse next semester
19. Copy a question into another exam
20. View all my exams with their current status

### Student — taking the exam (12)

21. Log in
22. View my upcoming and available exams
23. Read the instructions and rules before starting
24. Start an exam, which starts the timer
25. Navigate between questions using a sidebar
26. Write code in the locked-down editor
27. Run my code against the visible sample tests
28. See console output, errors and per-sample-test results
29. Have my code auto-saved periodically
30. Submit an individual question
31. Submit the whole exam
32. See a countdown with warnings, and be auto-submitted at expiry

### Grading (8)

33. Queue a submission for grading the moment it is received
34. Execute the submission against all hidden tests in isolation
35. Award partial credit based on the proportion of tests passed
36. Record a distinct status for compile error, runtime error, timeout and memory limit
37. Show the teacher live grading progress across the cohort
38. Re-run grading for every submission to a question, after fixing a bad test case
39. View a student's code, console output and per-test results side by side
40. Override the automatic score with manual points and a written comment

### Integrity and monitoring (7)

41. Log tab-switch and window-blur events with timestamps
42. Request full-screen and log every exit
43. Block paste into the editor and log attempts
44. View a live monitoring dashboard during an exam
45. View per-student progress and flag counts during the exam
46. View an integrity report per student after the exam
47. Resume an interrupted session without losing work or extra time

### Results and administration (7)

48. View the results table for an exam
49. Export grades as CSV for the gradebook
50. View per-question analytics: pass rate and average score
51. Manage users and roles
52. Create and manage classes and sections
53. View the audit log
54. View system health: queue depth and worker status

### Learning platform (8)

55. Enter practice mode and attempt any published practice question, untimed and with unlimited runs
56. Filter the practice question bank by topic and difficulty
57. View my own practice attempt history (questions attempted, pass rate)
58. As a teacher, assign homework: a set of questions with a soft due date and no exam timer
59. As a student, complete homework at my own pace, using the same editor and sandbox as an exam
60. As a student, author a practice question with test cases and submit it for teacher approval
61. As a teacher, approve, edit or reject a student-authored question before it is visible to the class
62. Post to and read a class discussion board, scoped to a class or to a specific question

### AI features (5)

63. As a student, ask the AI assistant for a hint on my current code, in practice mode or on homework
64. Have the AI assistant read my current editor state automatically, without pasting code into a chat box
65. Confirm the AI assistant is unreachable from the exam-taking screen and its API routes for the duration of any active exam session
66. View an AI-assisted flag on the monitoring dashboard that combines similarity, tab-switch and behavioural signals, with the supporting evidence attached
67. Confirm that no AI-generated flag can change a grade, reject a submission, or lock out a student without an explicit teacher decision recorded against it

*Stretch requirements not counted above: weighted test cases, hybrid multiple-choice questions.*

---

## 7. System architecture

```
┌──────────────────────────────────────────────────────────┐
│  BROWSER                                                 │
│  Jinja-rendered pages (forms, tables, dashboards)        │
│  + JS only where needed: Monaco editor, countdown,       │
│    auto-save, Run/Submit, polling for live views         │
└───────┬──────────────────────────┬───────────────────────┘
        │ HTML page requests       │ JSON (fetch)
┌───────▼──────────────────────────▼───────────────────────┐
│  FLASK                                                   │
│  ├─ page routes  → render_template(...)  [Jinja]         │
│  └─ api routes   → jsonify(...)          [REST]          │
│                                                          │
│  blueprints: auth · exams · questions · sessions ·       │
│  submissions · monitor · reports · admin                 │
│                                                          │
│  server-authoritative clock — the browser never decides  │
│  when time is up                                         │
└──────┬──────────────────────────┬────────────────────────┘
       │                          │
┌──────▼─────────┐      ┌─────────▼──────────────────────┐
│  MySQL 8       │      │  GRADING WORKER                │
│  18 tables     │      │  pulls from the queue,         │
│  Alembic       │      │  calls Judge0 per test case,   │
└────────────────┘      │  writes results back           │
                        └─────────┬──────────────────────┘
                                  │ HTTP
                        ┌─────────▼──────────────────────┐
                        │  JUDGE0 (self-hosted)          │
                        │  runs untrusted code in        │
                        │  isolated containers with      │
                        │  CPU / memory / wall limits    │
                        └────────────────────────────────┘

    Everything above runs on one VPS via docker compose.
```

The important structural point: **Flask never executes student code itself.** The request handler writes a submission row and returns. A separate worker process picks it up and talks to Judge0. That separation is what keeps the exam responsive when thirty students submit at once, and it is what makes the system recoverable when execution fails.

### The Flask stack, and why each piece is there

| Package | Role | Why we need it |
| --- | --- | --- |
| `Flask` | The web framework | Page routes and JSON routes, organised as blueprints |
| `Jinja2` | Templating | Ships with Flask. Renders every page on the server |
| `Flask-SQLAlchemy` | ORM | Talks to MySQL with Python objects instead of SQL strings |
| `Flask-Migrate` | Migrations (Alembic) | One command and everyone's database matches. Without it, six people drift into six schemas |
| `Flask-Login` | Session auth | Cookie sessions, `@login_required`, `current_user` in templates |
| `Flask-WTF` | Forms + CSRF | Form validation and CSRF tokens. **Not optional** once forms post to the server |
| `PyMySQL` | MySQL driver | Pure Python, installs cleanly in a container |
| `python-dotenv` | Config | Reads `.env` in development; real environment variables in production |
| `requests` | HTTP client | The only thing `judge0.py` uses |
| `gunicorn` | WSGI server | Runs Flask in production. The dev server is never exposed |
| `pytest` + `pytest-flask` | Testing | Flask's test client drives routes without a browser |

Deliberately **not** used: Flask-RESTful, Flask-Marshmallow, Celery. Plain blueprints returning `jsonify()` are enough for 40 endpoints, and Celery is more machinery than our queue needs.

### How the grading worker runs

The worker is a plain Python process in the same repository, started as its own container. It does not serve HTTP.

```python
# worker/run.py
from app import create_app, db
from app.services import grading

app = create_app()

while True:
    with app.app_context():            # reuse the same models and config
        submission = grading.claim_next()   # SELECT ... FOR UPDATE SKIP LOCKED
        if submission is None:
            time.sleep(1)
            continue
        grading.grade(submission)      # calls Judge0 per test case
```

Two decisions worth writing down:

- **The queue is a MySQL table, not Redis.** `submissions.status = 'queued'` is the queue. Claiming a row uses `SELECT ... FOR UPDATE SKIP LOCKED` so two workers never grade the same submission. This is less machinery to learn, one fewer service to run, and it means the queue survives a restart. If load testing in week 13 shows it cannot keep up, we can move to RQ then — and that decision, with the measurement behind it, belongs in the report either way.
- **The worker shares the app factory.** It calls `create_app()` and runs inside `app.app_context()`, so it uses exactly the same models, config and database connection settings as the web process. No duplicated configuration.

---

## 8. The exam state machine

This is the most intellectually interesting part of the project and the part most likely to be built badly if nobody owns it explicitly.

```
SESSION                   SUBMISSION
─────────                 ──────────
NOT_STARTED               QUEUED
    │ student starts          │ worker picks up
    ▼                         ▼
IN_PROGRESS               RUNNING
    │                         │ all test cases executed
    ├── student submits ──▶   ▼
    ├── timer expires ───▶  GRADED
    │      (auto-submit)      │ teacher overrides
    ├── window closes ──▶     ▼
    ▼                       REVIEWED
SUBMITTED
    │ all questions graded
    ▼
COMPLETE
```

### The edge cases that decide whether this works

| Situation | Required behaviour |
| --- | --- |
| Network drops mid-exam | Student reconnects into the same session. Their last auto-saved code is restored. **They get no extra time** — the clock ran on the server the whole time |
| Browser crashes or laptop dies | Same as above. Auto-save is what makes this survivable |
| Student closes the tab and never returns | At the exam window close, the session is auto-submitted with whatever was saved |
| Timer expires while code is being typed | Server rejects further saves, auto-submits what it has. The client shows expiry, but the server decides it |
| Teacher grants an extension mid-exam | Session deadline is recalculated. Already-expired sessions can be reopened explicitly |
| Grading queue backs up | Submissions sit in `QUEUED`. The student sees "submitted, grading in progress". No submission is lost |
| Judge0 is down when a submission arrives | Submission stays `QUEUED` and is retried. It never silently becomes a zero |
| A hidden test case was wrong | Teacher fixes it and re-runs grading for every submission to that question |
| Two submissions for the same question | The latest counts. Earlier ones are kept for the audit trail |

> **The rule that must never be broken: the timer is server-authoritative.** The browser displays a countdown, but the server holds the real deadline and rejects anything that arrives after it. A client-side timer can be paused with dev tools in about ten seconds. If we get this wrong, every other integrity feature is decoration.

---

## 9. Code execution — the most important decision

### Why we are not building our own sandbox

We will be running arbitrary code written by people who are actively motivated to break the system during the exam. The attack surface includes:

- **Fork bombs** — a two-line program that spawns processes until the host dies
- **Infinite loops** — must be killed by a wall-clock limit, not just CPU time
- **Memory exhaustion** — allocating until the host swaps
- **Filesystem access** — reading other students' submissions, writing to the host
- **Network access** — fetching a solution, or attacking our own API from inside the sandbox
- **Container escape** — rarer, but the reason professionals use hardened runtimes

Companies with dedicated security teams get this wrong. Six beginners in 21 weeks will get it wrong.

> **Decision: we self-host Judge0.** It is open source, purpose-built for exactly this, and handles process limits, time limits, memory limits, network isolation and cleanup. We install it with docker-compose on our VPS and call it over HTTP.
>
> We write this into the report as a design decision, not an omission: *"We evaluated building our own execution sandbox, documented the threat model, and concluded the security surface exceeded the scope of this project. We self-hosted Judge0 and directed our engineering effort at the grading pipeline, the exam state machine and burst-load handling."* That paragraph is worth more marks than a home-made sandbox that fails to a fork bomb in the viva.

### How a submission is executed

```
1  Student submits question Q
2  API writes submission row, status = QUEUED, returns immediately
3  Worker picks up the submission
4  For each hidden test case of Q:
       POST code + stdin to Judge0
       with cpu_time_limit, wall_time_limit, memory_limit
       collect stdout, stderr, exit status
       compare stdout to expected output (normalised whitespace)
       write one submission_result row
5  Score = (tests passed / tests total) × question points
6  Submission status = GRADED
```

*Judge0's exact parameter names and language IDs must be confirmed against its documentation in week 4 — the names above are indicative.*

### Result statuses we must handle distinctly

`ACCEPTED` · `WRONG_ANSWER` · `TIME_LIMIT_EXCEEDED` · `MEMORY_LIMIT_EXCEEDED` · `COMPILE_ERROR` · `RUNTIME_ERROR` · `INTERNAL_ERROR`

These must be distinct, and the last one especially. If our infrastructure fails, the student must not silently receive zero. `INTERNAL_ERROR` means "our fault, retry, flag for the teacher" — never "the student was wrong".

### Burst load

Thirty students press Run within the same ten seconds at the start of an exam. This is the single most predictable failure moment in the whole project. Mitigations:

- A queue, not synchronous execution, so nothing is dropped
- Rate limit Run per student — for example one execution every few seconds. Legitimate use is unaffected
- Visible-test runs use only the small sample set; the full hidden set runs only on submit
- A load test written in week 13 that fires 30 concurrent submissions and records queue depth and latency. **The graph from that test belongs in the report.**

---

## 10. Database — 18 tables

```
users              (id, name, email, password_hash,
                    role = student | teacher | admin, active)

classes            (id, name, section, teacher_id → users)
class_members      (id, class_id → classes, student_id → users)

exams              (id, title, teacher_id, duration_minutes,
                    opens_at, closes_at, language,
                    status = draft | published | closed | archived)

questions          (id, exam_id → exams (nullable), position, title,
                    statement, starter_code, points, cpu_limit, memory_limit,
                    author_id → users (nullable), source = teacher | student,
                    approved_at)      ← exam_id is null for practice-bank questions;
                                        author_id + approved_at exist for section 14.1

test_cases         (id, question_id → questions, stdin, expected_stdout,
                    is_hidden, weight, position)

exam_assignments   (id, exam_id → exams, class_id → classes)

exam_sessions      (id, exam_id, student_id, started_at, deadline_at,
                    submitted_at, time_multiplier,
                    status = not_started | in_progress | submitted
                             | auto_submitted | complete)

code_snapshots     (id, session_id → exam_sessions, question_id,
                    code, saved_at)            ← auto-save history

submissions        (id, session_id, question_id, code, submitted_at,
                    is_final, status = queued | running | graded,
                    auto_score, tests_passed, tests_total)

submission_results (id, submission_id → submissions, test_case_id,
                    status, stdout, stderr, time_ms, memory_kb)

grade_overrides    (id, submission_id, teacher_id, manual_score,
                    comment, created_at)

integrity_events   (id, session_id, event_type = tab_blur | fullscreen_exit
                    | paste_attempt | reconnect, occurred_at, detail)

audit_log          (id, user_id, action, entity, entity_id, created_at)

homework_assignments (id, teacher_id → users, class_id → classes, title,
                    due_at, created_at)          ← section 14.1

homework_questions (id, homework_id → homework_assignments,
                    question_id → questions, position)

practice_attempts  (id, student_id → users, question_id → questions,
                    code, status, tests_passed, tests_total, attempted_at)
                                                  ← ungraded, separate from
                                                    submissions on purpose

discussion_posts   (id, class_id → classes, question_id → questions (nullable),
                    author_id → users, body, created_at)

ai_flags           (id, session_id → exam_sessions, flag_type, evidence_json,
                    created_at, reviewed_by → users (nullable), reviewed_at,
                    decision)                    ← section 14.3. reviewed_by
                                                    and decision are null until
                                                    a teacher acts; nothing reads
                                                    this row as a verdict until they do
```

### Three design points worth defending if asked

- **Auto-save is its own table.** Snapshots are append-only, so a student who overwrites good code can be recovered, and so we can show a teacher how the answer developed over time.
- **Per-test results are stored individually.** That is what makes partial credit explainable — a teacher can see exactly which three of eight tests failed, and why.
- **Overrides are separate from auto-scores, never overwriting them.** The automatic result stays visible next to the human decision. That is an audit trail an exam board would actually accept.
- **Practice attempts are a separate table from submissions, and `ai_flags` is separate from `integrity_events`.** Both choices exist so that a bug or a scope cut in section 14 cannot touch exam data. The exam pillar's tables would be identical if section 14 did not exist at all — that boundary is deliberate, not an accident of how the schema grew.

---

## 11. Routes — pages and API

Flask serves two kinds of route. Keep them in separate blueprints so it is always obvious which is which: page routes return HTML, API routes return JSON and never render a template.

### Page routes (Jinja)

| Method | Route | Renders |
| --- | --- | --- |
| GET | `/login` | Login form |
| GET | `/` | Role-aware home: student exam list or teacher exam list |
| GET | `/exams/<id>/instructions` | Rules and duration, with the Start button |
| GET | `/exams/<id>/take` | The exam screen — the only page with significant JS |
| GET | `/exams/new`, `/exams/<id>/edit` | Exam authoring forms |
| GET | `/exams/<id>/questions/<qid>/edit` | Question and test-case editor |
| GET | `/exams/<id>/preview` | Student view, read-only |
| GET | `/exams/<id>/monitor` | Live monitoring shell; polls the API for updates |
| GET | `/submissions/<id>` | Submission review, with the override form |
| GET | `/exams/<id>/results` | Results table and analytics |
| GET | `/admin/users`, `/admin/classes`, `/admin/audit` | Admin pages |
| GET | `/practice` | Practice question bank, filterable by topic and difficulty |
| GET | `/practice/<qid>` | Practice screen — same editor and run panel as the exam screen, no timer, AI assistant panel present |
| GET | `/homework/<id>` | Homework screen — same as practice, plus a due date |
| GET | `/homework/new`, `/homework/<id>/edit` | Teacher: homework authoring forms |
| GET | `/practice/new` | Student: author a practice question and its test cases |
| GET | `/practice/moderation` | Teacher: approve, edit or reject student-authored questions |
| GET | `/classes/<id>/discussion` | Class discussion board |

Form POSTs (create exam, add question, override a grade, upload roster) post to the same blueprint and redirect on success — the standard post/redirect/get pattern. **Every form must carry a CSRF token** (see section 17).

### JSON API routes (REST)

All JSON routes live under `/api/`, return `jsonify()`, and never render a template.

| Group | Endpoints |
| --- | --- |
| Sessions | `POST /api/exams/<id>/start` · `GET /api/sessions/<id>/state` (time remaining, per-question status) · `POST /api/sessions/<id>/submit` · `POST /api/sessions/<id>/extend` |
| Code | `PUT /api/sessions/<id>/questions/<qid>/code` (auto-save) · `POST /api/run` (visible tests only) · `POST /api/submissions` |
| Grading | `GET /api/submissions/<id>` · `POST /api/questions/<id>/regrade` · `GET /api/exams/<id>/grading-progress` |
| Integrity | `POST /api/sessions/<id>/events` · `GET /api/exams/<id>/monitor` |
| Exams and questions | `POST /api/questions/reorder` · `POST /api/questions/<id>/copy` · `POST /api/exams/<id>/publish` · `POST /api/exams/<id>/duplicate` |
| Test cases | `POST /api/questions/<id>/tests` · `PATCH /api/tests/<id>` · `DELETE /api/tests/<id>` |
| Reports | `GET /api/exams/<id>/analytics` · `GET /exams/<id>/export.csv` (file download, page blueprint) |
| System | `GET /api/health` · `GET /api/queue/status` |
| Practice and homework | `POST /api/practice/<qid>/run` · `POST /api/practice/<qid>/attempt` · `POST /api/homework/<id>/attempt` · `POST /api/practice/questions` (student submits for approval) · `POST /api/practice/questions/<id>/approve` |
| Discussion | `GET /api/classes/<id>/discussion` · `POST /api/classes/<id>/discussion` |
| AI assistant | `POST /api/ai/hint` (practice/homework only — this route does not exist under `/api/exams/` or `/api/sessions/`, by design, not by convention) |
| AI monitoring | `GET /api/exams/<id>/ai-flags` · `POST /api/ai-flags/<id>/review` (records `reviewed_by` and `decision`; the only way an ai_flag row is ever acted on) |

The JSON endpoints are the ones the exam screen and the dashboards depend on. Everything a teacher fills in as a form goes through a page route instead — there is no reason to write JavaScript to create an exam.

Notice that no route under `Practice and homework`, `Discussion`, or `AI assistant` lives anywhere near the `Sessions`, `Code`, `Grading`, or `Integrity` groups above. That separation is section 14's exam-screen exclusion rule made structural: a bug that exposes the wrong route to the wrong blueprint is a routing mistake anyone reviewing the pull request should be able to spot, not a runtime check that might fail silently.

---

## 12. Frontend — 14 Jinja pages and the editor

| # | Page | Rendering | JavaScript needed |
| --- | --- | --- | --- |
| 1 | Login | Jinja form | None |
| 2 | Student exam list | Jinja | None |
| 3 | Exam instructions | Jinja | None |
| 4 | **Exam screen** | Jinja shell + JS | **Heavy** — Monaco, countdown, auto-save, Run, Submit, integrity events |
| 5 | Teacher authoring | Jinja forms | Light — add/remove test-case rows |
| 6 | Exam preview | Jinja, read-only | None |
| 7 | Live monitoring | Jinja shell + JS | Polling every few seconds |
| 8 | Submission review | Jinja | None — the override is a normal form POST |
| 9 | Results and analytics | Jinja + Chart.js | Light — charts only |
| 10 | Practice question bank | Jinja | None |
| 11 | **Practice / homework screen** | Jinja shell + JS | **Heavy** — same editor and run panel as the exam screen, plus the AI assistant panel; no timer, no integrity events |
| 12 | Student: author a practice question | Jinja form | Light — reuses the test-case-row partial from teacher authoring |
| 13 | Teacher: practice moderation | Jinja | None — approve/reject is a normal form POST |
| 14 | Class discussion board | Jinja shell + JS | Light — post without a full reload |

Ten of 14 pages need essentially no JavaScript. That is the main practical benefit of choosing Jinja, and it is why this stack suits a team of beginners. Page 11 deliberately shares almost all of its markup and JS with page 4 — same Monaco configuration, same run panel — except it has no countdown, no auto-submit, and no integrity-event listeners, and it has the AI assistant panel that page 4 must never load. That difference is the exam-screen exclusion rule from section 14.2 made visible in the template layer, not just the routing layer.

### Template structure

```
templates/
├─ base.html              nav, flash messages, CSS/JS blocks
├─ auth/login.html
├─ student/
│  ├─ exam_list.html
│  ├─ instructions.html
│  └─ take.html           the exam screen
├─ teacher/
│  ├─ exam_list.html
│  ├─ exam_form.html
│  ├─ question_form.html
│  ├─ preview.html
│  ├─ monitor.html
│  ├─ submission_review.html
│  └─ results.html
├─ admin/
│  ├─ users.html  classes.html  audit.html
├─ practice/
│  ├─ bank.html            question bank, filterable
│  ├─ attempt.html         practice/homework screen, extends the exam screen's macros
│  ├─ author.html          student authors a question
│  └─ moderate.html        teacher approves/rejects
├─ discussion/
│  └─ board.html
└─ partials/
   ├─ _question_nav.html  _test_case_row.html
   ├─ _result_table.html  _flash.html
   ├─ _ai_assistant_panel.html   ← included by attempt.html only, never by take.html
```

Use `{% extends "base.html" %}` everywhere and put anything repeated into `partials/`. Two rules that save a lot of pain later: **no business logic in templates** — if a template needs a calculation, do it in the route or a helper; and **never build HTML with string concatenation in Python** — Jinja autoescapes, your concatenation will not.

### The editor specification

Monaco is VS Code's editor component, and by default it helps the student far too much. Most of the work is switching things off.

**Include**

- Syntax highlighting
- Line numbers
- Auto-indent on newline, tab support
- Run button with a console panel
- Submit button that locks the question
- An always-visible timer

**Exclude — these count as help**

- Autocomplete and IntelliSense
- Auto-closing brackets and quotes
- Parameter hints and import suggestions
- Inline error squiggles — errors appear only on Run
- Paste from outside the browser
- Minimap and spellcheck

```js
monaco.editor.create(container, {
  language: 'python',
  suggestOnTriggerCharacters: false,
  quickSuggestions: false,
  parameterHints: { enabled: false },
  autoClosingBrackets: 'never',
  autoClosingQuotes: 'never',
  wordBasedSuggestions: false,
  autoIndent: 'brackets',
  lineNumbers: 'on',
  minimap: { enabled: false },
});
```

If Monaco proves heavy on slow lab machines, CodeMirror is a lighter alternative, and a styled `textarea` with Prism.js highlighting is the minimal fallback. Decide this in week 5 after testing on an actual college machine, not a personal laptop.

---

## 13. Plagiarism detection (stretch)

Only after the must-ship list is complete. The approach, if we get there:

1. **Tokenise** each submission — strip comments and whitespace, replace identifier names with generic tokens, so renaming variables does not defeat it
2. **Fingerprint** using overlapping k-grams (the winnowing approach behind MOSS)
3. **Compare** every pair of submissions for a question and compute a similarity score
4. **Flag** pairs above a threshold for teacher review, with a side-by-side diff

> **The guardrail.** The system flags pairs for a human to review. It never accuses anyone, never notifies a student, and never applies a penalty automatically. High similarity has innocent causes — a short problem with one obvious solution produces near-identical answers from honest students. The teacher decides. The UI must say this on the screen, not just in our report.

---

## 14. Learning platform and AI features

This is the project's second pillar, equal in scope to the exam platform, not an add-on to it. It runs on the same editor, the same sandbox and the same grading pipeline, but outside a timed, invigilated session. Where the exam platform is summative — one attempt, marked, final — this half is formative: students use it every week, not once a semester.

### 14.1 Learning platform requirements

| Feature | What it does |
| --- | --- |
| Practice mode | Untimed. Students attempt past or sample questions using the same editor and sandbox, with no deadline and unlimited runs |
| Question bank | Practice questions are tagged by topic and difficulty and can be reused across practice sessions and, later, exams |
| Teacher-assigned homework | A teacher posts an ungraded or lightly-graded set of questions with a soft due date. Students complete it in their own time |
| Student-authored questions | A student writes a question and its test cases and submits it for the class to attempt. It is not visible to classmates until a teacher approves it |
| Class discussion board | A simple per-class or per-question thread. Students ask for help, teachers post clarifications. Entirely separate from any graded submission |

None of this is timed, none of it is invigilated, and none of it feeds a final grade unless a teacher explicitly turns a piece of homework into one. That distinction is what keeps this pillar from quietly reopening every integrity problem section 15 exists to manage.

### 14.2 The AI assistant

Modelled on Boot.dev's "Boots": an assistant that reads the student's current code automatically and responds with hints, clarifying questions and explanations of the underlying concept, not a working solution.

- Available in practice mode and on homework only.
- Reads editor state directly — the student never pastes code in to ask a question.
- Prompted specifically to withhold complete solutions and prefer a question back to the student over a direct answer, in the style of Socratic tutoring rather than a search engine.
- Backed by a hosted LLM API rather than anything we train ourselves — this is a prompting and integration problem, not a modelling one, and we should describe it that way in the report.

> **The one rule that cannot bend: the assistant does not exist inside the exam-taking screen.** Not hidden, not disabled by a flag that a curious student could flip in dev tools — genuinely absent from that page's HTML and unreachable from its API routes. If it can be reached from an active exam session by any means, integrity monitoring in section 15 is decoration.

### 14.3 AI-assisted exam monitoring

The tab-switch logging and similarity detection in section 15 already produce signals. This adds a lightweight layer that looks at those signals together — a similarity score alongside a burst of tab-switches alongside an unusual typing pattern — and raises a single flag instead of three separate ones, so the dashboard in section 15 shows a teacher one thing to look at rather than a wall of low-value alerts.

> **The guardrail, stated as plainly as the one in section 13.** An AI-assisted flag is written to the teacher's dashboard with the evidence behind it — which signals fired, when, and the raw data (a diff, a timestamp list). It never changes a grade, rejects a submission, or locks a student out on its own. A teacher reviews the flag and decides. This is a hard rule enforced in code, not a policy we intend to follow: the endpoint that would apply a consequence to a submission requires a `teacher_id` and a decision on record, and there is no code path that skips it.

### Where this sits in the plan

Practice mode is listed as "add if time allows" in section 5 for a reason: it is real scope, on top of an already full 21 weeks. Homework, student-authored questions, discussion boards and the AI assistant are new scope beyond the original must-ship list, and the team should treat them exactly like the plagiarism detection in section 13 — attempted only once the exam platform (must-ship, weeks 1–12) is complete, demoable, and has survived the rehearsal in week 15. Section 21 and section 22 reflect this ordering.

---

## 15. Integrity features — and what we will admit

A browser page cannot lock down a computer. Everything in this section raises the effort required to cheat; none of it prevents cheating. **Saying so ourselves, before anyone asks, is worth more than the features.**

| Feature | What it does | Honest limitation |
| --- | --- | --- |
| Tab-switch logging | Records every time the exam loses focus, with timestamps | Cannot see what they switched to. A second device defeats it entirely |
| Full-screen enforcement | Logs every exit from full-screen | The student can simply decline. It is a signal, not a lock |
| Paste blocking | Blocks the paste event into the editor and logs attempts | Retyping from another window works fine |
| Right-click and dev-tools blocking | Raises the effort slightly | Trivially bypassed by anyone who knows a keyboard shortcut |
| Flag counts on the dashboard | Shows the invigilator who to walk past | Correlation, not evidence. Must be presented as such |
| AI-assisted flag combination (section 14.3) | Combines similarity, tab-switching and behavioural signals into one reviewable flag with evidence attached | Still correlation, not proof, and still requires a teacher's decision before anything happens to a student — the model does not get a vote on the outcome |

### Why webcam monitoring is cut

The original draft suggested random webcam snapshots. We are removing it, and the reasoning belongs in the report:

- It collects biometric data about students, stored on infrastructure managed by students, with no institutional data protection agreement behind it
- It would photograph people's homes and families, not just their faces
- A leak or misuse would be a serious incident, not an inconvenience
- It contributes almost nothing — a phone under the desk is invisible to a webcam pointed at a face

Cutting a feature for a stated ethical reason, and writing the reason down, demonstrates better engineering judgement than building it.

---

## 16. Infrastructure and cost

> **This project cannot be deployed on a free tier, and the team must accept that before committing.** Sandboxed execution needs a Docker daemon on a host we control. Render, Railway and similar free platforms run our app *inside* a container and will not let us spawn sibling containers. Judge0's hosted free tier is rate-limited far below thirty students submitting at once.

### What we need

| Item | Spec | Approximate cost |
| --- | --- | --- |
| VPS | 2 vCPU, 4 GB RAM, Ubuntu 22.04 — enough for the API, MySQL, Judge0 and a worker | Around 5–6 USD per month |
| Domain (optional) | A subdomain is fine; an IP address also works | 0–10 USD once |
| TLS certificate | Let's Encrypt via Caddy or nginx | Free |
| **Total for five months** | | **Roughly 30 USD, split six ways** |

*Prices are indicative and must be checked at purchase time. Hetzner, DigitalOcean and Linode are the usual options.* **Someone must own this and pay for it in week 1** — not week 14.

### Deployment shape

```
VPS
 └── docker compose
      ├── web        (Flask + gunicorn, serves pages and API)
      ├── worker     (same image, runs worker/run.py instead)
      ├── mysql      (with a named volume)
      ├── judge0     (server + workers + its own db/redis)
      └── caddy      (TLS termination, reverse proxy)
```

Nightly `mysqldump` to a private repository or cloud drive. If we lose an exam's submissions the week before submission, the project is over.

---

## 17. Security — our own threat model

| Threat | Mitigation |
| --- | --- |
| Malicious student code escaping the sandbox | Judge0 with network disabled, strict process and memory limits, non-root execution |
| Student reading hidden test cases through the API | Hidden tests are never serialised to a student-facing response. Enforced at the schema layer, not by hiding in the UI |
| Student calling the submit or run endpoints directly to bypass the client | Every endpoint re-checks session ownership, session state and the server-side deadline |
| Student extending their own time | Deadline lives in the database, set at start, never accepted from the client |
| One student viewing another's submission | Authorisation checks on every read, tested explicitly |
| Credentials in the repository | `.env` gitignored from commit one, `.env.example` committed, secrets as server environment variables |
| CSRF on form POSTs | Flask-WTF CSRF protection enabled globally. Every Jinja form includes the token. JSON endpoints called from our own pages send the token in a header |
| Session cookie theft | Flask-Login with `HttpOnly`, `Secure` and `SameSite=Lax` cookies, and a strong `SECRET_KEY` from the environment — never committed |
| XSS through a question statement or student code shown to a teacher | Jinja autoescaping stays on. Never use `\|safe` on anything a user typed. Student code is displayed inside `<pre>`, escaped |
| Exam paper leaking before the exam | Questions are not readable through the API until the exam opens |

Each of these becomes a test. "We wrote a test that proves a student cannot fetch another student's submission" is a strong sentence in a viva.

---

## 18. Testing strategy

- **Unit tests** — pure functions, no Flask needed: partial credit calculation, output comparison and whitespace normalisation, deadline arithmetic with time multipliers, state transitions
- **Integration tests** — the whole submission path: create exam, start session, submit, grade, override, export
- **Authorisation tests** — one per row of the threat model in section 17
- **Template and route tests** — every page route returns 200 for the right role and 403 for the wrong one; forms reject a missing CSRF token; no template renders unescaped user input
- **Adversarial tests** — submit an infinite loop, a memory bomb, a syntax error, an empty file, and code that prints nothing. Each must return the correct distinct status and must not disturb other submissions
- **Load test** — 30 concurrent submissions in week 13, with a graph of queue depth and latency for the report
- **A full exam rehearsal** — the six of us sit a real exam on the system, at the same time, in week 15

CI runs unit, integration and authorisation tests on every pull request. Broken code never reaches the main branch.

---

## 19. Repository and Git conventions

```
codeexam/
├─ app/
│  ├─ __init__.py       create_app(), extensions, blueprint registration
│  ├─ config.py         config classes, reads .env
│  ├─ models/           SQLAlchemy ORM
│  ├─ forms/            Flask-WTF form classes (exam, question, override)
│  ├─ views/            PAGE blueprints — render_template only
│  │                    auth · student · teacher · admin
│  ├─ api/              JSON blueprints — jsonify only
│  │                    sessions · code · grading · monitor · system
│  ├─ services/
│  │  ├─ grading.py     partial credit, status mapping
│  │  ├─ judge0.py      the only file that talks to Judge0
│  │  └─ sessions.py    state machine, deadlines
│  ├─ templates/        see section 12
│  └─ static/
│     ├─ css/           app.css
│     └─ js/            editor.js · timer.js · autosave.js ·
│                       monitor.js · api.js
├─ worker/              grading loop (separate process)
├─ migrations/          Flask-Migrate / Alembic
├─ tests/
├─ infra/               docker-compose.yml, Caddyfile, deploy notes
├─ docs/                ERD, API notes, threat model, load-test results
├─ .github/workflows/   ci.yml
├─ wsgi.py              gunicorn entry point
└─ README.md
```

**The one structural rule:** a file in `views/` never returns JSON, and a file in `api/` never renders a template. When that line blurs, nobody can tell what a route does without reading it.

**Branching:** protected `main`, `develop` for integration, short `feat/<issue>-<slug>` branches that live three days at most. One approving review from someone who did not write the code. Squash merge.

**Commits:** Conventional Commits — `feat(grading): add partial credit scoring`, `fix(sessions): use server clock for deadline`. One GitHub issue per task, referenced in the pull request. This is also what produces the per-person contribution evidence the module requires.

---

## 20. Who does what

| Role | Owns | Learns |
| --- | --- | --- |
| Infrastructure and DevOps | Judge0 deployment, grading worker, queue and burst handling, docker-compose, CI, VPS, backups, the state machine | Containers, resource isolation, queueing, deployment, reliability |
| Backend — exams | Auth, exam and question CRUD, test cases, classes, roster import | REST design, SQLAlchemy, Alembic |
| Backend — sessions | Session lifecycle, auto-save, deadlines, submission endpoints | Stateful API design, concurrency edge cases |
| Frontend — student | Exam screen template and its JS: Monaco configuration, countdown, auto-save, run panel, navigator | Jinja, editor integration, fetch, UI state |
| Frontend — teacher | `base.html` and the shared partials, authoring forms, monitoring, review, results, analytics | Jinja, Flask-WTF forms, tables, Chart.js |
| QA and documentation | Test suite, adversarial tests, load test, user testing with a real lecturer, report, demo video | Testing, technical writing, presenting |

**Section 14 (Phase 3B only):** does not get a dedicated role — it is picked up by whoever finishes their Phase 1–3 ownership first, in the priority order listed in section 21. In practice this tends to be backend — sessions (practice mode and homework reuse the session/submission plumbing directly) and frontend — teacher (student-authored question moderation and the discussion board are authoring-style screens). The AI assistant integration — a single service module that calls the LLM API and enforces the exam-screen exclusion — should have one named owner decided in week 12, not discovered by accident in week 15.

**The dependency to manage:** everyone waits on the submission and grading response format. Whoever owns infrastructure must ship a *stub* `POST /submissions` in week 3 that returns a hardcoded graded result in the final shape. Five people then build for weeks without being blocked.

**Bus factor:** by week 8, one person other than the infrastructure owner must be able to redeploy and restart Judge0. If only one person can run the system, one bad week stops six people.

---

## 21. The 21-week plan

### Phase 1 — foundation, weeks 1 to 4

**Gate: by week 3 the stub submission endpoint exists and its response format is frozen.**

- VPS purchased, access shared, Judge0 running on it and reachable
- Repository, branch protection, issue board, roles agreed
- App factory, blueprints and `base.html` agreed in week 2 — before anyone writes a page, so nobody builds the same layout twice
- `docker compose up` works on all six machines
- Database schema agreed, first migration written
- Wireframes — use the SDLC coursework for this, not a separate example
- One lecturer interviewed about how they currently grade code exams

### Phase 2 — core build, weeks 5 to 10

**Gate: by week 8 we demo end to end — start an exam, write code, run it, submit, see it graded.** Book that supervisor meeting in week 1.

- Auth with Flask-Login, `base.html` and the shared partials agreed early so nobody builds pages twice
- Exam and question authoring as Jinja forms with CSRF
- Session start, server-side deadline, auto-save
- Monaco configured and locked down, run against visible tests
- Real grading through Judge0, partial credit, all statuses handled
- Teacher results table and submission review

### Phase 3 — depth, weeks 11 to 16

**Gate: deployed with TLS and used for a real exam rehearsal by week 15.**

- Manual override, CSV export, analytics
- Integrity logging and the monitoring dashboard (polling first)
- Load test with 30 concurrent submissions, results recorded
- Adversarial tests: fork bomb, infinite loop, memory bomb
- Full rehearsal — all six of us sit a real exam simultaneously
- If possible, a pilot quiz with an actual class

### Phase 3B — second pillar, weeks 15 to 17 (only if Phase 3's gate holds)

**Gate: this phase does not start until the exam rehearsal in week 15 has actually happened.** If the rehearsal slips, this phase shrinks or disappears — it does not push the feature freeze back.

Realistically, three weeks is not enough to build all of section 14 well. Build in this order and stop wherever week 17 finds you; everything below this point is genuinely optional, in priority order:

- Practice mode (reuses the exam editor and Judge0 pipeline directly — the smallest addition)
- Teacher-assigned homework (reuses practice mode's plumbing plus a due date)
- AI assistant, scoped to practice mode and homework only, with the exam-screen exclusion adversarially tested before it is called done
- Student-authored questions with teacher moderation
- Class discussion board
- AI-assisted flag combination on the monitoring dashboard

If only the first one or two ship, say so plainly in the report as a scoping decision made under a fixed deadline — the same honesty this document already asks for around Judge0 and webcam monitoring.

### Phase 4 — land it, weeks 17 to 21

**Feature freeze at week 17. Written down now. No exceptions.**

- Bug bash — all six use the deployed system and file issues
- Fixes and tests only
- Report, threat model, ERD, API documentation, load-test graphs
- Demo video and presentation rehearsal
- Week 21 is buffer. Something will break. That is why it exists

*Identify festival and exam weeks now and mark them zero-output. No gate goes inside one.*

---

## 22. Risk register

| Risk | Why it happens | What we do |
| --- | --- | --- |
| Nobody pays for the VPS | It is nobody's job by default | Named owner and payment in week 1. It is the first item on the plan |
| Sandbox built from scratch, then breaks | It looks like the impressive part | Decision already made: Judge0. Documented as engineering judgement, not retreat |
| Everything works until 30 people submit at once | Only ever tested by one person at a time | Load test in week 13 and a six-person rehearsal in week 15, both scheduled now |
| Scope explodes — multi-language, WebSockets, plagiarism, webcam, and now a second whole pillar | The feature list is genuinely exciting, and section 14 adds real scope on top of an already full plan | Must-ship list in section 5 is fixed and comes first. The learning platform and AI features are sequenced after it, not alongside it, and can be cut back to practice mode alone without the project failing |
| The AI assistant leaks a full solution instead of a hint | Prompting an LLM to withhold an answer is a soft constraint, not a hard one — students will actively try to extract the answer | Test this adversarially before it ships, the same way we adversarially test the sandbox in section 9. Treat "the assistant gave away the answer" as a bug with its own issue, not an acceptable edge case |
| An AI-assisted flag is treated as a verdict instead of a suggestion | Once something is labelled by "the AI," it is tempting to trust it more than a human hunch | Section 14's guardrail is enforced in code: the endpoint that would act on a submission requires a recorded teacher decision. There is no path that skips it, and this is tested like any other authorisation rule in section 18 |
| Infrastructure owner becomes a bottleneck | Six people wait on the grading format | Stub shipped in week 3, format frozen, real pipeline swapped in behind it |
| Two people do 80% of the work | Standard in six-person teams | Owned files per person. Review the contributor graph at weeks 5, 10 and 15 and reallocate then, not in week 19 |
| Drift in the long middle | 21 weeks feels endless until it does not | Three public gates at weeks 3, 8 and 15, and a number posted in the group every Friday |
| Data loss | One bad command on a single VPS | Nightly database dump off the server, plus a local-only run path that always works |
| Demo-day failure | Cold start, expired certificate, dead container | Rehearse the demo twice on the deployed system, and keep a recorded video as a fallback |

---

## 23. Definition of done

**A feature is done when:** the code is merged through a reviewed pull request; unit tests pass in CI; it works on the deployed server, not only on a laptop; it is documented in `docs/`; and one teammate who did not build it has used it successfully.

**The project is done when:** a teacher who is not on our team can create an exam, publish it, have a student sit it, and export the grades — without any of us touching a keyboard.

That last sentence is the real acceptance test. Write it on the wall.

---

## 24. Settle this week

### Ask the module leader

- Confirm in writing whether calling a hosted LLM API for the AI assistant and AI-assisted monitoring (section 14) satisfies the brief's machine learning requirement, or whether the brief expects us to train or fine-tune a model ourselves. These are very different amounts of work and the answer changes what we commit to in week 1, not week 14
- Confirm that CRUD variants count separately toward the 35-feature requirement
- Can we book a supervisor demo for week 8 now?

### Decide among ourselves

- Who buys the VPS, from which provider, and how the six of us split the cost
- Who owns infrastructure, and who is the backup who can also redeploy
- Which lecturer we interview, and when
- Which weeks are lost to festivals and exams

---

## 25. How we pitch it

1. **Open with the current reality, no technology.** "Our coding exams are written by hand on paper. The code is never run. A teacher marks 50 programs by eye."
2. **Name the cost.** Hours of marking, inconsistency between markers, students penalised for handwriting rather than programming. Use the numbers we got from the lecturer interview.
3. **Demo, sixty seconds.** Sit the exam. Write code. Run it — one sample test fails. Fix it. Submit. Switch to the teacher view: the submission is already graded, with seven of eight hidden tests passed and partial credit awarded.
4. **Show the hard part.** The load-test graph, and the fork bomb that gets killed in 2 seconds without disturbing anyone else's submission. This is the slide that separates us from a CRUD app.
5. **If section 14 shipped, show the other half in ten seconds.** Switch to practice mode, ask the AI assistant for a hint, and show that it asks a question back instead of handing over the answer. Then show the same assistant is simply absent from the exam screen — open dev tools live if it makes the point faster. If an AI-assisted flag exists on the monitoring dashboard, click into it and show the evidence panel, then say the words: "this never acts on its own — a teacher reviews every one of these."
6. **End on the limitation and the next step.** "Tab-switch logging raises the effort to cheat; it does not prevent it, and a second device defeats it entirely. We cut webcam monitoring on privacy grounds. Next step: a pilot with one real class."

Ending on a limitation makes people trust everything that came before it. Ending on "this will transform assessment" makes them trust none of it. If section 14 did not ship in time, step 5 is simply dropped from the pitch — the exam half stands on its own, and that is exactly why it was built first.

---

*Project plan for team discussion. Judge0 parameters, VPS pricing and free-tier terms should be verified by whoever owns that part before we depend on them.*
