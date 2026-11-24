# Week 4 Lab — From Informal Specs to SDD

**Time: 2 hours · API calls used: 0**

This whole lab is writing. No code runs except a six-line structure check at
the end. That is deliberate — the skill being built is specifying, and you
cannot build it by typing Python.

| # | Activity | Time |
|---|----------|------|
| 1 | Ambiguity hunt on your Semester 1 spec | 25 min |
| 2 | Rewrite that spec in SDD structure | 30 min |
| 3 | Write 8 acceptance criteria for it | 20 min |
| 4 | Write `SPEC.md` for the Spec Review Assistant | 35 min |
| 5 | Run the spec linter, swap with a partner | 10 min |

---

## 1. Ambiguity hunt (25 min)

Open `worksheets/ambiguity-hunt.md` and go through your Semester 1 spec line
by line. **By hand, before any tool does it for you.**

Four tells:

| Tell | Example |
|---|---|
| Unquantified adjective | "fast", "simple", "robust" |
| Undefined actor | "the system should notify the user" |
| Hidden decision | "handle invalid input appropriately" |
| No failure case | "the system reads the file" — and if it is not there? |

Most Semester 1 specs yield 6–12 findings. Fewer than four means you are
reading what you meant rather than what you wrote — swap with a partner.

**Keep this sheet.** In Week 7 you compare it against what your program finds.
If you never did it by hand, you have no way to judge whether the tool is
right, and judging the tool is what Week 7 is for.

---

## 2. Rewrite the spec in SDD structure (30 min)

Copy `templates/SPEC_TEMPLATE.md` to `SPEC_SEM1.md` and fill in the first
four sections for your Semester 1 project.

Two rules that do most of the work:

- **One behaviour per functional requirement.** If a row contains "and",
  consider splitting it.
- **Every non-functional requirement carries a number.** "Fast" is not a
  requirement. "Under 2 seconds for a 10-page file" is.

Section 4, **Out of Scope**, feels like a waste of time and is not. It is most
of what stops scope creep three weeks from now.

---

## 3. Write 8 acceptance criteria (20 min)

Section 5 of `SPEC_SEM1.md`. Eight criteria. Two rules:

1. **Binary.** Pass or fail, no judgement. If two reasonable people could
   disagree about whether it passed, rewrite it.
2. **Mapped.** Each one names the FR or NFR it tests.

The test: *can you say out loud how you would run it?* If not, it is not a
criterion.

> ~~The findings are helpful and well written.~~ — nobody can fail this.
>
> Every finding contains a `SUGGESTED:` line proposing a concrete rewrite. —
> you run it, you look, it is there or it is not.

---

## 4. Write `SPEC.md` for the Spec Review Assistant (35 min)

**This is the specification you implement in Week 7.** It is the centre of
Assessment A2.

The system: reads a specification from a PDF, reports untestable requirements,
ambiguous wording and missing failure conditions.

`SPEC.md` in this repo is the worked version. Read it, then write your own —
all six components:

1. Problem Statement
2. Functional Requirements (numbered)
3. Non-Functional Requirements (quantified)
4. Out of Scope
5. **8 Acceptance Criteria**, each mapped to a numbered requirement
6. Evaluation

Write it as if someone else will build it, because in three weeks' time
someone will — a version of you who has forgotten what you meant.

---

## 5. Lint it and swap (10 min)

```powershell
python -m pytest tests
```

Six structural checks: all six components present, exactly eight acceptance
criteria, every AC mapped to a requirement, no duplicate IDs, every NFR
quantified, no weasel words.

Point it at your own spec by editing the path at the top of
`tests/test_spec.py`.

**A passing linter does not mean a good spec.** It means the shape is right.
Now swap with a partner and read each other's for meaning — that is the part
no test can do.

---

## Before you leave

- [ ] Ambiguity hunt completed on your Semester 1 spec — **keep this sheet**
- [ ] `SPEC_SEM1.md` written with all six components
- [ ] 8 binary acceptance criteria, each mapped to a numbered requirement
- [ ] `SPEC.md` for the Spec Review Assistant written
- [ ] `python -m pytest tests` passes
- [ ] A partner has read your spec and you have read theirs

## Looking ahead

| Week | What happens to this spec |
|---|---|
| 5 | You write its 10-case test suite and its failure mode tables |
| 6 | You run a 5-ambiguity prompt against it **by hand** and save the output |
| 7 | You **implement** it, then compare what it finds against what you found |
