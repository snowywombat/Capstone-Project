from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

today = datetime.now()

class Culture(db.Model):
    __tablename__ = 'cultures'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    banner_img = db.Column(db.String(1000), nullable=False)
    article = db.Column(db.String(1000000), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=today)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)

    # Many-To-One between Culture and Users
    user = db.relationship("User", back_populates="cultures")

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'banner_img': self.banner_img,
            'article': self.article,
            'created_at': self.created_at,
            'user_id': self.user_id,
            'user': self.user,
        }
