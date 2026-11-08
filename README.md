# Quantum Computing: A First Qubit

This beginner-friendly example uses **Qiskit** to create a single qubit, put it into superposition with a Hadamard gate, and measure it. It demonstrates a basic quantum circuit; measurement results are probabilistic.

## Requirements

- Python 3.10 or later
- Qiskit

## Install and run

```bash
python -m pip install qiskit
python first_qubit.py
```

The script uses Qiskit's local statevector simulator, so it does not require access to a quantum computer or cloud account.

## What the program does

1. Starts one qubit in the `|0⟩` state.
2. Applies a Hadamard (`H`) gate to create an equal superposition.
3. Measures the qubit and prints the circuit and counts from 1,000 simulator shots.

Run it several times; due to sampling, the counts may vary around an even split.
