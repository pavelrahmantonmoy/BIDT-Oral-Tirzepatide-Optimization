"""
Biologically Informed Digital Twin (BIDT) - Module 02
Response Surface Methodology (RSM) via Central Composite Design (CCD)
Stat-Ease 360 Benchmark Model Re-construction
Author: Pavel Rahman Tonmoy
"""

import numpy as np
import pandas as pd
from scipy.optimize import minimize

# 13-Run Central Composite Design Data Matrix from Stat-Ease
ccd_data = {
    "Std": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    "Run": [4, 6, 10, 3, 1, 13, 7, 2, 8, 12, 5, 9, 11],
    "Factor_A_HPMC_K100M": [
        15.0,
        35.0,
        15.0,
        35.0,
        10.86,
        39.14,
        25.0,
        25.0,
        25.0,
        25.0,
        25.0,
        26.5,
        25.0,
    ],
    "Factor_B_SNAC_Ratio": [
        5.0,
        5.0,
        25.0,
        25.0,
        15.0,
        15.0,
        0.86,
        29.14,
        15.0,
        15.0,
        15.0,
        16.8,
        15.0,
    ],
    "R3_Desirability_Score": [
        0.20,
        0.35,
        0.38,
        0.42,
        0.12,
        0.58,
        0.28,
        0.68,
        0.915,
        0.920,
        0.910,
        0.945,
        0.915,
    ],
}

df = pd.DataFrame(ccd_data)


def rsm_predict_desirability(A, B):
    """
    Polynomial Response Surface approximation for Desirability
    Peak centered around A = 25.0% (HPMC K100M) and B = 15.0 (SNAC Ratio)
    """
    term_a = -0.0035 * (A - 25.0) ** 2
    term_b = -0.0028 * (B - 15.0) ** 2
    desirability = 0.920 + term_a + term_b
    return np.clip(desirability, 0.0, 1.0)


print("=" * 65)
print("RSM CENTRAL COMPOSITE DESIGN (CCD) OPTIMIZATION SUMMARY")
print("=" * 65)
print(df[["Std", "Run", "Factor_A_HPMC_K100M", "Factor_B_SNAC_Ratio", "R3_Desirability_Score"]])

# Identify maximum desirability point from the design matrix
opt_idx = df["R3_Desirability_Score"].idxmax()
opt_row = df.loc[opt_idx]

print("\n" + "=" * 65)
print("OPTIMAL FORMULATION COORDINATES (DESIGN SPACE APEX)")
print("=" * 65)
print(f"Optimal Factor A (HPMC K100M Conc. %) : {opt_row['Factor_A_HPMC_K100M']}%")
print(f"Optimal Factor B (SNAC Molar Ratio)   : {opt_row['Factor_B_SNAC_Ratio']}")
print(f"Maximized Desirability Score (D)      : {opt_row['R3_Desirability_Score']}")
print("=" * 65)
