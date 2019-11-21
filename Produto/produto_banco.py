import psycopg2

class ProdutoBanco:

    def __init__(self):
        self.connection = psycopg2.connect(dbname='produto', user='postgres', password='Miserski8') , host='localhost' port='5432')
        