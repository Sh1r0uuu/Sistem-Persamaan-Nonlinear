
import math


def g1A(x, y):
    """Fungsi iterasi untuk x dari f1."""
    if (10 - x * y) < 0: return None
    return math.sqrt(10 - x * y)

def g2A(x, y):
    """Fungsi iterasi untuk y dari f2."""
    return 57 - 3 * x * y**2

# --- Kombinasi g1B dan g2B ---
def g1B(x, y):
    """Fungsi iterasi alternatif untuk x dari f1."""
    if y == 0: return None
    return (10 - x**2) / y

def g2B(x, y):
    """Fungsi iterasi alternatif untuk y dari f2."""
    penyebut = 3 * x
    if penyebut == 0: return None
    pembilang = 57 - y
    if (pembilang / penyebut) < 0: return None
    return math.sqrt(pembilang / penyebut)