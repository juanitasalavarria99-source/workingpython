import pandas as pd

print('Bienvenido a la primer clase de Pandas')

serData = pd.Series(data=[10,20,30,40], index=['Carlos', 'Juan', 'Marcos', 'Pablo'])
print(serData)
print(serData.index)
print(serData['Marcos'])
print('Juanita' in serData)

serDate1 = serData * 2
print(serDate1)

serDate1 = serData ** 2
print(serDate1)

print('------------------------Estructura de datos en 2 dimensiones-------------------------------')

dictionary = {
    'one': pd.Series(data=[1, 2, 3, 4, 5], index=['Carlos', 'Juan', 'Marcos', 'Pablo', 'Luis']),
    'two': pd.Series(data=[6, 7, 8, 9, 10], index=['Carlos', 'Juan', 'Marcos', 'Pablo', 'Luis'])
}

df = pd.DataFrame(dictionary)
print(df)
print(df.index)
print(df.columns)

df['three'] = df['one'] * df['two']
print(df)

df['filter'] = df['three'] > 45
print(df)

del df['filter']
print(df)

df.insert(1, 'copy of one', df['one'])
print(df)

print('-------------Import CSV files -----------------------------------')

movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')
links = pd.read_csv('links.csv')
tags = pd.read_csv('tags.csv')

print(movies.columns, movies.shape)
print(ratings.columns, ratings.shape)
print(links.columns, links.shape)
print(tags.columns, tags.shape)

print(tags.tail(2))

# Eliminamos columna timestamp
del ratings['timestamp']
del tags['timestamp']

print('Variables de tags:')
print(tags.columns)
print('Variables de ratings:')
print(ratings.columns)

print(tags.iloc[0])

print(tags.iloc[[0,22,500]])
print(tags.index)

print('-------------------ratings---------------------------')
print(ratings.head(5))
print(ratings['rating'].describe())
print(ratings['rating'].mean())
print(ratings['rating'].min())
print(ratings['rating'].max())

print('----------------------------------------------')
is_highly_rated=ratings['rating']>=4
print(ratings[is_highly_rated].head(4))
print(ratings.shape)
print(ratings[is_highly_rated].shape)
print(movies.columns)
print(movies.head(2))

is_amimation=movies['genres'].str.contains('Animation')
print(movies.shape)
print(movies[is_amimation].shape)

print('movies')
print(movies.columns)
print('ratings')
print(ratings.columns)