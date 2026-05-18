import numpy as np
import matplotlib.pyplot as plt

from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

# -----------------------------------------------------------
# 1) Construccion del estado |->
# -----------------------------------------------------------
# Opcion A (directa): etiqueta '-' de Qiskit
psi = Statevector.from_label('-')  # |->

print("Estado |-> (vector de estado):", psi.data)
# Esperado: [ 1/sqrt(2) +0.j, -1/sqrt(2) +0.j ]

# -----------------------------------------------------------
# 2) Visualizacion en la esfera de Bloch
# -----------------------------------------------------------
fig = plot_bloch_multivector(psi)

# Mostrar en pantalla
plt.show()

# (Opcional) Guardar en fichero para incluir en el PDF
# fig.savefig("bloch_ket_minus.png", dpi=300, bbox_inches="tight")
