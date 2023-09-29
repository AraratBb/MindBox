from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

products = spark.createDataFrame([
    ('1', 'продукт1'),
    ('2', 'продукт2'),
    ('3', 'продукт3'),
    ('4', 'продукт4')
], ['Id продукта', 'Имя продукта'])

# Создание датафрейма с категориями
categories = spark.createDataFrame([
    ('1', 'категория1'),
    ('2', 'категория1'),
    ('3', 'категория2'),
    ('4', 'категория2')
], ['Id категории', 'Имя категории'])

connections = spark.createDataFrame([
    ('1', '2'),
    ('2', '2'),
    ('3', '3'),
    ('4', '1'),
    ('3', '1'),
    ('3', '2'),
], ['Id категории', 'Id продукта'])

df = products.join(connections, products["Id продукта"] == connections["Id продукта"], "left") \
    .join(categories, categories["Id категории"] == connections["Id категории"], "left") \
    .select(['Имя продукта', 'Имя категории']) \
    .show()