from umeng.dao.model.channel import Channel


def save_and_update(session, channels=[]):
    for channel in channels:
        result = session.query(Channel).filter(Channel.app_id == channel.app_id,
                                               Channel.channel_id == channel.channel_id).first()
        if result is None:
            session.add(channel)
        else:
            channel.id = result.id
            session.merge(channel)


def query_channel(session, app_id="", is_shown="True"):
    return session.query(Channel).filter(Channel.app_id == app_id).all()
