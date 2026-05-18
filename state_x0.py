import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

# -----------------------------------------------------------
# 1) Estado inicial |0>
# -----------------------------------------------------------
qc0 = QuantumCircuit(1)  # por defecto, el estado inicial es |0>
psi0 = Statevector.from_instruction(qc0)

print("Estado inicial |0>:", psi0.data)  # esperado: [1.+0.j 0.+0.j]

# Visualizacion del estado |0> en Bloch
fig0 = plot_bloch_multivector(psi0)
fig0.suptitle("Bloch sphere: |0>")

# -----------------------------------------------------------
# 2) Aplicar puerta X al estado |0>  ->  X|0> = |1>
# -----------------------------------------------------------
qcX = QuantumCircuit(1)
qcX.x(0)  # aplica la puerta X al qubit 0
psiX = Statevector.from_instruction(qcX)

print("Estado tras X|0>:", psiX.data)  # esperado: [0.+0.j 1.+0.j]

# Visualizacion del estado X|0> (= |1>) en Bloch
figX = plot_bloch_multivector(psiX)
figX.suptitle("Bloch sphere: X|0> = |1>")

plt.show()

# -----------------------------------------------------------
# 3) (Opcional) Guardar figuras para incluir en el PDF
# -----------------------------------------------------------
# fig0.savefig("bloch_ket0.png", dpi=300, bbox_inches="tight")
# figX.savefig("bloch_X_ket0.png", dpi=300, bbox_inches="tight")
