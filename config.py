import configparser
import os

def load_config():
    config_env = os.getenv('CONFIG_ENV', 'local')  # Default to 'local' if not set

    config_file = f'config/{config_env}.ini'

    config = configparser.ConfigParser()

    try:
        # Read the config file
        config.read(config_file)

        # Load RabbitMQ details from the configuration
        rabbitmq_host = config['RabbitMQ']['host']
        exchange_name = config['RabbitMQ']['exchange_name']
        username = config['RabbitMQ']['username']
        password = config['RabbitMQ']['password']
        virtualHost = config.get('RabbitMQ', 'virtualhost', fallback='/')

        return {
            "rabbitmq_host": rabbitmq_host,
            "rabbitmq_username": username,
            "rabbitmq_password": password,
            "exchange_name": exchange_name,
            "rabbitmq_virtualhost": virtualHost
        }

    except Exception as e:
        print(f"Error reading config file {config_file}: {e}")
        raise Exception("Failed to read RabbitMQ configuration")
