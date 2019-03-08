
def run():
    for i in range(1,100):
        response = requests.get('https://xkcd.com/()'.format(i))
        suop = BeautifulSoup(response.content, 'html.parser')
        image_container = soup.find(id='comic')

        image_url = image_container.find('ing')['src']
        image_name = image_url.split('/')[-1]
        print('Descargando la imagen ()'.format(image_name))
        urllib.urlretrieve('https:()'.format(image_url), image_name)

if __name__ == '__main__':
    run()







# import socket, string, sys, os, time
#
# clear = lambda: os.system('cls')
#
# def principal():
#     mi_socket = socket.socket()
#     mi_socket.connect(('127.0.0.1',9090))
#
#     print("[DICIONARIO BINARIO]")
#     time.sleep(1)
#     clear()
#
#     while True:
#         mensaje = input("[]: ")
#         mi_socket.send(mensaje.encode())
#         if(mensaje == 'cerrar'):
#             break
#         recibido=mi_socket.recv(1024)
#         print(recibido.decode())
#
#     print("adios")
#     mi_socket.close()
#
#
# if (__name__ == '__main__'):
#     principal()
