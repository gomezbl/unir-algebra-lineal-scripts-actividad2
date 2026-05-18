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
# 2) Aplicar puerta Y al estado |0>  ->  Y|0> = i|1>
# -----------------------------------------------------------
qcY0 = QuantumCircuit(1)
qcY0.y(0)  # aplica la puerta Y al qubit 0
psiY0 = Statevector.from_instruction(qcY0)

print("Estado tras Y|0>:", psiY0.data)  # esperado: [0.+0.j 0.+1.j]

figY0 = plot_bloch_multivector(psiY0)
figY0.suptitle("Bloch sphere: Y|0> = i|1>")
plt.show()

# -----------------------------------------------------------
# 3) (Opcional) Guardar figuras para incluir en el PDF
# -----------------------------------------------------------
# fig0.savefig("bloch_0.png", dpi=300, bbox_inches="tight")
# figY0.savefig("bloch_Y_0.png", dpi=300, bbox_inches="tight")
