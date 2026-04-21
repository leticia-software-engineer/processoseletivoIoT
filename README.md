Projeto de Semáforo usando ESP32
---

### 👤 Identificação do Candidato

- **Desenvolvedora: Letícia Maria dos Santos Dias**  
- **GitHub: leticia-software-engineer**  

---

## 1️⃣ Visão Geral da Solução
 
O objetivo do Projeto de Semáforo usando ESP32 é desenvolver um firmware simples e leve para ser utilizado em sistema embarcado de Semáforo para controle de trânsito. Além disso, consolidar os aprendizados desenvolvidos durante as trilhas de IoT e Sistemas embarcados do Programa Nacional de Aprendizado Acelerado(PNAAT). 

O presente sistema é capaz de acender os leds com um delay de segundos pré determinado, sendo os leds vermelho e verde mantidos por 3 segundos e o amarelo por 2 segundos, como uma forma de simulação rápida do que acontece na prática. Esse delay foi definido pela necessidade de demonstrar de maneira rápida o funcionamento do programa, mas os valores são configuráveis e podem ser adaptados para qualquer semáforo, modificando-os no arquivo main.py, dentro do diretório src. Após ser inicializado o sistema entra em loop infinito sem necessitar de interverção dos usuários. A cada iteração no loop uma mensagem é exibida no terminal informando a conclusão bem sucedida de um ciclo.

---

## 2️⃣ Arquitetura do Sistema Embarcado

Explique a arquitetura lógica do seu projeto, abordando:

A arquitetura lógica do projeto está disposta na seguinte estrutura:

```python
processoseletivoIoT/
├── .github/
│   └── workflows/
│       └── ci.yml            
├── .devcontainer/            
│   └── devcontainer.json
├── binaries
│   └── bootloader.bin
│   └── micropython.bin
│   └── partition-table.bin
├── src/                   
│   └── main.py               # 📄Firmware do semáforo
├── diagram.json              # ⚡Modelo do sistema projetado com Wokwi
├── Dockerfile
├── flasher_args.json
├── fs.bin
├── requirements.txt          # Instala as bibliotecas necessárias para execução do programa
├── wokwi.toml                #
└── README.md                 # 📝 Relatório final 
```
---


### Fluxo Principal

No arquivo src/main.py encontra-se o código principal que faz o diagrama funcionar na prática. Nesse arquivo há a declaração de estados, loops estruturas de dados e funções. A linguagem usada foi micropython e as bibliotecas machine para controle dos pinos (GPIO) e time para controle de temporização.
 
Depois disso, utilizei um array para armazenar as informações dos pinos pelos quais cada led seria representado. Estando todos conectados à placa ESP32. Cada pino representa um componente de saída pois nenhum receberá intervenção do usuário para ser executado, sendo responsáveis apenas por transmitir luz.

```python
leds = [
    Pin(22, Pin.OUT),  # vermelho
    Pin(19, Pin.OUT),  # amarelo
    Pin(4, Pin.OUT)    # verde
]
```

Também adicipnei duas funções, uma para apagar todos os leds que será ativada no momento da inicialização do semáforo, evitando que ao iniciar existam leds acesos e causem uma certa confusão ao sistema, garantindo que não fique mais de um led aceso simultaneamente no momento da troca, o que evita casos de acidentes de trânsito.
Já a função de acender torna configuravel a mudança do estado baixo(desligado ou 0) para o estado alto(ligado ou 1), bem como o tempo que o led devrá se manter aceso, evitando repetições e otimizando o código. 

Por fim, é utilizado um loop infinito que irá executar aquele código com a função de acender configurada para cada elemento do vetor leds. Como pode ser visto a seguir:
```python
while True:
    acender(leds[0], 3) #Acende o led vermelho
    acender(leds[2], 3) #Acende o led verde
    acender(leds[1], 2) #Acende o led amarelo
    #Após isso o ciclo se repete voltando a acender o led vermelho.
    print("CICLO_OK") #A cada ciclo concluído com sucesso uma mensagem de sucesso é exibida no terminal
```
Dessa forma é possível acompanhar os ciclos pelo terminal e manter o programa funcionando enquanto o hardware for capaz de executado.

### Como os componentes interagem entre si  

Nesse projeto, o ESP32 atua como o controlador central responsável por enviar sinais digitais para os LEDs através dos pinos GPIO.
Cada LED recebe o sinal que foi passado por um resistor, que limita a corrente elétrica, o que garante mais a integridade do componente.
---

## 3️⃣ Componentes Utilizados na Simulação

Liste os principais componentes definidos no `diagram.json`, por exemplo:

A placa utilizada foi a ESP32 e os componentes foram: três leds comuns e 3 resistores com 220 Ω cada, valor frequentemente utilizado para lâmpadas led. Veja a seguir de maneira mais ilustrativa:

1 placa ESP32
3 resistores de 220 Ω
3 leds(um vermelho, um amarelo e um verde)
1 simulador Wokwi

![alt text](image.png)

---

## 4️⃣ Decisões Técnicas Relevantes

Algumas das decisões técnicas que tomei foram principalmente voltadas a eficiência do firmware. Meu foco não era trazer um sistema revolucionário, mas um sistema aplicável, simples e sobretudo eficiente, capaz de atender todos os requisitos esperados, por isso escolher o tema foi um verdadeiro desafio. 
Algo que foi um pouco difícil no começo foi evitar repetições no código para deixá-lo mais limpo, por isso acabei optando por adicionar funções "acender" e "desligar" que reduziram uma quantidade significativa de linhas de código redundante. 

Além disso, usar um loop infinito foi uma decisão muito importante que bateu de frente com a necessidade de manter um status de funcionamento e por isso optei por adicionar uma mensagem no terminal a cada iteração.

Por último, mas não menos importante, acabei precisando reduzir o delay de 30, 30 e 4 segundos nos leds - padrão nos semáforos de cidades movimentadas - para utilizar um delay de exemplo(3, 3 e 2 segundos), visando atender o requisito de apresentar a solução completa em dez segundos garantindo a agilidade para a correção, considerando uma média de 2 segundos para a inicialização do loop.  

---

## 5️⃣ Resultados Obtidos

Descreva o comportamento final do sistema:

- O que funciona corretamente  
- Quais requisitos foram atendidos  
- Resultado observado na simulação do Wokwi  
O sistema apresentou o comportamento esperado:

Apenas um LED é aceso por vez, a sequência de funcionamento (vermelho → verde → amarelo) está correta, a temporização é respeitada, a execução não apresentou nenhuma falha, mensagens são exibidas corretamente no terminal e os testes de integração passaram.

Na simulação do Wokwi, por meio do arquivo diagram.json você pode observar claramente o funcionamento do sistema, basta ter os requirements instalados e todos os arquivos deste projeto, clicando na seta verde acima ele executa e pode-se visualizar com exatidão o protótipo e o terminal da solução.
---

## 6️⃣ Comentários Adicionais 

Os principais aprendizados que obtive com o seguinte projeto foram:
Manipulação de GPIO no ESP32
Estruturação de firmware em MicroPython: entendi mais sobre como estruturar e organizar um firmware do zero com micropython, tendo total autonomia ao poder escolher tema e organização.
Simulação de circuitos no Wokwi: aprendi a usar o wokwi com maior facilidade, a desenvolver diagramas por meio dele e fui incentivada a pesquisar e a ser protagonista do meu aprendizado.
Em suma, foi uma experiência engrandecedora. 
---

