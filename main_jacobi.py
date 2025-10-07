
from fungsi_iterasi import g1A, g2A 

def jacobi_iteration(gx, gy, x0, y0, tol=1e-6, max_iter=100):
    x, y = x0, y0
    print(f"\n--- Metode Jacobi ({gx.__name__}, {gy.__name__}) ---")
    print(f"{'Iter':<5} {'x':<20} {'y':<20} {'Galat x':<15} {'Galat y':<15}")
    print("-" * 75)

    for i in range(1, max_iter + 1):
        x_old, y_old = x, y
        
        x_new, y_new = gx(x_old, y_old), gy(x_old, y_old)

        if x_new is None or y_new is None:
            print(f"Iterasi {i}: Perhitungan tidak valid (domain error). Iterasi dihentikan.")
            return

        x, y = x_new, y_new
        error_x, error_y = abs(x - x_old), abs(y - y_old)
        print(f"{i:<5} {x:<20.6f} {y:<20.6f} {error_x:<15.6f} {error_y:<15.6f}")

        if error_x < tol and error_y < tol:
            print(f"\n✅ Solusi konvergen: x ≈ {x:.6f}, y ≈ {y:.6f}")
            return
            
    print(f"\n Gagal konvergen setelah {max_iter} iterasi.")

if __name__ == "__main__":
    jacobi_iteration(g1A, g2A, x0=1.5, y0=3.5)