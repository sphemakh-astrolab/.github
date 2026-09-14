# sphemakh-astrolab -- conventions for coding agents

Organisation-wide baseline for the PHYS1026 astronomy computer labs. A
repository with its own `AGENTS.md` carries the conventions specific to it --
read that one too, and where the two disagree, **the repository's file wins**.
This file only holds what is true across all of them.

Lab template repositories are the exception: they never carry an `AGENTS.md`.
See *Student repositories* below.

## Core rule

Avoid unnecessary complexity like the plague.

Prefer the boring construct that a reader understands on sight. A mechanism
earns its place by removing more complexity than it adds, and a feature nobody
asked for is a liability, not a head start. When a repository's `AGENTS.md`
says a thing is deliberately left out, it is left out on purpose -- do not
helpfully add it back.

## This repository is public

`sphemakh-astrolab/.github` is the organisation's profile repository, and a
profile repository has to be public. Everything pushed here is world-readable
at once, and deleting it afterwards does not unpublish it. Never commit:

- **Student data:** names, student numbers, GitHub usernames matched to people,
  marks, or submission records. These live in the private, staff-only
  `lab-admin` repository and nowhere else.
- **Staff-only material:** instructor logistics such as the Digital Dome staff
  brief, memos, solutions and test papers. The Dome brief lives in a secret
  gist. A local working copy may sit in this checkout, excluded only by the
  clone-local `.git/info/exclude`, so a fresh clone has no such protection.
  Check `git status` before every commit.

## Two audiences

Everything student-facing is read by first-year students. They met C++ in
Semester 1, meet Python in Lab V, and work in Ubuntu under WSL on the lab's
Windows machines. Anything written for them -- course plan, announcements, lab
READMEs, starter files, slides -- follows these rules:

- **No answers.** Worked examples use different data from the exercise they
  support. A slide that solves Exercise 2 on the way to explaining slicing has
  taken Exercise 2 away.
- **Every snippet runs, and every output shown is real.** Run it before it
  ships. Starter files must run as handed out, with every `TODO` still in place.
- **Setup commands must work on a fresh Ubuntu WSL install.** For Python
  packages that means `apt` (`python3-numpy`), not `pip install` into the system
  Python, which recent Ubuntu refuses with `externally-managed-environment`.
- **Numbering matches the handout.** Labs are IV–IX in Semester 2; exercises
  and parts are numbered in the lab README, and everything else follows it.

## Policy is staff's call

Deadlines, late work, what counts as a submission, marking, and the schedule
are decided by the teaching staff. An agent describes the mechanism and leaves
the policy to them. "Your work is collected from `main` at midnight" describes
a mechanism; "anything pushed after midnight is not marked" sets a policy, and
was nearly shipped once. When wording needs a policy that has not been stated,
ask.

## Dates

[`course-plan/README.md`](course-plan/README.md) is the source of truth for the
schedule. Times are SAST (UTC+2); a deadline of "midnight" means 23:59 on that
date. A date is repeated in more places than it looks: announcements, the lab's
own README, and the `due` field `lab-admin` uses to snapshot submissions. A
changed date is not changed until every copy agrees.

## Student repositories

GitHub Classroom was retired on 28 August 2026. Each student now gets a
**private** repository per lab, named `<lab>-<github-username>`, generated from
that lab's template repository by `lab-admin`.

- **Never fork a template to a student, and never make a student repository
  public.** A fork of a public repository cannot be made private. The Lab IV
  and Lab V repositories created by Classroom were public forks, and making
  them private took rebuilding the fork network one repository at a time.
- **A template is copied verbatim into every student repository.** It holds
  only what students should see: no solutions, no staff notes, and no
  `AGENTS.md`. Generation copies files once, so a template fix made after a
  lab opens does not reach the repositories already created.

## Toolchain

There is no shared build. The labs use `g++` (Semester 1 and Lab IV) and
Python 3 with NumPy and Matplotlib from `apt`. Staff tooling is plain Python 3
(standard library only) driving the `gh` CLI. Slides are LaTeX Beamer, built
with `latexmk -pdf`.

## Attribution: commit trailers yes, PR trailers no

A commit made with an assistant's help says so in a trailer on the **commit
message**, naming the assistant and the model behind it:

```
Assisted-by: <LLM> <MODEL>
```

-- e.g. `Assisted-by: Claude Opus 5`, `Assisted-by: Codex GPT-5`. One line,
last in the message, after any `Co-authored-by:` for real people.

Agents default to a `Co-authored-by:` trailer with an address; replace it. Both
halves of that default are wrong here. `Co-authored-by:` claims more than
happened -- these tools assist, and the person who ran them owns the change and
answers for it. The address is what makes the claim bite: GitHub renders a
trailer as co-authorship only when one is present, so
`Co-authored-by: Claude <noreply@anthropic.com>` attaches a vendor to the
authorship of work this organisation owns. `Assisted-by:` with no address
records the same fact as plain text and attaches nobody.

Commits here from before September 2026 carry the old
`Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>` default. They are left
as they are -- history is not rewritten to change a trailer.

**Pull request descriptions carry no trailer at all** -- no `Assisted-by:`, no
`Co-authored-by:`, no "Generated with", no tool badge. A PR body is review
material: it exists to tell a reviewer what changed and why, and what to check.
Provenance already lives on every commit the PR contains, where it is attached
to the specific change rather than repeated once per PR, so a trailer in the
description is duplication in the one place that has no room for it. Agents
default to adding one; delete it.

Neither form is a substitute for the message itself. A commit that explains a
decision badly does not improve by naming the model that helped make it -- see
the existing history for the standard: what changed, what it deviates from and
why, and what a reviewer should not assume held still.

## Reviewing changes: check the tree, not just the diff

A diff shows what moved; it does not show what the change made wrong
elsewhere. Before calling work done, look at the other pages that describe the
thing you changed. When Classroom was retired, the course plan went on calling
every lab "a GitHub Classroom exercise" and telling students to open a pull
request to submit -- nothing in any diff was wrong, and the page was. A change
that leaves a page describing something that is no longer true is not
finished.
