import numpy as np
import matplotlib.pyplot as plt

from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

# -----------------------------------------------------------
# 1) Construccion del estado |1>
# -----------------------------------------------------------
psi = Statevector.from_label('1')  # |1>

print("Estado |1> (vector de estado):", psi.data)
# Esperado: [0.+0.j 1.+0.j]

# -----------------------------------------------------------
# 2) Visualizacion en la esfera de Bloch
# -----------------------------------------------------------
fig = plot_bloch_multivector(psi)

# Mostrar en pantalla
plt.show()

# (Opcional) Guardar en fichero (por ejemplo para incluir en el PDF)
# fig.savefig("bloch_ket1.png", dpi=300, bbox_inches="tight")
