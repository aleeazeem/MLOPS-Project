import logging
import os
import yaml
from dotenv import load_dotenv
from typing import Any

class Config:
    """Centralized configuration management"""
    
    def __init__(self, params_path: str = 'params.yaml'):
        # Load environment variables from .env file. Silently ignore if the file does not exist.
        # The env variables will be picked up from CICD environment in production.
        load_dotenv()
        
        with open(params_path, 'r') as f:
            self.params = yaml.safe_load(f)
        
    @property
    def aws_access_key(self) -> str:
        key = os.getenv('AWS_ACCESS_KEY')
        if not key:
            raise ValueError("AWS_ACCESS_KEY not found in environment")
        return key
    
    @property
    def aws_secret_key(self) -> str:
        key = os.getenv('AWS_SECRET_KEY')
        if not key:
            raise ValueError("AWS_SECRET_KEY not found in environment")
        return key
    
    @property
    def s3_bucket(self) -> str:
        return os.getenv('S3_BUCKET_NAME', 'complaints-datagrid-alee')
    
    @property
    def environment(self) -> str:
        env = os.getenv('ENVIRONMENT')
        if not env:
            logging.warning("ENVIRONMENT not set, running against production by default")
        return env
    
    @property
    def dagshub_token(self) -> str:
        token = os.getenv('DAGSHUB_ACCESS_TOKEN')
        if not token:
            raise ValueError("DAGSHUB_ACCESS_TOKEN token not found in environment")
        return token
    
    @property
    def dagshub_username(self) -> str:
        username = os.getenv('DAGSHUB_USERNAME')
        if not username:
            raise ValueError("DAGSHUB_USERNAME not found in environment")
        return username
    
   # Static config from params.yaml
    @property
    def s3_bucket_name(self) -> str:
        return self.params['bucket']['name']
    
    @property
    def aws_region(self) -> str:
        return self.params['bucket']['region']
    
    @property
    def mlflow_tracking_uri(self) -> str:
        return self.params['mlflow']['tracking_uri']
    
    @property
    def mlflow_owner(self) -> str:
        return self.params['repository']['owner']
    
    @property
    def mlflow_repo_name(self) -> str:
        return self.params['repository']['name']
    
    @property
    def max_features(self) -> int:
        return self.params['feature_engineering']['max_features']
    
    def get_param(self, *keys, default=None) -> Any:
        """Get nested param value: get_param('bucket', 'name')"""
        value = self.params
        for key in keys:
            if isinstance(value, dict):
                value = value.get(key)
            else:
                return default
        return value if value is not None else default

# Create singleton instance
config = Config()