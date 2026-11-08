"""Create and simulate a one-qubit superposition circuit with Qiskit."""

from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler


def build_circuit() -> QuantumCircuit:
    """Return a measured one-qubit circuit in an equal superposition."""
    circuit = QuantumCircuit(1, 1)
    circuit.h(0)
    circuit.measure(0, 0)
    return circuit


def main() -> None:
    circuit = build_circuit()
    sampler = StatevectorSampler()
    result = sampler.run([circuit], shots=1000).result()[0]
    counts = result.data.c.get_counts()

    print("Circuit:")
    print(circuit.draw())
    print("Measurement counts (expected approximately 50/50):")
    print(counts)


if __name__ == "__main__":
    main()
