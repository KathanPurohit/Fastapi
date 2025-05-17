"""add content column to the post table

Revision ID: 5e1644663563
Revises: 344bd6df6123
Create Date: 2025-05-16 21:44:21.057017

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e1644663563'
down_revision: Union[str, None] = '344bd6df6123'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
