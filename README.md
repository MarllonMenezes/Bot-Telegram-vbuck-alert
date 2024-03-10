## Bot de Alerta de V-Bucks do Fortnite

Este é um bot Telegram que fornece alertas diários sobre missões que oferecem V-Bucks como recompensa no jogo Fortnite Save the World. O bot é capaz de enviar alertas tanto em resposta a um comando específico quanto automaticamente em um horário programado todos os dias.

### Funcionalidades

1. **Comando de alerta manual**: Os usuários podem enviar o comando `/alert` para solicitar um alerta manualmente a qualquer momento. O bot irá buscar as informações mais recentes sobre as missões de V-Bucks e enviar um alerta em resposta.

2. **Alerta automático diário**: O bot é configurado para enviar automaticamente um alerta todos os dias às 21:01 (horário configurável) para um chat específico. Este alerta contém informações sobre as missões de V-Bucks disponíveis no momento.

3. ** Grupo em que o bot está ativo [https://t.me/+7Q13LKLNk9NjZjk5]

### Pré-requisitos

- Python 3.x instalado no seu sistema. (3.12 recomendável)
- Conta no Telegram.
- Token de acesso do bot do Telegram.

### Instalação e Configuração

1. Clone este repositório em sua máquina local:

   ```bash
   git clone (https://github.com/MarllonMenezes/Bot-Telegram-vbuck-alert)
   ```

2. Certifique-se de ter todas as dependências instaladas. Você pode instalar as dependências usando pip:

   ```bash
   pip install requests beautifulsoup4 pyTelegramBotAPI schedule
   ```

3. Configure o arquivo `config.py` com o token do seu bot do Telegram:

   ```python
   botToken = 'SEU_TOKEN_AQUI'
   ```

### Uso

1. Inicie o bot executando o script `bot.py`:

   ```bash
   python bot.py
   ```

2. Agora você pode iniciar uma conversa com o seu bot no Telegram e usar o comando `/alert` para receber um alerta manual ou aguardar o alerta automático diário.

### Contribuição

Se você quiser contribuir para este projeto, fique à vontade para abrir uma nova issue ou enviar um pull request.

### Observações

- Este bot faz scraping no site [freethevbucks.com](https://freethevbucks.com/) para obter informações sobre as missões de V-Bucks. 
- Este bot foi desenvolvido apenas para fins educacionais e de demonstração. O uso deste bot é de responsabilidade do usuário.

### Autores

- [Marllon Menezes]([https://github.com/seuusuario](https://github.com/MarllonMenezes)) - Desenvolvimento inicial

### Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.
