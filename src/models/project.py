from . import Base, Team
from typing import List, Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    n_sprints: Mapped[int]
    # image_name: Mapped[Optional[str]] = mapped_column(String(255))

    # FKs
    team_id: Mapped[int] = mapped_column(ForeignKey(Team.id, ondelete="CASCADE"))
    team: Mapped[Team] = relationship(back_populates="projects")
    scores: Mapped[List["Score"]] = relationship(
        back_populates="project", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f'{{ "id": {self.id!r}, "name": {self.name!r}, "n_sprints": {self.n_sprints!r}, \
            "team_id": {self.team_id!r} }}'
