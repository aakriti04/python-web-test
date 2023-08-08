from sqlalchemy import create_engine, text

engine = create_engine(
)


def get_db_values():
  print(" in get_db_values  ")
  with engine.connect() as conn:
    data_list = []
    result = conn.execute(text("select * from test_table;"))
    results = result.all()
    # print(results)
    # print(type(results[0]))
    # print(results[0])
    for row in results:
      # print(row._mapping)
      data_list.append(row._mapping)
    print(f"values : {data_list}")
    return data_list


print("in db")
# get_db_values()
