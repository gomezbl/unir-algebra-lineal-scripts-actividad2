import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

# -----------------------------------------------------------
# 1) Estado inicial |1>
# -----------------------------------------------------------
qc1 = QuantumCircuit(1)
qc1.x(0)  # prepara |1> a partir de |0>
psi1 = Statevector.from_instruction(qc1)

print("Estado inicial |1>:", psi1.data)  # esperado: [0.+0.j 1.+0.j]

# Visualizacion del estado |1> en Bloch
fig1 = plot_bloch_multivector(psi1)
fig1.suptitle("Bloch sphere: |1>")

plt.show()

# -----------------------------------------------------------
# 2) Aplicar puerta X al estado |1>  ->  X|1> = |0>
# -----------------------------------------------------------
qcX1 = QuantumCircuit(1)
qcX1.x(0)  # prepara |1>
qcX1.x(0)  # aplica X de nuevo: X|1> = |0>
psiX1 = Statevector.from_instruction(qcX1)

print("Estado tras X|1>:", psiX1.data)  # esperado: [1.+0.j 0.+0.j]

# Visualizacion del estado X|1> (= |0>) en Bloch
figX1 = plot_bloch_multivector(psiX1)
figX1.suptitle("Bloch sphere: X|1> = |0>")

plt.show()

# -----------------------------------------------------------
# 3) (Opcional) Guardar figuras para incluir en el PDF
# -----------------------------------------------------------
# fig1.savefig("bloch_ket1.png", dpi=300, bbox_inches="tight")
# figX1.savefig("bloch_X_ket1.png", dpi=300, bbox_inches="tight")
