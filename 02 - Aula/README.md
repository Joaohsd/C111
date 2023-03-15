# **Coleções no Python**

São estruturas de dados estruturados, que possibilitam armazenar um ou mais valores.

## **1 - Tuplas**

As Tuplas são coleções no Python responsáveis por armazenar valores homogêneos ou heterogêneos. Ela é uma coleção imutável, ou seja, não é possível adicionar valores, ou até mesmo modificá-los. Dessa maneira, ela acaba sendo utilizada para dados que não serão alterados no contexto de execução do código. Isto é, um exemplo clássico de utilidade para tal estrutura seria as siglas dos estados do Brasil:

* ### **Criando uma tupla**

<div align="center">

`estados = ('MG', 'SP', 'RJ', 'AM', 'PR', 'GO')`

</div>

## **2 - Listas**

As Listas são estruturas de dados, ou seja, coleções no Python responsáveis por armazenar múltiplos dados, homogêneos ou heterogêneos. Ao contrário das tuplas, ela permite alterar, adicionar e, até mesmo, excluir elementos da Lista criada. Dito isso, é possível realizar um CRUD completo nessa coleção.

* ### **Criando uma lista**

<div align="center">

`nomes = ['Goku', 'Vegeta', 'Trunks', 'Gohan']`

</div>

* ### **Adicionando um elemento a lista**

<div align="center">

`nomes.append('Pan')`

</div>

* ### **Atualizando um elemento da lista**

<div align="center">

`nomes[0] = 'Piccolo'`

</div>

* ### **Deletando um elemento da lista**

Nesse caso, é possível remover um elemento pelo seu próprio valor ou  pelo seu índice.

* #### **Pelo valor**

<div align="center">

`nomes.remove('Trunks')`

</div>

* #### **Pelo índice**

<div align="center">

`nomes.pop(2)`

</div>

## **3 - Conjuntos**

Os conjuntos são estruturas de dados, que possibilitam armazenar informações homogêneas ou heterogêneas. Ao contrário das listas, ele não permite que tenha elementos repetidos e estes podem estar dispostos de maneira desordenada. Ainda assim, não é possível realizar um CRUD completo. Dessa maneira, é possível apenas criar, adicionar e remover elementos. 

* ### **Criando um conjunto**

<div align="center">

`nomes = {'Goku', 'Trunks', 'Vegeta', 'Trunks', 'Gohan'}`

</div>

* ### **Adicionando um elemento ao conjunto**

<div align="center">

`nomes.add('Piccolo')`

</div>

* ### **Deletando um elemento do conjunto**

<div align="center">

`nomes.remove('Trunks')`

</div>

## **4 - Dicionários**

Finalizando as coleções do Python, temos os dicionários. Sua estrutura é do tipo chave-valor (possuindo várias chaves dentro do dicionário) e se assemelha com o formato JSON (JavaScript Object Notation). Assim como o conjunto, seu armazenamento é feito de maneira desordenada. Em um dicionário, é possível realizar o CRUD completo, assim como nas listas. Dessa maneira, podemos criar um dicionário, adicionar os elementos, atualizar os elementos e remover os elementos presentes nele.

## **Criando um dicionário**

<div align="center">

`pessoa = {'nome': 'Goku','idade': 42}`

</div>

* ### **Adicionando um elemento ao dicionário**

<div align="center">

`pessoa['sexo'] = 'M'`

</div>

* ### **Atualizando um elemento do dicionário**

<div align="center">

`pessoa['idade'] = 40`

</div>

* ### **Deletando um elemento da lista**

Nesse caso, é possível remover um elemento pelo sua própria chave de duas maneiras diferentes.

* #### **Removendo sem saber o seu valor**

<div align="center">

`del pessoa['nome']`

</div>

#### **Removendo com valor retornado, o método pop retorna o valor relacionado aquela chave**

<div align="center">

`x = pessoa.pop('sexo')`

</div>