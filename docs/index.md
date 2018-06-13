<p align="center">
<img src="https://www.favicon.cc/logo3d/154115.png">
</p>

# Simian Engine

Esta Game Engine busca encapsular a utilização da biblioteca [Pygame](https://www.pygame.org/wiki/about) e abstrair sua utilização, acelerando o desenvolvimento de jogos com python sem exigir grandes conhecimentos e entendimento do funcionamento interno de uma Game Engine, mantendo o foco do desenvolvedor no jogo e nas suas regras.

#### Disponível em https://pypi.org/project/simian-engine/

Equipe

| Nome | E-mail | GitHub |
| ---- | ------ | ------ |
| Álax de Carvalho Alves | alaxallves@gmail.com | [@alaxalves](https://github.com/alaxalves) |
| Fabíola Fleury | fabiola.mfleury@gmail.com | [@fabiolamfleury](https://github.com/fabiolamfleury) |
| Hugo Neves Carvalho | hugonvsc@gmail.com | [@hugonxc](https://github.com/hugonxc) |
| Josué Nascimento | josuetk63@gmail.com | [@josutk](https://github.com/josutk) |
| Matheus Joranhezon | mjoranhezon@gmail.com | [@Joranhezon](https://github.com/Joranhezon) |
| Pablo Diego Silva da Silva| pablodiegoss@hotmail.com | [@pablodiegoss](https://github.com/pablodiegoss) |
| Rodrigo Oliveira Campos | rodrigo.redcode@gmail.com | [@rodrigocam](https://github.com/rodrigocam) |
| Roger Lenke | rogerlenke@gmail.com | [@Rdlenke](https://github.com/Rdlenke) |

Colaboradores

Farão parte como consultores do projeto, apenas a professora, que terá como papel avaliar os artefatos criados assim como direcionar e orientar a equipe a tomar as decisões que levem o projeto a obter sucesso dentro das metas estabelecidas.

Professora Orientadora

| Nome | E-mail | GitHub |
| ---- | ------ | ------ |
| Milene Serrano | mileneserrano@gmail.com | [@mileneserrano](https://github.com/mileneserrano) |


-------------------------------------------------------------------------------------------------


# Descrição do Framework

|  Autor | Data  |   
|---|---|
| Josué Nascimento | 20/05 |
| Álax Alves | 20/05 |
| Roger Lenke | 20/05 |
| Fabíola Fleury | 25/05 |
| Roger Lenke | 25/05 |
| Álax Alves | 05/06 |
| Matheus Joranhezon | 08/06 |
| Álax Alves | 09/06 |
| Hugo Carvalho | 10/06 |

SimianFramework

O _Simian_ é um framework pensado para fornecer uma game engine utilizando a biblioteca  [pygame](https://www.pygame.org/news), criada para aplicações multimídia.

Este framework é construído utilizando a linguagem de programação Python. A distribuição, por sua vez, é dada por meio de um Python Index Package (PIP).

Características do Framework

Tipo do Framework

Frameworks podem ser agrupados em relação a como sua reutilização é feita. Existem três categorias principais: <b>caixa branca</b>, <b>caixa preta</b> e <b>caixa cinza</b>.

* <b>Caixa Branca:</b> Sua reutilização é proveniente de pontos flexíveis, fazendo proveito do uso de herança e implementação de interfaces. Esse tipo de framework também pode ser entendido como um framework orientado à hot spots. Esse frameworks são instanciados através do uso de herança, usando o padrão de projeto <i>Template Method</i> (Gamma, 1995), métodos abstratos que são implementados na subclasse, ou métodos com um comportamento pré-definido, mas que que podem ser alterados na subclasse. Uma particularidade desse tipo de framework é que eles normalmente são distribuídos com o código fonte, já que o desenvolvedor que o utiliza precisa saber como funcionam as superclasses para extendê-las.

* <b>Caixa Preta:</b> Tem a reutilização proveniente através de composições ao invés de heranças, de maneira que uma funcionalidade é implementada decompondo cada pedaço em diversos objetos e interfaces. Pelo fato de uma funcionalidade ser decomposta em várias classes, a produção de um framework caixa preta é mais complexa, e sua extensibilidade é limitada. Apesar disso, os frameworks caixa preta permitem uma facilidade maior ao desenvolvedor que os utiliza, pois é necessário pouco conhecimento de como o framework foi construído para utilizá-lo. A implementação de frameworks caixa preta são feitos geralmente em cima do padrão <i>strategy</i>. Esse tipo de framework é orientado à frozen spots.

* <b>Caixa cinza:</b> Os frameworks caixa cinza são frameworks que combinam a decomposição e a facilidade de uso dos frameworks caixa preta com a extensibilidade dos frameworks caixa branca. Ou seja, fazem uso de hot e frozen spots.

O _Simian_ será desenvolvido como um **framework caixa cinza**. Essa decisão foi tomada pela equipe pelo fato de que a produção de um framework caixa branca é mais fácil, o que o torna mais adequado para o desenvolvimento em um curto período de tempo. Além disso, os componentes de um jogo, sejam texto, cenas, tabuleiro, as ações dos jogadores, sprites são abstrações fundamentais, porém devem ser bastante flexíveis para a adequação ao contexto de cada desenvolvedor, o que também apoia a utilização de frameworks caixa branca, bem como frisa a necessidade de uma boa documentação para utilização da game engine. 

Ainda neste contexto, componentes como músicas, efeitos sonoros e animações, são parte de um jogo porém o desenvolvedor não precisa redefinir a lógica por trás do funcionamento destes, apenas utilizam por meio de composições. Sendo assim, assemelha-se a utilização de caixa preta. De modo que ao incorporarmos essas duas premissas presentes em nosso contexto, foi bastante claro ver que tínhamos um framework de caixa cinza em nossas mãos, já que é evidente a presença de aspectos inerentes a caixa branca e caixa preta.

Em suma, O Simian caracteriza-se como um framework caixa cinza. O que isso quer dizer? Quer dizer que ele possui elementos de frameworks caixa branca (white box) e caixa preta (black box). No caso de frameworks do tipo caixa branca, estes requerem que o usuário entenda os componentes internos do framework para usá-lo efetivamente. O comportamento, nesse caso, é estendido através da criação de subclasses, utilizando-se da herança. Por outro lado, um framework do tipo caixa preta não exige que o usuário compreenda profundamente seu funcionamento interno. Nota-se que o resto do framework é classificado como caixa preto.

Tecnologia de apoio utilizada para a implementação do framework

Para a implementação do tatics framework será utilizada a seguinte tecnologia:

[**pygame**][pygame] : Uma biblioteca para python escrita sendo como base a biblioteca, em linguagem C, Simple DirectMedia Layer (SDL) para construção de aplicações multimídia como arte digital, música e jogos. Pygame é uma game engine, ou seja,  é um software ou um conjunto de bibliotecas usado na simplificação do desenvolvimento de jogos, que irá abstrair todas as funções visuais e de processamento como base do código, e a essência do jogo como a estratégia, o design e a ideia principal que serão realmente pensadas e estudadas para o jogo.

Funcionalidades

Configuração da engine

O _simian_ deve permitir que o desenvolvedor configura alguns aspectos de seu jogo por meio de objetos ou um arquivo de configuração. Essas configurações podem ser relacionadas ao _framerate_ do jogo, tamanho da tela, entre outros aspectos.

Game Objects

Um _game object_ é a estrutura fundamental utilizada no desenvolvimento de um jogo. Qualquer coisa que deve ser atualizada e/ou desenhada em um jogo é um gameobject.

O _simian_ deve permitir ao desenvolvedor criar seus próprios game objects, sobrescrevendo métodos básicos que serão executados a cada frame pela engine. Além disso, deve ser possível adicionar múltiplos game objects em cenas.

Animações

A _engine_ deve permitir o **gerenciamento** das animações do jogo por meio de _sprites_. Uma _sprite_ é um conjunto de imagens que é integrada para criar movimento. Esse gerenciamento deve acontecer possibilitando ao desenvolvedor definir a posição da animação, velocidade, se a animação se repete ou não, entre outros aspectos.

Cenas

A estrutura de cenas em uma engine é a estrutura responsável por gerenciar as telas do jogo, mudanças entre fases, carregamento de objetos específicos a cada tela, entre outros. O _simian_ deve permitir ao desenvolvedor a **criar novas cenas**, **adicionar game objects em cada cena**, **mudar entre uma cena e outra**, etc.

Músicas

O _simian_ deve permitir com que o desenvolvedor insira músicas, tanto em suas cenas quanto em seus game objects. Deve ser possível pausar, resumir e iniciar uma música, definir até onde esta irá ser tocada, se irá se repetir, etc.

Efeitos sonoros

Deve ser possível ao desenvolvedor efeitos sonoros em seus game objects, podendo iniciá-los a qualquer momento.

Física

O _simian_ deve oferecer uma estrutura que facilite o cálculo da física dos jogos, realizando este cálculo separadamente a 
atualização dos game objects a cada frame.

Periféricos

O _simian_ deve disponibilizar classes e métodos para que o usuário possa obter dados dos periféricos conectados ao ambiente, por exemplo: alguma tecla ou botão do mouse é pressionada. Desse modo é o usuário é capaz de controlar todo o jogo utilizando estes recursos.  

Referências

- PyGame: https://www.pygame.org/news

-------------------------------------------------------------------------------------------------

# Plano de Gerenciamento do Projeto

| Autor | Data |   
| ----- | ----- |
| Fabíola Fleury| 05/06 |
| Álax Alves| 05/06 |

Introdução

O seguinte documento tem como objetivo, em termos simples, mostrar todo o processo seguido pelo time para o gerenciamento do projeto. Isso irá incluir o ciclo de vida do projeto, requisitos, estratégias de gerência e de maneira geral os rituais adotados para monitoramento e controle do projeto.

Visão Geral do Documento

Encontra-se neste documento  as definições relacionadas ao gerenciamento do projeto simian. De forma resumida apresentam-se o escopo do projeto, assim como seu ciclo de vida, deixando claro as linhas de base do projeto.

Ciclo de vida do projeto

O ciclo de vida a ser utilizado será adaptativo por meio de iterações, utilizando a metodologia Kanban para traduzir a abordagem ágil adequada a este contexto.

Kanban

O kanban documenta o fluxo de trabalho de forma transparente, tendo colunas nomeadas "Backlog" "In progress" "Done" que mapeam o estado de "fichas", representadas neste projeto por issues. Ele fica disponível para todos os integrantes do projeto e cada um é responsável por atualizar o estado da issue que está trabalhando.

Escolheu-se o uso do kanban pela sua versatilidade e adaptabilidade como o ciclo de vida deste projeto é curto, ele permite o gerenciamento do projeto sem comprometimento da qualidade e das entregas planejadas. Além disso, a equipe já trabalhou em outro projeto da disciplina e já atingiu um nível de integração e comunicação desejável para conseguir utilizar de forma madura o kanban.

Linhas de base

Engenharia de Requisitos

A definição da documentação de requisitos por meio de issues do github e kanban do zenhub e das técnicas de elicitação devem estar documentadas.

Escopo

O escopo inicial do projeto foi documentado [aqui](https://github.com/Desenho2018-1/simian/wiki/Descri%C3%A7%C3%A3o-do-framework). Este documento ainda será refinado para uma especificação do framework.

Cronograma

O cronograma é baseado nas datas definidas por meio de plano de ensino da disciplina relacionadas ao Módulo II - Arquitetura de software. Este módulo possui duas entregas, o ponto de controle 1, inicial, com data em 21/05/2018, e a entrega final em 18/06/2018. De modo que o cronograma foi idealizado da seguinte forma:

* 11/05/2018: Primeira Aula do módulo
* 11/05/2019 - 21/05/2018: Preparação do projeto e estudos do conteúdo  
* 22/05/2018 - 01/06/2018: Ciclo 1
* 02/06/2018 - 15/06/2018: Ciclo 2
* 16/06/2018 - 18/06/2018: Finalização e entrega do trabalho

Monitoramento e Controle

Para acompanhamento do fluxo de trabalho e andamento do projeto, será utilizada a metodologia Kanban, como já bem explicado em seção anterior, de maneira que o grupo ficará responsável pelo monitoramento e controle do projeto por meio da visualização das issues que serão transportadas nas colunas do kanban de acordo com seu estado atual.
Escolheu-se essa técnica já que torna-se simples acompanhar e administrar os passos de cada projeto, sendo possível aprimorar a sua gestão e tornar as operações mais eficientes, além de ser visível a qualquer _stakeholder_.

Referências 

- Duncan, W. R. (1996). A guide to the project management body of knowledge.
- Jyothi, V. E., & Rao, K. N. (2012). Effective Implementation of Agile Practices-Incoordination with Lean Kanban. International Journal on Computer Science and Engineering, 4(1), 87.

-------------------------------------------------------------------------------------------------

# Engenharia de Requisitos

| Autor | Data |   
| ----- | ----- |
| Álax Alves| 05/06 |
| Fabíola Fleury| 13/06 |

Introdução

Podemos dizer que a engenharia de requisitos é uma forma apropriada para entender de fato o que o cliente deseja, ajuda a analisar essas necessidades e verificar a viabilidade das mesmas. Através da engenharia de requisitos é possível negociar prazos e definir um escopo claro por meio de uma especificação do sistema, tirando todas as possíveis ambiguidades que o projeto poderia vir a ter.

Requisitos de Qualidade

É conhecido que os requisitos de qualidade representam alguns desafios no decorrer do projeto, pois estes muitas vezes são difíceis de modelar, apresentam ambiguidade , acabam sendo ignorados durante o desenvolvimento porém tem sua função crítica para o desenvolvimento do projeto.

Dentro do contexto do Simian, os requisitos de qualidade são mapeadas para as issues do Git e são organizadas no KanBan da equipe fornecido pela ferramenta ZenHub. Para visualizar a escrita de uma issue basta acessar o KanBan do projeto.

Tracking

A estratégia de rastreabilidade dos requisitos tem início na Pré Rastreabilidade, onde os requisitos começam a ser visualizados nos mais altos níveis de projeto. No Simian, a rastreabilidade de requisitos inicia-se em alto nível já que tem-se uma ideia bem consolidada da proposta. É claro que não se limita a isso, de maneira que esse _tracking_ poderá ser abstraído em níveis mais baixos.

Fase de Elicitação

Dentro do contexto do projeto, a elicitação de requisitos aconteceu em uma conversa entre os membros da equipe a respeito de quais abstrações seriam feitas de maneira a tornar a aplicação mais genérica, tendo em vista que não seria aproveitado o software anterior, implementado na primeira parte da disciplina.

Após a conversa entre os membros da equipe, as issues foram inicialmente identificadas e associadas a sua label correspondente, de modo que fosse capaz dividi-las entre a equipe e separá-las para que fossem devidamente implementadas.

Então, para assegurar-se da corretude dos requisitos inicialmente levantados, procurou-se apoio bibliográfico no que diz respeito a arquitetura de game engines, com apoio no livro "Game Engine Architecture" do autor Jason Gregory e também na bibliografia da disciplina de Arquitetura e Desenho de Software. Assim, foram verificados os requisitos e reformulados e inseridos novos quando necessários.

Labels

Foi adotada a estrategia de que os requisitos do simian seriam mapeados na forma de _issues_ do Git, de forma que pudessem ser classificados através das [labels](https://github.com/Desenho2018-1/simian/labels), estas tem um significado que pode ser o tipo de requisito que aquela issue representa, o nível de criticidade e também que tipo de artefato as tasks dela afetarão.

bug
Representa um bug encontrado na aplicação.

cli
Representa aspectos relacionados ao contexto do _cli_ da aplicação.

duplicate
Indica que essa issue já foi identificada e registrada.

engine basics
Representa aspectos inerentes a estrutura básica de uma engine.

enhancement
Indica uma proposição de melhoria.

good first issue
Indica que é uma boa issue para se trabalhar a fim de iniciar contato com a aplicação.

help wanted
Representa que o membro assinado a essa issue está enfrentando problemas com ela e necessita ajuda.

invalid
Indica algum comportamento inesperado.

manager
Representa histórias relacionadas a entidade Manager.

question
Representa a necessidade de haver maiores informações a respeito.

wontfix
Indica que não será empregado mais esforço na frente em questão.

technical
São relacionadas a dividas técnicas do projeto e requisitos de qualidade.

Referências

- SOMMERVILLE, I., Engenharia de Software, 9ª Edição. São Paulo: Pearson Prentice Hall, 2011.
- PMI. Um guia do conhecimento em gerenciamento de projetos. Guia PMBOK 5a. ed. - EUA: Project Management Institute, 2013.

-------------------------------------------------------------------------------------------------

# Diagramação

|  Autor | Data  |   
|---|---|
| Josué Nascimento | 20/05 |
| Álax Alves | 20/05 |
| Roger Lenke | 21/05 |
| Roger Lenke | 25/05 |
| Roger Lenke | 29/05|
| Josué Nascimento |30/05|
| Josué Nascimento |01/06|
| Fabíola Fleury |04/06|
| Matheus Joranhezon |04/06|
| Álax Alves | 06/06 |
| Roger Lenke | 06/06 |
| Matheus Joranhezon | 08/06 |

Introdução

O diagrama de classes é o diagrama principal utilizado para representar e documentar a estrutura do _Simian_ Framework. Ele identifica os _Hot Spots_ e também os _Frozen Spots_, mostrando os pontos de reutilização que podem ser utilizados pelo desenvolvedor.

Diagrama de Classes

_Hot Spots_

Em relação à estrutura de um framework, as suas partes variáveis são chamadas de hot spots, já as fixas, são chamadas de frozen spots. Os frameworks em que os hot spots são implementados através da especialização de classes abstratas são chamados de frameworks de caixa branca. Já os frameworks em que os hot spots são implementados através da composição de componentes são chamados de frameworks de caixa preta.

Os hot spots podem ser identificados no diagrama pelas classes verdes.

| Hot Spot | Descrição |   
|:--:|:--:|
|GameObject|Um GameObject é a estrutura fundamental da engine, que representa qualquer entidade que precise ser desenhada e/ou atualizada. O GameObject é implementado como um Hotspot, de maneira que o desenvolvedor consiga produzir os elementos do jogo de acordo com o contexto|
|BaseScene| Uma Scene é a estrutura que controla vários GameObjects num contexto específico. Toda tela de um jogo é uma Scene. A classe BaseScene serve de estrutura base para que o desenvolvedor crie suas próprias telas.|

_Frozen Spots_ 

Frozen Spots definem a arquitetura básica do framework, são aspectos dos quais não poderão ser mudados em cada instância do do framework. Esses pontos também são chamamos de core do framework. Os Frozen Spots definem uma arquitetura geral, definindo o comportamento dos componentes básicos bem como os relacionamentos entre eles. Estes permanecem físicos no framework.

Os frozen spots podem ser identificados no diagrama pelas classes vermelhas.

| Frozen-Spot | Descrição |   
|:--:|:--:|
|GameEngine|A classe principal da Engine, que será utilizada pelo desenvolvedor pra incluir suas cenas personalizadas.|
|WindowManager|Classe utilizada para definir e adquirir o _canvas_ do jogo.|
|SceneManager|Classe utilizada pela Engine para controlar as cenas adicionadas pelo desenvolvedor, a sua ordem de execução, a exclusão de seus objetos, entre outras atividades de gerenciamento.|
|AnimationManager|Classe utilizada para gerenciar a execução de animações, sua velocidade, se são repetíveis, etc. A classe não é extendível, mas pode ser adicionada a qualquer GameObject, mesmo um GameObject específico para o jogo.|
|Sprite|A classe que representa a animação em si, possuindo o caminho da imagem da animação, o tamanho de cada quadro, entre outros atributos.|
|SoundManager|Classe utilizada para gerenciar a execução de sons e músicas de um GameObject. A classe não é extendível, mas pode ser adicionada a qualquer GameObject, mesmo um GameObject específico para o jogo.|
|Sound|Classe que representa um som em si.|

Diagrama

Versão 7
[[/img/FrameworkClassDiagram7.png]]
[Ampliar imagem](https://raw.githubusercontent.com/wiki/Desenho2018-1/simian/img/FrameworkClassDiagram7.png)

Versão 6
[[/img/FrameworkClassDiagram6.jpg]]
[Ampliar imagem](https://raw.githubusercontent.com/wiki/Desenho2018-1/simian/img/FrameworkClassDiagram6.jpg)

Versão 4
[[/img/FrameworkClassDiagram4.jpg]]
[Ampliar imagem](https://raw.githubusercontent.com/wiki/Desenho2018-1/simian/img/FrameworkClassDiagram4.jpg)

Versão 3
[[/img/FrameworkClassDiagram3.png]]
[Ampliar imagem](https://raw.githubusercontent.com/wiki/Desenho2018-1/simian/img/FrameworkClassDiagram3.png)

Versão 2
[[/img/FrameworkClassDiagram2.png]]
[Ampliar imagem](https://raw.githubusercontent.com/wiki/Desenho2018-1/simian/img/FrameworkClassDiagram2.png)

Versão 1
[[/img/FrameworkClassDiagram.png]]
[Ampliar imagem](https://raw.githubusercontent.com/wiki/Desenho2018-1/simian/img/FrameworkClassDiagram.png)


-------------------------------------------------------------------------------------------------

# Documentos Complementares

## Deploy contínuo no Docker

| Autor | Data |   
| ----- | ----- |
| Álax Alves| 09/06 |
| Álax Alves| 13/06 |

Como foi configurado no Simian

```
deploy:
  - provider: script
    script: bash scripts/sh/docker-deploy.sh
    on:
      branch: master
```

O _stage_ de deploy do travis reconhece o Docker por default, porém foi escolhido realizá-lo atráves de um script específico, no caso o `docker-deploy.sh` já que são feitas configurações adicionais.

O script pode ser visto abaixo:

```
#!/bin/bash

# Represents the latest version of the project according to setup.py file
VERSION=$(python setup.py --version)

echo "Latest Simian version is $VERSION";

if [[ "${TRAVIS_BRANCH}" == "master" ]]; then
	echo "Deploying to Docker registry latest Simian...";
	docker login -u "$DOCKER_USERNAME" -p "$DOCKER_PASSWORD";
	docker build -f /home/travis/build/Desenho2018-1/simian/scripts/docker/Dockerfile -t simian:"$VERSION" .;
	docker tag simian:$VERSION $DOCKER_USERNAME/simian:$VERSION;
	docker push alaxalves/simian:"$VERSION";
else
	echo "Skipping Docker registry deploy";
fi;
```

Aqui temos que obtém-se a última versão do Simian a partir do arquivo `setup.py`, de maneira que é feita uma nova validação da branch em shell, se estivermos na branch master então é realizado um upload da última versão do Simian no registry.

Fazendo upload para o Docker em 5 passos

Passos:

1. Crie uma conta no [DockerHub](https://hub.docker.com/)

2. Ative a sua conta através do link fornecido no email registrado.

3. Crie um script Dockerfile com comandos necessários a construção do seu ambiente.

4. Gere uma imagem da sua aplicação
```
docker build -t nome-de-usuario/nome-da-imagem:versao-da-imagem -f caminho/do/dockerfile .
```

4. Faça login no docker através do terminal
```
docker login
```

5. Suba sua imagem para o seu registry
```
docker push nome-de-usuario/nome-da-imagem:versao-da-imagem
```

Confira sua mais nova imagem em https://hub.docker.com/r/nome-de-usuario/nome-da-imagem/

Configurando deploy contínuo no Travis CI para o Docker em 3 passos

Passos:

1. Escreva um script que execute os passos para deploy.

2. Tendo configurado uma primeira vez o [Upload no Docker](#fazendo-upload-para-o-docker-em-5-passos), coloque em seu `.travis.yml` a seguinte _task_, por exemplo.

```
deploy:
  - provider: script
    script: caminho/para/o/seu/script.sh
    on:
      branch: master
```

E Pronto! Está configurado o deploy no DockerHub.


## Deploy contínuo no PyPi

| Autor | Data |   
| ----- | ----- |
| Álax Alves| 07/06 |
| Álax Alves| 08/06 |
| Álax Alves| 09/06 |

Como foi configurado no Simian

```
deploy:
  - provider: pypi
    user: alaxalves
    password:
      secure: A9BgjsRjxt.....
    on:
      branch: master
      python: 3.5
```

O _stage_ de deploy do travis reconhece o PyPi como provedor default, o que facilita bastante a vida do desenvolvedor, daí é só adicionar as suas credenciais - encriptadas - e configurar algo a mais que deseja configurar, como a branch de deploy por exemplo.

Fazendo upload para o PyPi em 7 passos

Passos:

1. Crie uma conta na [PyPI](https://pypi.org/) e [PyPi Test](https://test.pypi.org/).

2. Ative a sua conta através do link fornecido no email registrado.

3. Certifique-se que seu projeto possui as dependências [Twine](https://pypi.org/project/twine/) e [Wheel](https://wheel.readthedocs.io/en/stable/) instaladas.

4. Configure o seu arquivo `setup.py` para que respeite as diretrizes no PyPi, como no [exemplo](https://github.com/Desenho2018-1/simian/blob/devel/setup.py).

5. Configure o arquivo `setup.cfg` para explicitar a Licença do seu projeto e utilizar o Wheel para construir pacote genéricos, como no [exemplo](https://github.com/Desenho2018-1/simian/blob/devel/setup.cfg).

6. Construa o seu pacote usando o Wheel.
`python setup.py sdist bdist_wheel`

Isso irá criar uma pasta chamada `dist` em seu repositório.

7. Faça o upload do seu pacote recém criado usando o Twine.
`twine upload -u nome-do-usuario -p senha-do-usuario dist/*`

Configurando deploy contínuo no Travis CI para o PyPi em 3 passos

Passos:

1. Tendo configurado uma primeira vez o [Upload na PyPi](#fazendo-upload-para-o-pypi-em-7-passos), coloque em seu `.travis.yml` a seguinte _task_, por exemplo.

```
deploy:
  provider: pypi
  user: username-no-pypi
  password: senha-no-pypi
  on:
    branch: uma-branch-estável
```
O travis dá suporte ao PyPi por padrão, de modo que apenas colocando os _steps_ acima você terá configurado o deploy automatizado.

2. Claro que você não quer sua senha no PyPi acessível ao mundo, por isso encripte a sua senha usando a _gem_, ou pacote do travis.
    a. Baixe a gem do travis:
    ```
    gem install travis
    ```
    
    b. Encripte a sua senha do PyPi:
    ```
    travis encrypt --add deploy.password
    ```

3. Após isso a gem irá automaticamente encriptar sua senha no `.travis.yml` e seu yml irá ficar algo como:
```
deploy:
  provider: pypi
  user: username-no-pypi
  password:
    secure: aqui-irá-aparecer-uma-hash-enorme-que-representa-a-sua-senha-encriptada
  on:
    branch: uma-branch-estável
```

E pronto! Temos configurado o deploy contínuo!

Referências
 - [Publishing a Package to PyPI using Travis](https://openedx.atlassian.net/wiki/spaces/OpenOPS/pages/41911049/Publishing+a+Package+to+PyPI+using+Travis)
- [PyPI deployment](https://docs.travis-ci.com/user/deployment/pypi/)
