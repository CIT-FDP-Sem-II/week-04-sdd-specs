# Week 4 — From Informal Specs to SDD

**CIT AI-Native Engineering Program · Year 1 · Semester 2 · Module M2**

Spec-Driven Development: writing the contract before writing the code. This is
the most important module of the semester, and this is the week that sets up
the next three.

**Lab time: 2 hours. API calls: 0.** See [LAB.md](LAB.md).

> **`SPEC.md` in this repo is the specification you implement in Week 7.**
> Write it properly now. In Week 7 you find out what you left out — that gap
> is the lesson.

## Contents

| Path | What it is |
|---|---|
| `SPEC.md` | The worked specification for the Spec Review Assistant — all six components |
| `templates/SPEC_TEMPLATE.md` | Empty version, for your Semester 1 spec rewrite |
| `worksheets/ambiguity-hunt.md` | Find the faults in your own spec, **by hand** |
| `tests/test_spec.py` | A six-check spec linter. No API calls. |

Nothing here calls an API. The skill being built is specifying, and you cannot
build it by typing Python.

## The six components of a spec

| # | Component | The question it answers |
|---|---|---|
| 1 | Problem Statement | What problem, for whom, and what is **not** a goal? |
| 2 | Functional Requirements | What does it do? (numbered, one behaviour each) |
| 3 | Non-Functional Requirements | How well? (**quantified** — every one has a number) |
| 4 | Out of Scope | What does it not do? |
| 5 | Acceptance Criteria | How do we know it is done? (**binary**, mapped to a requirement) |
| 6 | Evaluation | How do we know it is any good? |

## Binary acceptance criteria

The single idea this week turns on.

> ~~AC-x: The findings are helpful and well written.~~

Nobody can fail that. Two people will disagree and there is no resolution.

> AC-6: Every finding contains a `SUGGESTED:` line proposing a concrete
> rewrite.

You run it, you look, it is there or it is not.

The test: **can you say out loud how you would run it?** If not, it is not a
criterion.

## The spec linter

```powershell
python -m pytest tests
```

Six structural checks:

1. all six components present
2. exactly eight acceptance criteria
3. every AC maps to an FR or NFR
4. no duplicate requirement IDs
5. every NFR contains something countable
6. no unquantified weasel words

**A passing linter does not mean a good spec.** It means the shape is right.
Reading for meaning is still a human job — yours and your partner's.

## Why you do the ambiguity hunt by hand

In Week 7 you build a program that finds these faults automatically. In Week 7
you also have to say which of its findings were **wrong**.

You cannot judge a tool against a standard you never established. The hand
sheet from `worksheets/ambiguity-hunt.md` is that standard. Keep it.

---

## Set B (non-IT background)

There is almost no code this week, so the gap between the two sets is at its
smallest. The spec is the deliverable, and it is written in English either way.

**`tests/test_spec.py`** — the only code here. Six checks that read `SPEC.md`
as text and look for patterns: do the six headings exist, are there eight
rows starting `AC-`, does each of those rows also mention an `FR-` or `NFR-`
number, are any IDs repeated, does each `NFR-` row contain a number or a
counting word, and does the file contain any of the four banned vague phrases.

### What Set B may simplify

- Requirements and acceptance criteria **may be written in plain English**,
  provided each one states a clear pass/fail condition. "The program says
  which file it could not find, and stops" is a perfectly good criterion.
- You do not have to use the FR-1 / NFR-1 / AC-1 numbering style as long as
  every criterion clearly points at the requirement it tests.
- You may write six acceptance criteria rather than eight, provided at least
  two of them are failure cases.

### What Set B may **not** simplify

- **Every criterion must be binary.** This is the whole module. "The output
  is clear and helpful" fails in both sets.
- **Every non-functional requirement must carry a number.**
- The ambiguity hunt must be done **by hand** before Week 7.
