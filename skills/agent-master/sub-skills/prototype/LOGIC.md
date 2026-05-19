A tiny interactive terminal app that lets the user drive a state model by hand. Use this when the question is about **business logic, state transitions, or data shape** — the kind of thing that looks reasonable on paper but only feels wrong once you push it through real cases.

- "I'm not sure if this state machine handles the edge case where X then Y."
- "Does this data model actually let me represent the case where..."
- "I want to feel out what the API should look like before writing it."
- Anything where the user wants to **press buttons and watch state change**.

If the question is "what should this look like" — wrong branch. Use [UI.md](UI.md).

### 1. State the question
Before writing code, write down what state model and what question you're prototyping. One paragraph, in the prototype's README or a comment at the top of the file. A logic prototype that answers the wrong question is pure waste.

### 2. Pick the language
Use whatever the host project uses. Match the project's existing conventions for tooling.

### 3. Isolate the logic in a portable module
Put the actual logic behind a small, pure interface that could be lifted out and dropped into the real codebase later. The TUI around it is throwaway; the logic module shouldn't be.

The right shape depends on the question:

- **A pure reducer** — `(state, action) => state`. Good when actions are discrete events and state is a single value.
- **A state machine** — explicit states and transitions. Good when "which actions are even legal right now" is part of the question.
- **A small set of pure functions** over a plain data type. Good when there's no implicit current state — just transformations.
- **A class or module with a clear method surface** when the logic genuinely owns ongoing internal state.

Keep it pure: no I/O, no terminal code. The TUI imports it and calls into it; nothing flows the other direction.

### 4. Build the smallest TUI that exposes the state
Build it as a **lightweight TUI** — on every tick, clear the screen and re-render the whole frame. Each frame has:

1. **Current state**, pretty-printed and diff-friendly (one field per line, or formatted JSON).
2. **Keyboard shortcuts**, listed at the bottom: `[a] add user  [d] delete user  [t] tick clock  [q] quit`.

Behaviour: Initialise state → Read one keystroke at a time → Dispatch to handler → Re-render full frame → Loop until quit.

### 5. Make it runnable in one command
Add a script to the project's existing task runner. The user should never need to remember a path.

### 6. Hand it over
Give the user the run command. The interesting moments are when they say "wait, that shouldn't be possible" or "huh, I assumed X would be different" — those are the bugs in the _idea_.

### 7. Capture the answer
When done, ask what it taught them. Leave a `NOTES.md` next to the prototype with the verdict before deleting.

**Don'ts:**
- Don't add tests. A prototype that needs tests is no longer a prototype.
- Don't wire it to the real database. Use an in-memory store.
- Don't generalise. The prototype answers one question.
- Don't blur the logic and the TUI together.
