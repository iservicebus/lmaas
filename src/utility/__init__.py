
import logging.config, yaml, os
from omegaconf import OmegaConf



def configure_logging():
    log_file = os.path.join(os.path.dirname(__file__), "../../config/logging.yaml")
    with open(log_file, 'r') as f:
        config = yaml.safe_load(f)
        logging.config.dictConfig(config)
    config_file = os.path.join(os.path.dirname(__file__), "../../config/config.yaml")
    
    with open(config_file, 'r') as stream:
        try:
                    # Load the YAML file
            return  OmegaConf.load(stream)
        except yaml.YAMLError as exc:
            print(f"Error loading YAML configuration: {exc}")
            raise

lmaas_config = configure_logging()
logger = logging.getLogger(lmaas_config.app.logging)






