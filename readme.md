CRUD DE VENDAS

CRIAR UM SISTEMA DE GERENCIAMENTO DE VENDAS USANDO LINGUAGEM PYTHON.

>>> USUÁRIO IRÁ CRIAR, LER, ATUALIZAR E EXCLUIR VENDAS.

>>> APLICAÇÃO DE CONCEITOS DE CRUD E REST API.

A APP terá interface com o usuário para inserção, visualização, edição e deleção de vendas.

O métodos utilizados serão:

> GET: /vendas
> POST: /vendas
> GET: /vendas/{id}
> PUT: /vendas/{id}
> DELETE: /vendas/{id}

    >   O sistema deverá:

        >>  tratar as exceções;
        >>  inserir informações com data da venda, produto vendido, quantidade e preço unitário;
        >>  visualizar uma venda e todas suas informações;
        >>  edição de qualquer informação de venda;
        >>  modificação de qualquer informação da venda;
        >>  exclusão de uma venda totalmente do servidor pelo usuário.

    >   Será utilizado o Banco de dados SQlite.

    >   Geração de relatórios:

        >> permissão para usuário gerar relatório com informações sobre as vendas em formato txt ou csv;
        >> poderá ser personalizado de acordo com a necessidade do solicitante;
        >> no relatório poderá conter data, produto, preço unitário, total da venda.

    >   Ao final o sistema deveverá permitir que o usuário:

        >> crie, leia e exclua vendas tanto através da interface e também via requisições HTTP. 