## Explicación de la estructura del proyecto:

### Test_1 y test_2 
son imagenes en formato base64 diferentes a las imagenes del dataset, se usan para realizar pruebas de detencción

### face_deteccin 
ejectua la función detect para identificar de quién es la cara de la imagen que recibe

### encode_faces_original 
es el encargado de crear el archivo .pickles con el vector de características del dataset
    **La idea es modificar este archivo para que reciba el archivo data.json y cree el mismo vector de características, con el fin de obtener el dataset de manera remota y no desde el cliente**

### data.json 
es el archivo json que representa el dataset

### app 
es el archivo principal, ejecuta la función takePhoto, la cual obtiene una foto en formato base64 e imprime quién aparece en la imágen

**Solo son ejecutables por consola app.py y encode_faces_original.py**

### 'Hecho con `python 2.7.15` en ambiente virtual anaconda'
