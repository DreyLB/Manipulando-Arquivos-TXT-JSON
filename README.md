Estudando sobre os fundamentos da linguagem Python, gostei do que fiz no último post e decidi "brincar" mais com a linguagem de programação. No entanto, perdi os dados que usei para fazer o relatório simplificado anterior. Nessa perda me veio a seguinte ideia: os dados vieram a mim em TXT, transformei em um relatório simplificado e agora seria interessante transformar esse TXT em JSON.

JSON - JavaScript Object Notation, é a forma mais comum que analistas extraem dados diretamente da WEB. Sua estrutura é muito parecida com dicionários em Python e na sua própria biblioteca é possível fazer uma conversão de Dicionário para JSON, com a função dumps.

Aprendendo bastante sobre manipulação de arquivos no curso da Data Science Academy, busquei maneiras, primeiramente, de transformar o TXT em listas, pois, a partir disso, conseguiria manipular os dados com maior facilidade.

Havendo quebras de linha a todo momento, seria um notório erro - que por sinal demorei a entender – então, arrumei uma maneira de remover o que representava esses espaços vazios na minha lista.

A partir desse pequeno tratamento, foi muito simples transformar a lista em listas separadas, as quais seriam posteriormente valores encontrados ao pesquisar sobre suas respectivas chaves.

Por meio desta, vale salientar que não foi simples chegar em um raciocínio que para muito é simples. E gostaria de encorajar todos os colegas presentes na minha rede, a pensar em algo tão simples quanto transformar um texto em uma estrutura de dados. E, daqui um tempo, iremos olhar nossos códigos antigos e pensar o quão imperfeito ele é, e notaremos o quanto evoluímos.