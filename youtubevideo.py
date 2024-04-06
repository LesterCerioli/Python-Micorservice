

class YoutubeVideo(Base):
    __tablename__ = 'YouTubeVideos'

    video_id = Column(String(50), primary_key=True)
    title = Column(String(255))
    description = Column(Text)
    channel_id = Column(String(50))
    published_at = Column(DateTime)
    like_count = Column(Integer)
    dislike_count = Column(Integer)
    view_count = Column(Integer)

Base.metadata.create_all(engine)