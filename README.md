# Pesquisa de CEP com Selenium

Este é um script Python para pesquisar detalhes de endereços usando o site dos Correios. Ele utiliza a biblioteca Selenium para automatizar o processo de inserir um CEP brasileiro e obter informações como rua, bairro, cidade e CEP. Este script também inclui uma interface gráfica simples construída com Tkinter para interação do usuário.

## Pré-requisitos

Antes de executar o script, certifique-se de que possui os seguintes requisitos instalados:

- Python (>=3.6)
- Selenium
- Chrome WebDriver
- Tkinter (para GUI)

Você pode instalar o Selenium e o Tkinter usando o pip:

```bash
pip install selenium
```

Você também precisa baixar o Chrome WebDriver compatível com a versão do seu navegador Chrome. Certifique-se de adicionar o executável do WebDriver ao PATH do seu sistema.

## Uso

1. Clone ou faça o download deste repositório para a sua máquina local.
2. Instale as bibliotecas necessárias conforme mencionado nos pré-requisitos.
3. Certifique-se de ter o Chrome WebDriver instalado e adicionado ao PATH do seu sistema.
4. Execute o script:

```bash
python cep_search.py
```

5. Uma janela GUI aparecerá, permitindo que você insira um CEP e clique no botão "Pesquisar" para obter informações de endereço.

## Aviso Legal

Observe que a raspagem da web e a automação podem estar sujeitas aos termos de serviço do site que você está acessando. Certifique-se de cumprir quaisquer diretrizes legais e éticas ao usar este script.

## Autor

Este script foi criado por Magno Alves.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.
