"""
LINE MAN Wongnai Pricing Assessment - Quiz 3 analysis.

Decomposes the delivery fee into:
    fee(rid, date, km) = base(rid, km) + surge(rid, date)

via two-way alternating least squares, then produces the summary stats and
charts referenced in assessment_response.md.

Usage:
    python analysis.py
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

HERE = Path(__file__).parent
CSV = HERE / "Copy of delivery_fee_movement.csv"
CHARTS = HERE / "charts"
CHARTS.mkdir(exist_ok=True)


def load() -> pd.DataFrame:
    df = pd.read_csv(CSV)
    df.columns = ["date", "city", "rid", "km", "fee"]
    df["date"] = pd.to_datetime(df["date"])
    return df


def decompose(df: pd.DataFrame, n_iter: int = 20) -> pd.DataFrame:
    """Two-way ALS: fee = base(rid,km) + surge(rid,date). Anchored so min surge = 0 per restaurant."""
    df = df.copy()
    df["surge"] = 0.0
    for _ in range(n_iter):
        base = (
            df.groupby(["rid", "km"], group_keys=False)
              .apply(lambda g: (g["fee"] - g["surge"]).mean(), include_groups=False)
              .rename("base").reset_index()
        )
        df = df.drop(columns=["base"], errors="ignore").merge(base, on=["rid", "km"])
        surge = (
            df.groupby(["rid", "date"], group_keys=False)
              .apply(lambda g: (g["fee"] - g["base"]).mean(), include_groups=False)
              .rename("surge_new").reset_index()
        )
        df = df.drop(columns=["surge_new"], errors="ignore").merge(surge, on=["rid", "date"])
        df["surge"] = df["surge_new"]
        df = df.drop(columns=["surge_new"])
    # Anchor: min surge per restaurant should be 0 (assume at least one zero-surge day per restaurant)
    min_surge = df.groupby("rid")["surge"].transform("min")
    df["surge"] = df["surge"] - min_surge
    df["base"] = df["base"] + min_surge
    # Snap to $0.25 grid to remove float noise
    df["base"] = (df["base"] * 4).round() / 4
    df["surge"] = (df["surge"] * 4).round() / 4
    return df


def report(df: pd.DataFrame) -> None:
    print(f"Mean fee : ${df['fee'].mean():.3f}")
    print(f"Mean base: ${df['base'].mean():.3f} ({df['base'].mean()/df['fee'].mean()*100:.1f}%)")
    print(f"Mean surge: ${df['surge'].mean():.3f} ({df['surge'].mean()/df['fee'].mean()*100:.1f}%)")
    print(f"Surge frequency: {(df['surge']>0.001).mean()*100:.1f}%")
    active = df.loc[df['surge'] > 0.001, 'surge']
    print(f"Surge|active mean=${active.mean():.2f}, median=${active.median():.2f}, max=${active.max():.2f}")


def charts(df: pd.DataFrame) -> None:
    daily = df.groupby('date').agg(fee=('fee','mean'), base=('base','mean'), surge=('surge','mean'))

    fig, ax = plt.subplots(figsize=(11, 4.5))
    ax.bar(daily.index, daily['base'], label='Base fee', color='#4C78A8')
    ax.bar(daily.index, daily['surge'], bottom=daily['base'], label='Dynamic surge', color='#F58518')
    ax.plot(daily.index, daily['fee'], color='black', marker='o', ms=3, lw=1, label='Total fee')
    ax.set_ylabel('Avg delivery fee ($)')
    ax.set_title('Daily avg delivery fee - base vs dynamic surge (Mar 2025)')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    ax.legend(); ax.grid(alpha=.3, axis='y')
    plt.tight_layout(); plt.savefig(CHARTS / '01_daily_decomposition.png', dpi=130); plt.close()

    dow_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    df_ = df.assign(dow=df['date'].dt.day_name())
    dow = df_.groupby('dow').agg(avg_surge=('surge','mean'),
                                  surge_freq=('surge', lambda s:(s>0.001).mean())).reindex(dow_order)
    fig, ax1 = plt.subplots(figsize=(9, 4.5))
    ax1.bar(dow.index, dow['avg_surge'], color='#F58518', label='Avg surge ($)')
    ax2 = ax1.twinx()
    ax2.plot(dow.index, dow['surge_freq']*100, color='#54A24B', marker='o', lw=2, label='% orders surged')
    ax1.set_ylabel('Avg surge ($)'); ax2.set_ylabel('% orders with surge>0')
    ax1.set_title('Surge by day of week'); ax1.grid(alpha=.3, axis='y')
    l1, lab1 = ax1.get_legend_handles_labels(); l2, lab2 = ax2.get_legend_handles_labels()
    ax1.legend(l1+l2, lab1+lab2, loc='upper left')
    plt.tight_layout(); plt.savefig(CHARTS / '03_surge_by_dow.png', dpi=130); plt.close()


if __name__ == "__main__":
    df = load()
    df = decompose(df)
    df.to_parquet(HERE / 'decomposed.parquet', index=False)
    report(df)
    charts(df)
    print("Done.")
