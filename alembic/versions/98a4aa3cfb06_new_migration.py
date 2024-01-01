"""New Migration

Revision ID: 98a4aa3cfb06
Revises: 
Create Date: 2023-12-31 01:55:41.331763

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98a4aa3cfb06'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('entry', 'title',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.create_index(op.f('ix_entry_id'), 'entry', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_entry_id'), table_name='entry')
    op.alter_column('entry', 'title',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    # ### end Alembic commands ###