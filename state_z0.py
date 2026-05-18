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
# 2) Aplicar puerta Z al estado |0>  ->  Z|0> = |0>
# -----------------------------------------------------------
qcZ0 = QuantumCircuit(1)
qcZ0.z(0)  # aplica la puerta Z al qubit 0
psiZ0 = Statevector.from_instruction(qcZ0)

print("Estado tras Z|0>:", psiZ0.data)  # esperado: [1.+0.j 0.+0.j]

figZ0 = plot_bloch_multivector(psiZ0)
figZ0.suptitle("Bloch sphere: Z|0> = |0>")
plt.show()

# -----------------------------------------------------------
# 3) (Opcional) Guardar figuras para incluir en el PDF
# -----------------------------------------------------------
# fig0.savefig("bloch_0.png", dpi=300, bbox_inches="tight")
# figZ0.savefig("bloch_Z_0.png", dpi=300, bbox_inches="tight")
