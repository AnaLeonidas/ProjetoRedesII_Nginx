# 🚀 Projeto Redes II: Comparação de Desempenho Nginx

Este repositório contém a infraestrutura e os scripts utilizados para realizar uma análise comparativa de desempenho (performance) entre os servidores web **Apache** e **Nginx**. O foco principal é coletar métricas para a comparação dos servidores.  

A metodologia empregada simula um ambiente, utilizando uma pilha de observabilidade para monitorar as métricas de desempenho em tempo real.

---

## 💻 Arquitetura e Componentes

A solução é  orquestrada via Docker Compose.

## 🛠️ Como Iniciar e Realizar os Testes

Para executar o projeto e replicar os testes de estresse, siga as instruções abaixo:

Navegue até o diretório raiz deste projeto no seu terminal e utilize o Docker Compose para levantar todos os serviços em segundo plano:

# Subir a rede, o Nginx, o Exporter, Prometheus e Grafana
docker-compose up -d
# Rodar o script de teste com a quantidade de requisições desejada
python load_test.py
# Parar os containers após o uso
docker-compose down
#Links
Vídeo: https://youtu.be/KF4USL-qVic?si=fIkwom7FrOHgM1pO
GitHub: https://github.com/AnaLeonidas/ProjetoRedesII_Apache
https://github.com/AnaLeonidas/ProjetoRedesII_Nginx
