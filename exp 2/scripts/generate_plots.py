#!/usr/bin/env python3
"""
generate_plots.py
=================
Experiment 2: Memory Performance Visualization (Virtual Machine vs Docker Container)

Generates publication-quality comparative visualizations comparing:
1. Memory Throughput (MiB/sec) - Higher is better
2. Total Execution Time (seconds) - Lower is better
3. Maximum Tail Latency (milliseconds) - Lower is better

Saves output plot to: ../images/memory-comparison.png
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    exp_dir = os.path.dirname(script_dir)
    images_dir = os.path.join(exp_dir, "images")
    os.makedirs(images_dir, exist_ok=True)

    # Modern high-contrast color scheme
    # Indigo for Virtual Machine, Teal/Emerald for Container
    vm_color = "#4F46E5"        # Indigo-600
    container_color = "#059669" # Emerald-600
    colors = [vm_color, container_color]

    labels = ["Ubuntu Virtual Machine\n(VMware Workstation)", "Docker Container\n(Process Isolation)"]

    # Quantitative empirical metrics
    throughput = [108900.87, 123725.89]   # MiB/sec
    total_time = [0.0931, 0.0819]         # Seconds
    max_latency = [3.04, 1.13]            # Milliseconds

    # Configure global Matplotlib styles
    plt.rcParams["font.sans-serif"] = ["Segoe UI", "DejaVu Sans", "Helvetica", "Arial"]
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["axes.edgecolor"] = "#CBD5E1"
    plt.rcParams["axes.linewidth"] = 0.9

    fig, axes = plt.subplots(1, 3, figsize=(15.5, 5.2), dpi=200)
    fig.patch.set_facecolor("#FFFFFF")
    plt.subplots_adjust(wspace=0.32, top=0.82, bottom=0.16)

    metrics_config = [
        {
            "data": throughput,
            "title": "Memory Throughput",
            "unit": "MiB / sec",
            "criterion": "▲ Higher is Better",
            "criterion_color": "#059669",
            "fmt": "{:,.2f}",
            "delta": "+13.61%",
            "delta_type": "positive"
        },
        {
            "data": total_time,
            "title": "Wall-Clock Execution Time",
            "unit": "Seconds (s)",
            "criterion": "▼ Lower is Better",
            "criterion_color": "#2563EB",
            "fmt": "{:.4f}",
            "delta": "-12.03%",
            "delta_type": "positive"
        },
        {
            "data": max_latency,
            "title": "Worst-Case Tail Latency",
            "unit": "Milliseconds (ms)",
            "criterion": "▼ Lower is Better",
            "criterion_color": "#DC2626",
            "fmt": "{:.2f}",
            "delta": "-62.83%",
            "delta_type": "positive"
        }
    ]

    for ax, cfg in zip(axes, metrics_config):
        data = cfg["data"]
        ax.set_facecolor("#FAFAFC")

        # Plot bars
        bars = ax.bar(
            labels,
            data,
            color=colors,
            width=0.52,
            edgecolor=["#3730A3", "#047857"],
            linewidth=1.2,
            zorder=3
        )

        # Title and Subtitle styling
        ax.set_title(cfg["title"], fontsize=12, fontweight="bold", color="#1E293B", pad=14)
        ax.text(
            0.5, 1.01,
            f"{cfg['criterion']}  [{cfg['unit']}]",
            transform=ax.transAxes,
            ha="center",
            va="bottom",
            fontsize=9.5,
            fontweight="semibold",
            color=cfg["criterion_color"]
        )

        ax.set_ylabel(cfg["unit"], fontsize=9.5, fontweight="normal", color="#475569")
        ax.tick_params(axis="x", labelsize=9, colors="#1E293B")
        ax.tick_params(axis="y", labelsize=8.5, colors="#64748B")

        # Light, subtle grid
        ax.grid(axis="y", linestyle="--", linewidth=0.7, color="#E2E8F0", alpha=0.9, zorder=1)
        ax.set_axisbelow(True)

        # Annotate exact bar values
        for bar, val in zip(bars, data):
            height = bar.get_height()
            ax.annotate(
                cfg["fmt"].format(val),
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 6),
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=9.5,
                fontweight="bold",
                color="#0F172A"
            )

        # Annotate advantage badge
        delta_label = f"Container Advantage: {cfg['delta']}"
        ax.text(
            0.5, 0.07,
            delta_label,
            transform=ax.transAxes,
            ha="center",
            va="center",
            fontsize=8.5,
            fontweight="bold",
            color="#047857",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#ECFDF5", edgecolor="#A7F3D0", linewidth=1.0)
        )

        # Upper headroom for value labels
        ax.set_ylim(0, max(data) * 1.20)

    # Global Figure Title
    fig.suptitle(
        "Sysbench Memory Performance Benchmark: Virtual Machine vs. Container\n"
        "[ Workload: 10 GiB Total Transfer | 1 MiB Block Size | 4 Parallel Threads | Sequential Global Write ]",
        fontsize=13,
        fontweight="bold",
        color="#0F172A",
        y=0.98
    )

    out_file = os.path.join(images_dir, "memory-comparison.png")
    plt.savefig(out_file, bbox_inches="tight", dpi=200, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close()
    print(f"[+] Benchmark visualization chart saved successfully: {out_file}")

if __name__ == "__main__":
    main()
