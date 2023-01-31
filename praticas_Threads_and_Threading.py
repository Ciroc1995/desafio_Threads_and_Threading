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

