from ui_frame.repository.ui_frame_repository_impl import UiFrameRepositoryImpl
from ui_frame.service.ui_frame_service import UiFrameService


class UiFrameServiceImpl(UiFrameService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__uiFrameRepository = UiFrameRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def switchFrameWithMenuName(self, menuName: str):
        print("UiFrameServiceImpl: switchFrameWithMenuName()")
        self.__uiFrameRepository.switchFrameWithMenuName(menuName)

    def registerMainMenuUiFrame(self, mainMenuFrame):
        print("UiFrameServiceImpl: registerMainMenuUiFrame()")
        self.__uiFrameRepository.registerUiFrame("main-menu", mainMenuFrame)

    def registerLoginMenuUiFrame(self, loginMenuFrame):
        print("UiFrameServiceImpl: registerLoginMenuUiFrame()")
        self.__uiFrameRepository.registerUiFrame("login-menu", loginMenuFrame)

    def registerAccountRegisterUiFrame(self, accountRegisterFrame):
        print("UiFrameServiceImpl: registerAccountRegisterUiFrame()")
        self.__uiFrameRepository.registerUiFrame("account-register", accountRegisterFrame)





