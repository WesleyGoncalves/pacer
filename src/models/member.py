from . import Base, Team
from ..enums import Roles
from typing import List, Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_login import UserMixin


class Member(Base, UserMixin):
    __tablename__ = "members"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(320))
    # password is deferred - loaded only when directly accessed
    password: Mapped[str] = mapped_column(String(255), deferred=True)
    # image_name: Mapped[Optional[str]] = mapped_column(String(255))
    role: Mapped[Roles]

    # FKs
    team_id: Mapped[int] = mapped_column(ForeignKey(Team.id, ondelete="CASCADE"))
    team: Mapped[Team] = relationship(back_populates="members")
    scores: Mapped[List["Score"]] = relationship(
        back_populates="member", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f'{{ "id": {self.id!r}, "name": {self.name!r}, "email": {self.email!r} \
            "role": {self.role.value.title()}, "team_id": {self.team_id!r} }}'
