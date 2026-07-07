---
name: quantum-engineering
description: "Master of quantum computing using Qiskit. Expert in building quantum circuits, transpilation optimization, and execution on IBM Quantum hardware."
---

# Quantum Engineering with Qiskit

Expertise in designing, optimizing, and executing quantum algorithms on simulators and real hardware.

## 🏗️ The Qiskit Workflow (Patterns)
1. **Map**: Translate the problem into quantum circuits and operators.
2. **Optimize**: Transpile the circuit for target hardware (Optimization levels 0-3).
3. **Execute**: Run on backend providers (IBM Quantum, Aer Simulators) using Primitives.
4. **Post-process**: Analyze results and mitigate errors.

## 🚀 Core Components
- **Quantum Circuits**: Build using gates (H, CX, RZ, etc.) and measurements.
- **Primitives (V2)**:
    - **Sampler**: For bitstring distributions and probability results.
    - **Estimator**: For computing expectation values of observables.
- **Transpilation**: Optimize for specific hardware topology and gate sets to minimize noise.

## ⚡ Hardware & Execution
- **IBM Quantum Runtime**: Use Sessions for iterative algorithms (VQE, QAOA) and Batch for parallel jobs.
- **Simulators**: Use `StatevectorSampler` for local noiseless testing.
- **Error Mitigation**: Apply resilience levels to improve result accuracy on real hardware.

## 📋 Verification Checklist
- [ ] Is the circuit transpiled for the specific target backend?
- [ ] Is the correct Primitive (Sampler vs Estimator) being used?
- [ ] Are iterative algorithms wrapped in a Runtime Session?
- [ ] Has the circuit been validated on a local simulator first?
- [ ] Are optimization levels (e.g., level 3) applied for production runs?

---

## 🔗 Quantum Framework Sub-Skills

- **[Cirq Quantum Engineering](sub-skills/cirq/SKILL.md)** — Google Quantum AI's Cirq framework for designing, simulating, and running quantum circuits. **Use when:** targeting Google/Sycamore hardware, performing gate decomposition, or running NumPy-backed circuit simulation with Cirq. **Not for:** Qiskit / IBM Quantum work — covered by this master's core Qiskit workflow.
