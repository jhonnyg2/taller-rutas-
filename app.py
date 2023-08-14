#importamos flask
from flask import Flask, jsonify, request
#iniciamos flask en el servidor app
app = Flask(__name__)

from products import products

# Testing Route/ ejemplo de peticion get, enviando archivos en formato json
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})

# Get Data Routes
#mediante la peticion get se retornan los productos mediante formato json del archivo productos y se muestran

@app.route('/products')
def getProducts():
    # return jsonify(products) de esta manera se hace una peticion normal en formato json
    return jsonify({'products': products}) #esta es otra manera en la cual se pueden mostrar los datos dentro de una propiedad
#tambien se pueden agregar mensajes


@app.route('/products/<string:product_name>')#peticion get mediante la solicitud de un nombre de producto
def getProduct(product_name):#se crea la funcion que retornara el producto mediante el nombre
    productsFound = [
        product for product in products if product['name'] == product_name.lower()]
    if (len(productsFound) > 0):
        return jsonify({'product': productsFound[0]})
    return jsonify({'message': 'Product Not found'})

# Create Data Routes
# nos sirve para crear datos mediante el metodo post
@app.route('/products', methods=['POST'])
def addProduct():#creamos una funcion la cual va a recibir datos en formato json que son 3 mediante una URL
    new_product = {
        'name': request.json['name'],
        'price': request.json['price'],
        'quantity': 10
    }
    products.append(new_product)
    return jsonify({'products': products})

# Update Data Route
#permite actualizar un producto mediante su nombre usando el metodo put
#Hacemos una peticion por URL mediante le metodo put para actualizar un dato en formato json
@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            'message': 'Product Updated',
            'product': productsFound[0]
        })
    return jsonify({'message': 'Product Not found'})

# DELETE Data Route
#Mediante el metodo delete podemos eleminar un dato
# Mediante la URL se realizara una peticion de un nombre en este ejemplo claro para eliminar ese dato en especifico en json
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        products.remove(productsFound[0])
        return jsonify({
            'message': 'Product Deleted',
            'products': products
        })
#hacemos que al ejecutar o iniciar si realizamos alguna cambio lo haga automaticamnte siempre
# y cuando este en el directorio main o principal
if __name__ == '__main__':
    app.run(debug=True, port=4000)