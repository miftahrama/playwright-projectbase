"""
Centralized configuration for test automation.
Load settings from environment variables with fallback defaults.
Supports multiple environments: staging, production.
"""
import os
from dotenv import load_dotenv

load_dotenv()


class Environments:
    """Environment-specific configurations."""

    STAGING = {
        "base_url": "https://portal-sekolah.com",
        "dashboard_url": "https://dashboard.portal-sekolah.com",
    }

    PRODUCTION = {
        "base_url": "https://portalsekolah.com",
        "dashboard_url": "https://dashboard.portalsekolah.com",
    }


class Settings:
    """Test environment settings."""

    def __init__(self, env: str = "staging"):
        """Initialize settings with specified environment."""
        env_config = getattr(Environments, env.upper(), Environments.STAGING)

        # Base URLs (from environment config or override with env vars)
        self.BASE_URL: str = os.getenv("BASE_URL", env_config["base_url"])
        self.DASHBOARD_URL: str = os.getenv("DASHBOARD_URL", env_config["dashboard_url"])

        # Browser settings
        self.BROWSER: str = os.getenv("BROWSER", "chromium")
        self.HEADLESS: bool = os.getenv("HEADLESS", "false").lower() == "true"

        # Timeout settings (milliseconds)
        self.TIMEOUT: int = int(os.getenv("TIMEOUT", "10000"))
        self.NAVIGATION_TIMEOUT: int = int(os.getenv("NAVIGATION_TIMEOUT", "30000"))

        # Static Test data
        self.DEFAULT_SCHOOL_SEARCH: str = os.getenv("DEFAULT_SCHOOL_SEARCH", "smp - qa demo school")
        self.DEFAULT_SCHOOL_NAME: str = os.getenv("DEFAULT_SCHOOL_NAME", "SMP - QA Demo School 123")
        self.DEFAULT_USERNAME: str = os.getenv("DEFAULT_USERNAME", "adminsmp.123")
        self.DEFAULT_PASSWORD: str = os.getenv("DEFAULT_PASSWORD", "password123*")

        # Screenshot settings
        self.SCREENSHOT_ON_FAILURE: bool = os.getenv("SCREENSHOT_ON_FAILURE", "true").lower() == "true"
        self.SCREENSHOT_DIR: str = os.getenv("SCREENSHOT_DIR", "test-screenshot/screenshots")


def get_settings(env: str = "staging") -> Settings:
    """Get settings for specified environment."""
    return Settings(env=env)


# Singleton instance with default staging environment
settings = get_settings()