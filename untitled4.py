from qiskit import execute, Aer, QuantumCircuit
from math import sqrt


qc = QuantumCircuit(1)
initial_state = [1/sqrt(2), 1/sqrt(2)]
qc.initialize(initial_state, 0)
qc.measure_all()
qc.draw(output='text')





from qiskit import execute, Aer, QuantumCircuit
from math import sqrt
from sklearn.metrics import recall_score, precision_score,
confusion_matrix

def pqc_classify():
    backend = Aer.get_backend('statevector_simulator')
    
    initial_state = [1/sqrt(2), 1/sqrt(2)]
    """backend −− a qiskit backend to run the quantum circuit at
    passenger_state −− a valid quantum state vector"""
    # Create a quantum circuit with one qubit
    qc = QuantumCircuit(1)
    
    # Define state |Psi> and initialize the circuit
    qc.initialize(initial_state, 0)
    
    # Measure the qubit
    qc.measure_all()
    
    # run the quantum circuit
    result=execute(qc,backend).result()
    
    # get the counts, these are either {'0': 1} or {'1': 1}
    counts=result.get_counts(qc)
    
    # get the bit 0 or 1
    return int(list(map(lambda item: item[0], counts.items()))[0])


pqc_classify()
