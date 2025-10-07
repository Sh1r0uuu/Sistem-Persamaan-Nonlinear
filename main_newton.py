
import numpy as np


def F(X):
    x, y = X[0], X[1]
    return np.array([x**2 + x*y - 10, y + 3*x*y**2 - 57])

def J(X):
    x, y = X[0], X[1]
    return np.array([[2*x + y, x], [3*y**2, 1 + 6*x*y]])

def newton_raphson(x0, y0, tol=1e-6, max_iter=50):
    X = np.array([x0, y0], dtype=float)
    print("\n--- Metode Newton-Raphson ---")
    print(f"{'Iter':<5} {'x':<25} {'y':<25}")
    print("-" * 60)
    
    for i in range(max_iter):
        print(f"{i:<5} {X[0]:<25.10f} {X[1]:<25.10f}")
        
        try:
            delta_X = np.linalg.solve(J(X), -F(X))
        except np.linalg.LinAlgError:
            print("Matriks Jacobian singular. Iterasi dihentikan.")
            return
        
        X += delta_X
        if np.linalg.norm(delta_X) < tol:
            print(f"{i+1:<5} {X[0]:<25.10f} {X[1]:<25.10f}")
            print(f"\n✅ Solusi konvergen: x ≈ {X[0]:.6f}, y ≈ {X[1]:.6f}")
            return
            
    print(f"\n Gagal konvergen setelah {max_iter} iterasi.")

if __name__ == "__main__":
    newton_raphson(1.5, 3.5)