import pandas as pd

# Загрузка данных
df = pd.read_csv('imdb_top_250.csv')

# Первые 5 строк
print("Первые 5 строк:")
print(df.head(5))

# Информация о данных
print("\nИнформация о данных:")
print(df.info())

# Статистика
print("\nСтатистическое описание:")
print(df.describe())