from . import Base
from typing import List, Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Team(Base):
    __tablename__ = "teams"

    # Maximum number of members in a team, including PO and Master
    MAX_MEMBERS = 9

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    # image_name: Mapped[Optional[str]] = mapped_column(String(255))

    # FKs
    projects: Mapped[List["Project"]] = relationship(
        back_populates="team", cascade="all, delete-orphan"
    )
    members: Mapped[List["Member"]] = relationship(
        back_populates="team", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f'{{ "id": {self.id!r}, "name": {self.name!r}, \
            "projects": {self.projects!r} }}'
