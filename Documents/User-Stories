# CodeExam — User Stories

Online Coding Exam Platform. Scrum Master: Sulav Shrestha. Developers: Aashish Shrestha, Prashna Bhukhaju, Dilkash Shekh, Basant Nayak, Ellie Bohora.

**Summary:** 8 features · 67 user stories · 143 story points · 10 one-week sprints · 27 High / 27 Medium / 13 Low priority.

## Contents

- [F1 — Exam Authoring](#f1-exam-authoring)
- [F2 — Exam Delivery](#f2-exam-delivery)
- [F3 — Taking the Exam](#f3-taking-the-exam)
- [F4 — Auto-Grading](#f4-auto-grading)
- [F5 — Integrity & Monitoring](#f5-integrity--monitoring)
- [F6 — Results & Administration](#f6-results--administration)
- [F7 — Learning Platform](#f7-learning-platform)
- [F8 — AI Features](#f8-ai-features)

## Overview

| ID | User Story | Priority | Points | Sprint |
|----|------------|----------|-------:|-------:|
| 1.1 | Teacher Registration & Login | High | 2 | 1 |
| 1.2 | Create Exam | High | 2 | 1 |
| 1.3 | Edit Exam Details | Medium | 1 | 1 |
| 1.4 | Archive or Delete Exam | Medium | 1 | 1 |
| 1.5 | Add Question | High | 2 | 1 |
| 1.6 | Edit Question | Medium | 1 | 2 |
| 1.7 | Delete Question | Medium | 1 | 2 |
| 1.8 | Reorder Questions | Low | 2 | 8 |
| 1.9 | Add Visible Sample Tests | High | 2 | 2 |
| 1.10 | Add Hidden Tests | High | 2 | 2 |
| 1.11 | Set Question Points | High | 1 | 2 |
| 1.12 | Preview Exam | Medium | 2 | 2 |
| 2.1 | Upload Class Roster | High | 3 | 2 |
| 2.2 | Assign Exam to Class | High | 2 | 3 |
| 2.3 | Publish & Schedule Exam | High | 3 | 3 |
| 2.4 | Unpublish or Cancel Exam | Medium | 1 | 3 |
| 2.5 | Per-Student Time Extension | Medium | 2 | 7 |
| 2.6 | Duplicate Exam | Low | 2 | 8 |
| 2.7 | Copy Question to Another Exam | Low | 1 | 7 |
| 2.8 | View My Exams | Medium | 1 | 2 |
| 3.1 | Student Login | High | 2 | 1 |
| 3.2 | View Available Exams | High | 1 | 3 |
| 3.3 | Read Exam Instructions | Medium | 1 | 3 |
| 3.4 | Start Exam | High | 3 | 3 |
| 3.5 | Question Navigation | High | 2 | 3 |
| 3.6 | Locked-Down Code Editor | High | 3 | 4 |
| 3.7 | Run Against Sample Tests | High | 5 | 4 |
| 3.8 | Console Output & Test Results | High | 2 | 4 |
| 3.9 | Auto-Save Code | High | 2 | 5 |
| 3.10 | Submit Individual Question | High | 2 | 5 |
| 3.11 | Submit Whole Exam | High | 2 | 5 |
| 3.12 | Countdown & Auto-Submit | High | 3 | 5 |
| 4.1 | Queue Submission for Grading | High | 5 | 5 |
| 4.2 | Isolated Execution | High | 5 | 4 |
| 4.3 | Partial Credit | High | 2 | 6 |
| 4.4 | Distinct Failure Statuses | Medium | 2 | 6 |
| 4.5 | Live Grading Progress | Medium | 2 | 6 |
| 4.6 | Re-run Grading | Medium | 2 | 6 |
| 4.7 | Submission Review | High | 3 | 6 |
| 4.8 | Manual Score Override | Medium | 2 | 6 |
| 5.1 | Tab-Switch Logging | Medium | 2 | 7 |
| 5.2 | Full-Screen Monitoring | Medium | 1 | 7 |
| 5.3 | Paste Blocking | Medium | 1 | 7 |
| 5.4 | Live Monitoring Dashboard | Medium | 3 | 7 |
| 5.5 | Per-Student Progress & Flags | Medium | 2 | 7 |
| 5.6 | Post-Exam Integrity Report | Low | 2 | 7 |
| 5.7 | Resume Interrupted Session | Medium | 2 | 6 |
| 6.1 | Results Table | High | 2 | 8 |
| 6.2 | Export Grades to CSV | Medium | 1 | 8 |
| 6.3 | Per-Question Analytics | Low | 3 | 8 |
| 6.4 | Manage Users & Roles | High | 2 | 1 |
| 6.5 | Manage Classes & Sections | High | 2 | 1 |
| 6.6 | View Audit Log | Medium | 2 | 8 |
| 6.7 | System Health | Low | 2 | 8 |
| 7.1 | Practice Mode | Medium | 2 | 9 |
| 7.2 | Filter Practice Bank | Low | 1 | 9 |
| 7.3 | Practice History | Low | 1 | 9 |
| 7.4 | Assign Homework | Medium | 2 | 9 |
| 7.5 | Complete Homework | Medium | 2 | 9 |
| 7.6 | Author Practice Question | Low | 2 | 9 |
| 7.7 | Moderate Student Questions | Low | 2 | 9 |
| 7.8 | Class Discussion Board | Low | 3 | 9 |
| 8.1 | AI Hint Assistant | Medium | 5 | 10 |
| 8.2 | Automatic Code Context | Medium | 2 | 10 |
| 8.3 | AI Blocked During Exams | Medium | 2 | 10 |
| 8.4 | AI-Assisted Integrity Flag | Low | 5 | 10 |
| 8.5 | Teacher Decision Required | Low | 2 | 10 |

---

## F1 — Exam Authoring

### 1.1 — Teacher Registration & Login

**Priority:** High · **Story points:** 2 · **Sprint:** 1

> As a teacher, I want to register and log in securely so that I can access my exam management dashboard.

**Acceptance Criteria**

- Registration requires valid name, email and password.
- Passwords are hashed before storage, never stored in plain text.
- Successful login redirects to the teacher dashboard.
- Incorrect credentials show an error without revealing which field was wrong.

**Scenario**

**Given** a teacher with a registered account  
**When** they enter their email and a correct password on the login page  
**Then** they are redirected to the teacher dashboard  
**And** entering a wrong password shows a generic error that does not say which field was wrong

### 1.2 — Create Exam

**Priority:** High · **Story points:** 2 · **Sprint:** 1

> As a teacher, I want to create an exam with a title, duration and open/close window so that students can sit it at the right time.

**Acceptance Criteria**

- Title, duration (minutes), open time and close time are required.
- Close time must be after open time, or the form is rejected.
- New exams are saved with status "draft".
- A success message confirms creation and links to adding questions.

**Scenario**

**Given** a teacher on the Create Exam form  
**When** they enter a title, 60 minutes duration, and an open time that is earlier than the close time, then save  
**Then** the exam is saved as "draft"  
**And** a success message links to adding questions

### 1.3 — Edit Exam Details

**Priority:** Medium · **Story points:** 1 · **Sprint:** 1

> As a teacher, I want to edit an exam's details so that I can correct mistakes before it opens.

**Acceptance Criteria**

- Form is pre-filled with the current exam data.
- The same validation rules as creation apply.
- Duration and window cannot be edited once any student has started.
- Changes are recorded in the audit log.

**Scenario**

**Given** a draft exam that no student has started  
**When** the teacher changes the duration and saves  
**Then** the pre-filled form is accepted and the change is stored  
**And** the change appears in the audit log

### 1.4 — Archive or Delete Exam

**Priority:** Medium · **Story points:** 1 · **Sprint:** 1

> As a teacher, I want to archive or delete an exam so that my exam list stays organised.

**Acceptance Criteria**

- Delete is only allowed for exams with no student sessions.
- Exams with sessions can only be archived, preserving submissions.
- Both actions require a confirmation step.
- Archived exams are hidden from the active list but viewable under a filter.

**Scenario**

**Given** an exam that already has student sessions  
**When** the teacher tries to delete it  
**Then** deletion is refused and only Archive is offered  
**And** after confirming, the exam leaves the active list but stays visible under the archived filter

### 1.5 — Add Question

**Priority:** High · **Story points:** 2 · **Sprint:** 1

> As a teacher, I want to add a question with a statement and starter code so that students know what to solve.

**Acceptance Criteria**

- Title and statement are required; starter code is optional.
- Starter code is loaded into the student editor when the exam opens.
- The question is added at the last position in the exam.
- Statement text is escaped when displayed, preventing XSS.

**Scenario**

**Given** a teacher editing a draft exam  
**When** they add a question with a title and statement but no starter code  
**Then** the question is added at the last position  
**And** any HTML in the statement is escaped when displayed

### 1.6 — Edit Question

**Priority:** Medium · **Story points:** 1 · **Sprint:** 2

> As a teacher, I want to edit a question so that I can fix errors in its wording or starter code.

**Acceptance Criteria**

- Form is pre-filled with the current question.
- Editing after the exam opens requires confirming a warning.
- Saved changes appear immediately in the preview.
- A success message confirms the update.

**Scenario**

**Given** a published exam that has already opened  
**When** the teacher edits a question's statement  
**Then** a warning must be confirmed before saving  
**And** after saving, the change shows immediately in the preview

### 1.7 — Delete Question

**Priority:** Medium · **Story points:** 1 · **Sprint:** 2

> As a teacher, I want to delete a question I no longer need so that the exam only contains relevant problems.

**Acceptance Criteria**

- Deletion requires confirmation.
- Its test cases are deleted with it.
- Remaining questions are renumbered with no gaps.
- Deletion is blocked if submissions exist for that question.

**Scenario**

**Given** a question with 3 test cases and no submissions  
**When** the teacher confirms deletion  
**Then** the question and its test cases are removed  
**And** the remaining questions are renumbered without gaps

### 1.8 — Reorder Questions

**Priority:** Low · **Story points:** 2 · **Sprint:** 8

> As a teacher, I want to reorder questions so that the exam flows from easy to hard.

**Acceptance Criteria**

- Questions can be moved up or down in the list.
- The new order saves without a full page reload.
- Students see questions in the saved order.
- Reordering does not change any question's points or tests.

**Scenario**

**Given** an exam with questions 1, 2 and 3  
**When** the teacher moves question 3 up to position 1  
**Then** the new order is saved without a page reload  
**And** students see the questions in the saved order, with points and tests unchanged

### 1.9 — Add Visible Sample Tests

**Priority:** High · **Story points:** 2 · **Sprint:** 2

> As a teacher, I want to add sample test cases students can see so that they can check their approach.

**Acceptance Criteria**

- Each test has stdin and expected output fields.
- Sample tests are saved as visible (is_hidden = false).
- Students can run their code against sample tests only.
- Test rows can be added or removed on the form before saving.

**Scenario**

**Given** a teacher editing a question  
**When** they add two test rows with stdin and expected output and save  
**Then** the tests are stored with is_hidden = false  
**And** students can run their code against these sample tests

### 1.10 — Add Hidden Tests

**Priority:** High · **Story points:** 2 · **Sprint:** 2

> As a teacher, I want to add hidden test cases so that grading checks cases students cannot hard-code.

**Acceptance Criteria**

- Hidden tests are saved with is_hidden = true.
- Hidden tests never appear in any student-facing API response.
- A question cannot be published without at least one hidden test.
- Students see the number of hidden tests, not their content.

**Scenario**

**Given** a teacher editing a question  
**When** they add a test marked hidden and save  
**Then** it is stored with is_hidden = true  
**And** students see only the count of hidden tests, never their content

### 1.11 — Set Question Points

**Priority:** High · **Story points:** 1 · **Sprint:** 2

> As a teacher, I want to set the point value of each question so that marks reflect difficulty.

**Acceptance Criteria**

- Points must be a positive whole number.
- The exam total updates when any question's points change.
- Points are shown to students beside each question.
- Partial credit is calculated from these points.

**Scenario**

**Given** an exam with two questions worth 10 points each  
**When** the teacher changes one question to 15 points  
**Then** the exam total updates to 25  
**And** entering 0 or a decimal is rejected

### 1.12 — Preview Exam

**Priority:** Medium · **Story points:** 2 · **Sprint:** 2

> As a teacher, I want to preview the exam exactly as a student sees it so that I can catch problems before publishing.

**Acceptance Criteria**

- Preview uses the same layout and editor as the student exam screen.
- Hidden tests are not shown in preview.
- Preview is read-only and creates no session or submission.
- Preview works for both draft and published exams.

**Scenario**

**Given** a draft exam with questions and hidden tests  
**When** the teacher clicks Preview  
**Then** the exam appears in the student layout and editor, read-only  
**And** hidden tests are not shown and no session or submission is created

---

## F2 — Exam Delivery

### 2.1 — Upload Class Roster

**Priority:** High · **Story points:** 3 · **Sprint:** 2

> As a teacher, I want to upload a class roster from CSV so that I don't have to add students one by one.

**Acceptance Criteria**

- Only .csv files with name and email columns are accepted.
- Invalid or duplicate rows are skipped and listed in an error summary.
- New students get accounts; existing students are linked, not duplicated.
- A summary shows how many students were added, linked and skipped.

**Scenario**

**Given** a teacher with a CSV containing valid rows, a duplicate and an invalid email  
**When** they upload the file  
**Then** valid rows create or link student accounts  
**And** bad rows are skipped and listed, with a summary of added, linked and skipped counts

### 2.2 — Assign Exam to Class

**Priority:** High · **Story points:** 2 · **Sprint:** 3

> As a teacher, I want to assign an exam to a class or section so that only the right students can sit it.

**Acceptance Criteria**

- Teacher can select one or more of their own classes.
- Only students in an assigned class see the exam in their list.
- A student outside the class receives 403 if they open the exam URL.
- Assignments can be removed until the exam opens.

**Scenario**

**Given** a draft exam and two classes the teacher owns  
**When** the teacher assigns the exam to one class  
**Then** only students in that class see it in their list  
**And** a student outside the class who opens the exam URL receives 403

### 2.3 — Publish & Schedule Exam

**Priority:** High · **Story points:** 3 · **Sprint:** 3

> As a teacher, I want to publish an exam and have it open automatically so that I don't need to be online at the start time.

**Acceptance Criteria**

- Publishing requires at least one question with a hidden test and an assigned class.
- Status changes from draft to published.
- Students can start only between the open and close times, checked by the server clock.
- Question content is not readable through the API before the open time.

**Scenario**

**Given** a draft exam with a question, a hidden test and an assigned class  
**When** the teacher publishes it  
**Then** the status changes to "published"  
**And** students can start only between the open and close times, and question content is not readable before opening

### 2.4 — Unpublish or Cancel Exam

**Priority:** Medium · **Story points:** 1 · **Sprint:** 3

> As a teacher, I want to unpublish or cancel a scheduled exam so that I can fix problems or respond to changes.

**Acceptance Criteria**

- Unpublishing returns the exam to draft status.
- Unpublishing is blocked once any student has started.
- The action requires confirmation.
- The exam disappears from assigned students' lists immediately.

**Scenario**

**Given** a published exam that no student has started  
**When** the teacher confirms Unpublish  
**Then** the exam returns to draft and disappears from students' lists immediately  
**And** once any student has started, unpublishing is blocked

### 2.5 — Per-Student Time Extension

**Priority:** Medium · **Story points:** 2 · **Sprint:** 7

> As a teacher, I want to grant a specific student extra time so that students with accessibility needs are treated fairly.

**Acceptance Criteria**

- Extension is set as a time multiplier or extra minutes per student.
- The session deadline is recalculated on the server, including mid-exam.
- The student's countdown reflects the new deadline on its next sync.
- Every extension is recorded in the audit log with the teacher's ID.

**Scenario**

**Given** a student with an active exam session  
**When** the teacher grants them a 1.5× time multiplier mid-exam  
**Then** the server recalculates the deadline  
**And** the student's countdown updates on its next sync and the audit log records the teacher's ID

### 2.6 — Duplicate Exam

**Priority:** Low · **Story points:** 2 · **Sprint:** 8

> As a teacher, I want to duplicate an exam so that I can reuse it next semester without rebuilding it.

**Acceptance Criteria**

- The copy includes all questions, test cases and points.
- The copy is created as a draft with no class assignments.
- No sessions or submissions are copied.
- The copy's title is marked "(Copy)" until edited.

**Scenario**

**Given** an existing exam with sessions and class assignments  
**When** the teacher duplicates it  
**Then** a new draft titled "… (Copy)" is created with all questions, tests and points  
**And** no sessions, submissions or class assignments are copied

### 2.7 — Copy Question to Another Exam

**Priority:** Low · **Story points:** 1 · **Sprint:** 7

> As a teacher, I want to copy a question into another exam so that I can reuse good questions.

**Acceptance Criteria**

- Teacher selects a target exam from their own exams.
- The question and all its test cases are copied.
- Editing the copy does not change the original.
- Copying into an exam that has already opened is blocked.

**Scenario**

**Given** a question in Exam A and a draft Exam B owned by the teacher  
**When** the teacher copies the question into Exam B  
**Then** the question and all its tests are copied  
**And** editing the copy leaves the original unchanged, and copying into an already-opened exam is blocked

### 2.8 — View My Exams

**Priority:** Medium · **Story points:** 1 · **Sprint:** 2

> As a teacher, I want to see all my exams with their current status so that I know what needs attention.

**Acceptance Criteria**

- List shows title, status, open time and assigned classes.
- Status is one of draft, published, closed or archived.
- List can be filtered by status.
- Teachers see only their own exams; admins see all.

**Scenario**

**Given** a teacher who owns exams in draft, published, closed and archived states  
**When** they open My Exams and filter by "published"  
**Then** only published exams are listed with title, status, open time and classes  
**And** other teachers' exams are not shown (admins see all)

---

## F3 — Taking the Exam

### 3.1 — Student Login

**Priority:** High · **Story points:** 2 · **Sprint:** 1

> As a student, I want to log in with my college credentials so that I can access my assigned exams and practice work.

**Acceptance Criteria**

- Login requires a valid email and password.
- Successful login redirects to the student dashboard.
- Deactivated accounts cannot log in.
- Session cookies are HttpOnly, Secure and SameSite=Lax.

**Scenario**

**Given** a student with an active account  
**When** they log in with a valid email and password  
**Then** they are redirected to the student dashboard with an HttpOnly, Secure, SameSite=Lax cookie  
**And** a deactivated account cannot log in

### 3.2 — View Available Exams

**Priority:** High · **Story points:** 1 · **Sprint:** 3

> As a student, I want to see my upcoming and available exams so that I know what I need to sit and when.

**Acceptance Criteria**

- List shows only exams assigned to my classes.
- Each exam shows title, duration, open and close times.
- Exams are labelled upcoming, open, in progress or completed.
- The Start button appears only while the exam is open.

**Scenario**

**Given** a student in a class with one exam open and one upcoming  
**When** they open their exam list  
**Then** both exams show title, duration and open/close times with the right labels  
**And** Start appears only on the open exam

### 3.3 — Read Exam Instructions

**Priority:** Medium · **Story points:** 1 · **Sprint:** 3

> As a student, I want to read the instructions and rules before starting so that I know what is allowed and monitored.

**Acceptance Criteria**

- Page shows duration, number of questions and total points.
- Page lists what is logged: tab switches, full-screen exits and paste attempts.
- Viewing instructions does not start the timer.
- Student must tick a confirmation box before Start is enabled.

**Scenario**

**Given** a student on the instructions page of an open exam  
**When** they read the page without ticking the confirmation box  
**Then** duration, question count, total points and the logged events are shown and the timer has not started  
**And** Start stays disabled until the box is ticked

### 3.4 — Start Exam

**Priority:** High · **Story points:** 3 · **Sprint:** 3

> As a student, I want to start an exam so that my timed session begins.

**Acceptance Criteria**

- Starting creates one session with started_at and deadline_at set by the server.
- A student cannot create a second session for the same exam.
- Deadline is the earlier of start + duration (with multiplier) and the exam close time.
- The student is taken straight to the first question.

**Scenario**

**Given** an open exam and a student who has ticked the confirmation  
**When** they click Start  
**Then** one session is created with started_at and deadline_at set by the server  
**And** they land on question 1, and a second Start for the same exam is refused

### 3.5 — Question Navigation

**Priority:** High · **Story points:** 2 · **Sprint:** 3

> As a student, I want to move between questions using a sidebar so that I can answer in any order.

**Acceptance Criteria**

- Sidebar lists every question with its number and points.
- Each question shows its status: not started, in progress or submitted.
- Switching questions keeps the code already written.
- Navigation does not reload the page or reset the timer.

**Scenario**

**Given** a student in an exam with three questions  
**When** they click question 2 in the sidebar  
**Then** question 2 opens with its status shown, without a page reload  
**And** code already written is kept and the timer is not reset

### 3.6 — Locked-Down Code Editor

**Priority:** High · **Story points:** 3 · **Sprint:** 4

> As a student, I want to write code in an editor with basic highlighting but no assistance so that the exam tests my own ability.

**Acceptance Criteria**

- Editor provides syntax highlighting, line numbers and auto-indent.
- Autocomplete, parameter hints and auto-closing brackets are disabled.
- No inline error squiggles; errors appear only after Run.
- Minimap and spellcheck are off.

**Scenario**

**Given** a student in the exam editor  
**When** they type code  
**Then** syntax highlighting, line numbers and auto-indent work  
**And** autocomplete, hints, bracket auto-closing, error squiggles, minimap and spellcheck are all off

### 3.7 — Run Against Sample Tests

**Priority:** High · **Story points:** 5 · **Sprint:** 4

> As a student, I want to run my code against the visible sample tests so that I can find bugs before submitting.

**Acceptance Criteria**

- Run executes code in the Judge0 sandbox against sample tests only.
- Run is rate-limited per student, e.g. once every few seconds.
- Running does not count as a submission.
- Run is rejected after the session deadline.

**Scenario**

**Given** a student with code written for a question  
**When** they click Run  
**Then** the code runs in the Judge0 sandbox against sample tests only  
**And** it does not count as a submission, and rapid repeat runs are rate-limited

### 3.8 — Console Output & Test Results

**Priority:** High · **Story points:** 2 · **Sprint:** 4

> As a student, I want to see console output, errors and per-test results so that I understand why my code passed or failed.

**Acceptance Criteria**

- Console shows stdout and stderr from the run.
- Each sample test shows PASS or FAIL with its status.
- Syntax errors, runtime errors and timeouts are shown as distinct messages.
- Hidden tests appear only as a count, never with results.

**Scenario**

**Given** a student who has just clicked Run  
**When** the run finishes  
**Then** the console shows stdout and stderr, and each sample test shows PASS or FAIL  
**And** syntax errors, runtime errors and timeouts show as distinct messages, and hidden tests appear only as a count

### 3.9 — Auto-Save Code

**Priority:** High · **Story points:** 2 · **Sprint:** 5

> As a student, I want my code saved automatically so that I don't lose work if my browser crashes.

**Acceptance Criteria**

- Code is saved to the server at a fixed interval and on question switch.
- Each save is stored as a new snapshot, not an overwrite.
- A "Saved" indicator shows the time of the last successful save.
- Saves arriving after the deadline are rejected by the server.

**Scenario**

**Given** a student typing code in an active session  
**When** the auto-save interval elapses or they switch questions  
**Then** the code is saved as a new snapshot and the "Saved" indicator shows the time  
**And** a save arriving after the deadline is rejected

### 3.10 — Submit Individual Question

**Priority:** High · **Story points:** 2 · **Sprint:** 5

> As a student, I want to submit one question at a time so that it is graded while I work on the rest.

**Acceptance Criteria**

- Submit asks for confirmation first.
- The submission is queued for grading and the response returns immediately.
- The question shows "submitted, grading in progress".
- If resubmitted, the latest submission counts and earlier ones are kept.

**Scenario**

**Given** a student with an answer ready for question 2  
**When** they click Submit and confirm  
**Then** the submission is queued and the response returns immediately  
**And** the question shows "submitted, grading in progress", and a resubmission replaces it as the latest while earlier ones are kept

### 3.11 — Submit Whole Exam

**Priority:** High · **Story points:** 2 · **Sprint:** 5

> As a student, I want to submit the whole exam when I'm finished so that my session ends and everything is graded.

**Acceptance Criteria**

- Confirmation lists any questions not yet submitted.
- Unsubmitted questions are submitted using their latest saved code.
- Session status changes to submitted and the editor locks.
- The student cannot re-enter a submitted exam.

**Scenario**

**Given** a student with one question not yet submitted  
**When** they click Submit Exam  
**Then** the confirmation lists the unsubmitted question  
**And** after confirming, its latest saved code is submitted, the session is marked submitted, the editor locks, and re-entry is blocked

### 3.12 — Countdown & Auto-Submit

**Priority:** High · **Story points:** 3 · **Sprint:** 5

> As a student, I want a visible countdown with warnings so that I can manage my time, and be auto-submitted when it runs out.

**Acceptance Criteria**

- Countdown is always visible and syncs with the server deadline.
- Warnings appear at 10 minutes and 1 minute remaining.
- At expiry the server auto-submits all saved code, even if the tab is closed.
- Changing the client clock or pausing JavaScript does not extend the deadline.

**Scenario**

**Given** a student with 10 minutes left  
**When** the countdown reaches 10 minutes, then 1 minute, then zero  
**Then** warnings appear at 10 minutes and 1 minute  
**And** at zero the server auto-submits all saved code even if the tab is closed, and changing the client clock does not extend the deadline

---

## F4 — Auto-Grading

### 4.1 — Queue Submission for Grading

**Priority:** High · **Story points:** 5 · **Sprint:** 5

> As the system, I want every submission queued the moment it arrives so that no submission is lost under burst load.

**Acceptance Criteria**

- A submission row is written with status "queued" before the API responds.
- Flask never executes student code in the request handler.
- Workers claim rows with SELECT ... FOR UPDATE SKIP LOCKED so that no submission is graded twice.
- Queued submissions survive a server or worker restart.

**Scenario**

**Given** a student submits a question  
**When** the API receives the request  
**Then** a row with status "queued" is written before the response is sent  
**And** Flask does not execute the code, workers claim rows with SKIP LOCKED so none is graded twice, and queued rows survive a restart

### 4.2 — Isolated Execution

**Priority:** High · **Story points:** 5 · **Sprint:** 4

> As the system, I want each submission run against all hidden tests in an isolated sandbox so that malicious code cannot harm the server or other students.

**Acceptance Criteria**

- Code runs in self-hosted Judge0 with network access disabled.
- CPU time, wall time and memory limits are enforced per test.
- A fork bomb or infinite loop is killed without affecting other submissions.
- One result row is stored per test case with stdout, stderr, time and memory.

**Scenario**

**Given** a queued submission and a worker  
**When** the worker runs it against all hidden tests in Judge0  
**Then** network access is disabled and CPU, wall-time and memory limits are enforced per test  
**And** an infinite loop or fork bomb is killed without affecting others, and one result row per test is stored

### 4.3 — Partial Credit

**Priority:** High · **Story points:** 2 · **Sprint:** 6

> As a student, I want partial credit for the tests I pass so that a mostly-correct answer isn't scored as zero.

**Acceptance Criteria**

- Score = (tests passed / tests total) × question points.
- Output comparison normalises trailing whitespace.
- tests_passed and tests_total are stored on the submission.
- Submission status changes to "graded" once all tests finish.

**Scenario**

**Given** a question worth 10 points with 5 hidden tests  
**When** a submission passes 3 tests  
**Then** the score is 6 (3/5 × 10)  
**And** tests_passed and tests_total are stored and the status becomes "graded" once all tests finish

### 4.4 — Distinct Failure Statuses

**Priority:** Medium · **Story points:** 2 · **Sprint:** 6

> As a teacher, I want each failure recorded with a specific status so that I can tell a wrong answer from a crash or a system fault.

**Acceptance Criteria**

- Statuses: Accepted, Wrong Answer, Time Limit, Memory Limit, Compile Error, Runtime Error, Internal Error.
- Each test result stores exactly one status.
- Internal Error is retried and flagged for the teacher, never scored as zero.
- If Judge0 is down, submissions stay queued and are retried.

**Scenario**

**Given** a submission whose tests produce a wrong answer, a timeout and a crash  
**When** grading completes  
**Then** each test result stores exactly one distinct status (e.g. Wrong Answer, Time Limit, Runtime Error)  
**And** an Internal Error is retried and flagged for the teacher, never scored as zero, and stays queued if Judge0 is down

### 4.5 — Live Grading Progress

**Priority:** Medium · **Story points:** 2 · **Sprint:** 6

> As a teacher, I want to see grading progress across the class so that I know when results are ready.

**Acceptance Criteria**

- Shows counts of queued, running and graded submissions.
- Progress updates by polling every few seconds, without reload.
- Submissions with Internal Error are highlighted.
- Only the exam's teacher and admins can view it.

**Scenario**

**Given** an exam with 30 submissions in various stages  
**When** the teacher opens the grading progress page  
**Then** counts of queued, running and graded submissions update by polling without a reload  
**And** submissions with Internal Error are highlighted, and only that exam's teacher and admins can see the page

### 4.6 — Re-run Grading

**Priority:** Medium · **Story points:** 2 · **Sprint:** 6

> As a teacher, I want to re-grade every submission to a question after fixing a bad test case so that students are scored fairly.

**Acceptance Criteria**

- Regrade re-queues every final submission for that question.
- Regrade requires confirmation showing how many submissions are affected.
- Manual overrides are kept and still shown after regrading.
- The regrade is recorded in the audit log.

**Scenario**

**Given** a question with a corrected test case and 20 final submissions  
**When** the teacher clicks Regrade  
**Then** a confirmation shows 20 affected submissions  
**And** after confirming, all are re-queued, manual overrides are kept and shown, and the audit log records the regrade

### 4.7 — Submission Review

**Priority:** High · **Story points:** 3 · **Sprint:** 6

> As a teacher, I want to see a student's code, console output and per-test results side by side so that I can judge whether the score is fair.

**Acceptance Criteria**

- Code is shown escaped inside a read-only block with line numbers.
- Each test shows input, expected output, actual output and status.
- Earlier submissions for the same question are viewable.
- Students cannot view other students' submissions (403).

**Scenario**

**Given** a graded submission  
**When** the teacher opens its review page  
**Then** the code appears escaped in a read-only block with line numbers, beside each test's input, expected output, actual output and status  
**And** earlier submissions are viewable, and another student requesting it receives 403

### 4.8 — Manual Score Override

**Priority:** Medium · **Story points:** 2 · **Sprint:** 6

> As a teacher, I want to override the automatic score with a written comment so that I can correct unfair machine grading.

**Acceptance Criteria**

- Override requires a score between 0 and the question's points, plus a comment.
- The automatic score is kept and shown beside the override.
- The override stores the teacher's ID and timestamp.
- Results and CSV export use the override when one exists.

**Scenario**

**Given** a submission with an automatic score of 6/10  
**When** the teacher enters an override of 8 with a comment  
**Then** the override is saved with the teacher's ID and timestamp, and the automatic score stays visible beside it  
**And** results and the CSV export use the override; a score above 10 or no comment is rejected

---

## F5 — Integrity & Monitoring

### 5.1 — Tab-Switch Logging

**Priority:** Medium · **Story points:** 2 · **Sprint:** 7

> As a teacher, I want tab switches and window blurs logged with timestamps so that I can see when a student left the exam.

**Acceptance Criteria**

- Every blur and return is sent to the server as an integrity event.
- Each event stores session, type and server timestamp.
- Events failing to send are retried when the connection returns.
- Logging never interrupts or blocks the student's work.

**Scenario**

**Given** a student in an active exam  
**When** they switch to another tab and return  
**Then** a blur and a return event are sent with session, type and server timestamp  
**And** failed sends are retried when the connection returns, and logging never blocks the student's work

### 5.2 — Full-Screen Monitoring

**Priority:** Medium · **Story points:** 1 · **Sprint:** 7

> As a teacher, I want the exam to request full-screen and log every exit so that I have an extra integrity signal.

**Acceptance Criteria**

- Full-screen is requested when the exam starts.
- Each exit is logged as a fullscreen_exit event.
- A banner offers to re-enter full-screen after an exit.
- Declining full-screen does not block the student from continuing.

**Scenario**

**Given** a student who has just started an exam  
**When** the exam requests full-screen and the student later exits it  
**Then** a fullscreen_exit event is logged and a banner offers to re-enter  
**And** if the student declines, they can continue the exam

### 5.3 — Paste Blocking

**Priority:** Medium · **Story points:** 1 · **Sprint:** 7

> As a teacher, I want pasting into the editor blocked and logged so that students cannot paste in prepared answers.

**Acceptance Criteria**

- Paste events in the exam editor are cancelled.
- Each attempt is logged as a paste_attempt event.
- The student sees a short notice that pasting is disabled.
- Paste stays enabled in practice and homework mode.

**Scenario**

**Given** a student in the exam editor  
**When** they try to paste text  
**Then** the paste is cancelled and a paste_attempt event is logged  
**And** a short notice says pasting is disabled, while paste still works in practice and homework mode

### 5.4 — Live Monitoring Dashboard

**Priority:** Medium · **Story points:** 3 · **Sprint:** 7

> As a teacher, I want a live dashboard during the exam so that I can see who is active and who needs attention.

**Acceptance Criteria**

- Dashboard lists every assigned student and their session status.
- Data refreshes by polling every few seconds.
- Students who have not started are clearly marked.
- Only the exam's teacher and admins can open it.

**Scenario**

**Given** an exam in progress with 25 assigned students  
**When** the teacher opens the live dashboard  
**Then** every assigned student and their session status is listed and refreshes by polling  
**And** students who have not started are clearly marked, and only the exam's teacher and admins can open it

### 5.5 — Per-Student Progress & Flags

**Priority:** Medium · **Story points:** 2 · **Sprint:** 7

> As a teacher, I want to see each student's progress and flag count during the exam so that I know who to walk past.

**Acceptance Criteria**

- Each row shows questions submitted, time remaining and flag count.
- Flag count is broken down by event type on hover or click.
- The table can be sorted by flag count.
- The screen states that flags are signals, not evidence of cheating.

**Scenario**

**Given** a student with several integrity events during an exam  
**When** the teacher views the dashboard row  
**Then** it shows questions submitted, time remaining and flag count, with a breakdown by event type on click  
**And** the table can be sorted by flag count, and a note states flags are signals, not evidence of cheating

### 5.6 — Post-Exam Integrity Report

**Priority:** Low · **Story points:** 2 · **Sprint:** 7

> As a teacher, I want an integrity report per student after the exam so that I can review any concerns calmly.

**Acceptance Criteria**

- Report lists every integrity event in time order.
- Report shows totals per event type.
- Report links to the student's submissions and code snapshots.
- Students cannot view integrity reports.

**Scenario**

**Given** a finished exam where a student has integrity events  
**When** the teacher opens that student's report  
**Then** events are listed in time order with totals per event type  
**And** links lead to the student's submissions and snapshots, and students cannot open the report

### 5.7 — Resume Interrupted Session

**Priority:** Medium · **Story points:** 2 · **Sprint:** 6

> As a student, I want to resume my exam after a crash or network drop so that I don't lose my work.

**Acceptance Criteria**

- Reopening the exam returns the student to the same session.
- The latest auto-saved code is restored for every question.
- No extra time is added; the server deadline is unchanged.
- The reconnect is logged as an integrity event.

**Scenario**

**Given** a student whose browser crashed mid-exam  
**When** they reopen the exam  
**Then** they return to the same session with the latest auto-saved code for every question  
**And** the server deadline is unchanged and the reconnect is logged as an integrity event

---

## F6 — Results & Administration

### 6.1 — Results Table

**Priority:** High · **Story points:** 2 · **Sprint:** 8

> As a teacher, I want a results table for each exam so that I can see every student's score at a glance.

**Acceptance Criteria**

- One row per student, one column per question, plus a total.
- Overridden scores are visibly marked.
- Table can be sorted by name or total score.
- Clicking a score opens that submission's review page.

**Scenario**

**Given** a graded exam with 30 students and 3 questions  
**When** the teacher opens the results table  
**Then** it shows one row per student, one column per question and a total, with overridden scores visibly marked  
**And** it can be sorted by name or total, and clicking a score opens that submission's review

### 6.2 — Export Grades to CSV

**Priority:** Medium · **Story points:** 1 · **Sprint:** 8

> As a teacher, I want to export grades as CSV so that I can import them into the college gradebook.

**Acceptance Criteria**

- CSV includes student name, email, per-question score and total.
- Final scores use overrides where they exist.
- File downloads with the exam title and date in its name.
- Only the exam's teacher and admins can export.

**Scenario**

**Given** a graded exam where some scores have overrides  
**When** the teacher clicks Export CSV  
**Then** a file named with the exam title and date downloads, with name, email, per-question scores and total  
**And** final scores use overrides where they exist, and non-owner teachers cannot export

### 6.3 — Per-Question Analytics

**Priority:** Low · **Story points:** 3 · **Sprint:** 8

> As a teacher, I want pass rates and average scores per question so that I can spot questions that were too hard or badly written.

**Acceptance Criteria**

- Shows pass rate and average score for each question.
- Shows the pass rate of each hidden test.
- Results are displayed as charts.
- Analytics are available only after grading completes.

**Scenario**

**Given** an exam where grading has completed  
**When** the teacher opens analytics  
**Then** pass rate and average score are shown per question, and the pass rate of each hidden test, as charts  
**And** before grading completes, analytics are unavailable

### 6.4 — Manage Users & Roles

**Priority:** High · **Story points:** 2 · **Sprint:** 1

> As an admin, I want to manage users and their roles so that the right people have the right access.

**Acceptance Criteria**

- User list shows name, email, role and active status.
- Admin can change role between student, teacher and admin.
- Deactivated users cannot log in.
- Every role or status change is recorded in the audit log.

**Scenario**

**Given** an admin viewing the user list  
**When** they change a user's role to teacher and deactivate another user  
**Then** the list shows name, email, role and active status with both changes applied  
**And** the deactivated user cannot log in and both changes are written to the audit log

### 6.5 — Manage Classes & Sections

**Priority:** High · **Story points:** 2 · **Sprint:** 1

> As an admin, I want to create and manage classes and sections so that exams can be assigned to the right groups.

**Acceptance Criteria**

- Class requires a name, section and assigned teacher.
- Students can be added to or removed from a class.
- A class with assigned exams cannot be deleted.
- Changes show immediately in teachers' class lists.

**Scenario**

**Given** an admin on the Classes page  
**When** they create a class with a name, section and assigned teacher, then add students  
**Then** the class appears immediately in that teacher's class list  
**And** a class with assigned exams cannot be deleted

### 6.6 — View Audit Log

**Priority:** Medium · **Story points:** 2 · **Sprint:** 8

> As an admin, I want to view the audit log so that I can trace who changed what and when.

**Acceptance Criteria**

- Log records user, action, entity and timestamp.
- Log can be filtered by user, action and date.
- Entries cannot be edited or deleted from the UI.
- Only admins can view the log.

**Scenario**

**Given** an admin on the audit log page  
**When** they filter by user, action and date  
**Then** matching entries show user, action, entity and timestamp  
**And** entries cannot be edited or deleted from the UI, and non-admins cannot view the log

### 6.7 — System Health

**Priority:** Low · **Story points:** 2 · **Sprint:** 8

> As an admin, I want to see queue depth and worker status so that I can spot problems before or during an exam.

**Acceptance Criteria**

- Shows the number of queued and running submissions.
- Shows whether Judge0 and each worker are reachable.
- A warning appears if a submission has been queued longer than a set time.
- The /api/health endpoint returns status for automated checks.

**Scenario**

**Given** an admin on the System Health page during an exam  
**When** a submission has been queued longer than the set time  
**Then** the page shows queued and running counts and whether Judge0 and each worker are reachable, with a warning for the stale submission  
**And** /api/health returns the status for automated checks

---

## F7 — Learning Platform

### 7.1 — Practice Mode

**Priority:** Medium · **Story points:** 2 · **Sprint:** 9

> As a student, I want to attempt published practice questions without a timer so that I can build skill before exams.

**Acceptance Criteria**

- Practice uses the same editor and Judge0 sandbox as exams.
- There is no timer and no limit on the number of runs.
- Attempts are saved to practice_attempts, never to exam submissions.
- No integrity events are logged in practice mode.

**Scenario**

**Given** a student on a published practice question  
**When** they run and save an attempt several times  
**Then** it uses the same editor and Judge0 sandbox as exams, with no timer or run limit  
**And** the attempts go to practice_attempts, never to exam submissions, and no integrity events are logged

### 7.2 — Filter Practice Bank

**Priority:** Low · **Story points:** 1 · **Sprint:** 9

> As a student, I want to filter practice questions by topic and difficulty so that I can focus on what I need to improve.

**Acceptance Criteria**

- Filters list topics and difficulty levels from the database.
- Topic and difficulty filters can be combined.
- A clear-filters option resets the list.
- A message appears when no questions match.

**Scenario**

**Given** a student on the practice bank page  
**When** they select a topic and a difficulty  
**Then** only questions matching both are listed  
**And** Clear filters resets the list, and a message appears when nothing matches

### 7.3 — Practice History

**Priority:** Low · **Story points:** 1 · **Sprint:** 9

> As a student, I want to see my practice history so that I can track my progress over time.

**Acceptance Criteria**

- Lists questions attempted with date and tests passed.
- Shows an overall pass rate across attempts.
- Sorted by most recent attempt first.
- Students see only their own history.

**Scenario**

**Given** a student who has attempted several practice questions  
**When** they open Practice History  
**Then** attempts show date and tests passed, most recent first, with an overall pass rate  
**And** they see only their own history

### 7.4 — Assign Homework

**Priority:** Medium · **Story points:** 2 · **Sprint:** 9

> As a teacher, I want to assign a set of questions as homework with a soft due date so that students practise between classes.

**Acceptance Criteria**

- Homework requires a title, a class and at least one question.
- Due date is shown to students but does not lock submission.
- Homework has no exam timer.
- Teacher can see which students have attempted each question.

**Scenario**

**Given** a teacher on the Assign Homework form  
**When** they enter a title, pick a class, add a question and set a due date  
**Then** homework is created with no exam timer and the due date is shown to students  
**And** the teacher can see which students have attempted each question

### 7.5 — Complete Homework

**Priority:** Medium · **Story points:** 2 · **Sprint:** 9

> As a student, I want to complete homework at my own pace using the same editor so that I practise in exam-like conditions.

**Acceptance Criteria**

- Homework opens in the practice screen with the due date shown.
- Student can leave and return without losing saved work.
- Late attempts are accepted and marked as late.
- Only students in the assigned class can open it.

**Scenario**

**Given** a student in the class with homework past its due date  
**When** they open it and submit an attempt  
**Then** it opens in the practice screen with the due date shown, and saved work persists if they leave and return  
**And** the late attempt is accepted and marked as late, and students outside the class cannot open it

### 7.6 — Author Practice Question

**Priority:** Low · **Story points:** 2 · **Sprint:** 9

> As a student, I want to write a practice question with test cases so that my classmates can learn from it.

**Acceptance Criteria**

- Form requires title, statement and at least one test case.
- Question is saved with source = student and no approval date.
- Question is not visible to classmates until approved.
- Author can see whether it is pending, approved or rejected.

**Scenario**

**Given** a student on the Author Practice Question form  
**When** they enter a title, statement and one test case and submit  
**Then** the question is saved with source = student and no approval date  
**And** classmates cannot see it until approved, and the author sees it as pending

### 7.7 — Moderate Student Questions

**Priority:** Low · **Story points:** 2 · **Sprint:** 9

> As a teacher, I want to approve, edit or reject student-authored questions so that only accurate questions reach the class.

**Acceptance Criteria**

- Moderation queue lists pending questions from my classes.
- Teacher can edit statement and tests before approving.
- Approval sets approved_at and publishes to the practice bank.
- Rejection requires a short reason shown to the author.

**Scenario**

**Given** a teacher with pending student questions in the queue  
**When** they edit the statement and approve one, and reject another with a reason  
**Then** approval sets approved_at and publishes it to the practice bank  
**And** the rejected author sees the teacher's reason, and rejection without a reason is not allowed

### 7.8 — Class Discussion Board

**Priority:** Low · **Story points:** 3 · **Sprint:** 9

> As a student or teacher, I want to post and read discussions for a class or question so that we can help each other outside class.

**Acceptance Criteria**

- Posts are scoped to a class, optionally to one question.
- New posts appear without a full page reload.
- Only class members and the teacher can read or post.
- The board is unavailable to students during an active exam session.

**Scenario**

**Given** a student in a class with a discussion board  
**When** they post a message tagged to one question  
**Then** it appears without a page reload for class members and the teacher  
**And** outsiders cannot read or post, and the board is unavailable during the student's active exam session

---

## F8 — AI Features

### 8.1 — AI Hint Assistant

**Priority:** Medium · **Story points:** 5 · **Sprint:** 10

> As a student, I want to ask the AI assistant for a hint in practice or homework so that I can get unstuck without being given the answer.

**Acceptance Criteria**

- Assistant replies with hints, questions or concept explanations, not full solutions.
- Adversarial prompts asking for the full answer are tested and refused.
- Hint requests are rate-limited per student.
- A friendly error appears if the LLM API is unavailable.

**Scenario**

**Given** a student stuck on a practice question  
**When** they ask the AI assistant for help, including a prompt demanding the full answer  
**Then** the assistant replies with hints or concept explanations, not a full solution  
**And** the full-answer prompt is refused, requests are rate-limited, and a friendly error appears if the LLM API is down

### 8.2 — Automatic Code Context

**Priority:** Medium · **Story points:** 2 · **Sprint:** 10

> As a student, I want the assistant to read my current code automatically so that I don't have to paste it into a chat box.

**Acceptance Criteria**

- Current editor content is sent with each hint request.
- The question statement and latest run output are included.
- Hidden test cases are never sent to the LLM.
- The hint panel shows which code version the hint refers to.

**Scenario**

**Given** a student asking for a hint in practice mode  
**When** the request is sent  
**Then** it includes the current code, the question statement and the latest run output  
**And** hidden test cases are never sent, and the hint panel shows which code version the hint refers to

### 8.3 — AI Blocked During Exams

**Priority:** Medium · **Story points:** 2 · **Sprint:** 10

> As a teacher, I want the AI assistant to be completely unreachable during an exam so that exam results reflect students' own work.

**Acceptance Criteria**

- The exam screen HTML does not include the AI assistant panel or its script.
- /api/ai/hint returns 403 for any student with an active exam session.
- No AI route exists under /api/exams/ or /api/sessions/.
- An automated test calls the hint route mid-exam and confirms it is refused.

**Scenario**

**Given** a student with an active exam session  
**When** they or a script call /api/ai/hint  
**Then** the request returns 403  
**And** the exam screen contains no AI panel or script, no AI route exists under /api/exams/ or /api/sessions/, and an automated test confirms the refusal

### 8.4 — AI-Assisted Integrity Flag

**Priority:** Low · **Story points:** 5 · **Sprint:** 10

> As a teacher, I want related integrity signals combined into one flag with evidence so that I review one clear item instead of many small alerts.

**Acceptance Criteria**

- A flag combines similarity, tab-switch and behavioural signals for one session.
- The flag shows which signals fired, when, and the raw evidence (diff, timestamps).
- Flags appear on the monitoring dashboard as "pending review".
- Flags are never shown to or sent to the student.

**Scenario**

**Given** a session with similarity, tab-switch and behavioural signals  
**When** the system raises an AI-assisted flag  
**Then** the flag lists which signals fired, when, and the raw evidence (diff, timestamps)  
**And** it appears on the dashboard as "pending review" and is never shown to the student

### 8.5 — Teacher Decision Required

**Priority:** Low · **Story points:** 2 · **Sprint:** 10

> As a student, I want any AI flag to need a teacher's decision before it affects me so that I'm never penalised by an automated system.

**Acceptance Criteria**

- No code path changes a grade, rejects a submission or locks a student from an AI flag alone.
- Acting on a flag requires reviewed_by, reviewed_at and a decision recorded.
- Each review decision is written to the audit log.
- An authorisation test confirms a consequence cannot be applied without a teacher decision.

**Scenario**

**Given** an AI integrity flag on a student's session  
**When** no teacher has reviewed it  
**Then** no grade, submission or access is changed by the flag alone  
**And** acting on it requires reviewed_by, reviewed_at and a decision, each decision is audit-logged, and an authorisation test confirms this
