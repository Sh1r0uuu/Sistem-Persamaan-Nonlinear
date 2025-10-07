
from fungsi_iterasi import g1A, g2A 

def seidel_iteration(gx, gy, x0, y0, tol=1e-6, max_iter=100):
    x, y = x0, y0
    print(f"\n--- Metode Seidel ({gx.__name__}, {gy.__name__}) ---")
    print(f"{'Iter':<5} {'x':<20} {'y':<20} {'Galat x':<15} {'Galat y':<15}")
    print("-" * 75)

    for i in range(1, max_iter + 1):
        x_old, y_old = x, y
        
        x = gx(x_old, y_old) 
        if x is None:
            print(f"Iterasi {i}: Perhitungan x tidak valid. Iterasi dihentikan.")
            return

        y = gy(x, y_old) 
        if y is None:
            print(f"Iterasi {i}: Perhitungan y tidak valid. Iterasi dihentikan.")
            return
        
        error_x, error_y = abs(x - x_old), abs(y - y_old)
        print(f"{i:<5} {x:<20.6f} {y:<20.6f} {error_x:<15.6f} {error_y:<15.6f}")

        if error_x < tol and error_y < tol:
            print(f"\n✅ Solusi konvergen: x ≈ {x:.6f}, y ≈ {y:.6f}")
            return

    print(f"\n Gagal konvergen setelah {max_iter} iterasi.")

if __name__ == "__main__":
    seidel_iteration(g1A, g2A, x0=1.5, y0=3.5)