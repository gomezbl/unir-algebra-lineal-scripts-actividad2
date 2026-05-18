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
# 2) Aplicar puerta H al estado |1>
#    H|1> = (|0> - |1>)/sqrt(2)
# -----------------------------------------------------------
qcH1 = QuantumCircuit(1)
qcH1.x(0)  # prepara |1>
qcH1.h(0)  # aplica H
psiH1 = Statevector.from_instruction(qcH1)

print("Estado tras H|1>:", psiH1.data)
# esperado: [ 1/sqrt(2) +0.j, -1/sqrt(2) +0.j ]

figH1 = plot_bloch_multivector(psiH1)
figH1.suptitle("Bloch sphere: H|1> = (|0>-|1>)/sqrt(2)")
plt.show()

# -----------------------------------------------------------
# 3) (Opcional) Guardar figuras para incluir en el PDF
# -----------------------------------------------------------
# fig1.savefig("bloch_1.png", dpi=300, bbox_inches="tight")
# figH1.savefig("bloch_H_1.png", dpi=300, bbox_inches="tight")
