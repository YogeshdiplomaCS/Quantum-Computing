from first_qubit import build_circuit


def test_first_qubit_circuit_has_hadamard_and_measurement():
    circuit = build_circuit()

    assert circuit.num_qubits == 1
    assert circuit.num_clbits == 1
    assert circuit.count_ops()["h"] == 1
    assert circuit.count_ops()["measure"] == 1
