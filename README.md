# Cloud Computing Laboratory

[![Course: Cloud Computing](https://img.shields.io/badge/Course-Cloud%20Computing-4F46E5?style=flat-square&logo=google-cloud&logoColor=white)](https://github.com)
[![Status: Completed](https://img.shields.io/badge/Status-Completed-059669?style=flat-square)](https://github.com)
[![Linux: Ubuntu 24.04 LTS](https://img.shields.io/badge/Environment-Ubuntu%2024.04%20LTS-E95420?style=flat-square&logo=ubuntu&logoColor=white)](https://github.com)

This experiment contains laboratory experiments, benchmarking suites, container definitions, telemetry logs, and performance analyses evaluating virtualization paradigms and cloud infrastructure performance.

---

## 📂 Laboratory Experiments

| Experiment | Title | Focus Area | Status | Documentation |
| :---: | :--- | :--- | :---: | :---: |
| **02** | **Memory Performance Evaluation: Virtual Machine vs. Docker Container** | Sysbench Memory Benchmarking, EPT/NPT 2D Page Walk Analysis, cgroups v2 | ✅ Completed | [View Exp 2 README](exp%202/README.md) |

---

## 🚀 Quick Navigation

- **[Experiment 2: Memory Performance Evaluation](exp%202/README.md)**
  - Automated benchmark harness: [`exp 2/scripts/benchmark.sh`](exp%202/scripts/benchmark.sh)
  - Results parser and statistical delta calculator: [`exp 2/scripts/parse_sysbench.py`](exp%202/scripts/parse_sysbench.py)
  - Visualization generator: [`exp 2/scripts/generate_plots.py`](exp%202/scripts/generate_plots.py)
  - Benchmarking container: [`exp 2/docker/Dockerfile`](exp%202/docker/Dockerfile)
  - Experimental data logs: [`exp 2/results/`](exp%202/results/)

---

## ⚙ Prerequisites & Dependencies

To execute and reproduce the laboratory benchmarks locally:

```bash
# Ubuntu / Debian
sudo apt update && sudo apt install -y sysbench docker.io python3 python3-pip
pip install matplotlib
```
