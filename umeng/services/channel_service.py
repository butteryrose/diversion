from umeng.services import base_service
from cache import config
from umeng.dao.model.channel import Channel
from umeng.dao import channle_dao


class ChannelService(base_service.BaseService):

    def __init__(self, name="渠道采集任务"):
        self.name = name
        self.url = config.get_umeng()["url"]["channels"]

    def collect_data(self):
        apps = self.get_apps()
        for app in apps:
            self.collect_data_inner(url=self.url.format(app_id=app.app_id.decode()),
                                    name=self.name + "--" + app.name.decode(),
                                    app_id=app.app_id.decode())

    def callback(self, result, **kwargs):
        channels = []
        for channel in result["datas"]:
            channels.append(Channel(name=channel["name"],
                                    channel_id=channel["id"],
                                    is_shown=str(channel["is_shown"]),
                                    app_id=kwargs["app_id"]))
        self.transaction_execute(function=lambda session, channels=channels:
                                 channle_dao.save_and_update(session=session, channels=channels))
