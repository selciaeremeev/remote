# coding: utf-8
import logging
import subprocess
from appium import webdriver

logger = logging.getLogger(__name__)


class TeamViewer:

    def __init__(self) -> None:
        desired_capabilities = dict()
        desired_capabilities["app"] = r"C:\Program Files (x86)\TeamViewer\TeamViewer.exe"
        self.driver = webdriver.Remote("http://127.0.0.1:4723", desired_capabilities)

    @property
    def ids(self) -> str:
        return self.driver.find_elements_by_name("使用中のID")[1].text

    @property
    def password(self) -> str:
        return self.driver.find_elements_by_name("パスワード")[1].text


p = subprocess.Popen("WinAppDriver")
t = TeamViewer()
logger.info(f"ID: {t.ids} Password: {t.password}")
p.kill()
