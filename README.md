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

### 4. Generate Comparison Graph

1. Open the `graphical_results.py` file in a text editor.
2. Fill the `results` dictionary with your benchmark results. The dictionary should have the following structure:
    ```python
    results = {
        "synchronous": {
            "no_io": <result_from_ping_sync>,
            "with_io": <result_from_ping_sync_io>
        },
        "asynchronous": {
            "no_io": <result_from_ping_async>,
            "with_io": <result_from_ping_async_io>
        }
    }
    ```
    Replace `<result_from_ping_sync>`, `<result_from_ping_sync_io>`, `<result_from_ping_async>`, and `<result_from_ping_async_io>` with the actual results from your tests.

3. Ensure `matplotlib` is installed on your system:
    ```bash
    pip install matplotlib
    ```

4. Run the script to generate the graph:
    ```bash
    python graphical_results.py
    ```

5. The script will generate a comparison graph and save it as an image file in the current directory.

## Notes
- Ensure the `wrk` tool is installed on your system before running the tests.
- Replace `http://0.0.0.0` with the appropriate host if necessary.
