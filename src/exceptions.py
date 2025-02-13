class TranscriptionError(Exception):
    """Базовый класс для ошибок транскрипции"""
    pass

class QueueConnectionError(TranscriptionError):
    """Ошибка подключения к очереди сообщений"""
    pass

class DownloadError(Exception):
    """Base class for download-related exceptions"""
    pass