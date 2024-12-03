code_snippets = [
    "def quantum_compute(data):\n    return [complex(x).real for x in data]",
    "class Blockchain:\n    def __init__(self):\n        self.chain = []",
    "import tensorflow as tf\nmodel = tf.keras.Sequential()",
    "from numpy import *\ndata = linspace(0, 10, 100)",
    "async def fetch_data(url):\n    return await aiohttp.get(url)"
]

def generate_code_snippet():
    return random.choice(code_snippets)

for _ in range(3):
    print("```python")
    print(generate_code_snippet())
    print("```")
