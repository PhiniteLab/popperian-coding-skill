# myMethods — every method attempted, in order, and the one that is current

```
myMethods/
  01-<name>-specification.md
  02-implementation-setup-plan.md
  03-<name>-v9-specification.md      <- the highest number is the CURRENT method
  04-v9-implementation-and-validation-plan.md
  evidence/                          <- the scripts that verified those specs
```

## Rules

- **The highest-numbered specification is the current method.** Earlier numbers are the
  history of how it got there and stay exactly as they were written. Never renumber, never
  delete a superseded version, and never present an earlier version as current.
- **A specification and its validation plan travel together.** A method with no executable
  validation plan is a proposal, not a method.
- `evidence/` holds the scripts that checked those specs — kernel verifications, exact
  enumerations, counterexample probes. They stay runnable so a verdict can be re-checked.
- The owner evaluates what is written here. An agent proposes and verifies; the decision
  that a method supersedes another is the owner's.
