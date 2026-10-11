# System Environment Baseline & Hardware Telemetry

This document outlines the host and guest testbed hardware topology, memory configuration, storage allocation, and kernel parameters utilized during Experiment 2.

---

## 1. Processor & Compute Architecture (`lscpu`)

| Parameter | Host / VM Configuration |
| :--- | :--- |
| **Architecture** | x86_64 (64-bit AMD/Intel) |
| **CPU Operating Mode** | 32-bit, 64-bit |
| **Byte Ordering** | Little Endian |
| **Address Topology** | 48 bits physical, 48 bits virtual |
| **vCPU Allocation** | 4 vCPUs (1 Socket, 4 Cores) |
| **Hypervisor Interface** | VMware Workstation Pro (Hardware-Assisted VT-x/AMD-V) |
| **Core Scheduling** | Direct 1:1 Thread Binding |

---

## 2. Memory Subsystem Layout (`free -h`)

| Memory Attribute | Allocated Capacity | Operational State |
| :--- | :--- | :--- |
| **Total Memory Pool** | 8.0 GiB (8,192 MiB) | High-speed DDR4/DDR5 unified RAM pool |
| **Pre-Benchmark Utilization** | ~1.1 GiB | Base OS services & kernel background tasks |
| **Active Buffers / Cache** | ~1.7 GiB | Linux page cache and dirty buffer buffers |
| **Available Free RAM** | ~5.2 GiB (6.6 GiB effective) | Dedicated to synthetic memory workloads |
| **Swap Space Configuration** | 2.0 GiB | Minimal swap pressure during active runs |

---

## 3. Storage Subsystem & Disk Topology (`lsblk`)

* **Target Volume (`/dev/sda`):** 60 GB Pre-allocated Virtual Disk (SCSI/NVMe)
  * `/dev/sda1` — BIOS/GPT Boot Reserved (1 MiB)
  * `/dev/sda2` — EFI System Partition FAT32 (512 MiB)
  * `/dev/sda3` — Linux Root Filesystem ext4 (59.5 GiB)

---

## 4. Software Stack & Engine Versions

* **Operating System:** Ubuntu 24.04 LTS (*Noble Numbat*)
* **Linux Kernel:** 6.8.0-generic (x86_64)
* **Container Engine:** Docker Engine v27.x.x (API v1.47, cgroups v2 enabled)
* **Base Container Image:** `ubuntu:24.04` (official minimal release)
* **Benchmarking Binary:** `sysbench 1.0.20` (LuaJIT 2.1.0-beta3 runtime)
