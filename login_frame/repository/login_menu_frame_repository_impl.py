from tkinter import ttk, CENTER

from login_frame.entity.login_menu_frame import LoginMenuFrame
from login_frame.repository.login_menu_frame_repository import LoginMenuFrameRepository


class LoginMenuFrameRepositoryImpl(LoginMenuFrameRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def createLoginMenuFrame(self, rootWindow):
        print("MainMenuFrameRepositoryImpl: createMainMenuFrame()")
        loginMenuFrame = LoginMenuFrame(rootWindow)

        return loginMenuFrame
