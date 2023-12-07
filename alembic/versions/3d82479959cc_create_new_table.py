"""create new table

Revision ID: 3d82479959cc
Revises: 
Create Date: 2023-12-02 21:32:40.115276

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d82479959cc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user_table',
        sa.Column("id_user", sa.Integer, primary_key=True),
        sa.Column("username", sa.String(100), unique=True, nullable=False),
        sa.Column("email", sa.String(100), unique=True, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('user_table')
