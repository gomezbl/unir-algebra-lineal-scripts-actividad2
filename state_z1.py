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

fig1 = plot_bloch_multivector(psi1)
fig1.suptitle("Bloch sphere: |1>")
plt.show()

# -----------------------------------------------------------
# 2) Aplicar puerta Z al estado |1>  ->  Z|1> = -|1>
# -----------------------------------------------------------
qcZ1 = QuantumCircuit(1)
qcZ1.x(0)  # prepara |1>
qcZ1.z(0)  # aplica Z
psiZ1 = Statevector.from_instruction(qcZ1)

print("Estado tras Z|1>:", psiZ1.data)  # esperado: [0.+0.j -1.+0.j]

figZ1 = plot_bloch_multivector(psiZ1)
figZ1.suptitle("Bloch sphere: Z|1> = -|1>")
plt.show()

# -----------------------------------------------------------
# 3) (Opcional) Guardar figuras para incluir en el PDF
# -----------------------------------------------------------
# fig1.savefig("bloch_1.png", dpi=300, bbox_inches="tight")
# figZ1.savefig("bloch_Z_1.png", dpi=300, bbox_inches="tight")