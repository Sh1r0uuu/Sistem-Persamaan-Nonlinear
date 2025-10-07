
import numpy as np


def F(X):
    x, y = X[0], X[1]
    return np.array([x**2 + x*y - 10, y + 3*x*y**2 - 57])

def approximate_jacobian(X, h=1e-6):
    n = len(X)
    J_approx = np.zeros((n, n))
    f0 = F(X)
    for j in range(n):
        X_h = X.copy(); X_h[j] += h
        J_approx[:, j] = (F(X_h) - f0) / h
    return J_approx

def secant_method(x0, y0, tol=1e-6, max_iter=50):
    X = np.array([x0, y0], dtype=float)
    print("\n--- Metode Secant ---")
    print(f"{'Iter':<5} {'x':<25} {'y':<25}")
    print("-" * 60)
    
    for i in range(max_iter):
        print(f"{i:<5} {X[0]:<25.10f} {X[1]:<25.10f}")
        
        try:
            delta_X = np.linalg.solve(approximate_jacobian(X), -F(X))
        except np.linalg.LinAlgError:
            print("Matriks Jacobian singular/aproksimasi gagal. Iterasi dihentikan.")
            return
            
        X += delta_X
        if np.linalg.norm(delta_X) < tol:
            print(f"{i+1:<5} {X[0]:<25.10f} {X[1]:<25.10f}")
            print(f"\n✅ Solusi konvergen: x ≈ {X[0]:.6f}, y ≈ {X[1]:.6f}")
            return
            
            print(f"\n[OK] Solusi konvergen: x ≈ {X[0]:.6f}, y ≈ {Y[1]:.6f}")

if __name__ == "__main__":
    secant_method(1.5, 3.5)