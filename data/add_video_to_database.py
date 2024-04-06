# add_video_to_database.py

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from your_module_name import YouTubeVideo  # Import your YouTubeVideo class here

# Create engine and session
DATABASE_URL = 'mssql+pyodbc://your_username:your_password@your_host/your_database?driver=ODBC+Driver+17+for+SQL+Server'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def add_video_to_database(video_id, title, description, channel_id):
    new_video = YouTubeVideo(
        video_id=video_id,
        title=title,
        description=description,
        channel_id=channel_id,
        published_at=datetime.now(),
        like_count=0,
        dislike_count=0,
        view_count=0
    )
    session.add(new_video)
    session.commit()


if __name__ == "__main__":
    add_video_to_database(
        video_id='your_video_id',
        title='Your Video Title',
        description='Your Video Description',
        channel_id='your_channel_id'
    )