import mysql.connector
from mysql.connector import Error

name = input('Digite seu nome: ')
weight = float(input('Digite seu peso: '))
height = float(input('Digite sua altura: '))
imc = weight / (height * height)
situation = ''

if imc < 17:
situation = 'Muito abaixo do peso'
elif imc >= 17 and imc < 18.5:
situation = 'Abaixo do peso'
elif imc >= 18.5 and imc < 25:
situation = 'Peso normal'
elif imc >= 25 and imc < 30:
situation = 'Acima do peso'
elif imc >= 30 and imc < 35:
situation = 'Obesidade I'
elif imc >= 35 and imc < 40:
situation = 'Obesidade II (severa)'
elif imc >= 40:
situation = 'Obesidade III (mórbida)'


try:
connection = mysql.connector.connect(host='localhost',database='db_imc',user='root', password='' )
insert_products = """INSERT INTO imc (nome, peso, altura, imc, status) VALUES (""" + "'" + name + "'" + "," + str(weight) + "," + str(height) + "," + str(imc) + "," + "'" + situation + "'" + ")"

cursor = connection.cursor()
cursor.execute(insert_products)
connection.commit()
print(cursor.rowcount, "Registro inserido com sucesso")
cursor.close()

except mysql.connector.Error as error:
print("Falha ao inserir registro no MySQL {}".format(error))

finally:
if (connection.is_connected()):
connection.close()
print("Conexão ao MySQL finalizada")