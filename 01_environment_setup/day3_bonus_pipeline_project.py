import time
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🔹 Starting: {func.__name__}()")
        result = func(*args, **kwargs)
        print(f"✅ Finished: {func.__name__}()\n")
        return result
    return wrapper

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️ Time taken by {func.__name__}: {end - start:.4f} sec\n")
        return result
    return wrapper
import random
from functools import reduce

@logger
@timer
def generate_data(n=15):
    """Generate n random numbers between 10 and 100"""
    data = [random.randint(10, 100) for _ in range(n)]
    print(f"Generated data: {data}")
    return data

@logger
@timer
def clean_data(data):
    """Filter out values below 40"""
    cleaned = list(filter(lambda x: x >= 40, data))
    print(f"Cleaned data: {cleaned}")
    return cleaned

@logger
@timer
def transform_data(data):
    """Square each number (as a form of transformation)"""
    transformed = [x**2 for x in data]
    print(f"Transformed data: {transformed[:5]} ...")  # print only few
    return transformed

@logger
@timer
def summarize_data(data):
    """Compute sum, average, and max value"""
    total = reduce(lambda a, b: a + b, data)
    avg = total / len(data)
    max_val = max(data)
    summary = {"sum": total, "avg": round(avg, 2), "max": max_val}
    print(f"Summary: {summary}")
    return summary
    

print("🚀 Running Data Processing Pipeline...\n")
raw = generate_data(5)
cleaned = clean_data(raw)
transformed = transform_data(cleaned)
summary = summarize_data(transformed)

print("\n🏁 Pipeline Completed Successfully!")
def safe_run(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"❌ Error in {func.__name__}: {e}")
    return wrapper