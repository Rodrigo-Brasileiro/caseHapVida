# Case HapVida

![image](https://github.com/Rodrigo-Brasileiro/caseHapVida/assets/126472820/d8b8028f-7585-4d39-a395-995cd41fc16f)

 <h2>Problema:</h2>
 <p>O Brasil, atual detentor do maior sistema de transplante de órgãos do mundo, enfrenta um desafio significativo na gestão das filas de espera por órgãos, com cerca de 65 mil pessoas aguardando, especialmente para transplantes cardíacos, fazendo parte de 386 desses casos. Apesar do engenhoso sistema, a espera por um órgão vital, como o coração, impacta negativamente a qualidade de vida dos pacientes, levando a desafios emocionais, psicológicos e limitações nas atividades diárias. A urgência em aprimorar o monitoramento e proporcionar suporte contínuo a esses indivíduos é crucial para minimizar os efeitos adversos dessa espera prolongada. Pensando nisso que a empresa HapVida, parceira dessa solução, buscando soluções na área da saúde nos contratou, HeathTeCh Solution.</p>

  <p>Click <a href="https://www.scielosp.org/pdf/csp/2006.v22n10/2229-2239/pt"> aqui </a> para saber mais sobre a lista de espera e transplante de órgãos.</p>

<h2>Solução:</h2>
 
  <p>O Interwatch Heath surge como uma inovadora solução para abordar os desafios enfrentados por aqueles que aguardam transplantes de órgãos, com ênfase especial na espera por corações. Este dispositivo de monitoramento contínuo é projetado para oferecer suporte 24 horas por dia, sete dias por semana, fornecendo dados clínicos essenciais para melhor gerenciar o período crítico de espera.</p>

  <p>A pulseira leve e portátil do Interwatch Heath é equipada com um medidor de batimentos e oxigênio no sangue (MAX30102), um acelerômetro para identificação de quedas (acoplado com um buzzer de aviso) e um Real Time Clocker (RTC), o qual pode ser programado para indicar a hora de remédios ou consultas, além de um microntrolador ESP32, responsável por gerenciar e processar os dados identificados pelos sensores, os quais, após processados, são enviados via processo Message Queuing Telemetry Transport(MQTT), que é um protocolo de comunicação leve e eficiente projetado para troca de mensagens em redes com largura de banda limitada ao Fiware(plataforma com aplicação que se programada, pode ser capaz de identificar desvios do padrão de batimentos cardíacos e alertar a emergência). Todas as informações são exibidas em uma tela OLED, proporcionando fácil acesso aos dados de saúde do usuário.</p>

  <p>O Interwatch Heath não apenas visa aprimorar a eficácia do monitoramento clínico, mas também busca mitigar os impactos emocionais e psicológicos da espera por um transplante, proporcionando dados precisos para intervenções médicas oportunas. Ao compreender e antecipar eventos críticos, este dispositivo visa reduzir os danos associados à espera por um órgão vital, promovendo assim uma melhoria significativa na qualidade de vida dos pacientes.</p>

 <h3>Componentes</h3>
    <p>Para implementar a solução você precisará dos seguintes componentes que estão distribuídos em duas etapas, são elas a etapa física e virtual. Para a etapa física, será necessário:</p>
    
  | Componente                                              | Preço   |
  |---------------------------------------------------------|---------|
  | Um Oxímetro MAX30102                                   | R$30,12  |
  | Acelerômetro                                            | R$22,00  |
  | Buzzer                                                  | R$2,50   |
  | Real Time Clocker (RTC) - O ESP32 possui RTC embutido    | R$0,00   |
  | Tela OLED 128x64                                         | R35,00 |
  | ESP32                                                   | R$70,00  |
  | Fio microUSB para ligar o ESP                            | R$12,50  |
  | Protoboard                                              | R$15,00  |
   <p>Observação: Os preços foram retirados da pesquisa feita na Santa ifigênia na loja Multicomercial, ou seja, passível de serem alteradas conforme a loja.</p>
  <p>Tendo esses componentes, basta seguir a foto da montagem disponibilizada <a href="https://github.com/Rodrigo-Brasileiro/caseHapVida/blob/main/MontagemInterWatch.png"> aqui </a> e utilizando Arduino IDE, caso não tenha, baixe-a Click <a href="https://www.arduino.cc/en/software">aqui</a>, após pegar o código disponibilizado nesse repositório e gravar no microcontrolador ESP32 clicando em send dentro da IDE.</p>
  <p> A segunda etapa é após o microcontrolador enviar os dados via MQTT, para essa etapa, utilizamos uma plataforma chamada fiware.</p>
   <p>Primeiramente, para a utilização desse software, é necessário alguns pré-requisitos, o primeiro é uma máquina virtual VirtualMachine(VM), a qual simulará um sistema Linux, nesse caso o Ubuntu. Dentro da máquina, realiza-se a instalação de ferramentas que facilitam criação, o gerenciamento e a execução de contêineres de aplicativos que serão usados nessa parte do projeto, por último realiza-se a instação do Fiware, agora mais profundamente, é uma plataforma aberta de código destinados a operação como back-end, com o intuito de facilitar as aplicações para smart cities(cidades inteligentes), Inthernet of Things(IoT ou internet das coisas) e sistemas baseados em dados contextuas em tempo real, tudo que condiz com o propósito da solução.Essa plataforma fornece um conjunto APIs (Interfaces de Programação de Aplicativos) e ferramentas que simplificam a criação de soluções inovadoras para melhorar a qualidade de vida nas cidades e impulsiona a transformação digital em diversos setores. </p>

  <h3>Instação da máquina virtual</h3>
    <p>A princípio, os requisitos de hardware para essa etapa são:</p>

   <ol>Núcleos de Processamento - **1vCPU**</ol>
   <ol>Memória RAM - **1GB** </ol>
   <ol>Armazenamento Secundário Mínimo - **20GB HD e/ou SSD**</ol>
     <p>Tendo essa etapa concluída, primeiro passo é entrar nesse <a href="https://www.virtualbox.org">site</a> e clicar no botão download para fazer a instação da máquina virtual, no nosso caso a VirtualBox. O próximo é instalar o programa que usaremos, nessa situação, o Ubuntu versão 22.04lts, nesse <a href="https://ubuntu.com/download/server">site</a>. O terceiro passo é criar e configurar a máquina, basta clicar no botão "novo" dentro do VirtualBox, em sequência dê o nome "ubuntu" a sua máquina, e clique em próximo até finalizar. Finalizado, marque a máquina criada e selecione a opção "configurações", nesse momento vá em armazenamento e do lado direito estará uma aba para adicionar o arquivo ubuntu que você baixou, após isso só iniciar a máquina e realizar as configuralções iniciais de usuário.</p>
  <h4>Inicialização</h4>
    <p>A primeira etapa após abrir o sistema Linux é abrir o terminal, feito isso, é preciso fazer a instalação de uma ferramenta chamada docker compose que faciliata a criação, gerenciamento e execução de contêiners de aplicativos, para isso, clique <a href="https://docs.docker.com/engine/install/ubuntu/"> aqui</a> e siga as instruções. Conluída essa etapa, seguimos para a instalação e inicialização do Fiware, faça esses comandos no terminal:</p>
      <ol> git clone https://github.com/Rodrigo-Brasileiro/caseHapVida - para copiar todos os arquivos disponíveis nesse repositório </ol>
      <ol> cd fiware - para entrar na pasta fiware </ol>
      <ol> docker compose up -d - para abrir as portas do fiware </ol>
    <p>Nesse instante, vamos verificar se está tudo correto com as portas abertas, para isso, vamos no site <a href="https://www.postman.com">postman</a> que é site de suporte de API que usaremos como comunicador e receptor de respostas do ESP32, crie uma conta e um "my workspace", jogue os arquivos do repositório desse github, vá na pasta 1.1, crie uma variável chamada url com seu enderço de IP e clique em send, com a resposta OK, a porta está saúdavel.</p>
    <p> Agora, basta testar o programa, primeiramente precisa criar na porta 3 sua varíavel, terminado isso, basta ligar o esp32 enviando dados e solicitá-los com a portas 17. Quando finalizar o programa, para fechar as portas, basta escrever o comando: docker compose down</p>
<h3>Componentes Complementares</h3>
   <p>A plataforma do Fiware conta com componentes complementares que vale a pena serem comentados, são eles:</p>
  <h4>Orion Context Broker </h4>
  
  <p>Orion Context Broker é responsável gestão de contextos, que envolve a coleta, armazenamento e disponibilização de informações contextuais relevantes, como dados de sensores, informações de localização e estados de dispositivos, ou seja, útil para gestão das tagid. </p>
  
  <h4>STH Comet</h4>
   <p>O STH-Comet, uma parte essencial da plataforma FIWARE, desempenha um papel fundamental na preservação em grande escala de informações contextuais passadas. Sua colaboração com o Orion Context Broker permite a captura, armazenamento e consulta eficientes de dados       históricos. Com capacidades avançadas, como o armazenamento otimizado de séries temporais e a realização de consultas agregadas e de séries temporais, o STH-Comet oferece uma interface RESTful para a interação, permitindo aos desenvolvedores acessar e analisar           dados passados de maneira ágil. Em suma, o STH-Comet simplifica o armazenamento e a recuperação de informações contextuais históricas na estrutura FIWARE.</p>
   <p>Clique <a href="https://github.com/Rodrigo-Brasileiro/caseHapVida/blob/main/sth-comet-architecture.png">aqui </a> para compreender melhor sobre o funcionamento do sthcomet. </p>
   
  
  <h4>MongoDB</h4>
  
  <p>O MongoDB é um sistema de banco de dados NoSQL usado na plataforma FIWARE para armazenar dados contextuais provenientes do Orion Context Broker e de outros componentes. Ele suporta documentos JSON flexíveis, possui recursos avançados para consultas e escalabilidade horizontal, tornando-o adequado para lidar com grandes volumes de dados na plataforma FIWARE.</p>
  
   <h4>Eclipse-Mosquitto</h4>
   
   <p>O Eclipse Mosquitto é um broker MQTT usado na plataforma FIWARE para facilitar a troca de mensagens entre dispositivos IoT e outros componentes. Ele suporta recursos de autenticação, segurança e controle de acesso, fornecendo uma solução escalável e configurável para a comunicação MQTT na plataforma FIWARE. Os dados são armazenados no tópico TEF (Telemetria e Monitoramento de Equipamentos).</p>
   
   <h3>Arquitetura da solução:</h3>
   
  ![image](https://github.com/Rodrigo-Brasileiro/caseHapVida/assets/126472820/2bef4fe3-4a10-4349-983d-aa7af963befd)
<p> Clique <a href="https://github.com/Rodrigo-Brasileiro/caseHapVida/blob/main/interwatch.drawio">aqui </a> para acessar o draw.io da arquitetura da solução.</p>
 
 <h2>Tecnologia usada e como iniciar o projeto</h2>
   
   <ol>Para esse projeto, utilizamos a IDE do arduino para programar o ESP32, desse modo, toda a linguagem é em c++. Entretanto, primeiramente é preciso instalar o pacote do ESP32 da espressif, seguindo <a herf="https://www.youtube.com/watch?v=Ozr1SXwir9g">esse</a> tutorial. Agora para a aplicação do Fiware, ela é toda configurada em python, abordada no tópico seguinde;</ol>
   <ol>Para toda a configuração da Tela OLED e acelerômetro, utilizamos as bibliotecas disponíveis na IDE do arduino, como: Adafruit GFX Library, Adafruit SSD1306 e Adafruit MPU6050, já para configurar o sistema a internet e protocolo mqtt utilizamos a biblioteca PubSubClient(by nick o'lary). Terminado isso basta utilizar o códigos que disponibilizamos e gravar o código no ESP32.</ol>
   <ol>Em seguida, ligue sua máquina virtual e estebeleça os passos do Fiware e teste o programa como supracitado.</ol>
    <p>Clique <a href="https://github.com/Rodrigo-Brasileiro/caseHapVida/blob/main/InterWatch_codigo.ino">aqui</a> para visualizar o código do ESP32.</p>
 
  <h2>Simulação no WOKWI</h2>
    <p>Wokwi é uma plataforma online que oferece simuladores de hardware para desenvolvimento e teste de projetos eletrônicos. Pensando nisso, foi realizado o mesmo projeto no WOKWI, para facilitar a compreensão e caso não seja possível a reprodução física.</p>
    <p>Caso queira verificar a simulação acesse esse link https://wokwi.com/projects/381962569105608705 ou Clique <a href="https://wokwi.com/projects/381962569105608705">aqui </a> 
    
   <h2>Dashboard para análise:</h2>
  <p>No intuito de deixar mais fácil a compreensão das leituras dos dados, foi criado um dashboard em python, o qual tem como objetivo a análise temporal dos dados que foram armazenados pelo STH-COMET com registro de batimentos cardíacos identificados pelo sensor ao longo do tempo.</p>

  ![image](https://github.com/Rodrigo-Brasileiro/caseHapVida/assets/126472820/2a69e46c-4c23-49d9-a8e3-6abc4bceae28)

  <p>Clique <a href="https://github.com/Rodrigo-Brasileiro/caseHapVida/blob/main/interwatch.py">aqui </a> para acessar o código do dashboard em python. Para utiliza-lá, basta baixar os arquivos e os executar em um ambiente apropriado, como Visual Studio Coden ou google Colab. </p>

  <h3>Referências</h3>
 <p>Buscando mais informações e aprimoramento, nossas referências foram:</p>
     <ol><li>Link: https://github.com/fabiocabrini/fiware</li>
         <li>Link: https://www.cnnbrasil.com.br/saude/transplante-de-coracao-quantas-pessoas-esperam-por-um-novo-orgao-no-brasil/#:~:text=A%20fila%20de%20espera%20para,Nacional%20de%20Transplantes%20(STN) </li>
         <li>Link: https://www.scielosp.org/pdf/csp/2006.v22n10/2229-2239/pt </li>
        <li> Link: https://www.analog.com/media/en/technical-documentation/data-sheets/max30102.pdf </li>
     </ol>

   

       
