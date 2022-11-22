# Python_Fundamentos_para_Analise_de_Dados
Resoluções de Projetos do Curso de Python Fundamentos para Análise de Dados 3.0 da DSAcademy

## 1) MiniProjetoCap06
 Contém as resoluções das 10 perguntas propostas no Mini Projeto do Cap06 do Curso.
 
#### OBS: A resolução da pergunta 7 diverge do gabarito da DSAcademy, conforme explicado abaixo. Um e-mail foi enviado em 14JAN2022 para a DSA tendo em vista, caso eu esteja certo, à atualização do gabarito no curso.

Na pergunta de projeto 7, a solução apresentada pela DSA, mais pro final, elabora os seguintes trechos:
```
#Calcular duração por gênero
genero_runtime = []
for item in generos_unicos:
    consulta = 'SELECT runtime_minutes Runtime FROM  titles  WHERE genres LIKE '+ '\''+'%'+item+'%'+'\' AND type=\'movie\' AND Runtime!=\'NaN\''
    resultado = pd.read_sql_query(consulta, conn)
    genero_runtime.append(np.median(resultado['Runtime']))
```
Mais precisamente na parte do RegEx: 
```
... LIKE '+ '\''+'%'+item+'%'+'\'  ...
```
há toda essa nomenclatura que teve um resultado bem parecido com o que utilizei através do **Like '%{item}%'**, pois a intenção era aceitar tanto o gênero ACTION sozinho, como também os gêneros que continham o ACTION, por exemplo: **Drama,Action** ou **Action,Documentary** ou **Fiction,Action,Drama**.

**Contudo**, ***há um detalhe imperceptível***, que pude constatar quando fui verificar se a contagem das quantidades de durações de filmes, resultante dessa QUERY supracitada, está igual às quantidades de filmes resultantes daquela primeira QUERY que fazemos no início, e depois aplicamos o CountVectorizer.

Com isso, verifiquei que quando a segunda QUERY, supracitada, é executada, o gênero **MUSIC** aglutinava as quantidades de durações de filmes do gênero **MUSICAL**, e com isso havia um **aumento** na contagem do gênero **MUSIC**.

Logo, após bater bastante a cabeça :exploding_head:, pude achar uma solução pra esse problema, que foi utilizar vários **LIKE e OR**, como se segue:
```
WHERE type='movie' AND tempo_duracao != 'NULL' AND (genres LIKE '%,{genero},%' OR
                                genres LIKE '{genero}' OR genres LIKE '%,{genero}' OR genres LIKE '{genero},%')
```
Com isso, a quantidade passava a bater.
Claro que não traz prejuízo ao ensinamento que é trazido pela questão7, mas como sempre gosto de fazer a prova real, acabei me deparando com isso.

## 2) DesafioCap07
Contém as resoluções das 5 missões propostas no Desafio do Cap07 do Curso.

## 3) MiniProjetoCap09
Contém 1 exercício de análise exploratória de autoria do curso. Foi salvo aqui como forma de se ter a mãos boas práticas e principais gráficos de análise exploratória;
Contém, também a resolução .......
