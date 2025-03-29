import random
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

class PasswordGenerator:
    def __init__(self, length=8):
        self.length = length
        self.character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-*,+?=&#%^"

    def generate_random_password(self):
        password = ""
        for i in range(0, self.length, 1):
            current_length = 7
            qc = QuantumCircuit(current_length, current_length)
            qc.h(range(current_length))
            qc.measure(range(current_length), range(current_length))

            simulator = Aer.get_backend('qasm_simulator')
            compiled_circuit = transpile(qc, simulator)
            job = simulator.run(compiled_circuit, shots=1)
            result = job.result()
            counts = list(result.get_counts().keys())[0]

            index = int(counts, 2) % len(self.character_set)
            password += self.character_set[index]

        return password