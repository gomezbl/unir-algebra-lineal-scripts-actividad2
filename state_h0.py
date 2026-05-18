import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

# -----------------------------------------------------------
# 1) Estado inicial |0>
# -----------------------------------------------------------
qc0 = QuantumCircuit(1)  # por defecto, inicializa en |0>
psi0 = Statevector.from_instruction(qc0)

print("Estado inicial |0>:", psi0.data)  # esperado: [1.+0.j 0.+0.j]

fig0 = plot_bloch_multivector(psi0)
fig0.suptitle("Bloch sphere: |0>")
plt.show()

# -----------------------------------------------------------
# 2) Aplicar puerta H al estado |0>  ->  H|0> = (|0>+|1>)/sqrt(2)
# -----------------------------------------------------------
qcH0 = QuantumCircuit(1)
qcH0.h(0)  # aplica la puerta H al qubit 0
psiH0 = Statevector.from_instruction(qcH0)

print("Estado tras H|0>:", psiH0.data)
# esperado: [1/sqrt(2) +0.j, 1/sqrt(2) +0.j]

figH0 = plot_bloch_multivector(psiH0)
figH0.suptitle("Bloch sphere: H|0> = (|0>+|1>)/sqrt(2)")
plt.show()

# -----------------------------------------------------------
# 3) (Opcional) Guardar figuras para incluir en el PDF
# -----------------------------------------------------------
# fig0.savefig("bloch_0.png", dpi=300, bbox_inches="tight")
# figH0.savefig("bloch_H_0.png", dpi=300, bbox_inches="tight")
