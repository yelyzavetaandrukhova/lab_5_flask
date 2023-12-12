"""create table

Revision ID: 7ace352299a9
Revises: ed585218d307
Create Date: 2023-12-10 23:23:53.325048

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ace352299a9'
down_revision: Union[str, None] = 'ed585218d307'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
