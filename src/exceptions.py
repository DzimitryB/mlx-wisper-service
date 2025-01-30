class TranscriptionError(Exception):
    """Базовое исключение для ошибок транскрипции"""
    pass

class DownloadError(TranscriptionError):
    """Ошибка загрузки медиа-контента"""
    pass

class QueueConnectionError(TranscriptionError):
    """Ошибка подключения к очереди сообщений"""
    pass