import matplotlib.pyplot as plt

results = {
    "sync_with_1s_io": {"requests_per_sec": 15.43, "latency_avg_ms": 1002},
    "async_with_1s_io": {"requests_per_sec": 465.58, "latency_avg_ms": 1006},
    "sync_without_io": {"requests_per_sec": 1267.59, "latency_avg_ms": 355.99},
    "async_without_io": {"requests_per_sec": 842.46, "latency_avg_ms": 494.68},
}

labels = list(results.keys())
rps_values = [results[k]["requests_per_sec"] for k in labels]
latency_values = [results[k]["latency_avg_ms"] for k in labels]

fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()

ax1.bar(labels, rps_values, color='cornflowerblue', label='Requests/sec')

ax2.plot(labels, latency_values, color='darkred', marker='o', linewidth=3, label='Avg Latency (ms)')

ax1.set_ylabel('Requests/sec', color='cornflowerblue')
ax2.set_ylabel('Latency (ms)', color='darkred')
ax1.set_title('Django Benchmark: Sync vs Async | With and Without I/O (1s)')
ax1.tick_params(axis='x', rotation=45)

ax1.legend(loc='upper left', bbox_to_anchor=(-0.15,1.15))
ax2.legend(loc='upper right', bbox_to_anchor=(1.15, 1.15))

plt.tight_layout()
plt.show()
