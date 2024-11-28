# Ecos de Pernambuco

**Ecos de Pernambuco** é um projeto interativo que utiliza sensores LDR e áudios para criar uma experiência imersiva baseada na cultura pernambucana. O sistema detecta interações do usuário através de luz para reproduzir áudios em diferentes idiomas, oferecendo uma experiência inclusiva e acessível.

---

## Funcionalidades

- **Interação baseada em sensores de luz (LDR):**

  - Cada sensor dispara um comando específico ao detectar luz por um determinado tempo.
  - Suporte para até 8 sensores de direção.

- **Reprodução de áudios:**

  - Arquivos de áudio podem ser reproduzidos em Português, Inglês ou Espanhol.
  - Suporte para interrupção de um áudio em execução para reproduzir outro.

---

## Tecnologias Utilizadas

- **Hardware:**

  - Arduino com sensores LDR para detecção de luz.
  - Componentes adicionais: resistores e divisores de tensão.

- **Software:**

  - **Python** para reprodução de áudios e comunicação serial com o Arduino.
  - Biblioteca `pygame` para controle de áudio.

---

## Requisitos

- **Hardware:**

  - Arduino (compatível com conexão serial).
  - Sensores LDR e resistores.

- **Software:**

  - Python 3.8 ou superior.
  - Bibliotecas: `pygame`, `pyserial`.

---

## Como Executar o Projeto

1. **Configuração do Hardware:**

   - Conecte os sensores LDR aos pinos analógicos do Arduino (A0 a A7 para direções, A8 a A10 para idiomas).
   - Certifique-se de ajustar os valores de `threshold` no código do Arduino para o ambiente de iluminação.

2. **Configuração do Software:**

   - Clone este repositório:
     ```bash
     git clone https://github.com/whosricardo/EcosDePernambuco
     ```
   - Instale as dependências:
     ```bash
     pip install pygame pyserial
     ```

3. **Carregue o código do Arduino:**

   - Utilize a IDE do Arduino para carregar o código na placa.

4. **Execute o script Python:**

   - Certifique-se de que o Arduino está conectado.
   - Execute o script principal:
     ```bash
     python main.py
     ```

---

## Estrutura de Arquivos

```
EcosDePernambuco/
├── arduino.ino               # Código para Arduino
├── main.py                # Script Python
├── audios/                # Arquivos de áudio
├── LICENSE                # Licença do projeto
└── README.md              # Documentação
```

---

## Contribuições

Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request com melhorias ou sugestões.

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE). Você é livre para usar, modificar e distribuir este projeto, desde que mantenha os créditos aos autores originais.

---

**Autores**: Equipe Ecos de Pernambuco 
