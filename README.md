# grocery price tracker

a Python project to track grocery prices across different stores and find the cheapest option
built using **FastAPI** for a REST API interface

---

## features
- add grocery items with their price and store name
- retrieve the cheapest item by name across all stores
- list all items in the database
- REST API for easy integration

---

## installation
### 1 - clone the repository
```bash
git clone https://github.com/yourusername/grocery-price-tracker.git
cd grocery-price-tracker
```

### 2 - install dependencies
```bash
pip install -r requirements.txt
```

### 3 - run the API Server
```bash
uvicorn grocery_price_tracker.api:app --reload
```
- API will be available at:  
  `http://127.0.0.1:8000`
- visit the **interactive API docs**:  
  `http://127.0.0.1:8000/docs`

---

## API Endpoints

| **Action**        | **Method** | **URL**                | **Example Data** |
|-------------------|-----------|------------------------|------------------|
| get API root      | `GET`     | `/`                    | — |
| add / update item | `POST`    | `/items/`              | `{"name": "milk", "store": "Walmart", "price": 3.50}` |
| list all items    | `GET`     | `/items/`              | — |
| get cheapest item | `GET`     | `/items/{name}`        | — |
