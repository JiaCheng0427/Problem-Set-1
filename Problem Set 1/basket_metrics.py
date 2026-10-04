"""Functions for auditing basket data and calculating robust means."""

import numpy as np
import pandas as pd
from scipy import stats


def audit_report(df: pd.DataFrame) -> pd.DataFrame:
    """Return one row per column with missingness, dtype, skew, and outlier count."""
    rows = []

    for col in df.columns:
        x = df[col]

        if pd.api.types.is_numeric_dtype(x):
            q1 = x.quantile(0.25)
            q3 = x.quantile(0.75)
            iqr = q3 - q1

            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr

            outlier_count = ((x < lower) | (x > upper)).sum()
            skew = x.skew()
        else:
            outlier_count = 0
            skew = np.nan

        rows.append({
            "column": col,
            "missingness": x.isna().mean(),
            "dtype": str(x.dtype),
            "skew": skew,
            "outlier_count": outlier_count
        })

    return pd.DataFrame(rows)


def robust_mean(x, method: str = "median") -> float:
    """Return a robust center using median, trimmed mean, or B2B exclusion."""
    x = pd.Series(x).dropna()

    if method == "median":
        return float(x.median())

    if method == "trimmed":
        return float(stats.trim_mean(x, 0.1))

    if method == "exclude_b2b":
        return float(x[x <= 500].mean())

    raise ValueError("Unknown method")

if __name__ == "__main__":
    demo = pd.Series([40, 50, 60, 1000])
    print(robust_mean(demo, "exclude_b2b"))
