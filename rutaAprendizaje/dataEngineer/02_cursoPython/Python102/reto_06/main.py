from my_functions import get_totals, calc_total

def get_total(orders):
  totales = get_totals(orders)
  sumatoria = calc_total(totales)
  #sumatoria =  lambda x : x + get_totals(orders)
  #return functools.reduce(lambda contador, item : contador + item, sumatoria)
  return sumatoria

orders = [
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]

total = get_total(orders)
print(total)

if __name__ == '__main__':
  get_total(orders)
  