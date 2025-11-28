import requests
import time
import hashlib
import statistics

MATRICULA = "20239037921"
NOME = "Ana"
URL = "http://localhost:80"
NUM_REQUISICOES_POR_CICLO = 1000
NUM_CICLOS = 10                     
TIMEOUT_REQUISICAO = 10             

def gerar_ID(matricula, nome):
    texto = f"{matricula} {nome}"
    hash_md5 = hashlib.md5(texto.encode('utf-8')).hexdigest()
    return hash_md5

CUSTOM_ID = gerar_ID(MATRICULA, NOME)
HEADERS = {"X-Custom-ID": CUSTOM_ID}

def executar_ciclo(num_requisicoes):
    erros_ciclo = 0
    print(f"  > Iniciando ciclo com {num_requisicoes} requisições...")

    tempo_inicio_ciclo = time.time()
    
    for i in range(num_requisicoes):
        try:
            response = requests.get(URL, headers=HEADERS, timeout=TIMEOUT_REQUISICAO)

            if not (response.status_code >= 200 and response.status_code < 400):
                erros_ciclo += 1
            
        except requests.exceptions.RequestException:
            erros_ciclo += 1
            if erros_ciclo < 5:
                print(f"\n[ERRO] Falha na Requisição (Conexão ou Timeout) na requisição {i + 1}.")
        except Exception as e:
            erros_ciclo += 1
            if erros_ciclo < 5:
                print(f"\n[ERRO GERAL] {e} na requisição {i + 1}.")

    tempo_fim_ciclo = time.time()
    tempo_total_ciclo = tempo_fim_ciclo - tempo_inicio_ciclo

    print(f"  FIM. Tempo Total: {tempo_total_ciclo:.3f} s. Erros: {erros_ciclo}")
    
    return tempo_total_ciclo

if __name__ == "__main__":
    
    tempos_ciclo = [] 

    print("="*60)
    print(f"  Teste de Carga em {URL}")
    print(f"  ID de rastreamento: {CUSTOM_ID}")
    print(f"  Configuração: {NUM_CICLOS} ciclos de {NUM_REQUISICOES_POR_CICLO} requisições cada.")
    print("="*60)

    for ciclo in range(NUM_CICLOS):
        print(f"\n[ CICLO {ciclo + 1}/{NUM_CICLOS} ]") 
        tempo_resultado = executar_ciclo(NUM_REQUISICOES_POR_CICLO)
        tempos_ciclo.append(tempo_resultado)

    print("\n" + "="*60)
    print("RESULTADO FINAL DOS TEMPOS DE CICLO")
    print("="*60)

    if not tempos_ciclo:
        print("Nenhum tempo de ciclo registrado para análise.")
    else:
        soma_tempos = sum(tempos_ciclo)
        media_tempos = statistics.mean(tempos_ciclo)
        dp_tempos = statistics.stdev(tempos_ciclo) if len(tempos_ciclo) > 1 else 0.0

        print(f"Tempos de cada ciclo ({NUM_REQUISICOES_POR_CICLO} reqs/ciclo):")
        for i, tempo in enumerate(tempos_ciclo):
            print(f"  Ciclo {i + 1}: {tempo:.3f} segundos")

        print("-" * 60)
        print(f"Soma Total dos Tempos: {soma_tempos:.3f} segundos")
        print(f"Média dos Tempos de Ciclo: {media_tempos:.3f} segundos")
        print(f"Desvio Padrão dos Tempos: {dp_tempos:.3f}")
        print("="*60)
    