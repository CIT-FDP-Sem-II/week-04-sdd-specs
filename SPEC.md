# SPEC — Spec Review Assistant

**Author:** (your name) · **Version:** 1.0 · **Date:** Week 4

> This is the specification you will **implement in Week 7**. Write it
> properly now. In Week 7 you find out what you left out, and that gap is the
> actual lesson of the module.

A complete spec has **six components**. All six are below.

---

## 1. Problem Statement

Students write specifications that look finished but are not testable. A
requirement like "the system should respond quickly" cannot be passed or
failed, so nobody notices it is meaningless until the code is built and the
argument starts.

Reading your own spec for these faults is hard, because you know what you
meant. A second reader catches them; a second reader is not always available.

**The Spec Review Assistant** reads a specification from a PDF and reports
three faults: untestable requirements, ambiguous wording, and missing failure
conditions.

**Who it is for:** a student in Week 4 of this module, about to commit a spec.
**What success looks like:** it finds faults the author missed, and the author
can tell which of its findings are wrong.

**Explicitly not a goal:** judging whether the spec describes a good product.
It judges whether the spec is *specified*, not whether it is *wise*.

---

## 2. Functional Requirements

What the system does. Numbered, so acceptance criteria can point at them.

| ID | Requirement |
|---|---|
| **FR-1** | The system accepts a path to a PDF file as a command-line argument. |
| **FR-2** | The system extracts the text of every page of that PDF. |
| **FR-3** | The system sends the extracted text to the Gemini API inside a context package built from the five roles. |
| **FR-4** | The system reports findings in exactly three categories: `UNTESTABLE`, `AMBIGUOUS`, `MISSING FAILURE CONDITION`. |
| **FR-5** | Each finding quotes the exact phrase from the specification that triggered it. |
| **FR-6** | Each finding states what would make it pass instead — a concrete rewrite, not "be more specific". |
| **FR-7** | The system writes all findings to a file in `output/`, named after the input PDF. |
| **FR-8** | The system also prints the findings to the terminal. |
| **FR-9** | The system reports the number of findings in each category at the end. |

---

## 3. Non-Functional Requirements

How well it does it. **Quantified** — a non-functional requirement with no
number is a wish.

| ID | Requirement |
|---|---|
| **NFR-1** | A specification of up to 10 pages is processed in **one** API call. |
| **NFR-2** | The whole run completes in under **60 seconds** for a 10-page PDF. |
| **NFR-3** | The API key is read from the environment. It appears in **no** file in the repository. |
| **NFR-4** | The system handles a missing file, an unreadable PDF and a failed API call **without a traceback**, printing a one-line message naming which of the three occurred. |
| **NFR-5** | Each of the five classes is under **80 lines**. |
| **NFR-6** | Running the same PDF twice produces findings in the same three categories, even if the wording differs. |

---

## 4. Out of Scope

Stating this is half of what stops scope creep in Week 7.

- Editing or rewriting the specification file itself
- Judging whether the product described is a good idea
- Any PDF that is a scan with no text layer (NFR-4 covers reporting this)
- Any format other than PDF
- Comparing two specifications against each other
- A web interface, a database, or storing findings between runs

---

## 5. Acceptance Criteria

Eight criteria. Each is **binary** — pass or fail, no judgement — and each
**maps to a numbered requirement**.

| ID | Criterion | Tests |
|---|---|---|
| **AC-1** | Given a valid 3-page PDF, the system prints findings and exits with code 0. | FR-1, FR-2, FR-8 |
| **AC-2** | Given a path that does not exist, the system prints `Cannot find <path>` and exits with code 1, with no traceback. | NFR-4 |
| **AC-3** | Given a PDF with no extractable text, the system prints `No text found in <path>` and exits with code 1. | FR-2, NFR-4 |
| **AC-4** | Every finding in the output begins with one of exactly three labels: `UNTESTABLE`, `AMBIGUOUS`, `MISSING FAILURE CONDITION`. | FR-4 |
| **AC-5** | Every finding contains a quoted phrase that appears verbatim in the source PDF text. | FR-5 |
| **AC-6** | Every finding contains a `SUGGESTED:` line proposing a concrete rewrite. | FR-6 |
| **AC-7** | After a successful run, `output/` contains a file named after the input PDF, holding the same findings that were printed. | FR-7 |
| **AC-8** | With `GEMINI_API_KEY` unset, the system prints `GEMINI_API_KEY is not set` and exits with code 1, **before** reading the PDF. | NFR-3, NFR-4 |

### Why these are binary

Compare the two:

> ~~AC-x: The findings are helpful and well written.~~

Nobody can fail that. Two people will disagree, and the disagreement has no
resolution.

> AC-6: Every finding contains a `SUGGESTED:` line proposing a concrete
> rewrite.

You run it, you look, it is there or it is not. That is the whole test.

---

## 6. Evaluation

How you will know it works — beyond the eight criteria passing.

| Question | How it is answered |
|---|---|
| Does it find faults a human missed? | Run it on your own Semester 1 spec. Compare its findings to the list you made by hand in Week 4 and the ambiguities you found in Week 6. |
| How often is it wrong? | Count its findings in three buckets: **caught** (you found it too), **missed** (you found it, it did not), **wrong** (it found it, you disagree). |
| Is it stable? | Run the same PDF twice. NFR-6 says the categories should match. |
| Did it change your spec? | `SPEC_REBUILT.md` in Week 7: every change traceable to a finding, with **at least one finding rejected and the reason given**. |

The rejected finding matters. A tool you never disagree with is a tool you
have stopped reading.

---

## Change log

| Version | Date | Change | Why |
|---|---|---|---|
| 1.0 | Week 4 | First version | — |
| | Week 7 | *(you will add rows here)* | *What the implementation forced you to change* |
