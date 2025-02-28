def total_revenue(purchases: dict) -> float:
    "Функция возвращает общую выручку."
    return sum(map(lambda x: x["price"] * x["quantity"], purchases))

def items_by_category(purchases: dict) -> dict:
    """Функция возвращает словарь, где ключ — категория, 
       а значение — список уникальных товаров в этой категории."""
    res = {}
    for purchas in purchases:
        res.setdefault(purchas["category"], set())\
           .add(purchas["item"])
    for k in res:
        res[k] = list(res.get(k))

    return res

def expensive_purchases(purchases: dict, min_price: float) -> list:
    """Функция возвращает список покупок, 
       где цена товара больше или равна min_price."""
    res = []
    for purchas in purchases:
        if purchas["price"] >= min_price:
            res.append(purchas)

    return res

def average_price_by_category(purchases: dict) -> dict:
    "Функция возвращает среднюю цену товаров по каждой категории."
    res = {}
    for purchas in purchases:
        res.setdefault(purchas["category"], [])\
           .append(purchas["price"])        
    for k in res:
        res[k] = round(sum(res.get(k)) / len(res.get(k)), 2)

    return res

def most_frequent_category(purchases: dict) -> str:
    "Функция возращает категорию, в которой куплено больше всего единиц товаров"
    dct = {}    
    for purchas in purchases:
        dct[purchas["category"]] = dct.get(purchas["category"], 0) + purchas["quantity"]

    return max(dct.items(), key=lambda x: x[1])[0]
