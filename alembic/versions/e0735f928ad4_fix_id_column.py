"""fix id column

Revision ID: e0735f928ad4
Revises: 2914cc35022e
Create Date: 2025-07-02 15:09:42.912984

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0735f928ad4'
down_revision: Union[str, Sequence[str], None] = '2914cc35022e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema: change UUID id back to Integer."""
    # Drop UUID column and recreate as Integer (cleanest way)
    with op.batch_alter_table("products") as batch_op:
        batch_op.drop_column("id")
        batch_op.add_column(sa.Column("id", sa.Integer, primary_key=True, autoincrement=True))


def downgrade() -> None:
    """Downgrade schema: revert Integer id to UUID."""
    with op.batch_alter_table("products") as batch_op:
        batch_op.drop_column("id")
        batch_op.add_column(sa.Column("id", sa.dialects.postgresql.UUID(), primary_key=True))
