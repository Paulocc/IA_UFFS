
<h1  align="center"> Trabalho Final IA UFFS </h1>

 O objetivo deste projeto é desenvolver um algoritmo utilizando o k-médias, onde posteriormente deve ser aplicado a 6 imagens dentro de um tema definido pelo próprio aluno, gerando assim, 7 imagens diferentes baseados nos valores aplicados no k-médias. Com isso feito, uma análise deve ser realizada, observando diversos pontos como tamanho do arquivo gerado, quantidade de cores, qualidade da imagem, entre outros pontos. Para uma descrição mais completa você pode abrir o arquivo [Descricao_Trabalho_final.pdf](https://github.com/Paulocc/IA_UFFS/blob/main/Descricao_Trabalho_final.pdf)

 O tema escolhido para esse trabalho foi **Cenários de jogos**, onde imagens diferentes foram escolhidas para ser aplicado o algoritmo, você pode verificar as imagens na pasta [images](https://github.com/Paulocc/IA_UFFS/tree/main/images), assim como pode ver as imagens geradas na pasta [generated](https://github.com/Paulocc/IA_UFFS/tree/main/generated).
 

***

<h2  align="center"> Tecnologias Utilizadas </h2>

***

<p  align="center">


<img  height="45"  src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" alt='Python'>

<img  height="45"  src="https://github.com/devicons/devicon/blob/master/icons/github/github-original.svg" alt='GitHub'>

</p>

  
* Python - Para o desenvolvimento da atividade, utilizando as diversas bibliotecas disponíveis em python.

* GitHub - Para auxiliar no controle de versão e envio do projeto.

***
<h2  align="center"> Funcionamento </h2>

***

### Pré-requisitos

* Ter o [Python](https://www.python.org/) instalado

* Ter o [Git](https://git-scm.com/downloads) instalado

1. Clone este repositório para o seu ambiente local:

```bash
git clone https://github.com/Paulocc/IA_UFFS.git
```

2. Instale todas as dependências do projeto com o PIP
```bash
pip install matplotlib pandas opencv-python scikit-learn
 
```

3. Execute o arquivo ``main.py``:
```bash
python main.py
```

Com o comando executado, as imagens serão geradas

## **IMPORTANTE**

A execução do código pode levar muito tempo dependendo do seu hardware, para isso modifique a seguinte linha do código:

```bash
n_clusters_values = [2, 5, 12, 25, 38, 47, 100]
```

Prefira começar apenas com o valor 2, só para fazer um teste, e posteriormente vá aumetando conforme a necessidade, caso já esteja com o código rodando, apenas use um ctrl+c no terminal para finalizar a execução.

***
<h2 align="center"> Arquivos criados </h2>

***

Ao fim da execução do código, 42 novas imagens serão geradas, além disso, na pasta [info](https://github.com/Paulocc/IA_UFFS/tree/main/info), é possível ver as informações sobre cada imagem:

<p><img  width= 100%  height=auto  src="https://i.imgur.com/3NeGdrc.png"></p>

Além disso, uma planilha é criada com informações sobre todas as imagens, porém esse arquivo está com um problema ao salvar o tamanho real da imagem, então não foi utilizado todos os valores que estão na planilha, é possível arrumar isso, mas acabei não arrumando ainda.
 

