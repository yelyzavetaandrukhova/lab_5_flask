"""create tables

Revision ID: ed585218d307
Revises: 
Create Date: 2023-12-10 23:19:19.418602

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ed585218d307'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'User',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('customerName', sa.String(255), nullable=False),
        sa.Column('emailAddress', sa.String(255), nullable=False)
    )

def downgrade():
    op.drop_table('Customer')