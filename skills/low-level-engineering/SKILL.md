---
name: low-level-engineering
description: "Master of systems programming, memory management, and high-performance C/C++ development. Focuses on resource constraints, pointers, and manual memory control."
---

# Low-Level Systems Engineering

Expertise in building high-performance, resource-efficient systems with C and C++.

## 🏗️ Core Principles
- **Memory Ownership**: In C, every allocation (`malloc`) must have a `free`. In C++, prefer **RAII** and **Smart Pointers** (`std::unique_ptr`, `std::shared_ptr`) to eliminate manual `delete`.
- **RAII (Resource Acquisition Is Initialization)**: Bind resource lifecycle to object lifetime.
- **Pointer Safety**: Always validate pointers before dereferencing. Avoid pointer arithmetic where index access is safer.
- **Modern C++ Features**: Leverage Move Semantics (`std::move`), Lambda expressions, and Template Metaprogramming for zero-overhead abstractions.
- **Error Handling**: Check return values of system calls. In C++, use exception safety guarantees (Strong vs. Basic).

## ⚡ Performance & Optimization
- **Memory Alignment**: Ensure data structures are aligned for CPU cache efficiency.
- **Inlining**: Use `inline` for small, high-frequency functions.
- **Profiling**: Profile before optimizing. Use tools like `valgrind`, `gprof`, or `perf`.
- **Stack vs Heap**: Prefer stack allocation for small, local data to avoid heap overhead.

## 🛡️ Safety & Debugging
- **Valgrind**: Always check for memory leaks and invalid accesses.
- **Static Analysis**: Use `clang-tidy` or `cppcheck` to find potential bugs early.
- **Sanitizers**: Compile with AddressSanitizer (ASan) or ThreadSanitizer (TSan) during development.

## 📋 Verification Checklist
- [ ] Is all allocated memory properly freed in all execution paths?
- [ ] Are return values of system calls and allocations checked?
- [ ] Are there any potential buffer overflows or out-of-bounds accesses?
- [ ] Has the code been profiled for performance bottlenecks?
- [ ] Does the code pass static analysis and sanitizer checks?
