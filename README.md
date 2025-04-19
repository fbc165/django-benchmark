# Django Benchmark Guide

This guide explains how to perform a benchmark to compare the performance of synchronous and asynchronous modes in a Django application.

## Steps to Perform the Benchmark

### 1. Run the Container in Synchronous Mode
1. Ensure the `Dockerfile` has the `CMD` for Gunicorn (synchronous mode) uncommented.
2. Start the container:
    ```bash
    docker-compose up --build
    ```
3. Test the benchmark using the `wrk` tool:
    - Without I/O operation:
      ```bash
      wrk -t4 -c500 -d30s http://0.0.0.0/ping-sync/
      ```
    - With I/O operation:
      ```bash
      wrk -t4 -c500 -d30s http://0.0.0.0/ping-sync-io/
      ```

### 2. Switch to Asynchronous Mode
1. Stop and remove the running container:
    ```bash
    docker-compose down
    ```
2. Edit the `Dockerfile`:
    - Comment out the `CMD` for Gunicorn.
    - Uncomment the `CMD` for Uvicorn (asynchronous mode).
3. Rebuild and start the container:
    ```bash
    docker-compose up --build
    ```
4. Test the benchmark using the `wrk` tool:
    - Without I/O operation:
      ```bash
      wrk -t4 -c500 -d30s http://0.0.0.0/ping-async/
      ```
    - With I/O operation:
      ```bash
      wrk -t4 -c500 -d30s http://0.0.0.0/ping-async-io/
      ```

### 3. Compare Results
Analyze the results from the `wrk` tests to compare the performance of synchronous and asynchronous modes under different conditions.

## Notes
- Ensure the `wrk` tool is installed on your system before running the tests.
- Replace `http://0.0.0.0` with the appropriate host if necessary.
