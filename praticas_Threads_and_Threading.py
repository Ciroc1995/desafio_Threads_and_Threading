import threading

# Desafio 1 

def navegar_ate_o_site(site):
    print(f'Navegando até o site {site}')

def baixar_fotos(site):
    print(f'Baixando fotos do site {site}')


nova_thread = threading.Thread(
    target=baixar_fotos, args=('https://www.globoesporte.com',), daemon=True)
nova_thread.start()
navegar_ate_o_site('https://www.globoesporte.com')
nova_thread.join()

# Desafio 2

def navegar_ate_o_site(site, produto):
    print(f'Navegando ate o site {site} e extraindo valores do produto {produto}')


produtos = ['celular', 'monitor', 'fone-de-ouvido', 'alto-falante', 'computador']
threads = []
for produto in produtos:
    nova_thread = threading.Thread(
        target=navegar_ate_o_site, args=('https://shopee.com.br', produto))
    threads.append(nova_thread)

for thread in threads:
    thread.start()
    print(f'Inicializando thread {thread.name}')

for thread in threads:
    thread.join()
    print(f'Finalizando thread {thread.name}')


