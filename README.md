# RasaDiscord

## Installation

To get started with RasaDiscord, follow these steps:

### Prerequisites

Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Install Dependencies

First, install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### Step 2: Setup Rasa

Navigate to the `rasa_server` directory and train the Rasa model:

```bash
cd rasa_server
rasa train
```

After training the model, you can run the Rasa server:

```bash
rasa run
```

### Step 3: Setup Discord Bot

1. Set up your Discord bot token:

    - Obtain your Discord bot token from [Discord Developer Portal](https://discord.com/developers/applications).
    - Create a `.env` file in the `discord_bot` directory and add your token:

    ```plaintext
    DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
    ```

2. Enable Message Content Intent:

    - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
    - Select your application.
    - Navigate to the "Bot" section.
    - Under "Privileged Gateway Intents," enable "Message Content Intent."

3. Start the Discord bot:

    ```bash
    python discord_bot/main.py
    ```

## Usage

Once both the Rasa server and Discord bot are running, your bot will be able to handle messages on your Discord server. Ensure that you have properly set your Discord bot token in the `.env` file and enabled Message Content Intent.
