## Discord Routine Bot

<p>This is a Discord bot that provides a routine schedule for each day of the week. It responds to specific commands and retrieves the schedule from a JSON file.
</p>

### Prerequisites

<p>
Before running the bot, make sure you have the following:
</p>
1. Python 3.7 or higher

### Installation

1. Clone the repository or download the source code files.
2. Install the required dependencies by running the following command:

```
pip install -r requirements.txt
```

3. Create a file named .env in the project directory and add the following line:

```
DISCORD_TOKEN=<your-discord-token>
```

Replace <span>`< your-discord-token >`</span> with your Discord bot token.

4. Create a JSON file named routine.json in the project directory and populate it with your desired routine schedule.

5. Run the bot using the following command:

```
make start
```

### Usage

Once the bot is running and connected to your Discord server, you can use the following commands to interact with it:

- **routine-sun**: Displays the routine schedule for Sunday.
- **routine-mon**: Displays the routine schedule for Monday.
- **routine-tue**: Displays the routine schedule for Tuesday.
- **routine-wed**: Displays the routine schedule for Wednesday.
- **routine-thu**: Displays the routine schedule for Thursday.
- **routine-fri**: Displays the routine schedule for Friday.
- **routine-help** : Displays a list of available commands.

Please note that the commands are case-insensitive.

### Contributing

If you have any suggestions, improvements, or bug fixes, feel free to contribute to this project. You can submit your contributions through pull requests.
