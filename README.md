# AttackGraph

**ML-powered cybersecurity attack relationship detection.**

AttackGraph analyzes relationships between security events and predicts how likely they are to be part of an attack. These relationships are then represented as an attack graph.

### How it works

```text
Security Events
      ↓
Semantic Embeddings
      ↓
Relationship Features
      ↓
Logistic Regression
      ↓
Attack Probability
      ↓
Attack Graph
```

The model currently uses:

* Semantic similarity
* Source IP relationship
* Time difference
* Target relationship

### Example

```text
PORT_SCAN
    ↓
LOGIN_ATTEMPT
```

AttackGraph can assign a probability to the relationship between these events.

---

## Setup

Clone the repository:

```bash
git clone https://github.com/Cookkiieess/AttackGraph.git
cd AttackGraph
```

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Train the model:

```bash
python tests/test_training.py
```

Test predictions:

```bash
python tests/test_prediction.py
```

Test the attack graph:

```bash
python tests/test_graph.py
```

Test the relationship builder:

```bash
python tests/test_builder.py
```

---

## V1 Results

V1 was trained on **75,000 synthetic examples**.

On the current test split:

* **99.82% accuracy**
* **99% attack recall**

An unseen attack relationship produced an attack probability of approximately **99.9977%**.

> Results are based on synthetic data and do not represent production performance.

---

## Roadmap

### V1 — Pairwise Attack Relationships ✅

Detect and score relationships between two security events.

### V2 — Multi-Event Attack Chains 🚧

Move from individual relationships to complete attack sequences:

```text
PORT_SCAN
    ↓
LOGIN_ATTEMPT
    ↓
PRIVILEGE_ESCALATION
    ↓
FILE_ACCESS
```

---

**AttackGraph is an experimental cybersecurity research project and is not production-ready.**
