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
# 2) Aplicar puerta Y al estado |1>  ->  Y|1> = -i|0>
# -----------------------------------------------------------
qcY1 = QuantumCircuit(1)
qcY1.x(0)  # prepara |1>
qcY1.y(0)  # aplica Y
psiY1 = Statevector.from_instruction(qcY1)

print("Estado tras Y|1>:", psiY1.data)  # esperado: [0.-1.j 0.+0.j]

figY1 = plot_bloch_multivector(psiY1)
figY1.suptitle("Bloch sphere: Y|1> = -i|0>")
plt.show()

# -----------------------------------------------------------
# 3) (Opcional) Guardar figuras para incluir en el PDF
# -----------------------------------------------------------
# fig1.savefig("bloch_1.png", dpi=300, bbox_inches="tight")
# figY1.savefig("bloch_Y_1.png", dpi=300, bbox_inches="tight")
