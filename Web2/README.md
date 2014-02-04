# PD => osc => NODE-OSC => websocket => HTML/JS

## Instalação

1. Instala node a partir de http://nodejs.org, ele já vem com o NPM, 
gerenciadode pacotes node

2. Instala no diretório local os módulos node necessários, usando NPM,
será criado um diretório node_modulos/ contendo esses módulos:

    npm install node-osc socket.io
  
3. O arquivo app.js irá criar dois servidores, um OSC e um WebSocket,
irá portanto receber as mensagens OSC vindas de qualquer aplicativo na
porta 3333 e irá criar um servidor WebSocket na porta 8081. Execute-o e
deixe esse terminal aberto:

    node app.js
    
4. Em um outro terminal, rode um servidor HTTP simples no diretório
deste arquivo, pode ser o Python SimpleHTTPServer mesmo, (se desejar
algo mais rebuscado, é possível servir esse conteúdo na própria app.js),
por enquanto usamos o SimpleHTTPServer para servir a página HTML do mapa,
o arquivo map.html:

    python -m SimpleHTTPServer 8080
    
5. Abra o browser no endereço http://localhost:8080/map.html

6. Execute o Pd ou outro aplicativo com suporte a OSC e envie mensagens
para a porta 3333. Nesse diretório há um patch Pd exemplo para enviar mensagens:
    puredata test-osc.pd
    
Em resumos, temos:

    Pd           == OSC ==> node-osc   + socket.io
    test-osc.pd             app.js       app.js    
                            porta 3333   porta 8081
                                      /\
                                      || 
                                   WebSocket
                                      ||
                                      \/
                                  servidor web: socket.io.js + HTML/JS
                                  map.html
                                  porta 8080
                               
    

