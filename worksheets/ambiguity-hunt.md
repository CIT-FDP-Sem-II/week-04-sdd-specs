# Worksheet 1 — Ambiguity Hunt

**Do this by hand, before any tool does it for you.** (25 minutes)

This is the point of Week 4. In Week 7 you build a program that finds these
automatically, and in Week 7 you compare its findings against this sheet. If
you never did it by hand, you have no way to judge whether the tool is right.

## Open your Semester 1 spec

Go through it line by line. Every time you hit one of these, write it down.

### The four tells

| Tell | Example | Why it fails |
|---|---|---|
| **Unquantified adjective** | "fast", "simple", "user-friendly", "robust" | No number, so no test |
| **Undefined actor** | "the system should notify the user" | Which user? Notify how? |
| **Hidden decision** | "handle invalid input appropriately" | "Appropriately" is the entire design, unwritten |
| **No failure case** | "the system reads the file" | What if it is not there? Empty? Locked? |

### Your findings

| # | Exact phrase from your spec | Which tell | What it should say instead |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |

Most Semester 1 specs yield 6–12. If you found fewer than four, you are
reading what you meant rather than what you wrote. Swap with a partner and
read theirs — it is much easier on someone else's.

## The one that broke something

Of everything above, which one actually caused a problem when you built the
Semester 1 project — a rewrite, an argument, a feature that did the wrong
thing?

> Phrase:
>
> What it cost:

Keep this. It is the strongest argument you have for why SDD is worth the
hour it costs.
