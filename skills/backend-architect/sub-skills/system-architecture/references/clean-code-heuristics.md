# Clean Code Heuristics & Design Smells

A checklist for maintaining code quality during development and review.

## 💎 Naming & Functions
- **Intent-Revealing Names**: If a name requires a comment, it’s a bad name.
- **Small Functions**: Functions should be 20 lines or less. They should do **one thing**.
- **One Level of Abstraction**: Don't mix high-level business logic with low-level string manipulation in the same function.
- **Few Arguments**: 0-2 is ideal. 3+ requires a very strong reason.

## 🤮 Design Smells (The Red Flags)
- **Rigidity**: A single change requires a cascade of changes in other modules.
- **Fragility**: A change breaks unrelated parts of the system.
- **Immobility**: Parts of the system cannot be reused in other projects because of tight coupling.
- **Viscosity**: It’s easier to "hack" a solution than to follow the design patterns.

## 🛠️ Heuristics
- **DRY (Don't Repeat Yourself)**: Eliminate duplication at every level.
- **YAGNI (You Ain't Gonna Need It)**: Don't implement features "just in case."
- **Fail Fast**: Throw exceptions as early as possible when something goes wrong.
- **Symmetry**: Code should be balanced. If there is a `load()`, there should be a `save()`.
