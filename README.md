# exercicio-cliente-servidor

## O que é necesário para usar este código?

- Ter uma versão do python instalada no computador
- Uma IDE(editor de código) configurada para o uso de programação python
- Saber o básico sobre como usar o terminal(prompt de comando, tilix,terminal do gnome, etc.)
- Baixar as bibliotecas Flask e Request, pode fazer isso com o comando abaixo

```
pip install Flask requests
```

- Caso seu terminal acuse que você não tem o pip instalado

```
python -m pip install --upgrade pip
```

- Também pode ser necessário, em alguns casos, criar um ambiente virtual na máquina.(Em nossa escola por exemplo algumas alterações/instalações são bloqueadas pelos administradores, evitando danos as máquinas da Faculdade)

```
python -m venv venv
python -m pip install --upgrade pip
```

## Comandos para usar o código pelo terminal

```
python ./python/servidor.py
```

```
python ./python/cliente.py
```

Caso tenha alterado sua máquina para usar o outro comando, o código que deve ser utilizado será este a sua alteração com o path(caminho) do código, no meun caso uso python3.

```
'comando' ./python/servidor.py
```

```
'comando' ./python/cliente.py
```

###Exemplo:
```
python3 ./python/servidor.py
```

```
python3 ./python/cliente.py
```

### Se quiser ver como as mensagens ficam salvas, no navegador acesse o link abaixo
##### Lembrese de estar com o código do servidor rodando para vizualizar

[link para vizualizar o JSON gerado para as mensagens](http://127.0.0.1:5555/receber)