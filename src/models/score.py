from . import Base, Member, Project
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Score(Base):
    __tablename__ = "scores"

    id: Mapped[int] = mapped_column(primary_key=True)
    n_sprint: Mapped[int]
    score_proatividade: Mapped[int]
    score_autonomia: Mapped[int]
    score_colaboracao: Mapped[int]
    score_entrega: Mapped[int]

    # FKs
    member_id: Mapped[int] = mapped_column(ForeignKey(Member.id, ondelete="CASCADE"))
    member: Mapped[Member] = relationship(back_populates="scores")
    project_id: Mapped[int] = mapped_column(ForeignKey(Project.id, ondelete="CASCADE"))
    project: Mapped[Project] = relationship(back_populates="scores")
