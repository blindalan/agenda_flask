<h1 align="center"> Design Patttern - Agenda com Flask usando Singleton</h1>

## Membros do trabalho:
<div>
<img src="https://github.com/blindalan.png" width="45" height="45" style="max-width: 100%;">
<img src="https://github.com/emiliodeoliveira.png" width="45" height="45" style="max-width: 100%;">
<img src="https://github.com/marlonlupa.png" width="45" height="45" style="max-width: 100%;">
</div>

Código desenvolvido por Marcos Alan.

Link do vídeo do trabalho: https://drive.google.com/file/d/13qB_YBDGyrCEpLi6JooJCT4tpX4AUZ8W/view

## Do que se trata esta aplicação?

Esta aplicação é uma agenda de contatos feita com Flask e utiliza o padrão Singleton. Para persistência de dados, foi escolhido o banco de dados MySQL. 

Esse projeto é uma refatoração do codigo abaixo:

https://github.com/blindalan/agenda_simples

## Tecnologias usadas

- Python 3.10
- Flask
- pymysql
- wtforms
- css3
- html5

## Singleton

Esse design pattern se caracteriza por ser um dos padrões mais simples de implementar. Ele fornece apenas uma classe para criação dos métodos e especificação deles.
<img src="https://miro.medium.com/max/1028/1*WXXQZp1glrQxLqrQ_TDN7Q.png" style="max-width: 100%;">

Aqui temos o diagrama de classe que mostra como funciona a criação de instâncias:

<img src="https://arquivo.devmedia.com.br/artigos/Higor_Medeiros/PadraoSingleton/PadraoSingleton_Java1.jpg" style="max-width: 100%;">

Nele podemos notar a presença do construtor da classe Singleton(), que é setado como privado. Ele não permite que a classe seja instanciada a não ser que seja feito por ela mesmo. Nesse caso será instanciada pelo método getInstance(), que é estático e pode ser acessado de qualquer outra classe sem precisar instanciar a classe Singleton().

Ele também é eficiente em simplificar as conexões com o banco de dados, evitando conexões irrelevantes.

Comparação de conexão do Singleton vs. Conexão tradicional:

<img src="https://phpenthusiast.com/theme/assets/images/blog/the-singleton-pattern-explained.png" style="max-width: 100%;">

## Prós e contras

Vantagens:
- Mais controle sobre o acesso às propriedades e métodos de uma classe;
- Reduz o consumo de memória desnecessário;
- Com apenas uma implementação interna do singleton pode-se fazer com que o singleton crie um número controlado de instâncias;
- É mais flexível que métodos estáticos por permitir o polimorfismo.

Desvantagens:
- Viola o Princípio da Responsabilidade Única. O padrão resolve dois problemas ao mesmo tempo;
- Qualquer parte do código pode chamar o método instance(), e ter o acesso aos dados dessa classe; 
- Falsa segurança: No java, por exemplo, não existe uma classe apenas por JVM. O conceito de carregamento de classes em java é feito por ClassLoader.

## Conclusão

Esse padrão é indicado quando se necessita de um único ponto para criação de instâncias de classe, ou de apenas uma instância de classe. Aplicativos que necessitam de um ponto de acesso global se beneficiam desse design pattern.

## Observações sobre o projeto:

### venv
- Significa virtual enveroment
- Para instalação local das bibliotecas usadas no projeto


### Editor e ide usada para o desenvolvimento
- vscode
- pycharm
