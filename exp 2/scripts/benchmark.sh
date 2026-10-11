#!/usr/bin/env bash
# ==============================================================================
# Cloud Computing Laboratory - Experiment 2
# Benchmark Automation Harness: Virtual Machine vs. Container Memory Performance
# ==============================================================================

set -euo pipefail

# Workload & Repetition Defaults
ITERATIONS=${ITERATIONS:-10}
BLOCK_SIZE=${BLOCK_SIZE:-"1M"}
TOTAL_SIZE=${TOTAL_SIZE:-"10G"}
THREADS=${THREADS:-4}
OPER_TYPE=${OPER_TYPE:-"write"}
SCOPE_TYPE=${SCOPE_TYPE:-"global"}
CONTAINER_TAG=${CONTAINER_TAG:-"vm-container-benchmark"}

# Resolve directory paths relative to script
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VM_LOG_DIR="$BASE_DIR/results/raw/memory/vm"
CONTAINER_LOG_DIR="$BASE_DIR/results/raw/memory/container"

mkdir -p "$VM_LOG_DIR" "$CONTAINER_LOG_DIR"

echo "=================================================================="
echo " Cloud Computing Lab: Experiment 2 Benchmark Suite"
echo " Target Workload:     Sysbench Memory ($OPER_TYPE, $SCOPE_TYPE)"
echo " Memory Transferred:  $TOTAL_SIZE ($BLOCK_SIZE block size)"
echo " Concurrency Level:   $THREADS worker threads"
echo " Iterations:          $ITERATIONS per testbed"
echo "=================================================================="

# ------------------------------------------------------------------------------
# 1. Native Virtual Machine Benchmark Execution
# ------------------------------------------------------------------------------
echo ""
echo "[+] Starting Phase 1: Native Virtual Machine Workloads..."
for i in $(seq 1 "$ITERATIONS"); do
    OUT_FILE="$VM_LOG_DIR/run_$i.txt"
    echo -n "    -> Running VM benchmark #$i of $ITERATIONS ... "
    sysbench memory \
        --memory-block-size="$BLOCK_SIZE" \
        --memory-total-size="$TOTAL_SIZE" \
        --threads="$THREADS" \
        --memory-oper="$OPER_TYPE" \
        --memory-scope="$SCOPE_TYPE" \
        run > "$OUT_FILE"
    echo "Completed (Logged: $(basename "$OUT_FILE"))"
done

# ------------------------------------------------------------------------------
# 2. Docker Container Benchmark Execution
# ------------------------------------------------------------------------------
echo ""
echo "[+] Starting Phase 2: Docker Container Workloads..."

# Verify container image availability
if ! docker image inspect "$CONTAINER_TAG" >/dev/null 2>&1; then
    echo "[-] Error: Docker image '$CONTAINER_TAG' not found."
    echo "    Build image using: docker build -t $CONTAINER_TAG -f docker/Dockerfile ."
    exit 1
fi

for i in $(seq 1 "$ITERATIONS"); do
    OUT_FILE="$CONTAINER_LOG_DIR/run_$i.txt"
    echo -n "    -> Running Container benchmark #$i of $ITERATIONS ... "
    docker run --rm \
        --cpus="$THREADS" \
        --memory="8g" \
        "$CONTAINER_TAG" \
        sysbench memory \
            --memory-block-size="$BLOCK_SIZE" \
            --memory-total-size="$TOTAL_SIZE" \
            --threads="$THREADS" \
            --memory-oper="$OPER_TYPE" \
            --memory-scope="$SCOPE_TYPE" \
            run > "$OUT_FILE"
    echo "Completed (Logged: $(basename "$OUT_FILE"))"
done

echo ""
echo "=================================================================="
echo " [✓] All benchmark runs concluded successfully."
echo " VM Output Logs:        $VM_LOG_DIR"
echo " Container Output Logs: $CONTAINER_LOG_DIR"
echo " Run 'python3 scripts/parse_sysbench.py' to generate statistical summary."
echo "=================================================================="
