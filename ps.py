import numpy as np
from multiprocessing import Pool

def dot_product_chunk(args):
    a_chunk, b_chunk = args
    return np.dot(a_chunk, b_chunk)

def parallel_dot_product(a, b, num_processes=None):
    # Ensure the vectors are numpy arrays
    a = np.array(a)
    b = np.array(b)

    if len(a) != len(b):
        raise ValueError("Vectors must be the same length.")

    # Split the vectors into chunks
    chunk_size = len(a) // num_processes
    chunks = [(a[i:i + chunk_size], b[i:i + chunk_size]) for i in range(0, len(a), chunk_size)]

    # Create a pool of workers
    with Pool(processes=num_processes) as pool:
        local_results = pool.map(dot_product_chunk, chunks)

    # Combine results
    total_dot_product = sum(local_results)
    return total_dot_product

# Example usage
if __name__ == "__main__":
    # Sample vectors
    a = np.random.rand(1000000)
    b = np.random.rand(1000000)
    
    # Number of processes
    num_processes = 4  # Adjust as needed

    result = parallel_dot_product(a, b, num_processes)
    print(f"The dot product is: {result}")

sdahfkbsfoszhgaoghsgd

