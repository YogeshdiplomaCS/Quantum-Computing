# Quantum Computing: A First Qubit

This beginner-friendly example uses **Qiskit** to create a single qubit, put it into superposition with a Hadamard gate, and measure it. Measurement results are probabilistic.

## Requirements

- Python 3.10 or later
- Dependencies listed in `requirements.txt`

## Install and run

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python first_qubit.py
```

The script uses Qiskit's local statevector sampler, so it does not require access to a physical quantum computer or cloud account.

## What the program does

1. Starts one qubit in the `|0⟩` state.
2. Applies a Hadamard (`H`) gate to create an equal superposition.
3. Measures the qubit and prints the circuit and counts from 1,000 simulator shots.

Run it several times; due to sampling, counts vary around an even split.

## Run the test

```bash
python -m pytest
```
