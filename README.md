# 📘 Log File Analysis API (FastAPI)

This project provides a REST API for **reading**, **filtering**, and **analyzing log files** stored in a directory.
It is built using **FastAPI** and supports structured access to logs in the format:

```
Timestamp<TAB>Level<TAB>Component<TAB>Message
```

Example:

```
2025-05-07 10:00:00	INFO	UserAuth	User 'john.doe' logged in successfully.
```

---

# 🚀 Features

### ✔ Read and parse log files from a directory

### ✔ Filter logs by:

* Level
* Component
* Start time
* End time

### ✔ Get log statistics:

* Total log entries
* Count per log level
* Count per component

### ✔ Retrieve specific log entry by ID

### ✔ Automatic ID generation

### ✔ Simple server runner (`server.py`)

### ✔ Clean modular folder structure

---

# 📂 Project Structure

```
log_api/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── models/
│   │   └── log_model.py
│   ├── utils/
│   │   ├── file_reader.py
│   │   └── parser.py
│   ├── routers/
│   │   └── logs_router.py
│   └── services/
│       └── log_service.py
│
├── logs/
│   ├── sample1.log
│   ├── sample2.log
│   ├── sample3.log
│
├── server.py
├── requirements.txt
└── README.md
```

---

# 📦 Installation

### 1. Create a virtual environment *(optional but recommended)*

```
python -m venv venv
source venv/bin/activate     # Linux / macOS
venv\Scripts\activate        # Windows
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

# ▶ Running the API

Start the server using the `server.py` file:

```
python server.py
```

This runs the API on:

```
http://0.0.0.0:8000
```

---

# 📑 API Endpoints

---

## **GET /logs**

Returns all parsed logs.

### Filters:

| Query Param | Example                           |
| ----------- | --------------------------------- |
| level       | `?level=ERROR`                    |
| component   | `?component=UserAuth`             |
| start_time  | `?start_time=2025-05-07 10:00:10` |
| end_time    | `?end_time=2025-05-07 10:00:25`   |

Example:

```
GET /logs?level=ERROR&component=Payment
```

---

## **GET /logs/stats**

Returns:

```json
{
  "total_entries": 12,
  "by_level": { "INFO": 5, "WARNING": 3, "ERROR": 4 },
  "by_component": { "UserAuth": 3, "Payment": 4, "GeoIP": 2 }
}
```

---

## **GET /logs/{log_id}**

Example:

```
GET /logs/5
```

Returns single log entry.

---

# 📝 Log File Format

Each entry must follow:

```
timestamp<TAB>level<TAB>component<TAB>message
```

Example:

```
2025-05-08 09:08:50	ERROR	Payment	Refund processing failed.
```

Multiple `.log` files can be placed inside the `logs/` directory—they are automatically parsed.

---

# 🧪 Testing

Using browser / curl / Postman:

```
http://localhost:8000/logs
http://localhost:8000/logs?level=ERROR
http://localhost:8000/logs/stats
http://localhost:8000/logs/10
```

Interactive API docs:

```
http://localhost:8000/docs
```

---

# 🔧 Configuration

Default log directory is defined in:

```
app/config.py
```

Modify:

```python
LOG_DIR = "logs/"
```