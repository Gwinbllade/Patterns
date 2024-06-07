from abc import ABC, abstractmethod


class Notification(ABC):
    def get_notification(self):
        pass


class BaseNotification(Notification):
    def get_notification(self) -> str:
        return 'some notification'


class NotificationDecorator(Notification, ABC):
    def __init__(self, notification: Notification):
        self._notification = notification

    @abstractmethod
    def get_notification(self) -> str:
        pass


class EmailDecorator(NotificationDecorator):
    def get_notification(self):
        return "Email:" + self._notification.get_notification()


class FacebookDecorator(NotificationDecorator):
    def get_notification(self) -> str:
        return "Facebook:" + self._notification.get_notification()


class TwitterDecorator(NotificationDecorator):
    def get_notification(self) -> str :
        return "Twitter:" + self._notification.get_notification()


if __name__ == "__main__":
    notification = BaseNotification()
    print(notification.get_notification())

    facebook_notification = FacebookDecorator(notification)
    print(facebook_notification.get_notification())

    email_notification = EmailDecorator(notification)
    print(email_notification.get_notification())

    twitter_notification = TwitterDecorator(notification)
    print(twitter_notification.get_notification())
