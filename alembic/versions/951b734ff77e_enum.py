"""Enum

Revision ID: 951b734ff77e
Revises: b6756cdb797b
Create Date: 2024-02-17 17:33:02.197016

"""

from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "951b734ff77e"
down_revision: Union[str, None] = "b6756cdb797b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "orders",
        "status",
        existing_type=postgresql.ENUM(
            "NEW", "IN_PROGRESS", "READY", "DELIVERED", name="status"
        ),
        type_=sa.String(),
        existing_nullable=False,
    )
    op.alter_column(
        "users",
        "role",
        existing_type=postgresql.ENUM("ADMIN", "COOK", "waiter", "CLIENT", name="role"),
        type_=sa.String(),
        existing_nullable=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users",
        "role",
        existing_type=sa.String(),
        type_=postgresql.ENUM("ADMIN", "COOK", "waiter", "CLIENT", name="role"),
        existing_nullable=False,
    )
    op.alter_column(
        "orders",
        "status",
        existing_type=sa.String(),
        type_=postgresql.ENUM(
            "NEW", "IN_PROGRESS", "READY", "DELIVERED", name="status"
        ),
        existing_nullable=False,
    )
    # ### end Alembic commands ###
